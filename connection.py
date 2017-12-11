from selenium import webdriver

class Connection():

    # ############################ browser configuration
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options)

