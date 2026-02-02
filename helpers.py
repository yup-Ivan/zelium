# Zelium/helpers.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def wait(driver, condition, timeout=5):
    return WebDriverWait(driver, timeout).until(condition)


def find(xpath, driver, timeout=5, visible=False):
    condition = (
        EC.visibility_of_element_located
        if visible else EC.presence_of_element_located
    )
    return wait(driver, condition((By.XPATH, xpath)), timeout)


def scroll(elem, driver):
    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});", elem
    )


def js_click(elem, driver):
    driver.execute_script("arguments[0].click();", elem)
