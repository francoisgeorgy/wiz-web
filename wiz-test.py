import socket
import json
import time


def send_udp_message(ip, port, message):
    addr = (ip, port)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(5)  # Set a timeout for the socket
    s.sendto(message, addr)
    try:
        data, _ = s.recvfrom(1024)  # Buffer size of 1024 bytes
        response = data.decode('utf-8')
    except socket.timeout:
        response = None
        print("No response received")
    s.close()
    return response


def main():
    # wiz_bulb_ip = input("bulb ip address: ")
    # wiz_bulb_port = int(input("bulb port: "))
    wiz_bulb_ip = '192.168.1.161'
    wiz_bulb_port = 38899

    message = {"method": "setPilot", "params": {"state": False}}
    message_json = json.dumps(message)
    response = send_udp_message(wiz_bulb_ip, wiz_bulb_port, message_json.encode())
    if response:
        print("Response from bulb:", response)

    time.sleep(2)

    message = {"method": "setPilot", "params": {"state": True}}
    message_json = json.dumps(message)
    response = send_udp_message(wiz_bulb_ip, wiz_bulb_port, message_json.encode())
    if response:
        print("Response from bulb:", response)


if __name__ == "__main__":
    main()
