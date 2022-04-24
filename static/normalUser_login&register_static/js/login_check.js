function button_submit() {

    // form 表单
    let login_form = document.getElementById('login_form');
    // 验证码输入正确隐藏框
    let tip_captcha_ok = document.getElementById('captcha_ok').innerText
    // 用户名输入正确隐藏框
    let tip_username_ok = document.getElementById('username_ok').innerText
    // 密码输入正确隐藏框
    let tip_password_ok = document.getElementById('password_ok').innerText

    if (tip_captcha_ok === 't' & tip_username_ok === 't' & tip_password_ok === 't' ) {
        // 提交表单
        login_form.submit()
    } else {
        // 提示框
        toastr.error('提交失败！请检查您输入的信息！')
    }
}