from selenium import webdriver


def before_all(context):
    """Start web driver"""
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    context.browser = webdriver.Chrome(chrome_options=chrome_options)
    context.browser.set_window_size(1280, 920)
    context.browser.implicitly_wait(10)


def after_all(context):
    context.browser.quit()
