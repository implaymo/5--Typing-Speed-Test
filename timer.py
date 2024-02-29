import time 

class Clock():
    def __init__(self, duration) -> None:
        self.duration = duration
        
    def start_timer(self):
        start_time = time.time()
        
        while True:
            current_time = time.time()
            elapsed_time = current_time - start_time
            remaining_time = self.duration - elapsed_time
            
            if remaining_time <= 0: 
                print("Time's up!")
                
                
            print(f"Time remaining: {int(remaining_time)} seconds")
            time.sleep(1)
        

            
        