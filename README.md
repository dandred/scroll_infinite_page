# scroll_infinite_page
When other methods to scrape an infinite page fail, you can use the <a href="https://selenium-python.readthedocs.io/">Selenium</a> library with <a href="https://selenium-python.readthedocs.io/api.html?highlight=PAGE_DOWN#module-selenium.webdriver.common.keys">PAGE_DOWN</a> key. Depending on the web page, you will only have to experiment with the sleep time between page down commands.

```
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

```
