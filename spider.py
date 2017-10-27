from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep

option = webdriver.FirefoxProfile()
#option.add_extension('user-agent="Mozilla/5.0 (iPod; U; CPU iPhone OS 2_1 like Mac OS X; ja-jp) AppleWebKit/525.18.1 (KHTML, like Gecko) Version/3.1.1 Mobile/5F137 Safari/525.20"'


browser = webdriver.Firefox()

browser.set_window_size(1400, 900)


wait = WebDriverWait(browser, 20)

def login(username,password):
    print('登录知乎')
    try:
        browser.get('https://www.zhihu.com/')
        browser.delete_all_cookies()

        submit = wait.until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[2]/div[1]/div/a[2]'))
        )
        submit.click()

        submit = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '.qrcode-signin-step1 > div:nth-child(4) > span:nth-child(1)'))
        )
        submit.click()
        input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'div.account > input:nth-child(1)'))
        )
        input.clear()
        input.send_keys(username)
        input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.verification > input:nth-child(1)'))
        )
        input.clear()
        input.send_keys(password)
        submit = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.button-wrapper:nth-child(3) > button:nth-child(1)')))
        submit.click()


        # tag = wait.until(
        #     EC.presence_of_element_located((By.CSS_SELECTOR, 'div.Captcha:nth-child(3) > div:nth-child(1) > label:nth-child(3)')))
        # print(tag.text)
        # if tag.text:
        #     img = wait.until(EC.url_contains(str='captcha'))
        #     print(img)


    except TimeoutException:
        pass


def main():
    login(username='', password='')


if __name__ == '__main__':
    main()