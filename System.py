'''Import all system libraries'''
import time, socket, datetime, os, fcntl, struct, sqlite3	#import time, IP, time and date
from flask import Flask, render_template, request, jsonify, request, send_file, redirect, url_for #import web app
import netifaces as ni
import RPi.GPIO as GPIO
import SystemLibrary as L

GPIO.setmode(GPIO.BCM)             # choose BCM or BOARD  
GPIO.setup(14, GPIO.OUT)    

os.system('clear')

IP = L.get_IP()
L.displayTime()
#L.shift(str(L.getCurrentBinary), 2)

app = Flask(__name__) 

global int_time
int_time = datetime.datetime.now()

@app.route('/') #Sets index
def index():
	return render_template('index.html') #Displays HTML page 'Relay.html'#

@app.route('/relay/<username>', methods=['GET', 'POST'])
def checkSwitch(username):
	timing = float(username)
	GPIO.output(14, 0)
	time.sleep(timing)
	GPIO.output(14, 1)
	time.sleep(timing)
	return render_template('index.html')

if __name__ == '__main__':
	app.run(debug=True, host=(str(IP)), threaded=True, port=80)
GPIO.cleanup()
