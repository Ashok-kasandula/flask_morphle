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
        top_output = subprocess.check_output(['ps', 'aux'], text=True)
    except Exception as e:
        top_output = str(e)

    username = os.environ.get('USER') or os.environ.get('LOGNAME') or 'Unknown'

    response = f'''
    <h1>System Information</h1>
    <p><strong>Name:</strong> Ashok Kasandula</p>
    <p><strong>Username:</strong> {username}</p>
    <p><strong>Server Time (IST):</strong> {server_time}</p>
    <h2>Process List:</h2>
    <pre>{top_output}</pre>
    '''
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
