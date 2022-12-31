import http.cookiejar as cookiejar
import browsercookie
import json
import myfitnesspal
import http.cookiejar as cookielib
import http.cookiejar as cookiejar
import browser_cookie3

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

    # Reading the cookies from the JSON file
    with open('cookies.json', 'r') as f:
        data2 = json.load(f)

    # Create a new CookieJar object
    jar2 = cookiejar.CookieJar()
    for cookie in data2:
        jar2.set_cookie(cookiejar.Cookie(**cookie))

    client = myfitnesspal.Client(jar2)

    print(client.get_date(2022, 8, 1).goals)


# Calling the function
download_cookies()
