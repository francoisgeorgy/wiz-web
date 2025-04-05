#!/opt/homebrew/bin/python3

import socket
import json
import sys
import os
from pathlib import Path

wiz_bulb_ip = '192.168.1.161'
wiz_bulb_port = 38899

PRESET_DIR = os.path.join(Path.home(), ".wiz")
if not os.path.exists(PRESET_DIR):
    os.makedirs(PRESET_DIR)


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


def wiz_get_status():
    message = {"method": "getPilot"}
    message_json = json.dumps(message)
    response = send_udp_message(wiz_bulb_ip, wiz_bulb_port, message_json.encode())
    if response:
        print("Bulb status:", response)
    else:
        print("Failed to retrieve bulb status.")


def wiz_percent(pc):
    message = {"method": "setPilot", "params": {"dimming": pc}}
    message_json = json.dumps(message)
    send_udp_message(wiz_bulb_ip, wiz_bulb_port, message_json.encode())
    print(f"Set dimming to {pc}%")


def wiz_temp(temp):
    message = {"method": "setPilot", "params": {"temp": temp}}
    message_json = json.dumps(message)
    send_udp_message(wiz_bulb_ip, wiz_bulb_port, message_json.encode())
    print(f"Set color temperature to {temp}K")


def wiz_scene(scene_id):
    message = {"method": "setPilot", "params": {"sceneId": scene_id}}
    message_json = json.dumps(message)
    send_udp_message(wiz_bulb_ip, wiz_bulb_port, message_json.encode())
    print(f"Set scene to {scene_id}")


def wiz_save_preset(preset_name):
    message = {"method": "getPilot"}
    message_json = json.dumps(message)
    response = send_udp_message(wiz_bulb_ip, wiz_bulb_port, message_json.encode())
    if response:
        preset_file = os.path.join(PRESET_DIR, f"preset_{preset_name}.json")
        with open(preset_file, "w") as file:
            file.write(response)
        print(f"Preset '{preset_name}' saved.")
    else:
        print("Failed to save preset.")


def wiz_recall_preset(preset_name):
    preset_file = os.path.join(PRESET_DIR, f"preset_{preset_name}.json")
    if os.path.exists(preset_file):
        with open(preset_file, "r") as file:
            preset_data = json.load(file)
        message = {"method": "setPilot", "params": preset_data.get("result", {})}
        message_json = json.dumps(message)
        send_udp_message(wiz_bulb_ip, wiz_bulb_port, message_json.encode())
        print(f"Preset '{preset_name}' recalled.")
    else:
        print(f"Preset '{preset_name}' does not exist.")


def main():
    if len(sys.argv) == 1:
        wiz_get_status()
        sys.exit(0)

    command = sys.argv[1].strip().lower()

    # Handle dimming directly with or without "dim" keyword
    if command.isnumeric():
        try:
            percent = int(command)
            if 0 <= percent <= 100:
                wiz_percent(percent)
            else:
                print("Please provide a dimming value between 0 and 100.")
        except (IndexError, ValueError):
            print("Error: invalid argument")
    elif command == "dim":
        try:
            percent = int(sys.argv[2])
            if 0 <= percent <= 100:
                wiz_percent(percent)
            else:
                print("Please provide a dimming value between 0 and 100.")
        except (IndexError, ValueError):
            print("Error: invalid argument")
    elif command == "temp":
        try:
            temp = int(sys.argv[2])
            wiz_temp(temp)
        except (IndexError, ValueError):
            print("Usage: temp <value>")
    elif command == "scene":
        try:
            scene_id = int(sys.argv[2])
            wiz_scene(scene_id)
        except (IndexError, ValueError):
            print("Usage: scene <id>")
    elif command in ["save", "s"]:
        try:
            preset_name = sys.argv[2]
            wiz_save_preset(preset_name)
        except IndexError:
            print("Usage: save <name>")
    elif command in ["recall", "r"]:
        try:
            preset_name = sys.argv[2]
            wiz_recall_preset(preset_name)
        except IndexError:
            print("Usage: recall <name>")
    else:
        print("Invalid command. Available commands:")
        print("  <value>           - Set dimming (0-100)")
        print("  dim <value>       - Set dimming (optional keyword)")
        print("  temp <value>      - Set color temperature (Kelvin)")
        print("  scene <id>        - Set scene ID")
        print("  save <name>       - Save current settings as preset")
        print("  recall <name>     - Recall saved preset")
        sys.exit(1)


if __name__ == "__main__":
    main()
