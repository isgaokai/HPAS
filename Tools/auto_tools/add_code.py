# -*- encoding : utf-8 -*-
# @Project -> File     ：HPAS -> add_code         
# @IDE      ：PyCharm
# @Author   ：Fenglchen
# @Date     ：2022/4/4 9:28 下午
# @Software : macos python3.8
import pymysql
import random
# 小写字母表
lower_alpha_table = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                     't', 'u', 'v', 'w', 'x', 'y', 'z']
# 大写字母表
upper_alpha_table = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                     'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# 数字表
number_table = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

code = ''.join(random.sample(number_table + upper_alpha_table + lower_alpha_table , 12))
print(code)
# 连接数据库
database = pymysql.connect(host='192.168.2.2', user='root', password='woaini', database='db_hpas', port=3306,
                           charset='utf8')
# 创建游标
cdk_hash = {'rNiAqCIORMhJ':1}
sor = database.cursor()
sql = 'insert into t_code(cdk,state) values(%s,%s)'
for _ in range(10000):
    code = ''.join(random.sample(number_table + upper_alpha_table + lower_alpha_table, 12))
    if code in cdk_hash:
        continue
    cdk_hash[code] = 1
    sor.execute(sql,(code,True))
    database.commit()
sor.close()
database.close()