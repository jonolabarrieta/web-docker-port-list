import docker
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

client = docker.from_env()
@app.route('/')
def hello():
    data = []
    for image in client.containers.list():
        data.append({
            "name" : image.name,
            "ports" : image.ports
        })
    return {"data": data}

app.run(host='0.0.0.0')