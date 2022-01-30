from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
import json, time


def open_target_page(url):
    """
    driver setup
    open target url
    :return:
    """
    global driver, wait
    driver = webdriver.Chrome(ChromeDriverManager().install())
    wait = WebDriverWait(driver, 20)
    driver.get(url)


def click_on_play_in_browser_button():
    wait.until(EC.visibility_of_element_located(Locators.play_in_browser_button))
    driver.find_element(*Locators.play_in_browser_button).click()


def click_on_launch_game_button():
    wait.until(EC.visibility_of_element_located(Locators.launch_game_button))
    driver.find_element(*Locators.launch_game_button).click()
    time.sleep(1)


# for getting data and dump it in dict format
def get_keyboard_control_instructions():
    control_dict = dict()
    wait.until(EC.visibility_of_all_elements_located(Locators.key_list))
    keys = driver.find_elements(*Locators.key_list)
    values = driver.find_elements(*Locators.value_list)
    num = 0
    for i in range(len(keys)):
        control_dict[keys[num].text] = values[num].text
        num += 1
    write_file_dict_data(control_dict)
    time.sleep(1)
    return control_dict


def write_file_dict_data(json_data):
    with open("control_dict.json", "w+") as fd:
        fd.write(json.dumps(json_data))


def get_game_pad_control_instructions():
    wait.until(EC.visibility_of_element_located(Locators.game_pad_section))
    driver.find_element(*Locators.game_pad_section).click()
    return driver.find_element(*Locators.error_massage_in_game_pad_section).text


def close_the_control_instructions_using_cross_button():
    driver.find_element(*Locators.control_closed_by_cross_icon).click()
    time.sleep(2)  # sleep for 2 seconds before closing


def main_method(url):
    # open target website in Chrome Browser
    open_target_page(url)
    # click on target button
    click_on_play_in_browser_button()
    # click on target button
    click_on_launch_game_button()
    # Print Game Control Instructions
    print("keyboard_control_instructions =>", get_keyboard_control_instructions())
    print("GamePad_control_instructions => ", get_game_pad_control_instructions())
    # close instruction box using cross button
    close_the_control_instructions_using_cross_button()
    driver.close()


if __name__ == '__main__':
    main_method(url="https://now.gg/apps/perfect-world/7724/perfect-world-mobile.html")
