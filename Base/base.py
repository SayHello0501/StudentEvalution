'''
    页面通用方法
'''

from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from tools.get_log import GetLog
from selenium.webdriver.common.action_chains import ActionChains

log = GetLog().get_logger()


class Base(object):
    def __init__(self, driver):
        self.driver = driver

    # 定位元素
    def get_element(self, loc, timeout=10, poll=0.5):
        log.info("开始查找元素{}".format(loc))
        try:
            element = WebDriverWait(self.driver,
                                    timeout=timeout,
                                    poll_frequency=poll).until(lambda x: x.find_element(*loc))
            return element
        except:
            log.error('未找到元素{}'.format(loc))

    # 元素操作方法
    def input_text(self, loc, text):
        log.info("正在调用输入方法{}，输入内容{}".format(loc, text))
        try:
            ge = self.get_element(loc)
            # 清除内容
            ge.clear()  # 区域元素没有clear属性
            # 输入内容
            ge.send_keys(text)
        except:
            pass

    # 点击操作
    def click_button(self, loc):
        log.info("正在调用点击方法{}".format(loc))
        try:
            self.get_element(loc).click()
        except:
            log.error("未找到可点击元素{}".format(loc))

    # 获取文本信息
    def base_get_text(self, loc):
        log.info("获取到文本信息{}".format(loc))
        return self.get_element(loc).text

    # 全选清除输入内容
    def clear_input(self, loc):
        try:
            self.driver.find_element(*loc).send_keys(Keys.CONTROL, "a")
            self.driver.find_element(*loc).send_keys(Keys.DELETE)
        except:
            pass

    # 鼠标单击事件
    def mouse_action_click(self, loc):
        try:
            mouse_click = self.driver.find_element(*loc)
            ActionChains(self.driver).click(mouse_click).perform()
        except:
            pass

    # 鼠标双击事件
    def mouse_action_double(self, loc):
        try:
            double_click = self.driver.find_element(*loc)
            ActionChains(self.driver).double_click(double_click).perform()
        except:
            pass

    # 鼠标右键点击事件
    def mouse_action_right_click(self, loc):
        try:
            mouse_right_click = self.driver.find_element(*loc)
            ActionChains(self.driver).context_click(mouse_right_click).perform()
        except:
            pass

    # 键盘enter事件
    def keyboard_action(self, loc):
        self.get_element(loc).send_keys(Keys.ENTER)

    # 处理弹框
    def switch_alert(self, loc):
        self.get_element(loc)

    # 切换iframe
    def switch_frame(self, loc):
        log.info("正在调用切换frame方法，切换对象：{}".format(loc))
        # 获取iframe的元素
        el = self.get_element(loc)
        # 切换iframe
        self.driver.switch_to.frame(el)

    # 切回到默认页面
    def switch_to_default_frame(self):
        self.driver.swotch_to.default_frame()

    # 处理下拉框
    def choose_select(self, loc, value):
        # 获取下拉框元素
        el = self.get_element(loc)
        # 实例化
        select = Select(el)
        # 选择下拉框内容
        select.select_by_index(value)

    # 切换窗口
    def switch_window(self):
        # 切换句柄
        new_window = self.driver.window_handles
        # print(new_window)
        # 切换到新窗口
        self.driver.switch_to.window(new_window[-1])
