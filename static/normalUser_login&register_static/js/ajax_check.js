// 验证码检验
function ajax_captcha() {
    // 接收前端用户输入的验证码
    let input_captcha = document.getElementById('txt_captcha').value;
    // 验证码输入正确隐藏框
    let tip_captcha_ok = document.getElementById('captcha_ok')
    // 发送异步的ajax请求
    $.ajax({
        // 请求类型
        type: 'get',
        // 请求地址
        url: '/ajax/check_captcha/',
        // 请求要传递的参数
        data: 'input_captcha=' + input_captcha,
        // 请求成功返回的回调函数
        success: function (response) {
            // 如果用户输入正确
            if (response === 'true') {
                // 提示框
                toastr.success('验证码输入正确！')
                tip_captcha_ok.innerText = 't'
            }
            // 如果用户输入错误
            else if (response === 'false' & input_captcha.length > 0) {
                // 提示框
                toastr.error('验证码输入错误！')
                tip_captcha_ok.innerText = 'f'
            }
        }
    })
}

// 用户名检验
function ajax_username() {
    // 接收前端用户输入的用户名
    let input_username = document.getElementById('txt_username').value;
    // 用户名输入正确隐藏框
    let tip_username_ok = document.getElementById('username_ok')
    // 手机号正则
    let mPattern = /^((13[0-9])|(19[8])|(14[5|7])|(15([0-3]|[5-9]))|(18[0,5-9]))\d{8}$/;
    // 邮箱正则
    let ePattern = /^[A-Za-z\d]+([-_.][A-Za-z\d]+)*@([A-Za-z\d]+[-.])+[A-Za-z\d]{2,5}$/;

    // 正则检验
    if (mPattern.test(input_username) || ePattern.test(input_username)) {
        // 发送异步的ajax请求
        $.ajax({
            // 请求类型
            type: 'get',
            // 请求地址
            url: '/ajax/check_username/',
            // 请求要传递的参数
            data: 'input_username=' + input_username,
            // 请求成功返回的回调函数
            success: function (response) {
                // 如果用户输入正确
                if (response === 'true') {
                    // 提示框
                    toastr.success('当前邮箱/手机号可用！')

                    tip_username_ok.innerText = 't'
                }
                // 如果已被注册/绑定
                else if (response === 'false') {
                    // 提示框
                    toastr.error('当前邮箱或手机号已被注册/绑定！')
                    tip_username_ok.innerText = 'f'
                }
                // 未通过检验
                else if (response === 'checkfalse') {
                    // 提示框
                    toastr.error('当前输入不符合注册规定!')
                    tip_username_ok.innerText = 'f'
                }
            }
        })

    }
    // 提示
    else if (input_username.length > 0) {
        // 提示框
        toastr.error('当前输入不符合注册规定!')
        tip_username_ok.innerText = 'f'
    }
    // 长度为0 则还原
    else if (input_username.length === 0) {
        tip_username_ok.innerText = ''
    }
}

// 激活码检验
function ajax_code() {
    // 接收前端用户输入激活码
    let input_code = document.getElementById('txt_code').value;
    // 激活码输入正确隐藏框
    let tip_code_ok = document.getElementById('code_ok');

    // 长度为0则还原
    if (input_code.length === 0){
        tip_code_ok.innerText = ''
    }
    // 判断长度是否12位
    else if (input_code.length === 12){
        // 发送异步ajax请求
        $.ajax({
            // 请求类型
            type: 'get',
            // 请求地址
            url: '/ajax/check_code',
            // 请求要传递的参数
            data: 'input_code=' + input_code,
            // 请求成功返回的回调函数
            success: function (response) {
            // 如果用户输入正确
            if (response === 'true') {
                // 提示框
                toastr.success('激活码有效！')
                tip_code_ok.innerText = 't'
            }
            // 如果用户输入错误
            else if (response === 'false' & input_code.length === 12) {
                // 提示框
                tip_code_ok.innerText = 'f'
            }
        }
        })
    }
    else {
        tip_code_ok.innerText = 'f'
    }
}

