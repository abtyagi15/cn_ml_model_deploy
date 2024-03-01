from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/login", methods=["POST"])
def login():
    return jsonify({"message": "Login Successful"})

 
if __name__ == "__main__":
    app.run(port=5000)
