from flask import Flask
from flask import request
import json
import os
import urllib.request
app = Flask(__name__)

@app.route("/airfoil/<file>")
def air(file):
	print("dolfin..")
	os.system("dolfin-convert ../cloudnaca/msh/" + file + ".msh " + "../cloudnaca/msh/" + file + ".xml")
	print("airfoiL..")
	args = request.query_string
	argsstring = urllib.request.unquote(args.decode("utf-8"))
	os.system("./airfoil " + argsstring + " ../cloudnaca/msh/"+file+".xml")
	with open ("results/drag_ligt.m", "r") as result:
		data = result.readlines()
		return json.dumps(data)

def get_mshes():
	mshes = [os.path.splitext(msh)[0] for msh in os.listdir("../cloudnaca/msh") if msh.endswith('.msh')]
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

if __name__ == "__main__":
	app.run(host='0.0.0.0')
	
