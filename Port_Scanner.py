'''
This is a tutorial i did to learn the threading, socket and Queue modules of python. This threading
layout can be used to apply to different uses, not just scanning ports.
'''
import socket
import threading
from queue import Queue

print_lock = threading.Lock()
target = "www.pythonprogramming.net"			#Target IP

def portscan(port):								#Port Scanning function. Replace this to thread something different.
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try:
		con = s.connect((target,port))
		with print_lock:
			print("Port",port,"is open!!!!")	
		con.close()
	except:
		pass
		
def threader():
	while True:
		worker = q.get()					#Gets work from the queue
		portscan(worker)
		q.task_done()
		
q = Queue()									#Creates a queue for threading

for x in range(10):							#This is how many workers you want
	t = threading.Thread(target=threader)	#Creating a thread
	t.daemon = True							
	t.start()
	
for worker in range(1,100):				#Assigning amount of jobs! ie, how many ports do you want to scan.
	q.put(worker)
	
q.join()	