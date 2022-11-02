import RPi.GPIO as GPIO
from time import sleep
import pymongo
from datetime import datetime

#disable warnings (optional)
GPIO.setwarnings(False)
#Select GPIO Mode
GPIO.setmode(GPIO.BCM)
#set red,green and blue pins
redPin = 12
greenPin = 19
bluePin = 13
#set pins as outputs
GPIO.setup(redPin,GPIO.OUT)
GPIO.setup(greenPin,GPIO.OUT)
GPIO.setup(bluePin,GPIO.OUT)

def turnOff():
    GPIO.output(redPin,GPIO.HIGH)
    GPIO.output(greenPin,GPIO.HIGH)
    GPIO.output(bluePin,GPIO.HIGH)
    
def white():
    GPIO.output(redPin,GPIO.LOW)
    GPIO.output(greenPin,GPIO.LOW)
    GPIO.output(bluePin,GPIO.LOW)
    
def red():
    GPIO.output(redPin,GPIO.LOW)
    GPIO.output(greenPin,GPIO.HIGH)
    GPIO.output(bluePin,GPIO.HIGH)

def green():
    GPIO.output(redPin,GPIO.HIGH)
    GPIO.output(greenPin,GPIO.LOW)
    GPIO.output(bluePin,GPIO.HIGH)
    
def blue():
    GPIO.output(redPin,GPIO.HIGH)
    GPIO.output(greenPin,GPIO.HIGH)
    GPIO.output(bluePin,GPIO.LOW)


client = pymongo.MongoClient('mongodb+srv://'+"Wongzh"+':'+ "FYP2022" +'@p2pet.6ufu7nf.mongodb.net/?retryWrites=true&w=majority', tls=True)
print("Connected to database")
cluster=client["P2PET"]

collection = cluster.newOrders

Prosumers ( 0-5 )
62cd362cbe040700b7eae7d0
62fcd07fe8210b1d10221822
62fcd08ee8210b1d10221824
62e4fef95f855068e3168bba
62e4fee75f855068e3168bb8

Consumers ( 0-5 )
6360d7ab770544ec3afbf36d
6360d7b8770544ec3afbf36f
6360d7c5770544ec3afbf371
6360d7cf770544ec3afbf373
6360d835770544ec3afbf375


while True:
    if datetime.now().second == 30 or datetime.now().second == 0:
        result=collection.find({"fromid":"6360d835770544ec3afbf375"})
        for item in result:
            ordertype = item['type']
        if ordertype == "buy":
            red()
        elif ordertype == "sell":
            green()
        else:
            white()