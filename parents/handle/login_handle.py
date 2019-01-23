# coding=utf-8
from parents.page.login_page import LoginPage


class LoginHandle:
    def __init__(self, driver):
        self.login_page = LoginPage(driver)

    # 操作登录页面的元素
    def send_username(self, user):
        '''
        输入用户名
        '''
        self.login_page.get_username_element().send_keys(user)

    def send_password(self, password):
        '''
        输入密码
        '''
        self.login_page.get_password_element().send_keys(password)

    def click_login(self):
        '''
        点击登录按钮
        '''
        self.login_page.get_login_button_element().click()

    def click_forget_password(self):
        '''
        点击忘记密码
        '''
        self.login_page.get_forget_password_element().click()

    def click_register(self):
        '''
        点击注册按钮
        '''
        self.login_page.get_register_element().click()

    def get_fail_tost(self, message):
        '''
        获取tost，根据返回信息进行反数据
        '''
        tost_element = self.login_page.get_tost_element(message)
        if tost_element:
            return True
        else:
            return False

    def get_mine_text(self):
        '''
        获取首页元素
        '''
        mine_element = self.login_page.get_mime_element()
        if mine_element:
            return True
        else:
            return False

    def click_close(self):
        '''
        点击关闭按钮
        '''
        self.login_page.get_close_button_element().click()

    def click_learn_head(self, text):
        self.login_page.get_learn_element(text).click()
