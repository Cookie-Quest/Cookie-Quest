from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import datetime

def format_expiry(expiry_timestamp):
    if expiry_timestamp:
        expiry_datetime = datetime.datetime.fromtimestamp(expiry_timestamp)
        return expiry_datetime.strftime('%Y-%m-%d %H:%M:%S')
    return "N/A"

def scan_website(website_url):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    service = Service('./driver/chromedriver.exe')
    driver = webdriver.Chrome(service=service, options=chrome_options)

    print(f"Scanning website: {website_url}")
    driver.get(website_url)
    print("Page title:", driver.title)

    cookie_names = [
        'osano_consentmanager',
        'osano_consentmanager_uuid',
        'TrustArc',
        'JSESSIONID'
    ]

    cookies = driver.get_cookies()
    
    for cookie in cookies:
        if cookie['name'] in cookie_names:
            print(f"Cookie Name: {cookie['name']}")
            print(f"Value: {cookie['value']}")
            print(f"Domain: {cookie['domain']}")
            print(f"Path: {cookie['path']}")
            print(f"Expires: {format_expiry(cookie['expiry'])}")
            print(f"Secure: {cookie['secure']}")
            print("-----")

    driver.quit()

def main():
    website_urls = [
        'https://ironwoodins.com/',
        # Add more website URLs here
    ]

    print("Starting the script")
    for url in website_urls:
        scan_website(url)
    print("Script execution finished")

if __name__ == "__main__":
    main()
