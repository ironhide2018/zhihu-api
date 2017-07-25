# encoding: utf-8

import requests
import requests.utils

from zhihu.models.account import Account
from .models.zhihu import Zhihu

try:
    input = raw_input  # py2
except:
    pass


def need_login(func):
    """
    用户认证装饰器(判断用户是否已经登录)
    """

    def wrapper(self, *args, **kwargs):
        if 'z_c0' not in requests.utils.dict_from_cookiejar(self._session.cookies):
            try:
                pass
                # Zhihu().user(user_slug='zhijun-liu')
            except:
                account = input("请输入Email或者手机号码:")
                password = input("请输入密码:")
                Account().login(account, password)
            else:
                self._session.cookies.load(ignore_discard=True)
                return func(self, *args, **kwargs)

    return wrapper
