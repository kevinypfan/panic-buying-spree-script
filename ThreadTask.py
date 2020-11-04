from threading import Thread

class CountdownTask: 
      
    def __init__(self): 
        self._running = True
        
    def terminate(self): 
        self._running = False
        
    def run(self, func): 
        while self._running: 
            func()
  
c = CountdownTask() 
t = Thread(target = c.run, args =(10, )) 
t.start() 
# Signal termination 
c.terminate()  
  
# Wait for actual termination (if needed)  
t.join()