import time
import mechanicalsoup

browser = mechanicalsoup.Browser()


for i in range(4):

    page = browser.get("http://olympus.realpython.org/dice")
    page_html = page.soup
    tag = page_html.select('#result')[0]
    result = tag.text

    print(f"The result of the dice roll is: {result}")
    if i < 3:
        time.sleep(10)
