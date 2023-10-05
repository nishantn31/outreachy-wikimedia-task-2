
# Python script to validate and return status code of URLs in CSV file

import csv
import requests
import re


def get_url(row: str):
    """
    Get URL from CSV row
    """
    if len(row) > 0:
        url = row[0]
        # Validating the URL using RegEx
        url_pattern = r"^(https?://)?([a-zA-Z0-9.-]+\.[a-zA-Z]{2,4})(/.*)?$"
        if re.match(url_pattern, url):
            return url
        raise Exception("Invalid URL")
    raise Exception("URL Not Found")


def get_status_code(url: str):
    """
    Get status code of URL
    """
    try:
        response = requests.get(url)
        return response.status_code
    except Exception:
        raise Exception(f"Error")


# Read CSV and get status code of URL from each row
with open("intern.csv", "r") as file:
    csv_data = csv.reader(file)
    next(csv_data)  # skip header
    for row in csv_data:
        try:
            url = get_url(row)
            status_code = get_status_code(url)
            print(f"({status_code}) {url}")
        except Exception as e:
            print(f"({e}) {url}")
