import http.cookiejar as cookiejar
import browsercookie
import json
import http.cookiejar as cookiejar

# Extracts all the user cookies from the browser and saves them in a file


def download_cookies():
    cookies = browsercookie.load()

    # Create a new CookieJar object
    jar = cookiejar.CookieJar()

    cookiefiles = []

    # Add the cookies to the CookieJar object
    for cookie in cookies:
        cookie_dict = cookie.__dict__
        cookie_dict['rest'] = cookie_dict['_rest']
        del cookie_dict['_rest']
        cookiefiles.append(cookie_dict)

    # Save the cookies to the JSON file
    with open('cookies.json', 'w') as f:
        json.dump(cookiefiles, f)


def load_cookies():
    # Reading the cookies from the JSON file
    with open('cookies.json', 'r') as f:
        data2 = json.load(f)

    # Create a new CookieJar object
    jar2 = cookiejar.CookieJar()
    for cookie in data2:
        jar2.set_cookie(cookiejar.Cookie(**cookie))

    # Return the CookieJar object
    return jar2


# Calling the function
download_cookies()
load_cookies()
