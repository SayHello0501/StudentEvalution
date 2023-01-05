# coding=utf-8
# -----------------------------------------------------------------
# ProjectName:      PycharmProjects
# FileName:         get_driver.py
# Author:           袁骏翼
# Email:            
# Datetime:         2022/10/14 9:25
# Description:      
# 命名规范：文件名全小写+下划线，类名大驼峰，方法和变量小写+下划线连接，常量大写
# -----------------------------------------------------------------

from selenium import webdriver
from tools.get_log import GetLog
from selenium.webdriver.common.keys import Keys

log = GetLog().get_logger()


class GetDriver:
    driver = None

    @classmethod
    def get_driver(cls, browser, url):
        log.info("正在获取浏览器{}".format(browser))
        if cls.driver is None:
            if browser.upper() == 'CHROME':
                cls.driver = webdriver.Chrome()
            elif browser.upper() == 'IE':
                cls.driver = webdriver.Ie()
            elif browser.upper() == 'FIREFOX':
                cls.driver = webdriver.Firefox()
            elif browser.upper() == 'SAFARI':
                cls.driver = webdriver.Safari()
            cls.driver.get(url)
            cls.driver.maximize_window()
        return cls.driver

    # 清除输入内容
    @classmethod
    def clear_input(cls, loc):
        cls.driver.find_element(*loc).send_keys(Keys.CONTROL, "a")
        cls.driver.find_element(*loc).send_keys(Keys.DELETE)

    # 关闭浏览器
    @classmethod
    def quit_browser(cls):
        log.info("关闭浏览器!")
        cls.driver.quit()
