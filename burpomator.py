"""Simple BURP Scanner Professional API Wrapper"""

import os
import requests
from dotenv import load_dotenv


class Scanner:
    """Creates a BURP Scanner Object to interact with Professional REST API"""

    load_dotenv("./.env")

    def __init__(self):
        self.api_key = os.getenv("API_KEY")
        self.scan_host = "127.0.0.1"
        self.scan_port = "1337"
        self.scan_proto = "http://"
        self.rest_api = (
            f"{self.scan_proto}{self.scan_host}:{self.scan_port}/{self.api_key}/v0.1"
        )

    def scan(self, urls):
        """Scans target URLs using BURP Scanner Professional API"""

        # Check out the API definition for scan configuration options
        data = {"urls": [urls]}
        headers = {"Content-Type": "application/json"}
        endpoint = f"{self.rest_api}/scan"
        response = requests.post(endpoint, json=data, headers=headers)
        if response.status_code == 201:
            print("Scan Successfully Started")
        elif response.status_code == 401:
            print("Unauthorized. Check API_KEY or .env")
        else:
            print("Scan Failed to Start: Code", response.status_code)
            print(response.json().get("error"))


if __name__ == "__main__":
    # Create a Scanner object
    scanner = Scanner()
    # Define a target
    TARGET = "http://127.0.0.1:3000"
    # Start the scan
    scanner.scan(urls=TARGET)
