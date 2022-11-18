from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

binary = FirefoxBinary(r'C:\Program Files\Firefox Developer Edition\firefox.exe')

options = Options()
options.headless = True
options.binary = binary

browser = webdriver.Firefox(options=options)


browser.get("https://rateyourmusic.com/charts/top/album/all-time/")
html = browser.page_source
browser.close()
browser.quit()

print(html)

