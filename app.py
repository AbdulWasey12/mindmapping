from flask import Flask, render_template
import subprocess
import platform
import datetime
import psutil

app = Flask(__name__)

@app.route('/htop')
def htop():
    name = "Your Full Name" # Replace with your full name
    username = platform.node()
    ist = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=5, minutes=30)))
    server_time = ist.strftime("%Y-%m-%d %H:%M:%S IST")
    top_output = subprocess.check_output(['htop', '-b', '-n', '1']).decode('utf-8')

    return render_template('htop.html', name=name, username=username, server_time=server_time, top_output=top_output)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
        