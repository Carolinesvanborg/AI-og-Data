""" Web Scraper"""

# the urllib.request module contains a function called urlopen() that you can use to open a URL within a program.
from urllib.request import urlopen

# The web page that you’ll open is at the following URL:
url = "http://olympus.realpython.org/profiles/aphrodite"

# To open the web page, pass url to urlopen():
page = urlopen(url)

# urlopen() returns an HTTPResponse object:
print(page)

# To extract the HTML from the page, first use the HTTPResponse object’s .read() method, which returns a sequence of bytes. Then use .decode() to decode the bytes to a string using UTF-8:
html_bytes = page.read()
html = html_bytes.decode("utf-8")

# Now you can print the HTML to see the contents of the web page:
print (html)

# With urllib, you accessed the website similarly to how you would in your browser. However, instead of rendering the content visually, you grabbed the source code as text.

"""Extract Text From HTML With String Methods"""
# you can use .find() to search through the text of the HTML for the <title> tags and extract the title of the web page.

title_index = html.find("<title>")

print(title_index)

# You don’t want the index of the <title> tag, though. You want the index of the title itself. To get the index of the first letter in the title, you can add the length of the string "<title>" to title_index:

start_index = title_index + len("<title>")

print(start_index)

# Now get the index of the closing </title> tag by passing the string "</title>" to .find():

end_index = html.find("</title>")
print (end_index)

# Finally, you can extract the title by slicing the html string:

title = html[start_index:end_index]
print(title)

"""Real-world HTML can be much more complicated and far less predictable than the HTML on the Aphrodite profile page. Here’s another profile page with some messier HTML that you can scrape:"""

url2 = "http://olympus.realpython.org/profiles/poseidon"

# Try extracting the title from this new URL using the same method as in the previous example

page2 = urlopen(url2)
html2 = page2.read ().decode("utf-8")
start_index2 = html2.find("<title>") + len("<title>")
end_index2 = html2.find("</title>")
title2 = html2[start_index2:end_index2]
print(title2)

# Whoops! There’s a bit of HTML mixed in with the title. Why’s that?

# The HTML for the /profiles/poseidon page looks similar to the /profiles/aphrodite page, but there’s a small difference. The opening <title> tag has an extra space before the closing angle bracket (>), rendering it as <title >.

# html.find("<title>") returns -1 because the exact substring "<title>" doesn’t exist. When -1 is added to len("<title>"), which is 7, the start_index variable is assigned the value 6.

# The character at index 6 of the string html is a newline character (\n) right before the opening angle bracket (<) of the <head> tag. This means that html[start_index:end_index] returns all the HTML starting with that newline and ending just before the </title> tag.

# These sorts of problems can occur in countless unpredictable ways. You need a more reliable way to extract text from HTML.

"""Get to Know Regular Expressions"""
# Regular expressions—or regexes for short—are patterns that you can use to search for text within a string. Python supports regular expressions through the standard library’s re module.

# To work with regular expressions, the first thing that you need to do is import the re module:
import re

# Regular expressions use special characters called metacharacters to denote different patterns. For instance, the asterisk character (*) stands for zero or more instances of whatever comes just before the asterisk.

# In the following example, you use .findall() to find any text within a string that matches a given regular expression:
findall = re.findall("ab*c", "ac")
print(findall)

# The first argument of re.findall() is the regular expression that you want to match, and the second argument is the string to test. In the above example, you search for the pattern "ab*c" in the string "ac".

# The regular expression "ab*c" matches any part of the string that begins with "a", ends with "c", and has zero or more instances of "b" between the two. re.findall() returns a list of all matches. The string "ac" matches this pattern, so it’s returned in the list.

# Here’s the same pattern applied to different strings:
findall2 = re.findall("ab*c", "abcd")
findall3 = re.findall("ab*c", "acc")
findall4 = re.findall("ab*c", "abcac")
findall5 = re.findall("ac*c", "abdc")
print(findall2, findall3, findall4, findall5)

# Notice that if no match is found, then .findall() returns an empty list.

# Pattern matching is case sensitive. If you want to match this pattern regardless of the case, then you can pass a third argument with the value re.IGNORECASE:

findall_case = re.findall("ab*c", "ABC")

findall_ignore_case = re.findall("ab*c", "ABC", re.IGNORECASE)

print(findall_case, findall_ignore_case)

# You can use a period (.) to stand for any single character in a regular expression. For instance, you could find all the strings that contain the letters "a" and "c" separated by a single character as follows:

find_period = re.findall("a.c", "abc")
find_period2 = re.findall("a.c", "abbc")
find_period3 = re.findall("a.c", "ac")
find_period4 = re.findall("a.c", "acc")

print(find_period, find_period2, find_period3, find_period4)

# The pattern .* inside a regular expression stands for any character repeated any number of times. For instance, you can use "a.*c" to find every substring that starts with "a" and ends with "c", regardless of which letter—or letters—are in between:
findall_any_number_of_times = re.findall("a.*c", "abc")
findall_any_number_of_times2 = re.findall("a.*c", "abbc")
findall_any_number_of_times3 = re.findall("a.*c", "ac")
findall_any_number_of_times4 = re.findall("a.*c", "acc")

print(findall_any_number_of_times, findall_any_number_of_times2, findall_any_number_of_times3, findall_any_number_of_times4)

# calling .group() on MatchObject will return the first and most inclusive result, which in most cases is just what you want:
match_results = re.search("ab*c", "ABC", re.IGNORECASE)
match_results.group()

# There’s one more function in the re module that’s useful for parsing out text. re.sub(), which is short for substitute, allows you to replace the text in a string that matches a regular expression with new text. It behaves sort of like the .replace() string method.

# The arguments passed to re.sub() are the regular expression, followed by the replacement text, followed by the string. Here’s an example:

string = "Everything is <replaced> if it's in <tags>."
string = re.sub("<.*>", "ELEPHANTS", string)
print(string)

# re.sub() uses the regular expression "<.*>" to find and replace everything between the first < and the last >, which spans from the beginning of <replaced> to the end of <tags>. This is because Python’s regular expressions are greedy, meaning they try to find the longest possible match when characters like * are used.

# Alternatively, you can use the non-greedy matching pattern *?, which works the same way as * except that it matches the shortest possible string of text:

string = "Everything is <replaced> if it's in <tags>."
string = re.sub("<.*?>", "ELEPHANTS", string)
print(string)

"""Extract Text From HTML With Regular Expressions"""
# Equipped with all this knowledge, now try to parse out the title from another profile page, which includes this rather carelessly written line of HTML: <TITLE >Profile: Dionysus</title  / >

# The .find() method would have a difficult time dealing with the inconsistencies here, but with the clever use of regular expressions, you can handle this code quickly and efficiently:

url3 = "http://olympus.realpython.org/profiles/dionysus"
page3 = urlopen(url3)
html3 = page3.read().decode("utf-8")

pattern = "<title.*?>.*?</title.*?>"
match_results = re.search(pattern, html3, re.IGNORECASE)
title3 = match_results.group()
title3 = re.sub("<.*?>", "", title3) # Remove HTML tags

print(title3)

"""Use an HTML Parser for Web Scraping in Python"""
# Although regular expressions are great for pattern matching in general, sometimes it’s easier to use an HTML parser that’s explicitly designed for parsing out HTML pages. There are many Python tools written for this purpose, but the Beautiful Soup library is a good one to start with.

# Create a BeautifulSoup Object

