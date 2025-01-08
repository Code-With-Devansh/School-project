import threading
import time
import signal
import sys
import keyboard

# Function to play music
def play_music():
    print("Playing music...")
    while True:
        pass

# Function to handle stopping music on Ctrl+C
def stop_music():
    print("Press Ctrl+C to stop the music.")
    signal.signal(signal.SIGINT, handler)  # Set up the signal handler for Ctrl+C
    while True:
        time.sleep(1)  # Keep the main thread alive to handle signal interrupts

# Signal handler to stop the music when Ctrl+C is pressed
def handler(signal, frame):
    print("\nStopping the music...")
    sys.exit(0)  # Exit the program gracefully when Ctrl+C is pressed

# Create and start the threads
if __name__ == "__main__":
    # Start the music-playing thread
    music_thread = threading.Thread(target=play_music, daemon=True)
    music_thread.start()
    
    # Start the thread that listens for Ctrl+C to stop the music
    stop_thread = threading.Thread(target=stop_music)
    stop_thread.start()

    # Keep the main thread alive
    stop_thread.join()
