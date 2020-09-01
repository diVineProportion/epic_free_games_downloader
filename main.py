import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

if __name__ == "__main__":

    TARGET_URL = "https://www.epicgames.com/store/en-US/"

    options = Options()

    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    # options.add_argument("--headless")
    # options.add_extension('crx\\uBlock Origin.crx')

    driver.get("https://www.epicgames.com/id/login/epic")
    time.sleep(2)

    base_common = '/html/body/div/div/div'
    base_signin = f'{base_common}/div/div/div[2]/div/form/div'
    username = driver.find_element_by_xpath(f'{base_signin}[1]/div/input')
    password = driver.find_element_by_xpath(f'{base_signin}[2]/div/input')
    login___ = driver.find_element_by_xpath(f'{base_signin}[4]/button/span')

    # use getenv over environ for 'key does not exist' default value of input
    username.send_keys(os.getenv('EPIC_USERNAME', input("ENTER USERNAME: ")))
    password.send_keys(os.getenv('EPIC_PASSWORD', input("ENTER PASSWORD: ")))

    login___.click()
    time.sleep(5)
    driver.get('https://www.epicgames.com/store/en-US/free-games')
    time.sleep(2)

    free_common = f'{base_common}[4]/main/div'
    game_common = f'{free_common}/div/div/div/div[2]/div[2]/div/div/section/div/div'

    free_list = ['[1]/div/div/a/div/div/div[1]/div[2]/div/div',
                 '[2]/div/div/a/div/div/div[1]/div[2]/div/div',
                 '[3]/div/div/a/div/div/div[1]/div[2]/div/div/span']

    for idx, val in enumerate(free_list):
        # TODO: gather title and dates, as well as upcoming title
        if idx < 2:
            _ = driver.find_element_by_xpath(f'{game_common}{val}')
            _.click()
            time.sleep(2)
            try:
                mature_check = driver.find_element_by_xpath(f'{free_common}[2]/div/div[2]/div/button')
            except Exception as e:
                print(e)
                # TODO: proper element not found exception
            else:
                mature_check.click()
            finally:
                time.sleep(2)
        else:
            pass
        # TODO: shorten xpaths using common xpath tags
        get_game = driver.find_element_by_xpath('/html/body/div/div/div[4]/main/div/div/div[2]/div/div[2]/div[2]/div/div/div[3]/div/div/div/div[3]/div/button')
        get_game.click()
        time.sleep(5)
        place_order = driver.find_element_by_xpath('/html/body/div[3]/div/div/div[4]/div/div[4]/div[1]/div[2]/div[5]/div/div/button')
        place_order.click()
        driver.get('https://www.epicgames.com/store/en-US/free-games')