import signal
import time

def handler(signum, frame):
    print("\nInterrupt received! Cleaning up before exit...")
    # Simulate cleanup work
    time.sleep(1)
    print("Cleanup done. Exiting now.")
    exit(0)

# Register handler for SIGINT (Ctrl+C)
signal.signal(signal.SIGINT, handler)

print("Processing... Press Ctrl+C to stop.")

# Simulate long-running process

while True:
    time.sleep(1)
    print("Working...")