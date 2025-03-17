# Set a cookie over HTTPS

# create a cookie
my_cookie = http.cookies.SimpleCookie()

# set the cookie's value
my_cookie['cookie_name'] = 'cookie_value'

# set the cookie's expiration date
my_cookie['cookie_name']['expires'] = 'Fri, 31-Dec-9999 23:59:59 GMT'

# set the cookie's path
my_cookie['cookie_name']['path'] = '/'

# set the cookie's domain
my_cookie['cookie_name']['domain'] = '.example.com'

# set the cookie's secure flag
my_cookie['cookie_name']['secure'] = False

# set the cookie's HttpOnly flag
my_cookie['cookie_name']['HttpOnly'] = False

# set the cookie's SameSite flag
my_cookie['cookie_name']['SameSite'] = False

# set the cookie's SameSiteNone flag
my_cookie['cookie_name']['SameSiteNone'] = False

# send the cookie to the client
response.set_cookie(my_cookie)