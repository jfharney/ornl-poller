import threading
import time

exitFlag = 0


def print_tim(threadName, delay, counter):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print "%s: %s" % (threadName, time.ctime(time.time()))
        counter -= 1

class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print "Starting " + self.name + "\n"
        print_tim(self.name, self.counter, 5)
        print "Exiting " + self.name



from Queue import Queue

from threading import Thread

import time

def main():
    
    #poller()
    #Wf = Workflow()
    
    #Wf.apple()
    
    #print 'dir: ' + str(dir(threading))
    
    #prod_cons()
    
    
     
    
    #poller()


def prod_cons(num_threads=1):
    
    num_threads = 1
    
    q = Queue(maxsize=0)
    
    
    def do_stuff(q):
        while True:
            print "q.get(): " + str(q.get()) + " Done by " + str(threading.current_thread())
            q.task_done()
    
    for i in range(num_threads):
        worker = Thread(target=do_stuff,name="Thread " + str(i),args=(q,))
        worker.setDaemon(True)
        worker.start()
    
    
    for y in range(1):
        for x in range(10):
            q.put((x+y)*100)
        q.join()
        print "Batch " + str(y) + " Done"
    
    q.join()
    
    
    # Define a function for the thread
def print_time( threadName, delay):
   count = 0
   while count < 5:
      time.sleep(delay)
      count += 1
      print "%s: %s" % ( threadName, time.ctime(time.time()) )



if __name__ == "__main__": main()


