# Import necessary modules
import datetime
import time

# Define the end time for blocking websites
end_time = datetime.datetime(2025, 4, 24)

# List of websites to block
site_block = ["www.jiocinema.com", "www.facebook.com"]

# Path to the hosts file (Windows system)
host_path = "C:/Windows/System32/drivers/etc/hosts"

# IP address to redirect blocked websites to (localhost)
redirect = "127.0.0.1"

# Infinite loop to keep the script running
while True:
    # Check if current time is before the blocking end time
    if datetime.datetime.now() < end_time:
        print("Start blocking websites...")

        # Open the hosts file in read and write mode
        with open(host_path, "r+") as host_file:
            content = host_file.read()
            for website in site_block:
                # If the website is not already blocked, add it
                if website not in content:
                    host_file.write(redirect + " " + website + "\n")
                else:
                    # If website already blocked, do nothing
                    pass
    else:
        # If current time is after the end time, unblock the websites
        with open(host_path, "r+") as host_file:
            content = host_file.readlines()
            host_file.seek(0)
            for lines in content:
                # Rewrite only those lines which do not contain blocked websites
                if not any(website in lines for website in site_block):
                    host_file.write(lines)
            # Truncate the file to remove leftover blocked websites
            host_file.truncate()

        # Sleep for 5 seconds before next check to avoid excessive CPU usage
        time.sleep(5)
