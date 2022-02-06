from flask import Flask

from pct_data.server.server_environment import ServerEnvironment

app = Flask(__name__)

server_environment = ServerEnvironment()


@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/summary")
def summary():
    return server_environment.get_summary()

if __name__ == '__main__':
    app.run()
