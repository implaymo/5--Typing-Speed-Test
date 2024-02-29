import time 

class Clock():
    def __init__(self, durantion_seconds) -> None:
        self.start_time = time.time()
        self.timer_duration = durantion_seconds
        
        
    
    def clock_timer(self):
        self.end_time = time.time()
        self.elapsed_time = self.end_time - self.start_time
        return self.elapsed_time
        
    def time_is_up(self):
        return self.elapsed_time >= self.timer_duration
    