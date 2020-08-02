from flask import Flask, request, make_response, jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "hello world from smart-snippet server"

@app.route("/test_server")
def test_server():
    return "Smart-snippet server running"

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
    