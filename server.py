from flask import Flask
import os
import subprocess
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/htop')
def htop():

    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S')

    try:
        top_output = subprocess.check_output(['top', '-b', '-n', '1'], text=True)
    except Exception as e:
        top_output = str(e)

    response = f'''
    <h1>System Information</h1>
    <p><strong>Name:</strong> Ashok kasandula</p>
    <p><strong>Username:</strong> {os.getlogin()}</p>
    <p><strong>Server Time (IST):</strong> {server_time}</p>
    <h2>Top Output:</h2>
    <pre>{top_output}</pre>
    '''
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
