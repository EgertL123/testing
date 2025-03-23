from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test():
    # Configure Firefox options
    options = webdriver.FirefoxOptions()
    profile_path = "/path/to/your/firefox/profile"  # Replace with your profile path
    options.profile = profile_path

    # Set up the Firefox driver with the options
    driver = webdriver.Firefox(options=options)

    # Open Google's website
    driver.get("https://www.google.com")

    # Wait for the page to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "q"))
    )

    try:
        # Wait and find the "Reject All" button
        reject_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[text()="Reject all"]'))
        )
        reject_button.click()  # Click the "Reject All" button
        print("Cookie consent rejected.")
    except Exception as e:
        print("Cookie consent button not found or already rejected.")

    # Find the search box
    search_box = driver.find_element(By.NAME, "q")

    # Enter a search query and press Enter
    search_box.send_keys("Selenium Python tutorial")
    search_box.send_keys(Keys.RETURN)

    # Wait for the results to load
    time.sleep(2)

    # Display the first few results
    search_results = driver.find_elements(By.XPATH, '//h3')
    for result in search_results[:5]:  # Display only the first 5 results
        print(result.text)

    # Close the browser
    driver.quit()

if __name__ == "__main__":
    test()
