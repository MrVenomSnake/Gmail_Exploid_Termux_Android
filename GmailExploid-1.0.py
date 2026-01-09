#   Author      : MrVenomSnake to Andy
#   Updated by  : MrVenomSnake (using Selenium for modern compatibility)
#   GitHub      : https://github.com/MrVenomSnake 
#   Year        : 2026
#   Description : GmailExploid-1.0 - Script for generating random Gmail account using Selenium.
#                 Handles modern Gmail UI but cannot automate CAPTCHA or phone verification.
#                 Stops at those steps and notifies user.
#                 Adapted for headless mode (no GUI) for compatibility with Android terminals like Termux.
#
#   Limitations : This script automates filling the signup form but requires manual intervention
#                 for CAPTCHA and phone verification. Automating account creation violates Google's
#                 Terms of Service and may lead to bans. Use at your own risk, preferably for testing
#                 or educational purposes only.

import sys
import time
import random
import string
import platform
import logging
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Setup logging
logging.basicConfig(filename='gmail_exploit.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Printing function with 3 modes
# 1 : Normal message
# 2 : Information message
# 3 : Caution message
def msg(_option_, _message_):
    if _option_ == 1:
        print('\x1b[0;32;40m> %s\x1b[0m' % _message_)
    elif _option_ == 2:
        print('\x1b[0;32;40m>\x1b[0m %s' % _message_)
    elif _option_ == 3:
        print('\n\x1b[0;32;40m[\x1b[0m%s\x1b[0;32;40m]\x1b[0m' % _message_)
    else:
        print('\n\x1b[0;31;40m[ERROR]\x1b[0m %s' % _message_)

# Exiting function
def ext():
    msg(1, 'Exiting...')
    sys.exit()

# Function to start browser with Selenium (adapted for headless and Android compatibility)
def open_browser(proxy=None):
    try:
        msg(1, 'Starting browser with Selenium (headless mode for Android compatibility)...')
        options = Options()
        # Set binary location based on OS
        if platform.system() == 'Windows':
            chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
            if os.path.exists(chrome_path):
                options.binary_location = chrome_path
                msg(2, f'Chrome binary found at: {chrome_path}')
            else:
                msg(4, f'Chrome binary not found at expected path: {chrome_path}')
        else:
            # On Linux/Android, let Selenium find Chromium in PATH
            msg(2, 'Using default Chromium binary for Linux/Android.')
        options.add_argument("--headless")  # No GUI for terminals
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920,1080")  # Simulate desktop for better compatibility
        # Rotate user-agents for evasion
        user_agents = [
            "Mozilla/5.0 (Linux; Android 10; SM-G975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.36",
            "Mozilla/5.0 (Linux; Android 11; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.210 Mobile Safari/537.36",
            "Mozilla/5.0 (Linux; Android 9; SM-G960F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36"
        ]
        selected_ua = random.choice(user_agents)
        options.add_argument(f"--user-agent={selected_ua}")
        msg(2, f'Selected user-agent: {selected_ua}')
        if proxy:
            options.add_argument(f'--proxy-server={proxy}')
            msg(2, f'Using proxy: {proxy}')
        service = Service(ChromeDriverManager().install())
        msg(2, f'ChromeDriver service installed at: {service.path}')
        driver = webdriver.Chrome(service=service, options=options)
        msg(1, 'Browser started successfully in headless mode.')
        return driver
    except Exception as e:
        msg(4, f'Failed to start browser: {e}')
        return None

# Function to navigate to Gmail signup
def navigate_to_gmail(driver):
    try:
        msg(1, 'Navigating to Gmail signup...')
        url = 'https://accounts.google.com/signup/v2/webcreateaccount?flowName=GlifWebSignIn&flowEntry=SignUp'
        driver.get(url)
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, 'firstName')))
        msg(1, 'Gmail signup page loaded.')
        return True
    except TimeoutException:
        msg(4, 'Failed to load Gmail signup page.')
        return False
    except Exception as e:
        msg(4, f'Error navigating to Gmail: {e}')
        return False

# Function to randomize credentials
def randomize(_option_, _length_):
    if _length_ > 0:
        if _option_ == '-p':
            characters = string.ascii_letters + string.digits + '!@#$%^&*()_+'
        elif _option_ == '-l':
            characters = string.ascii_letters
        elif _option_ == '-n':
            characters = string.digits
        elif _option_ == '-m':
            characters = 'JFMASOND'

        if _option_ == '-d':
            return random.randint(1, 28)
        elif _option_ == '-y':
            return random.randint(1950, 2000)
        else:
            return ''.join(random.choice(characters) for _ in range(_length_))
    else:
        msg(3, 'No valid length specified...')
        ext()

