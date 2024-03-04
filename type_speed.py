import time

class Speed():
    """Class to calculate typing speed based on elapsed time and total words."""

    def typing_speed_result(self, total_words, start_time):
        """Calculate and return typing speed."""
        if start_time is None:
            return "Start time not available"
        
        elapsed_time = time.time() - start_time
        minutes = elapsed_time / 60
        speed = total_words / minutes
        return f"{speed:.2f} words per minute"