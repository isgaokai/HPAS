from django.db import models


# Create your models here.
# 管理员表
class Administrator(models.Model):
    # 昵称
    nickname = models.CharField(max_length=16, null=True, blank=True, verbose_name="昵称")
    # 手机号
    phone = models.CharField(max_length=11, null=True, blank=True, verbose_name='手机号')
    # 邮箱
    email = models.CharField(max_length=30, null=True, blank=True, verbose_name='邮箱')
    # 密码
    password = models.CharField(max_length=33, verbose_name='密码')
    # 密码加盐
    password_salt = models.CharField(max_length=6,verbose_name='密码加盐',default='eqwe./')
    # 头像
    head_portrait = models.ImageField(upload_to='admin_portraits', null=True, blank=True)
    # 注册ip
    registered_ip_address = models.GenericIPAddressField(protocol='IPv4',verbose_name='注册IP')
    # 最后登陆ip
    last_ip = models.GenericIPAddressField(protocol='IPv4', verbose_name="最后登陆IP", null=True, blank=True)
    # 登陆时间
    last_login = models.DateTimeField(auto_now_add=True,verbose_name='最后登陆时间', null=True, blank=True)
    # 是否被删除
    is_deleted = models.BooleanField(default=False)
    # 元数据
    class Meta:
        # 修改表名
        db_table = 't_admin'
        verbose_name = '管理员'
        verbose_name_plural = verbose_name


# 普通用户表
class NormalUser(models.Model):
    # 昵称
    nickname = models.CharField(max_length=16, null=True, blank=True, verbose_name="昵称")
    # 手机号
    phone = models.CharField(max_length=11, null=True, blank=True, verbose_name='手机号')
    # 邮箱
    email = models.CharField(max_length=30, null=True, blank=True, verbose_name='邮箱')
    # 密码
    password = models.CharField(max_length=33, verbose_name='密码')
    # 密码加盐
    password_salt = models.CharField(max_length=6,verbose_name='密码加盐',default='eqwe./')
    # 头像
    head_portrait = models.ImageField(upload_to='user_portraits', null=True, blank=True )
    # 注册ip
    registered_ip_address = models.GenericIPAddressField(protocol='IPv4',verbose_name='注册IP')
    # 最后登陆ip
    last_ip = models.GenericIPAddressField(protocol='IPv4', verbose_name="最后登陆IP", null=True, blank=True )
    # 登陆时间
    last_login = models.DateTimeField(auto_now_add=True,verbose_name='最后登陆时间', null=True, blank=True)
    # 使用的激活码
    used_code = models.CharField(max_length=12,null=True,verbose_name='绑定激活码')
    # 是否被删除
    is_deleted = models.BooleanField(default=False)
    # 元数据
    class Meta:
        db_table = 't_normal_user'
        verbose_name = '普通用户'
        verbose_name_plural = verbose_name

# 激活码
class Code(models.Model):
    # 激活码
    cdk = models.CharField(max_length=12)
    # 状态
    state = models.BooleanField(default=True)
    # 元数据
    class Meta:
        db_table = 't_code'
        verbose_name = '激活码'
        verbose_name_plural = verbose_name