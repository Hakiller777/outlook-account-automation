import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import time

def main():
    # Initialize Chrome browser using undetected_chromedriver to avoid bot detection
    driver = uc.Chrome()
    
    # Open the Microsoft Outlook signup page
    driver.get("https://signup.live.com/signup")
    print("🚀 Page loaded")

    # Create a wait object to wait for elements to be clickable or present
    wait = WebDriverWait(driver, 30)

    try:
        # Wait for the email input field to be clickable and select it
        email_input = wait.until(EC.element_to_be_clickable((By.ID, "floatingLabelInput5")))
        print("✅ Email input found")
        email_input.click()  # Click to focus the field
        time.sleep(0.5)
        email_input.clear()  # Clear any pre-filled text
        
        # IMPORTANT: Replace the email below with your own email address before running the script
        email_input.send_keys("your_email@example.com")  # Enter the email address
        print("📧 Email entered")

        # Wait for the 'Next' button and click it
        next_button = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(text(),'Next') or contains(text(),'Siguiente')]")
        ))
        next_button.click()
        print("➡️ Clicked on Next")

        # Wait for the verification code input field to appear
        print("⏳ Waiting for code input field...")
        wait.until(EC.presence_of_element_located((By.NAME, "otc")))
        print("📍 Now manually enter the verification code in the browser.")

        # Pause the script until user confirms they've entered the code
        input("🕐 Press Enter once you have entered the code...")

        # Fill in the country and birthdate form fields using dropdown selects
        print("🚀 Filling in country and birth date...")

        country = Select(wait.until(EC.presence_of_element_located((By.NAME, "Country"))))
        country.select_by_value("PY")  # Select Paraguay

        day = Select(wait.until(EC.presence_of_element_located((By.NAME, "BirthDay"))))
        day.select_by_value("10")  # Day 10

        month = Select(wait.until(EC.presence_of_element_located((By.NAME, "BirthMonth"))))
        month.select_by_value("1")  # January (month 1)

        year = Select(wait.until(EC.presence_of_element_located((By.NAME, "BirthYear"))))
        year.select_by_value("1995")  # Year 1995

        print("📆 Personal data filled")

        # Click the 'Next' button to proceed
        next_btn = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(text(),'Siguiente') or contains(text(),'Next')]")
        ))
        next_btn.click()
        print("✅ Clicked 'Next'. Moving to the next step.")

    except Exception as e:
        # Print any error encountered during the process
        print(f"❌ Error: {e}")

    # Keep the browser open indefinitely so you can see what happens
    print("📌 The browser will stay open indefinitely. To close the script, close this window or kill the process manually.")
    while True:
        time.sleep(60)

if __name__ == "__main__":
    main()

# --------------------------------------------------------------------------------
# NOTE:
# This script is a demonstration of how to automate the signup process on Microsoft's
# website using undetected_chromedriver and Selenium.
#
# It requires manual input for the verification code step.
#
# The email address used in the script should be replaced by your own before running.
#
# This project is a work in progress and can be further developed or customized.
# Feel free to use and modify it according to your needs.
# --------------------------------------------------------------------------------
