'''
Team 8: Jeffrey Garrett, Jesse Krepelka, Moses Garcia Cesar Sanchez
Date: 05/10/2020
Class: CST 311 
Description: Client takes input from keyboard and sends it to TCP 
			 server to convert to Uppercase
'''

from socket import *
serverName = '127.0.0.1'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
sentence = input('Input lowercase sentence:')
clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(1024)
print('From Server: ', modifiedSentence.decode())
clientSocket.close()
