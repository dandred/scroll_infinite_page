# Using Selenium library and PAGE_DOWN to scroll an infinite page
When other methods to process an infinite page *fail*, you can use the <a href="https://selenium-python.readthedocs.io/">Selenium</a> library with <a href="https://selenium-python.readthedocs.io/api.html?highlight=PAGE_DOWN#module-selenium.webdriver.common.keys">PAGE_DOWN</a> key. 
Depending on how fast the web page is loading the next section, you will have to experiment with the sleep time between page down commands. Most of the "infinite" pages are actually finite, so the number of iterations depends on the length of the page. If there are more iterations then necessary, the for loop will reach the end of the page and will continue to execute without error, but it will add a delay.


```python
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
    
```
