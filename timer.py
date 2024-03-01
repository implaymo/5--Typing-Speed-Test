import time 

class Clock():
    def __init__(self, duration) -> None:
        self.duration = duration
        self.start_time = None
        
    def start(self):
        self.start_time = time.time()
        return self.start_time
    
    def elapsed_time(self):
        current_time = time.time()
        elapsed_time = current_time - self.start_time
        return elapsed_time

                
    def time_remaining(self):
        return max(0, self.duration - self.elapsed_time())

        

            
        