import captcha_api
import urllib.request
import os.path
import http.client
import mimetypes
from codecs import encode

def main():

    conn = http.client.HTTPSConnection("swordslegends.com")
    dataList = []
    boundary = 'wL36Yn8afVp8Ag7AmP8qZ0SA4n1v9T'
    dataList.append(encode('--' + boundary))
    dataList.append(encode('Content-Disposition: form-data; name=username;'))

    dataList.append(encode('Content-Type: {}'.format('text/plain')))
    dataList.append(encode(''))

    dataList.append(encode("hacker173"))
    dataList.append(encode('--' + boundary))
    dataList.append(encode('Content-Disposition: form-data; name=email;'))

    dataList.append(encode('Content-Type: {}'.format('text/plain')))
    dataList.append(encode(''))

    dataList.append(encode("hacker173@test.com"))
    dataList.append(encode('--' + boundary))
    dataList.append(encode('Content-Disposition: form-data; name=password;'))

    dataList.append(encode('Content-Type: {}'.format('text/plain')))
    dataList.append(encode(''))

    dataList.append(encode("hacker173"))
    dataList.append(encode('--' + boundary))
    dataList.append(encode('Content-Disposition: form-data; name=password_again;'))

    dataList.append(encode('Content-Type: {}'.format('text/plain')))
    dataList.append(encode(''))

    dataList.append(encode("hacker173"))
    dataList.append(encode('--' + boundary))
    dataList.append(encode('Content-Disposition: form-data; name=captcha_code;'))

    dataList.append(encode('Content-Type: {}'.format('text/plain')))
    dataList.append(encode(''))

    dataList.append(encode("test"))
    dataList.append(encode('--' + boundary))
    dataList.append(encode('Content-Disposition: form-data; name=register;'))

    dataList.append(encode('Content-Type: {}'.format('text/plain')))
    dataList.append(encode(''))

    dataList.append(encode("Register"))
    dataList.append(encode('--'+boundary+'--'))
    dataList.append(encode(''))
    body = b'\r\n'.join(dataList)
    payload = body
    headers = {
        'Cookie': 'PHPSESSID=8528f6269c7c459d5cf9c837010ed440',
        'Content-type': 'multipart/form-data; boundary={}'.format(boundary)
    }
    conn.request("POST", "/swords/register.html", payload, headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))


    captcha_code_url = 'https://swordslegends.com/swords/libs/securimage/securimage_show.php'
    urllib.request.urlretrieve(captcha_code_url, 'tmp.png')
    captcha_code = captcha_api.predict('tmp.png')

    # url = "https://swordslegends.com/swords/register.html"

    # payload={'username': 'hacker173',
    #     'email': 'hacker173@test.com',
    #     'password': 'hacker173',
    #     'password_again': 'hacker173',
    #     'captcha_code': captcha_code,
    #     'register': 'Register'
    # }
    # files=[]
    # headers = {
    #   'Cookie': 'PHPSESSID=8528f6269c7c459d5cf9c837010ed440'
    # }

    # response = requests.request("POST", url, headers=headers, data=payload, files=files)

    # print(response.text)

    # print(captcha_code)

if __name__ == '__main__':
    main()


