from celery import Celery
import os
import json

cel = Celery('tasks', backend='amqp',
broker='amqp://ukri:qwertyu7654321@192.168.1.40/ukriv')


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
	print("NAME: " + name)
	print("ARGS: " + args)
        print("creating file..")
        create_file(name, content)
        print("dolfin..") 
        os.system("dolfin-convert " + name + ".msh " + name + ".xml")
        print("airfoil..")
        os.system("./airfoil " + args + " " + name + ".xml")
        with open ("results/drag_ligt.m", "r") as result:
                data = result.readlines()
        return json.dumps(data)