# Function to generate and fill info
def fill_form(driver):
    try:
        msg(1, 'Generating and filling credentials...')
        logging.info('Starting form fill')
        # Debug: Print input elements
        elements = driver.find_elements(By.TAG_NAME, 'input')
        msg(2, f"Total inputs: {len(elements)}")
        for i, e in enumerate(elements):
            name = e.get_attribute('name') or 'none'
            id_ = e.get_attribute('id') or 'none'
            placeholder = e.get_attribute('placeholder') or 'none'
            msg(2, f"Input {i}: name='{name}', id='{id_}', placeholder='{placeholder}'")
        # First name
        first_name = randomize('-l', 7)
        driver.find_element(By.NAME, 'firstName').send_keys(first_name)
        time.sleep(random.uniform(0.5, 1.5))
        # Last name
        last_name = randomize('-l', 8)
        driver.find_element(By.NAME, 'lastName').send_keys(last_name)
        time.sleep(random.uniform(0.5, 1.5))
        # Click Next to go to date step
        try:
            next_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Siguiente')]")))
            next_button.click()
            msg(2, 'Clicked Next button to date step')
            time.sleep(random.uniform(2, 4))  # Wait for page to load
        except Exception as e:
            msg(4, f'Failed to click Next: {e}')
            return False
        # Fill date
        day = randomize('-d', 1)
        year = randomize('-y', 1)
        driver.find_element(By.ID, 'day').send_keys(str(day))
        time.sleep(random.uniform(0.5, 1))
        driver.find_element(By.ID, 'year').send_keys(str(year))
        time.sleep(random.uniform(0.5, 1))
        # Month - custom dropdown (for mobile UI compatibility)
        month_num = random.randint(1, 12)
        months = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre']
        month_name = months[month_num - 1].capitalize()
        try:
            month_div = driver.find_element(By.ID, 'month')
            month_div.click()
            time.sleep(random.uniform(1, 2))  # Wait for options to appear
            option = driver.find_element(By.XPATH, f"//div[contains(text(), '{month_name}')]")
            option.click()
            msg(2, f'Filled date: {month_num}/{day}/{year} ({month_name})')
        except Exception as e:
            msg(4, f'Error selecting month: {e}')
            # Fallback: try if it's still a select
            try:
                from selenium.webdriver.support.ui import Select
                month_select = driver.find_element(By.ID, 'month')
                select = Select(month_select)
                select.select_by_value(str(month_num))
                msg(2, f'Filled date using Select: {month_num}/{day}/{year}')
            except:
                msg(4, 'Failed to fill month, continuing...')
        # Click Next again to go to username step
        try:
            next_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Siguiente')]")))
            next_button.click()
            msg(2, 'Clicked Next button to username step')
            time.sleep(random.uniform(2, 4))
        except Exception as e:
            msg(4, f'Failed to click Next again: {e}')
            return False
        # Username (add @gmail.com implicitly)
        username = randomize('-l', 10)
        driver.find_element(By.ID, 'username').send_keys(username)
        time.sleep(random.uniform(0.5, 1.5))
        # Password
        password = randomize('-p', 16)
        driver.find_element(By.NAME, 'Passwd').send_keys(password)
        time.sleep(random.uniform(0.5, 1))
        driver.find_element(By.NAME, 'ConfirmPasswd').send_keys(password)
        time.sleep(random.uniform(0.5, 1))
        msg(2, f'Name: {first_name} {last_name}')
        msg(2, f'Username: {username}')
        msg(2, f'Password: {password}')
        # Save credentials
        with open('generated_accounts.txt', 'a') as f:
            f.write(f'Username: {username}@gmail.com\nPassword: {password}\nName: {first_name} {last_name}\nBirth: {month_name} {day}, {year}\n\n')
        logging.info(f'Credentials saved for {username}@gmail.com')
        # Birth date (already filled above)
        # For simplicity, click next or submit
        driver.find_element(By.ID, 'accountDetailsNext').click()  # Next button
        msg(2, f'Date of birth: {month_name} {day}, {year}')
        # Gender: Rather not say (might need to select)
        # Wait for next page
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'view_container')))
        # Check for CAPTCHA
        try:
            captcha = driver.find_element(By.CLASS_NAME, 'recaptcha-checkbox-border')  # Approximate
            msg(3, 'CAPTCHA detected. Please solve it manually and press Enter to continue.')
            input('Press Enter after solving CAPTCHA...')
        except NoSuchElementException:
            msg(1, 'No CAPTCHA found.')
        # Phone verification (impossible to automate)
        msg(3, 'Phone verification required. Cannot proceed automatically. Script will stop here.')
        logging.info('Form fill completed, waiting for manual verification')
        return True
    except Exception as e:
        msg(4, f'Error filling form: {e}')
        logging.error(f'Error in fill_form: {e}')
        return False

# Main function
if __name__ == '__main__':
    proxy = input('Enter proxy (e.g., http://proxy_ip:port) or leave blank: ').strip() or None
    driver = open_browser(proxy)
    if not driver:
        ext()
    if not navigate_to_gmail(driver):
        driver.quit()
        ext()
    if not fill_form(driver):
        driver.quit()
        ext()
    msg(1, 'Form filled. In headless mode, browser is running in background.')
    msg(3, 'To complete: Use a separate browser or device to access the same session if possible, or check logs/screenshots.')
    msg(3, 'CAPTCHA and phone verification must be done manually on the target device.')
    # Keep browser open briefly for headless
    time.sleep(5)  # Give time for any async operations
    driver.quit()
    msg(1, 'Done...')