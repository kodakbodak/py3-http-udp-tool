#!/usr/bin/env python3

'''
TO DO LIST
	Packet content randomizer
	multiple targets?
	custom packet contents (text or files)
	nmap style attack speeds
	increase http verbosity
	error messages for both modules
	other stuff that I think of later
	receive udp messages
'''

'''
import libraries
	requests: to send packets
	time: for sleep() and timing of attacks
	random: for using to determine number of requests and timing
	socket: for UDP messages
	sys and signal for shutdown watcher
'''
import requests 
import time
import random 
import socket
import sys
import signal

'''
create a function to listen for shutdown signals


def signal_handler(signal, frame):
	print('Exiting Program')
	sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)
'''
	

'''
use a functon to determine how many requests to send
using different tiers of random requests
'''
def howManyRequests():
		
		randChoose = input('Please type approximately how many requests you would like to make (1-500): ')

		global newRandChoose

		if 1 <= int(randChoose) < 50:
			newRandChoose = randChoose
		
		elif 51 <= int(randChoose) <= 100:
			newRandChoose = random.randint(51,100)
		
		elif 101 <= int(randChoose) <= 150:
			newRandChoose = random.randint(101, 150)
		
		elif 151 <= int(randChoose) <= 200:
			newRandChoose = random.randint(151,200)
		
		elif 201 <= int(randChoose) <= 250:
			newRandChoose = random.randint(201,250)
		
		elif 251 <= int(randChoose) <= 300:
			newRandChoose = random.randint(251, 300)
		
		elif 301 <= int(randChoose) <= 350:
			newRandChoose = random.randint(301, 350)
		
		elif 351 <= int(randChoose) <= 400:
			newRandChoose = random.randint(351, 400)
		
		elif 401 <= int(randChoose) <= 450:
			newRandChoose = random.randint(401, 450)
		
		elif 451 <= int(randChoose) <= 500:
			newRandChoose = random.randint(451, 500)

'''
Use a function to send packets to the target using random timing
as well as the random numberof requests from userInput()
also uses methodList (from requests library) and random.choice() to randomly pick a type of request
'''
def sendRequests():

	for x in range (howManyReqs): # using howManyReqs as number of iterations, send requests within a for loop

		methodList = ['get', 'head', 'patch', 'post', 'out'] #use a list to determine the request type

		useThisMethod = random.choice(methodList)

		y = random.randint(1, 5) #set a random amount of time (sec) to wait between requests

		x = requests.request(useThisMethod, target)

		time.sleep(y)

		print('Status: ' + str(x.text))

'''
Create function to receive UDP messages
'''
def udpReceive():
	
	REC_IP = ''
	
	REC_PORT = input('Please enter the port to listen on: ')

	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

	sock.bind((REC_IP, int(REC_PORT)))

	while True:
		
		data, addr = sock.recvfrom(1024)
		
		print('Received message: %s' % data)
	
'''
Use a function to send messages over UDP to a specific address and port
'''
def udpSend():
	
	UDP_IP = input('Type in the target IP addresss: ')
	
	UDP_PORT = input('Input the target port: ')
	
	UDP_MESSAGE = input('Input a message to send using UDP packets: ')

	NUM_OF_PACKETS = int(input('How many packets would you like to send? '))

	PACKET_DELAY = float(input('Enter a number to set the delay between packets:'))

	PORT = int(UDP_PORT)

	for x in range (NUM_OF_PACKETS):

		#if PACKET_DELAY == '2':
		
			#PACKET_DELAY = random(0.0, 5.0)

		sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	
		sock.sendto(UDP_MESSAGE.encode(), (UDP_IP, PORT))

		time.sleep(PACKET_DELAY)

		print('sent: ' + str(PACKET_DELAY))

'''
Use a function to choose to use UDP or HTTP requests mode
'''
def chooseMode():
	
	print('1. UDP Send')
	
	print('2. UDP Reveive -- Still under development')
	
	print('3. Send HTTP Requests')

	print('4. Exit Program')
	
	whichMode = input("Please make a selection: ")

	global mode

	if int(whichMode) == 1:
		print('UDP Mode')
		mode = 1
	
	elif int(whichMode) == 2:
		print('UDP Receive')
		mode = 2
	
	elif int(whichMode) == 3:
		print('HTTP Requests Mode')
		mode = 3
	
	elif int(whichMode) == 4:
		print('Exiting Program')
		exit()
	
	else:
		print('---Please Choose a Valid Option---')
		chooseMode()

'''
Create main function to:
	run chooseMode to determine which function to use
	take global mode form the function to call either modeUDP or sendRequests
'''
def main():
	
	print('------------------------')
	
	print('--HTTP/UDP Packet Tool--')
	
	print('------------------------')
	
	chooseMode()
	
	if mode == 1:
		udpSend()
	
	elif mode == 2:
		udpReceive()
	
	elif mode == 3:
		
		global target
		
		target = input('Enter the target URL or IP and include scheme: ')
		
		howManyRequests()
		
		global howManyReqs
		
		howManyReqs = int(newRandChoose)
		
		print ('Will send ' + str(newRandChoose) + ' requests')
		
		sendRequests()
	
	else:
		main()
	

if __name__ == '__main__':
	main()
