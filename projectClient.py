from socket import *
import time

server1Name = '127.0.0.1'
server1Port = 12000
server2Name = '127.0.0.1'
server2Port = 16000



clientSocket1 = socket (AF_INET, SOCK_STREAM)
clientSocket1.connect ((server1Name, server1Port))
clientSocket2 = socket (AF_INET, SOCK_STREAM)
clientSocket2.connect ((server2Name, server2Port))
no1 = input ('Enter first number: ')
no2 = input ('Enter second number: ')
range11 = no1
range12 = 0
range21 = 0 
range22 = no2

if (int (no1) + int (no2)) % 2 == 0:
	range12 = (int (no1) + int (no2)) / 2
else:
	range12 = int ((int (no1) + int (no2)) / 2)

range21 = range12 + 1
vals1 = str (range11) + " " + str (range12)
timer1 = time.time() * 1000;
clientSocket1.send (str.encode (vals1))
count1 = clientSocket1.recv (1024)
vals2 = str (range21) + " " + str (range22)
timer2 = time.time() * 1000;
clientSocket2.send (str.encode (vals2))
count2 = clientSocket2.recv (1024)


time1 = time.time() * 1000 - timer1
time2 = time.time() * 1000 - timer2

print ("Reply From Server 1: ", count1.decode ("ascii"), "Time: ", str (time1) + " miliseconds")
print ("Reply From Server 2: ", count2.decode ("ascii"), "Time: ", str (time2) + " miliseconds")
print ("Total:", int (count1.decode ("ascii")) + int (count2.decode ("ascii")))

clientSocket2.close()
clientSocket1.close()
