"""Use an HTML Parser for Web Scraping in Python"""
# Although regular expressions are great for pattern matching in general, sometimes it’s easier to use an HTML parser that’s explicitly designed for parsing out HTML pages. There are many Python tools written for this purpose, but the Beautiful Soup library is a good one to start with.

# Create a BeautifulSoup Object

from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles/dionysus"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")

# This program does three things:

# 1) Opens the URL http://olympus.realpython.org/profiles/dionysus by using urlopen() from the urllib.request module

# 2)Reads the HTML from the page as a string and assigns it to the html variable

# 3)Creates a BeautifulSoup object and assigns it to the soup variable

# The BeautifulSoup object assigned to soup is created with two arguments. The first argument is the HTML to be parsed, and the second argument, the string "html.parser", tells the object which parser to use behind the scenes. "html.parser" represents Python’s built-in HTML parser.

print(soup.get_text())

# There are a lot of blank lines in this output. These are the result of newline characters in the HTML document’s text. You can remove them with the .replace() string method if you need to.

# Often, you need to get only specific text from an HTML document. Using Beautiful Soup first to extract the text and then using the .find() string method is sometimes easier than working with regular expressions.

# However, other times the HTML tags themselves are the elements that point out the data you want to retrieve. For instance, perhaps you want to retrieve the URLs for all the images on the page. These links are contained in the src attribute of <img> HTML tags.

#In this case, you can use find_all() to return a list of all instances of that particular tag:

print(soup.find_all("img"))

# You can explore this a little by first unpacking the Tag objects from the list:

image1, image2 = soup.find_all("img")

# Each Tag object has a .name property that returns a string containing the HTML tag type:

print(image1.name)

# You can access the HTML attributes of the Tag object by putting their names between square brackets, just as if the attributes were keys in a dictionary.

# For example, the <img src="/static/dionysus.jpg"/> tag has a single attribute, src, with the value "/static/dionysus.jpg". Likewise, an HTML tag such as the link <a href="https://realpython.com" target="_blank"> has two attributes, href and target.

# To get the source of the images in the Dionysus profile page, you access the src attribute using the dictionary notation mentioned above:

print(image1["src"], image2["src"])

# Certain tags in HTML documents can be accessed by properties of the Tag object. For example, to get the <title> tag in a document, you can use the .title property:

print(soup.title)

# Beautiful Soup automatically cleans up the tags for you by removing the extra space in the opening tag and the extraneous forward slash (/) in the closing tag.

# You can also retrieve just the string between the title tags with the .string property of the Tag object:

print(soup.title.string)

# One of the features of Beautiful Soup is the ability to search for specific kinds of tags whose attributes match certain values. For example, if you want to find all the <img> tags that have a src attribute equal to the value /static/dionysus.jpg, then you can provide the following additional argument to .find_all():

print(soup.find_all("img", src="/static/dionysus.jpg"))

# This example is somewhat arbitrary, and the usefulness of this technique may not be apparent from the example. If you spend some time browsing various websites and viewing their page sources, then you’ll notice that many websites have extremely complicated HTML structures.

# When scraping data from websites with Python, you’re often interested in particular parts of the page. By spending some time looking through the HTML document, you can identify tags with unique attributes that you can use to extract the data you need.

# Then, instead of relying on complicated regular expressions or using .find() to search through the document, you can directly access the particular tag that you’re interested in and extract the data you need.

"""Interact With HTML Forms"""
# Sometimes you need to interact with a web page to obtain the content you need. For example, you might need to submit a form or click a button to display hidden content.

# Create a Browser Object
import mechanicalsoup
browser = mechanicalsoup.Browser()

# Browser objects represent the headless web browser. You can use them to request a page from the Internet by passing a URL to their .get() method:

url2 = "http://olympus.realpython.org/login"
page2 = browser.get(url2)

# page is a Response object that stores the response from requesting the URL from the browser:

print(page2)

# The number 200 represents the status code returned by the request. A status code of 200 means that the request was successful. An unsuccessful request might show a status code of 404 if the URL doesn’t exist or 500 if there’s a server error when making the request.

# MechanicalSoup uses Beautiful Soup to parse the HTML from the request, and page has a .soup attribute that represents a BeautifulSoup object:

print(type(page2.soup))

# You can view the HTML by inspecting the .soup attribute:
print(page2.soup)
