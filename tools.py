# zelium/tools.py
from selenium.common.exceptions import WebDriverException

def open(url, driver):
    try:
        driver.get(url)
    except WebDriverException as e:
        print(f"[WebDriverError] No se pudo abrir {url}: {e}")
    except Exception as e:
        print(f"[Error inesperado] No se pudo abrir {url}: {type(e).__name__}: {e}")
