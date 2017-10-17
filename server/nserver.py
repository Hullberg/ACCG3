from celery import Celery
from flask import Flask
from flask import request
import json
import os
import urllib.request
app = Flask(__name__)


cel = Celery('tasks', backend='amqp',
broker='amqp://ukri:qwertyu7654321@192.168.1.40/ukriv')

def get_mshes():
	mshes = [os.path.splitext(msh)[0] for msh in os.listdir("msh") if msh.endswith('.msh')]
	return json.dumps(mshes)

@app.route("/mshes")
def msh():
	return get_mshes()

@app.route("/createmshes")
def createmshes():
	args = request.query_string
	argsstring =  urllib.request.unquote(args.decode("utf-8"))
	os.system("./runme.sh "+argsstring)
	return get_mshes()

def get_file_content(f):
	with open("msh/"+f+".msh", 'r') as file:
		c = file.read()
	return c

def create_file(name, content):
	with open(name+".msh", 'w') as file:
		file.write(content)
		file.close()

@cel.task
def add(x,y):
	return x+y

@cel.task
def sub(x,y):
        return x-y

@cel.task
def async_air(name, content, args):
	print("creating file..")
	create_file(name, content)
	print("dolfin..") 
	os.system("dolfin-convert " + name + ".msh " + name + ".xml")
	print("airfoil..")
	os.system("./airfoil " + args + " " + name + ".xml")
	with open ("results/drag_ligt.m", "r") as result:
		data = result.readlines()
	return json.dumps(data)

@app.route("/airfoil/<file>")
def air(file):
	from nserver import async_air
	args = request.query_string
	argsstring = urllib.request.unquote(args.decode("utf-8"))
	task = async_air.delay(file, get_file_content(file), argsstring)
	return json.dumps(task.id)

@app.route("/airfoil/task/<taskid>")
def get_status(taskid):
	task = async_air.AsyncResult(taskid)
	if task.state == "SUCCESS":
		return json.dumps({'state': task.state, 'result': task.result})
	return json.dumps({'state': task.state})

if __name__ == "__main__":
	app.run(host='0.0.0.0')
