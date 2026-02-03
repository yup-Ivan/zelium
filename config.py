# zelium/config.py
import os
from seleniumwire import webdriver as sw_webdriver
from selenium import webdriver as selenium_normal
from selenium.webdriver.chrome.options import Options

from .alarm import Alarm
from .js import JS


def start(modo="normal", proxy=None, headless=False, usar_seleniumwire=True, perfil=None,):
    """
    Inicia un navegador Chrome con distintas opciones.

    Args:
        modo (str): "normal", "limpio" o "extension"
        proxy (str | None): proxy en formato host:puerto
        headless (bool): ejecutar Chrome en modo headless
        usar_seleniumwire (bool): usar Selenium Wire (necesario si hay proxy)
        perfil (str | None): ruta a perfil de Chrome (modo extension)

    Returns:
        webdriver.Chrome: instancia del driver
    """

    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--log-level=3")
    chrome_options.add_argument("--remote-debugging-port=0")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--blink-settings=imagesEnabled=false")
    chrome_options.add_experimental_option(
        "excludeSwitches", ["enable-logging"]
    )

    chrome_options.add_argument(
        "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/115.0.0.0 Safari/537.36"
    )

    if headless:
        chrome_options.add_argument("--headless=new")

    # ─────────────────────────────
    # Modo de ejecución
    # ─────────────────────────────
    if modo == "extension":
        perfil_path = perfil or r"C:\SeleniumProfile"
        os.makedirs(perfil_path, exist_ok=True)
        chrome_options.add_argument(
            f"--user-data-dir={os.path.abspath(perfil_path)}"
        )

    elif modo == "limpio":
        chrome_options.add_argument("--incognito")

    # ─────────────────────────────
    # Proxy
    # ─────────────────────────────
    seleniumwire_options = {}

    if proxy:
        if usar_seleniumwire:
            seleniumwire_options = {
                "proxy": {
                    "http": f"http://{proxy}",
                    "https": f"http://{proxy}",
                    "no_proxy": "localhost,127.0.0.1",
                },
                "verify_ssl": False,
            }
        else:
            chrome_options.add_argument(
                f"--proxy-server=http://{proxy}"
            )

    # ─────────────────────────────
    # Inicializar driver
    # ─────────────────────────────
    if usar_seleniumwire and proxy:
        driver = sw_webdriver.Chrome(
            options=chrome_options,
            seleniumwire_options=seleniumwire_options,
        )
    else:
        driver = selenium_normal.Chrome(options=chrome_options)

    # ─────────────────────────────
    # Inyectar driver en módulos
    # ─────────────────────────────
    Alarm.set_driver(driver)
    JS.set_driver(driver)

    return driver
