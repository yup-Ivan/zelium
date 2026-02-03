import zelium as Zelium
import time

driver = Zelium.start()

Zelium.open("https://example.com/", driver)

Zelium.click("/html/body/div/p[2]/a", driver)

time.sleep(5)

driver.quit()
