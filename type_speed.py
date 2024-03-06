import time

class Speed():
    """Class to calculate typing speed based on elapsed time and total words."""
    def __init__(self) -> None:
        self.current_score = 0
            

    def typing_speed_result(self, total_words, start_time):
        """Calculate and return typing speed."""
        if start_time is None:
            return "Start time not available"
        
        elapsed_time = time.time() - start_time
        minutes = elapsed_time / 60
        speed = total_words / minutes
        self.current_score = speed
        self.typing_high_score()
        return f"{speed:.2f} words per minute"
    
    def typing_high_score(self):
        """ Stores highest score ever made"""
        self.new_highscore = False
        try:
            with open('highscores_storage.txt', 'r') as file:
                content = file.read()
                high_score = float(content)
                if self.current_score > high_score:
                    high_score = self.current_score
                    with open('highscores_storage.txt', 'w') as write_file:
                        write_file.write(str(round(high_score, 2)))
                        self.new_highscore = True
                
        except FileNotFoundError:
                with open('highscores_storage.txt', 'w') as file:
                    high_score = 0.0
                    file.write(str(high_score))
                with open('highscores_storage.txt', 'r') as read_file:
                    content = read_file.read()
                    high_score = float(content)
                    return round(high_score, 2)
        else:   
            return round(high_score, 2)