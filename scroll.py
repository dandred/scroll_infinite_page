from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

URL = 'http://scrollmagic.io/examples/advanced/infinite_scrolling.html'

def scroll(browser):
    for _ in range(100):  # this number should be large enough to cover the entire length of the page
        browser.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)
        sleep(4)  # try different values depending on how fast the page is loading

browser = webdriver.Firefox()
browser.get(URL)
sleep(1)

# Call the scroll function
if __name__ == '__main__':
    scroll(browser)
    
    
