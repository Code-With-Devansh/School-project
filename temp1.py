import threading
import time
import sys

# Event that will signal the music thread to stop
stop_event = threading.Event()

# Function to play music
def play_music():
    try:
        print("Playing music...")
        while True:
            pass
    except Exception as e:
        print(f"Error playing music: {e}")
    print("Music finished or stopped.")

# Function to handle the main thread listening for Ctrl+C
def listen_for_ctrl_c():
    try:
        print("Press Ctrl+C to stop the music.")
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nCtrl+C pressed. Stopping music...")
        stop_event.set()  # Signal the music thread to stop
        sys.exit(0)  # Exit gracefully

# Create and start the music thread
music_thread = threading.Thread(target=play_music, daemon=True)
music_thread.start()

# Start the thread that listens for Ctrl+C
listen_for_ctrl_c()
