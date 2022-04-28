// 检验旧密码
function ajax_old_password() {
     // 接收前端用户输入的密码
    let input_old_password = document.getElementById('txt_old_password').value;
    // 密码输入正确隐藏框
    let tip_old_password_ok = document.getElementById('old_password_ok');
    // 长度为0 则还原
    if (input_old_password.length === 0) {
        tip_old_password_ok.innerText = ''
    }
    // 判断输入密码长度
    else if (input_old_password.length < 6 || input_old_password.length > 16) {
        // 提示框
        tip_old_password_ok.innerText = 'f'
    } else {
        // 发送异步的ajax请求
        $.ajax({
            // 请求类型
            type: 'get',
            // 请求地址
            url: '/ajax/check_old_password/',
            // 请求需要携带的参数
            data: 'input_old_password=' + input_old_password,
            // 请求成功的回调函数
            success: function (response) {
                // 如果用户输入错误
                if (response === 'False') {
                    // 提示框
                    tip_old_password_ok.innerText = 'f'
                }
                // 极高强度密码
                else {
                    // 提示框
                    tip_old_password_ok.innerText = 't'
                }
            }
        })
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

function button_submit() {
    // 密码输入正确隐藏框
    let tip_password_ok = document.getElementById('password_ok').innerText
    // 重复密码正确隐藏框
    let tip_re_password_ok = document.getElementById('re_password_ok').innerText
    // 原密码输入正确隐藏框
    let tip_old_password_ok = document.getElementById('old_password_ok').innerText;
    let new_password = document.getElementById('txt_password').value;
    let user_id = document.getElementById('txt_id').getAttribute('placeholder');

    if ( tip_password_ok === 't' & tip_re_password_ok === 't'&tip_old_password_ok==='t') {
        // 提交表单
        ajax_change_user_password(user_id,new_password)
    } else {
        // 提示框
        toastr.error('修改失败！请检查您输入的信息！')
    }
}

function ajax_change_user_password(user_id,new_password) {
    // 发送ajax请求
    $.ajax({
        type: "GET",
        url: "/ajax/change_user_password/",
        data: 'change_user_id=' + user_id +'&new_password=' + new_password,
        success: function (response) {
            if (response === 'false') {
                toastr.error('修改失败！')
            } else {
                toastr.success('修改成功！')
            }
        }
    })

}

