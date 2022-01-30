from selenium.webdriver.common.by import By
class Locators:
    play_in_browser_button = (By.XPATH, """//div[@class="play-btn-wrapper"]""")
    video_footer_progress = (By.XPATH, """//p[@id="prog-percentage" and contains(text(),'100%')]""")
    launch_game_button = (By.XPATH, """//button[@data-str-id="launchGame"]""")
    heading_game_controls_text = (By.XPATH, """//div[@id="sidebar-wrap"]/h1//span[@data-str-id="gameControlsTitle"]""")
    sidebar_control_button_if_checked = (
        By.XPATH, """//div[@id="sidebar-wrap"]//div[@class="check-switch overlaySwitch checked"]""")
    sidebar_control_button_if_not_checked = (
        By.XPATH, """//div[@id="sidebar-wrap"]//div[@class="check-switch overlaySwitch"]""")
    keyboard_section = (By.XPATH, """//div[@class="tab-header"]/div[@onclick='window.sidebar.changeTab("keyboard")']""")
    game_pad_section = (By.XPATH, """//div[@onclick='window.sidebar.changeTab("gamepad")']""")
    error_massage_in_game_pad_section = (By.XPATH, """//div[@class="tab-content gamepad"]//h1""")
    control_closed_by_cross_icon = (By.XPATH, "//span[@class='icon-close-round']")
    key_list = (By.XPATH, """//ul[@class="control-list"]/li/span[1]""")
    value_list = (By.XPATH, """//ul[@class="control-list"]/li/span[2]""")