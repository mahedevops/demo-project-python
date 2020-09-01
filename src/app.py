from flask import Flask
from flask import jsonify
from datetime import datetime
import time
app = Flask(__name__)
startime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
@app.route('/health')
def hello_world():
     return jsonify({"status":"OK","version":"0.0.1","uptime":"up since "+str(startime)})

if __name__ == '__main__':
    app.run(host= '0.0.0.0')
