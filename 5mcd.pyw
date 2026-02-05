#!/usr/bin/python
### Matt Eckelman  Oct 2, 2025
### 

import tkinter as tk
from tkinter import font
import time

# --- Configuration ---
# Initial time in seconds (5 minutes = 300 seconds)
INITIAL_TIME_SECONDS = 300
# Approximating a 2-inch height (font size 200pt is visually large)
FONT_SIZE = 400 
FONT_FAMILY = "Inter" # Using a modern, clear font

class CountdownTimerApp:
    def __init__(self, master):
        self.master = master
        master.title("5 Minute Countdown Timer")
        
        # Current time state, initialized to 300 seconds
        self.current_time_left = INITIAL_TIME_SECONDS
        self.is_running = True

        # Center the window and make it dark for high contrast
        master.config(bg="#1E1E1E") 
        master.attributes('-fullscreen', True) # Keep the timer on top, fullscreen
        
        # 1. Define the custom, large font
        self.timer_font = font.Font(family=FONT_FAMILY, size=FONT_SIZE, weight="bold")
        
        # 2. Create the display label
        self.time_label = tk.Label(
            master, 
            text="5:00", 
            font=self.timer_font, 
            fg="#FFD700", # Gold color for visibility
            bg="#1E1E1E"
        )
        # Use pack to center the widget and expand to fill available space
        self.time_label.pack(expand=True, padx=50, pady=50)

        # 3. Start the countdown loop
        self.update_timer()

    def update_timer(self):
        """
        Updates the timer label every second.
        This function is called recursively using master.after(1000, ...)
        """
        if not self.is_running:
            return

        if self.current_time_left > 0:
            # Decrement time
            self.current_time_left -= 1

            # Calculate minutes and seconds
            minutes = self.current_time_left // 60
            seconds = self.current_time_left % 60
            
            # Format the time string (M:SS format)
            time_string = f"{minutes}:{seconds:02d}"
            
            # Update the label text
            self.time_label.config(text=time_string)
            
            # Schedule the next update after 1000 milliseconds (1 second)
            self.master.after(1000, self.update_timer)
            
        else:
            # Time has run out
            self.is_running = False
            self.timer_font.configure(family=FONT_FAMILY, size=200, weight="bold")
            self.master.update()
            self.time_label.config(text="Service\n Starting!", fg="#FF4500") # Red color for final message
            self.master.update()
            time.sleep(60)
            self.master.destroy()
            
            # Stop updating further

# --- Main Application Execution ---
if __name__ == "__main__":
    root = tk.Tk()
    app = CountdownTimerApp(root)
    # Start the Tkinter event loop
    root.mainloop()

