'''
Team 8: Jeffrey Garrett, Jesse Krepelka, Moses Garcia, Cesar Sanchez
Date: 05/10/2020
Class: CST 311 
Description: The server receives the data and converts the characters to 
			 uppercase and in return send it back to the client
'''

from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('The server is ready to receive')
while True:
 connectionSocket, addr = serverSocket.accept()
 sentence = connectionSocket.recv(1024).decode()
 capitalizedSentence = sentence.upper()
 connectionSocket.send(capitalizedSentence.encode())
 connectionSocket.close()
