import time
import smtplib
from selenium import webdriver
from selenium.webdriver.common.by import By


def get_driver(URL):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)

    driver = webdriver.Chrome(options=options)
    driver.get(URL)
    return driver


def send_alert(percentage_change):
    # Set up the email server and send the email
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login("mahamud.0.khalid@gmail.com", "gfnfucfessmvuois")

    subject = "Stock Alert: Price Drop"
    body = f"The stock price has dropped to {percentage_change}%."
    message = f"Subject: {subject}\n\n{body}"

    server.sendmail("mahamud.0.khalid@gmail.com", "khalid.0.mahamud@gmail.com", message)
    server.quit()


def check_stock_price(url):
    driver = get_driver(url)
    time.sleep(2)
    
    percentage_change_element = driver.find_element(
        By.XPATH, "//*[@id='app_indeks']/section[1]/div/div/div[2]/span[2]"
    )
    percentage_change = float(percentage_change_element.text.strip("%"))
    print(percentage_change)
    
    if percentage_change < 0:
        send_alert(percentage_change)


if __name__ == "__main__":
    url = "https://zse.hr/en/indeks-366/365?isin=HRZB00ICBEX6"
    while True:
        check_stock_price(url)
        time.sleep(300)  # Wait for 5 minutes before checking again