// 密码检验
function ajax_password() {
    // 接收前端用户输入的密码
    let input_password = document.getElementById('txt_password').value;
    // 密码输入正确隐藏框
    let tip_password_ok = document.getElementById('password_ok');
    // 长度为0 则还原
    if (input_password.length === 0) {
        tip_password_ok.innerText = ''
    }
    // 判断输入密码长度
    else if (input_password.length < 6 || input_password.length > 16) {
        // 提示框
        toastr.error('密码长度错误！')
        tip_password_ok.innerText = 'f'
    } else {
        // 发送异步的ajax请求
        $.ajax({
            // 请求类型
            type: 'get',
            // 请求地址
            url: '/ajax/check_password/',
            // 请求需要携带的参数
            data: 'input_password=' + input_password,
            // 请求成功的回调函数
            success: function (response) {
                // 如果用户输入错误
                if (response === 'False') {
                    // 提示框
                    toastr.error('当前密码不符合注册规定！')
                    tip_password_ok.innerText = 'f'
                }
                // 低强度密码
                else if (response === 'LowSecurity') {
                    // 提示框
                    toastr.error('密码未通过验证！当前强度：低！')
                    tip_password_ok.innerText = 'f'
                }
                // 中等强度密码
                else if (response === 'MediumSecurity') {
                    // 提示框
                    toastr.success('密码通过验证！当前强度：中！')
                    tip_password_ok.innerText = 't'
                }
                // 高等强度密码
                else if (response === 'HighSecurity') {
                    // 提示框
                    toastr.success('密码通过验证！当前强度：高！')
                    tip_password_ok.innerText = 't'
                }
                // 极高强度密码
                else if (response === 'ExtermeHighSecurity') {
                    // 提示框
                    toastr.success('密码通过验证！当前强度：极高！')
                    tip_password_ok.innerText = 't'
                }
            }
        })
    }
}

// 二次输入密码检验
function ajax_re_password() {
    // 接收前端用户输入的第一遍密码
    let input_first_password = document.getElementById('txt_password').value;
    // 重复密码正确隐藏框
    let tip_re_password_ok = document.getElementById('re_password_ok');
    // 接收用户输入的第二遍密码
    let input_second_password = document.getElementById('txt_re_password').value;


    if (input_second_password.length === 0) {
        tip_re_password_ok.innerText = ''
    } else if (input_first_password === input_second_password) {
        // 提示框
        toastr.success('两次输入密码一致！')
        tip_re_password_ok.innerText = 't'
    } else {
        toastr.error('两次输入密码不一致！')
        tip_re_password_ok.innerText = 'f'
    }

}

// 登陆用户名检验
function ajax_login_username() {
    // 接收前端用户输入的用户名
    let input_username = document.getElementById('txt_username').value;
    // 用户名输入正确隐藏框
    let tip_username_ok = document.getElementById('username_ok')
    // 手机号正则
    let mPattern = /^((13[0-9])|(19[8])|(14[5|7])|(15([0-3]|[5-9]))|(18[0,5-9]))\d{8}$/;
    // 邮箱正则
    let ePattern = /^[A-Za-z\d]+([-_.][A-Za-z\d]+)*@([A-Za-z\d]+[-.])+[A-Za-z\d]{2,5}$/;


    // 正则检验
    if (mPattern.test(input_username) || ePattern.test(input_username)) {
        // 发送异步的ajax请求
        $.ajax({
            // 请求类型
            type: 'get',
            // 请求地址
            url: '/ajax/check_username/',
            // 请求要传递的参数
            data: 'input_username=' + input_username,
            // 请求成功返回的回调函数
            success: function (response) {
                // 未查询到该用户
                if (response === 'true') {
                    tip_username_ok.innerText = 'f'
                    toastr.error('当前用户未注册！')
                }
                // 查询到该用户
                else if (response === 'false') {
                    tip_username_ok.innerText = 't'
                }
                // 未通过检验
                else if (response === 'checkfalse') {
                    tip_username_ok.innerText = 'f'
                }
            }
        })

    }
    // 提示
    else if (input_username.length > 0) {
        tip_username_ok.innerText = 'f'
    }
    // 长度为0 则还原
    else if (input_username.length === 0) {
        tip_username_ok.innerText = ''
    }
}

// 登陆密码检验
function ajax_login_password() {
    // 接收前端用户输入的密码
    let input_password = document.getElementById('txt_password').value;
    // 密码输入正确隐藏框
    let tip_password_ok = document.getElementById('password_ok')
    // 密码正则检验 支持字母数字标点符合 特殊符合 6，16位
    let pPattern = /^(?:(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])|(?=.*[A-Z])(?=.*[a-z])(?=.*[^A-Za-z0-9])|(?=.*[A-Z])(?=.*[0-9])(?=.*[^A-Za-z0-9])|(?=.*[a-z])(?=.*[0-9])(?=.*[^A-Za-z0-9])).{6,}|(?:(?=.*[A-Z])(?=.*[a-z])|(?=.*[A-Z])(?=.*[0-9])|(?=.*[A-Z])(?=.*[^A-Za-z0-9])|(?=.*[a-z])(?=.*[0-9])|(?=.*[a-z])(?=.*[^A-Za-z0-9])|(?=.*[0-9])(?=.*[^A-Za-z0-9])|).{6,16}$/

    // 长度为0 则还原
    if (input_password.length === 0) {
        tip_password_ok.innerText = ''
    } else if (pPattern.test(input_password)) {
        tip_password_ok.innerText = 't'

    } else {
        toastr.error('输入密码格式错误！')
        tip_password_ok.innerText = 'f'
    }

}