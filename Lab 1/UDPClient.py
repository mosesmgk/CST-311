'''
Team 8: Jeffrey Garrett, Jesse Krepelka, Moses Garcia Cesar Sanchez
Date: 05/10/2020
Class: CST 311 
Description: Client takes input from keyboard and sends it to UDP 
			 server to convert to Uppercase
'''

from socket import *       # allows the creation of sockets 

serverName = '127.0.0.1'    
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = input('Input lowercase sentence: ')
clientSocket.sendto(message.encode(), (serverName, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print(modifiedMessage.decode())
clientSocket.close()
