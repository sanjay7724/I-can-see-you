from flask import Flask, render_template
from time import sleep

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/ssh")
def ssh():

    def generate():
        with open("../ssh/ssh_logs/ssh.log", "r") as f:
            while True:
                line = f.readline()
                if not line:
                    sleep(0.1)  # Sleep briefly before trying to read more
                    continue
                yield line

    return app.response_class(generate(), mimetype="text/plain")


@app.route("/iplocation")
def iplocation():

    def generate():
        with open("../ssh/ssh_logs/clients_ip.log", "r") as f:
            while True:
                line = f.readline()
                if not line:
                    sleep(0.1)  # Sleep briefly before trying to read more
                    continue
                yield line

    return app.response_class(generate(), mimetype="text/plain")


if __name__ == "__main__":
    app.run(debug=True)
