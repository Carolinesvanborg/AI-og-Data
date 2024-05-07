import mechanicalsoup

browser = mechanicalsoup.Browser()
page = browser.get("http://olympus.realpython.org/dice")
tag = page.soup.select("#result")[0]
result = tag.text

print(f"The result of your dice roll is: {result}")

# To periodically get a new result, you’ll need to create a loop that loads the page at each step. So everything below the line browser = mechanicalsoup.Browser() in the above code needs to go in the body of the loop.

# For this example, you want four rolls of the dice at ten-second intervals. To do that, the last line of your code needs to tell Python to pause running for ten seconds. You can do this with .sleep() from Python’s time module. The .sleep() method takes a single argument that represents the amount of time to sleep in seconds.

# Here’s an example that illustrates how sleep() works:

import time

print("I'm about to wait for five seconds...")
time.sleep(5)
print("Done waiting!")

# For the die roll example, you’ll need to pass the number 10 to sleep(). Here’s the updated program:

import time
import mechanicalsoup

browser = mechanicalsoup.Browser()

for i in range(4):
    page = browser.get("http://olympus.realpython.org/dice")
    tag = page.soup.select("#result")[0]
    result = tag.text
    print(f"The result of your dice roll is: {result}")
    time.sleep(10)

# The program continues running for another ten seconds before it finally stops. That’s kind of a waste of time! You can stop it from doing this by using an if statement to run time.sleep() for only the first three requests:

import time
import mechanicalsoup

browser = mechanicalsoup.Browser()

for i in range(4):
    page = browser.get("http://olympus.realpython.org/dice")
    tag = page.soup.select("#result")[0]
    result = tag.text
    print(f"The result of your dice roll is: {result}")

    # Wait 10 seconds if this isn't the last request
    if i < 3:
        time.sleep(10)

# With techniques like this, you can scrape data from websites that periodically update their data. However, you should be aware that requesting a page multiple times in rapid succession can be seen as suspicious, or even malicious, use of a website.