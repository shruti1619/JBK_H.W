import threading
import time

class job1(threading.Thread):
    def run(self):
        for i in range(5):
            print(threading.current_thread().name, "is running of run method")
            print("shruti")
            time.sleep(1)
        print("end of", threading.current_thread().name)
        
        
print("Main thread started")     
print(threading.current_thread().name)       
t1=job1()
t1.name="name of thread t1 by default it takes Thread-1"
t1.start()

for i in range(5):
    print(threading.current_thread().name)
    print("i am very successful")
    time.sleep(1)
print("end of main thread work")
    
    
print("end of main thread")