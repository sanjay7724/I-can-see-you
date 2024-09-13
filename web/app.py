from flask import Flask, render_template
from time import sleep
import subprocess
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/ssh')
def ssh():
    #log = os.system("cat ../ssh/ssh_logs/ssh.log")
    # log = subprocess.Popen(['cat','../ssh/ssh_logs/ssh.log'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    # print(log)
    # stdout,stderr = log.communicate()

    # return str(stdout.decode('utf-8'))
    def display():
        with open ('../ssh/ssh_logs/ssh.log') as f:
            while True:
                yield f.read()
                sleep(1)
    return app.response_class(display(),mimetype='text/plain')

if __name__ =='__main__':
    app.run(debug=True)