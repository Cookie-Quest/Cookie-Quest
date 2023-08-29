# Lines 7 - 11 import the required modules for the web app. 
#Flask is used for creating and managing the web app and 
#render_remplate adn jasonify are used for rending HTML templates adn formatting JSON 
#respones respectively. The Selenium modules are imported for web scraping using selenium.
#The datatime module is used to handle the date and times information

from flask import Flask, render_template, jsonify
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import datetime



app = Flask(__name__)
#the function format_expiry takes an expiration timestamp and coverts it into 
#human-readable date and time format. If no timestamp is provided, it returns N/A
def format_expiry(expiry_timestamp):
    if expiry_timestamp:
        expiry_datetime = datetime.datetime.fromtimestamp(expiry_timestamp)
        return expiry_datetime.strftime('%Y-%m-%d %H:%M:%S')
    return "N/A"

#@app.route('/') associates the '/' URL endpoint with the index function 
#When a user access the root URL of the application, the index function is called
#Which returns an HTML template named 'index.html' 
@app.route('/')
def index():
    return render_template('index.html')


#This decorator (@app.route('/scan_cookies')) associates the /scan_cookies URL
#endpoint with the scanCookies() function. This function is responsible for 
#scanning cookies from a website. It configures chrome browser options, making it run in headless mode 
# and sets up the chrome service and Webdriver
@app.route('/scan_cookies')
def scan_cookies():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    service = Service('./driver/chromedriver.exe')
    driver = webdriver.Chrome(service=service, options=chrome_options)


#This section of code scans the specified website for cookies.
# It retrieves the cookies using driver.get_cookies(), iterates through them,
# and appends details about the cookies (if their names match those in the cookie_names list) 
# to the scanned_cookies list. After scanning, the WebDriver is closed, and a JSON response is generated 
# containing the scanned cookies.
    website_url = 'https://ironwoodins.com/'
    driver.get(website_url)

    cookie_names = [
        'osano_consentmanager',
        'osano_consentmanager_uuid',
        'TrustArc'
    ]

    cookies = driver.get_cookies()
    scanned_cookies = []

    for cookie in cookies:
        if cookie['name'] in cookie_names:
            scanned_cookies.append({
                'name': cookie['name'],
                'value': cookie['value'],
                'domain': cookie['domain'],
                'path': cookie['path'],
                'expiry': format_expiry(cookie['expiry']),
                'secure': cookie['secure']
            })

    driver.quit()
    return jsonify({'cookies': scanned_cookies})



#This block of code starts the Flask application only when the script is executed directly (not when imported as a module).
# It runs the app using app.run().
if __name__ == '__main__':
    app.run()
