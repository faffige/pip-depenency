from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/<string:module>', methods=['POST'])
def pip():
    name = request.args.get("module")
    return f'Hello, {escape(modle)}!'