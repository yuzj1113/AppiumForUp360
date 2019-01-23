# coding=utf-8
import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from util.get_by_local import GetByLocal


class LoginPage:
    # 获取登录页面所有的页面元素信息
    def __init__(self, driver):
        self.driver = driver
        self.get_by_local = GetByLocal(self.driver)

    def get_username_element(self):
        # 获取用户名元素信息
        return self.get_by_local.get_element('username')

    def get_password_element(self):
        # 获取密码元素信息
        return self.get_by_local.get_element('password')

    def get_login_button_element(self):
        # 获取登陆按钮元素信息
        return self.get_by_local.get_element('login_button')

    def get_forget_password_element(self):
        # 忘记密码元素
        return self.get_by_local.get_element('forget_password')

    def get_register_element(self):
        # 注册元素
        return self.get_by_local.get_element('register')

    def get_tost_element(self, message):
        # 获取tostelement
        time.sleep(2)
        tost_element = ("xpath", "//*[contains(@text," + message + ")]")
        return WebDriverWait(self.driver, 10, 0.1).until(EC.presence_of_element_located(tost_element))

    def get_mime_element(self):
        # 首页元素
        return self.get_by_local.get_element('mine')

    def get_close_button_element(self):
        return self.get_by_local.get_element('close_button')

