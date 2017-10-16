from flask import Flask
import json
import os
app = Flask(__name__)

@app.route("/airfoil/<xml>")
def air(xml):
        os.system("./airfoil  10 0.0001 10. 1 ../cloudnaca/msh/"+xml)
        with open ("results/drag_ligt.m", "r") as result:
                data = result.readlines()
                return json.dumps(data)


@app.route('/')
def hello_world():
    return 'Flask Dockerized'

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')