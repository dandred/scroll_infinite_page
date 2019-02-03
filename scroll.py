from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

URL = 'http://scrollmagic.io/examples/advanced/infinite_scrolling.html'

# Change the n number to cover the entire lenght of the page
# Try different values of sleep_time_s, depending on how fast the sections are loading
def scroll(browser, n=100, sleep_time_s=4 ):
    for _ in range(n):
        browser.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)
        sleep(sleep_time_s)

# Call the scroll function
if __name__ == '__main__':
    browser = webdriver.Firefox()
    browser.get(URL)
    sleep(1)
    scroll(browser)    
    
