# Scroll an infinite page with Python and Selenium
When other methods to scrape an infinite page fail, you can use the <a href="https://selenium-python.readthedocs.io/">Selenium</a> library with <a href="https://selenium-python.readthedocs.io/api.html?highlight=PAGE_DOWN#module-selenium.webdriver.common.keys"><b>PAGE_DOWN</b></a> key. 
Depending on how fast the web page is loading the next section, you will have to experiment with the sleep time between page down commands. Most of the "infinite" pages are actually finite, so the number of iterations depends on the length of the page. If there are more iterations then necessary, the for loop will reach the end of the page and will continue to execute without error, but it will add a delay.


```
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

URL = 'http://scrollmagic.io/examples/advanced/infinite_scrolling.html'

def scroll(browser):
    for _ in range(100):  # change this number to cover the entire lenght of the page
        browser.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)
        sleep(4)  # try different values depending on how fast the page is loading

browser = webdriver.Firefox()
browser.get(URL)
sleep(1)

# Call the scroll function
scroll(browser)

```
