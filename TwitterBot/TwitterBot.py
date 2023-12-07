from selenium import webdriver
import time

# Configure webdriver options
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument("--disable-notifications")

# Set webdriver path to the chromedriver.exe location
driver_path = "D:\\LEO\\TwitterBot\\chromedriver.exe"

# Initialize the webdriver
driver = webdriver.Chrome(executable_path=driver_path, options=options)

# Navigate to the Twitter login page
driver.get("https://twitter.com/login")

# Wait for the page to load
time.sleep(2)

# Enter login credentials
email_xpath = "//input[@name='session[username_or_email]']"
password_xpath = "//input[@name='session[password]']"
login_xpath = "//div[@data-testid='LoginForm_Login_Button']"

email = "thor@gmail.com"
password = "12345676"

driver.find_element_by_xpath(email_xpath).send_keys(email)
driver.find_element_by_xpath(password_xpath).send_keys(password)
driver.find_element_by_xpath(login_xpath).click()

# Wait for the page to load
time.sleep(5)

# Close the webdriver
driver.quit()
