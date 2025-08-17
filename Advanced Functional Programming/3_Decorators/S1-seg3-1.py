import atexit

# Function to save logs or clean up resources at program exit

@atexit.register
def save_logs():
    
    print("Saving logs before program exit...")
    
    # Simulate saving logs (could be file/database operations)
    with open("app_logs.txt", "a") as f:
        f.write("Application closed properly.\n")

print("Program is running...")

# When the script ends, save_logs() will run automatically