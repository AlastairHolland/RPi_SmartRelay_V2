import time, socket, datetime, os, fcntl, struct, sqlite3	#import time, IP, time and date
from flask import Flask, render_template, request, jsonify, request, send_file #import web app
from w1thermsensor import W1ThermSensor
import RPi.GPIO as GPIO
import netifaces as ni

def get_IP():
	'''Automatically gets the IP address of the Pi'''
	ni.ifaddresses('eth0')
	IP = ni.ifaddresses('eth0')[ni.AF_INET][0]['addr']
	return IP
	
def displayTime():
	'''Sorts the time out for the app'''
	localtime = time.asctime( time.localtime(time.time()) ) #Gets the time
	print (" * Current time :" + str(localtime)) #Displays Time
	
