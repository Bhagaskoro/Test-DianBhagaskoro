import re
def usernameCheck(user):
    reg = "^(?=.*\A@)[A-Za-z\d@$!#%*?&]{2,12}$"

    x = False
    pattern = re.compile(reg)
    match = re.search(pattern, user)
    if match:
        x = True
    else:
        x = False
    print(x)

def passwordCheck(user):
    reg = "^[\d]{6,6}$"
    x = False
    pattern = re.compile(reg)
    match = re.search(pattern, user)
    if match:
        x = True
    else:
        x = False
    print(x)

username1 = "@koders"
username2 = "@programmerhandal"
password1 = "212223"
password2 = "2!2a3B"
usernameCheck(username1)
usernameCheck(username2)
passwordCheck(password1)
passwordCheck(password2)

# source:
# -https://www.geeksforgeeks.org/password-validation-in-python/
# -https://www.w3schools.com/python/python_regex.asp
