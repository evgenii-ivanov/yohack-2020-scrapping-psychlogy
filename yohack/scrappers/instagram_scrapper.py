import datetime
import hashlib
import requests
from time import sleep
from selenium import webdriver

class InstagramScrapper:


    BASE_URL = 'https://www.instagram.com/'

    browser = None

    def save_image(self, pic_url):
        with open(hashlib.md5(str(datetime.datetime.now()).encode()).hexdigest() + '.jpg', 'wb') as handle:
            response = requests.get(pic_url, stream=True)

            if not response.ok:
                print(response)

            for block in response.iter_content(1024):
                if not block:
                    break

                handle.write(block)

    def open_browser(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(5)

    def close_browser(self):
        self.browser.close()

    def login(self):
        self.browser.get(self.BASE_URL)

        username_input = self.browser.find_element_by_css_selector("input[name='username']")
        password_input = self.browser.find_element_by_css_selector("input[name='password']")

        username_input.send_keys("zakonoposluschniyg")
        password_input.send_keys("11111Qqqqq-")

        login_button = self.browser.find_element_by_xpath("//button[@type='submit']")
        login_button.click()

        sleep(5)

        not_now_btn = self.browser.find_element_by_css_selector("button.aOOlW.HoLwm")
        not_now_btn.click()

    def search(self, string):
        search_input = self.browser.find_element_by_css_selector("input.XTCLo.x3qfX")
        search_input.send_keys(string)
        sleep(2)

    def get_posts(self):
        posts = self.browser.find_elements_by_css_selector("div.v1Nh3.kIKUG._bz0w > a")
        return posts

    def scrape(self, username):
        self.browser.get(self.BASE_URL + username)
        sleep(2)
        posts = self.get_posts()
        posts_href = []
        for post in posts:
            posts_href.append(post.get_attribute('href'))
        for post in posts_href:
            self.browser.get(post)
            sleep(2)
            image = self.browser.find_elements_by_css_selector("img.FFVAD")
            src = image.get_attribute("src")
            try:
                self.save_image(src)
            except Exception:
                print('image {} can\'t be saved'.format(src))
        sleep(2)

    def scrape_list(self, users):
        self.open_browser()
        self.login()
        sleep(2)
        for username in users:
            self.scrape(username)
        self.close_browser()

scrapper = InstagramScrapper()
scrapper.scrape_list(['digitalskynet'])