
import io
from flask import*
from flask import Flask,render_template,request,redirect,flash
from werkzeug.utils import secure_filename

import io
import os
import webbrowser
import json
import time
app = Flask(__name__)

    
@app.route('/config',methods=['POST','GET'])
def config():
    if request.method == 'POST':
        ssid = request.form['wifi']
        pask = request.form['password']
        confirmpassword=request.form['confirmpassword']
        

        filename = 'wpa_supplicant.conf'
        with open(filename, 'a') as file:
            file.write("country=IN\n")
            file.write("ctrl_interface=DIR=/var/run/wpa_supplicant\n")
            file.write("GROUP=netdev\n")
            file.write("update_config=1\n")
            file.write("network={\n")
            file.write(f"""\tssid="{ssid}"\n""")
            file.write(f"""\tpsk="{pask}"\n""")
            file.write("}\n")
            

        return send_file(filename, as_attachment=True)

    return render_template('wifi_up.html')   

if __name__ == '__main__':
    app.run(host='192.168.10.233', port=8000, debug=True)


