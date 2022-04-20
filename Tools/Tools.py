# -*- encoding : utf-8 -*-
# @Author : Fenglchen

# 工具类
import hashlib
import random
import re


class Tools:
    # 小写字母表
    lower_alpha_table = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                         't', 'u', 'v', 'w', 'x', 'y', 'z']
    # 大写字母表
    upper_alpha_table = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                         'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    # 数字表
    number_table = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    # 特殊符号表
    seq_table = ['~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', '|',
                 ':', ';', ',', '.', '<', '>', '/', '?', '`', '\'', '\\']

    # 检验密码
    @staticmethod
    def checkout_password(string):

        # 接收用户输入字符串
        test_password = string

        # 符号个数
        count_sign = 0
        # 数字个数
        count_num = 0
        # 空格个数
        count_blank = test_password.count(' ')
        # 小写字母个数
        count_lower_case = 0
        # 大写字母个数
        count_upper_case = 0
        # 字母个数
        count_alphabet = 0

        # 对符合注册要求对字符数进行统计
        if len(test_password) in range(8, 17):

            #  验证字符串内数字个数
            for j in test_password:
                if j in Tools.number_table:
                    count_num = count_num + 1

            # 验证字符串内大写字母个数
            for j in test_password:
                if j in Tools.upper_alpha_table:
                    count_upper_case = count_upper_case + 1

            # 验证字符串内小写字母个数
            for j in test_password:
                if j in Tools.lower_alpha_table:
                    count_lower_case = count_lower_case + 1

            # 字符串内特殊符号个数
            count_sign = len(test_password) - count_num - count_upper_case - count_blank - count_lower_case

            # 字符串字母总个数
            count_alphabet = count_lower_case + count_lower_case

        # 如果输入为空
        if len(test_password) == 0:
            return False

        # 位数少于8位
        elif len(test_password) < 6:
            return False

        # 如果输入存在空格
        elif count_blank != 0:
            return False

        # 如果输入为纯特殊符号
        elif count_sign == len(test_password):
            return False

        elif len(test_password) in range(6, 8):
            # 长度6～8位 包含数字，大写字母，小写字母，特殊符号 强度为中
            if count_num != 0 and count_sign != 0 and count_lower_case != 0 and count_upper_case != 0:
                level = 'MediumSecurity'
                return level
            else:
                # 剩下强度为低
                level = 'LowSecurity'
                return level

        elif len(test_password) in range(8, 13):
            # 长度8～12位 包含数字，大写字母，小写字母，特殊符号 强度为高
            if count_num != 0 and count_sign != 0 and count_lower_case != 0 and count_upper_case != 0:
                level = 'HighSecurity'
                return level
            # 长度8～12位 纯数字/字母 强度为低
            elif count_num == len(test_password) or count_alphabet == len(test_password):
                # 强度为低
                level = 'LowSecurity'
                return level
            # 其他情况 强度为中
            else:
                level = 'MediumSecurity'
                return level

        elif len(test_password) in range(13, 17):
            # 长度13～16位 包含数字，大写字母，小写字母，特殊符号 强度为极高
            if count_num != 0 and count_sign != 0 and count_lower_case != 0 and count_upper_case != 0:
                level = 'ExtermeHighSecurity'
                return level
            # 长度13～16位 纯数字/字母强度为低
            elif count_num == len(test_password) or count_alphabet == len(test_password):
                # 强度为低
                level = 'LowSecurity'
                return level
            # 长度13～16位 包含数字，字母（大小写字母只存在一种），特殊符号 强度为高
            elif count_num != 0 and count_sign != 0 and count_alphabet != 0:
                level = 'HighSecurity'
                return level
            # 其他情况 强度为中
            else:
                level = 'MediumSecurity'
                return level

    @staticmethod
    # 随机生成盐
    def get_password_salt():
        # 生成六~七位长度随机字符串
        salt = ''.join(
            random.sample(Tools.number_table + Tools.upper_alpha_table + Tools.lower_alpha_table + Tools.seq_table, 6))
        return salt

    @staticmethod
    # 密码加密
    def password_encryption(password, pwd_salt=None):
        # 加密方式md5加密
        md5 = hashlib.md5()
        # 判断是否输入salt 没有则随机生成
        if not pwd_salt:
            # 获取盐
            pwd_salt = Tools.get_password_salt()
        # update只接收byte类型的数据 同时对输入数据进行加盐
        md5.update((pwd_salt + password).encode())
        # 返回十六进制加密后的数据
        return pwd_salt, md5.hexdigest()

    @staticmethod
    # 检测用户登陆状态
    def check_user_login(request):
        # 获取session中登陆状态
        logged_in = request.session.get('logged_in', 'no')

        # 获取session中用户名
        username = request.session.get('username', 'null')

        # 邮箱正则
        ePattern = re.compile(r'^[A-Za-z\d]+([-_.][A-Za-z\d]+)*@([A-Za-z\d]+[-.])+[A-Za-z\d]{2,5}$')
        # 手机号正则
        mPattern = re.compile(r'^((13[0-9])|(19[8])|(14[5|7])|(15([0-3]|[5-9]))|(18[0,5-9]))\d{8}$')

        # # 获取cookie中的username
        # cookie_username = request.COOKIES.get('username')
        # # 获取cookie中的password
        # cookie_password = request.COOKIES.get('password')

        # 检验登陆状态
        if logged_in != 'no' and username != 'null' and ePattern.search(username):
            now_user = username
            username_head = now_user.split('@')[0][:len(now_user.split('@')[0]) // 2]
            username_tail = '@' + now_user.split('@')[1]
        elif logged_in != 'no' and username != 'null' and mPattern.search(username):
            now_user = username
            username_head = now_user[:3]
            username_tail = now_user[-4:]
        else:
            username_head, username_tail, now_user = None, None, None
        # 对结果进行返回
        return now_user, username_head, username_tail


