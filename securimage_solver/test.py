import captcha_api
import requests
import os.path


def main():

    cookie = 'PHPSESSID=72d03bd5a5b8f37fc9c87ac1b2f3ca75'
    username = 'mrapplehack1234'
    email = 'mrapplehack1234@test.com'
    password = 'mrapplehack1234'
    password_again = 'mrapplehack1234'
    captcha_code = ''
    register = 'Register'

    response = requests.request(
        "POST",
        "https://swordslegends.com/swords/register.html",
         headers = {
             'cookie': cookie
         },
         data = {
            'username': username,
            'email': email,
            'password': password,
            'password_again': password_again,
            'captcha_code': captcha_code,
            'register': register
         },
         files = [
         ])

    print(response.text)
    # print(captcha_code)

if __name__ == '__main__':
    main()


