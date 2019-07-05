from socket import *

"""def isPrime (n):
    if n <= 1:
        return False
    for i in range (2, int (int (n) / 2)):
        if int (n) % i == 0:
            return False
        
    return True

def countPrimes (m, n):
    count = 0
    for i in range (m, n + 1):
        if isPrime (i):
            count += 1
    return count

def sieve (lower, n):
    m = (n - 1) // 2
    b = [True] * m
    i, p, ps = 0, 3, [2]
    while p * p < n:
        if b[i]:
            ps.append (p)
            j = 2 * i * i + 6 * i + 3
            while j < m:
                b [j] = False
                j = j + 2 * i + 3
        i += 1; p += 2
    while i < m:
        if b [i]:
            ps.append (p)
        i += 1; p += 2
    count = 0
    for k in ps:
        if k >= lower:
            count += 1
    return (count)"""

def GetPrimes (n, low):
#Generates a list filled with 1's of size n
    Sieve = [1 for x in range (n)]
    #Iterates through list starting at 3 and skipping all even numbers
    temptemp = 0
    for q in range (3, n, 2):
        k = q
        if q == low or q == low - 1:
            temptemp = getCount (Sieve, q)
        if (Sieve [k] != 0):
            for y in range(k * k, n, k << 1):
                Sieve [y] = 0
    temp = getCount (Sieve, n)
    return temp - temptemp


def getCount (Sieve, p):
    count = 0
    for x in range (3, p, 2):
        if Sieve [x]:
            count += 1
    return count

serverPort = 16000
serverSocket = socket (AF_INET, SOCK_STREAM)
serverSocket.bind (("", serverPort))
serverSocket.listen (1)
print ("The server 2 is ready to receive")
while 1:

	connectionSocket, addr = serverSocket.accept()
	line = connectionSocket.recv (1024)
	str1, str2 = line.split (str.encode (" "))
	int1 = int (float (str1.decode ("ascii")))
	int2 = int (float (str2.decode ("ascii")))
	
	count = GetPrimes (int2, int1)
			
	ans = str.encode (str (count))
	
	connectionSocket.send (ans)
	connectionSocket.close()
	
