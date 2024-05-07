import mechanicalsoup

#In the next example, you’ll see how to use MechanicalSoup to fill out and submit this form using Python!

# The important section of HTML code is the login form—that is, everything inside the <form> tags. The <form> on this page has the name attribute set to login. This form contains two <input> elements, one named user and the other named pwd. The third <input> element is the Submit button.

# Now that you know the underlying structure of the login form, as well as the credentials needed to log in, take a look at a program that fills the form out and submits it

# 1
browser = mechanicalsoup.Browser()
url = "http://olympus.realpython.org/login"
login_page = browser.get(url)
login_html = login_page.soup

# 2
form = login_html.select("form")[0]
form.select("input")[0]["value"] = "zeus"
form.select("input")[1]["value"] = "ThunderDude"

# 3
profiles_page = browser.submit(form, login_page.url)

print(profiles_page.url)

# Now break down the above example:

# 1) You create a Browser instance and use it to request the URL http://olympus.realpython.org/login. You assign the HTML content of the page to the login_html variable using the .soup property.

# 2) login_html.select("form") returns a list of all <form> elements on the page. Because the page has only one <form> element, you can access the form by retrieving the element at index 0 of the list. When there is only one form on a page, you may also use login_html.form. The next two lines select the username and password inputs and set their value to "zeus" and "ThunderDude", respectively.

# 3) You submit the form with browser.submit(). Notice that you pass two arguments to this method, the form object and the URL of the login_page, which you access via login_page.url.

# In the interactive window, you confirm that the submission successfully redirected to the /profiles page. If something had gone wrong, then the value of profiles_page.url would still be "http://olympus.realpython.org/login".



# Now that you have the profiles_page variable set, it’s time to programmatically obtain the URL for each link on the /profiles page.

# To do this, you use .select() again, this time passing the string "a" to select all the <a> anchor elements on the page:

links = profiles_page.soup.select("a")

# Now you can iterate over each link and print the href attribute:
for link in links:
        address = link["href"]
        text = link.text
        print(f"{text}:{address}")

# The URLs contained in each href attribute are relative URLs, which aren’t very helpful if you want to navigate to them later using MechanicalSoup. If you happen to know the full URL, then you can assign the portion needed to construct a full URL.

# In this case, the base URL is just http://olympus.realpython.org. Then you can concatenate the base URL with the relative URLs found in the src attribute:

base_url = "http://olympus.realpython.org"
for link in links:
    address = base_url + link["href"]
    text = link.text
    print(f"{text}: {address}")