function button_submit() {

    // form 表单
    let register_form = document.getElementById('register_form')
    // 激活码输入正确隐藏框
    let tip_code_ok = document.getElementById('code_ok').innerText
    // 验证码输入正确隐藏框
    let tip_captcha_ok = document.getElementById('captcha_ok').innerText
    // 用户名输入正确隐藏框
    let tip_username_ok = document.getElementById('username_ok').innerText
    // 密码输入正确隐藏框
    let tip_password_ok = document.getElementById('password_ok').innerText
    // 重复密码正确隐藏框
    let tip_re_password_ok = document.getElementById('re_password_ok').innerText

    if (tip_captcha_ok === 't' & tip_username_ok === 't' & tip_password_ok === 't' & tip_re_password_ok === 't' & tip_code_ok === 't') {
            // 提交表单
            register_form.submit()
        } else {
            // 提示框
            toastr.error('提交失败！请检查您输入的信息！')
        }
}

