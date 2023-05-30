import argparse
import requests
from glob import glob

def main():
    parser = argparse.ArgumentParser(description='Fate Grand Order APK Sender')
    parser.add_argument('-d', '--discord', help='Discord Webhook URL')

    args = parser.parse_args()
    discord = args.discord
    apks = glob("*.apk")

    for apk in apks:
        with open(apk, 'rb') as file:
            data = {f'{apk.replace("./", "")}': file}
            requests.post(discord, files=data)

if __name__ == "__main__":
    main()
