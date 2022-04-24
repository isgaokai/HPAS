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
            url: '/ajax/check_admin_username/',
            // 请求要传递的参数
            data: 'input_username=' + input_username,
            // 请求成功返回的回调函数
            success: function (response) {
                // 未查询到该用户
                if (response === 'true') {
                    tip_username_ok.innerText = 'f'
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