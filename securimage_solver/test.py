import captcha_api
import urllib.request
import os.path

def main():
    url = 'https://swordslegends.com/swords/libs/securimage/securimage_show.php'
    urllib.request.urlretrieve(url, 'tmp.png')
    print(captcha_api.predict('tmp.png'))

if __name__ == '__main__':
    main()


