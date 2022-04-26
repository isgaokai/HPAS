// ajax加载数据
function ajax_load_data() {
    // 获取div
    let user_table = document.getElementById('tUser');

    let page_count = document.getElementById('page_count');

    $.ajax({
        // 请求类型
        type: "GET",
        // 请求地址
        url: "/ajax/load_data/",
        // 请求传递参数
        data: 'page_count=' + page_count.innerText,
        // 请求成功回调函数
        success: function (response) {
            if (response === 'false') {

            } else {
                // 读取json格式
                response = JSON.parse(response)
                // 循环添加子元素
                for (var i = 0; i < response.length; i++) {
                    // 当前用户
                    now_user = response[i]

                    // 创建新用户
                    let new_user = document.createElement('tr');

                    let user_id = document.createElement('td');
                    let user_detail = document.createElement('a');
                    let user_nickname = document.createElement('td');
                    let user_phone = document.createElement('td');
                    let user_email = document.createElement('td');
                    let user_registered_ip_address = document.createElement('td');
                    let user_last_login = document.createElement('td');
                    let user_used_code = document.createElement('td');
                    let user_is_deleted = document.createElement('td');
                    let user_button_td = document.createElement('td');
                    let user_button_f = document.createElement('div');
                    let user_button_s = document.createElement('div');
                    let user_button = document.createElement('button');
                    let user_button_span = document.createElement('span');
                    let user_button_text = document.createTextNode('\n' +
                        '                                                        删除\n' +
                        '                                                    ')

                    // 为子元素设置内容
                    user_detail.innerText = now_user['user_id']
                    user_nickname.innerText = now_user['user_nickname']
                    user_phone.innerText = now_user['user_phone']
                    user_email.innerText = now_user['user_email']
                    user_registered_ip_address.innerText = now_user['user_registered_ip_address']
                    user_last_login.innerText = now_user['user_last_login']
                    user_used_code.innerText = now_user['user_used_code']
                    user_detail.href = '/myAdmin/user_detail/?user_id=' + now_user['user_id']

                    // 为子元素设置样式
                    user_id.style = "text-align: center"
                    user_nickname.style = "text-align: center"
                    user_phone.style = "text-align: center"
                    user_email.style = "text-align: center"
                    user_registered_ip_address.style = "text-align: center"
                    user_last_login.style = "text-align: center"
                    user_used_code.style = "text-align: center"
                    user_is_deleted.style = "text-align: center"
                    user_button_f.className = "am-btn-toolbar"
                    user_button_s.className = "am-btn-group am-btn-group-xs"
                    user_button.className = "am-btn am-btn-default am-btn-xs am-text-danger am-hide-sm-only"
                    user_button_span.className = "am-icon-trash-o"

                    if (now_user['user_is_deleted'] === true) {
                        user_button.style = "pointer-events:none"
                        user_is_deleted.innerText = "True"
                    } else {
                        user_is_deleted.innerText = "False"
                        // user_button.onclick = "ajax_search_user()"

                    }
                    // 为子元素绑定父元素
                    user_id.appendChild(user_detail)
                    new_user.appendChild(user_id)
                    new_user.appendChild(user_nickname)
                    new_user.appendChild(user_phone)
                    new_user.appendChild(user_email)
                    new_user.appendChild(user_registered_ip_address)
                    new_user.appendChild(user_last_login)
                    new_user.appendChild(user_used_code)
                    new_user.appendChild(user_is_deleted)
                    user_button.appendChild(user_button_span)
                    user_button.appendChild(user_button_text)
                    user_button_s.appendChild(user_button)
                    user_button_f.appendChild(user_button_s)
                    user_button_td.appendChild(user_button_f)
                    new_user.appendChild(user_button_td)
                    user_table.appendChild(new_user)
                    // 添加按钮


                }
                // 成功加载一页
                page_count.innerText = Number(page_count.innerText) + 1
            }

        }
    })

}

// ajax搜索用户
function ajax_search_user() {
    // 输入框数据
    let input_search_user = document.getElementById('input_search_user').value;

    // 判断输入是否有效
    if (input_search_user) {
        // 发送ajax请求
        $.ajax({
            type: "GET",
            url: "/ajax/search_user/",
            data: 'input_search_user=' + input_search_user,
            success: function (response) {
                if (response === 'false') {
                    toastr.error('未查询到该用户！')
                } else {
                    window.location.href = '/myAdmin/user_detail/?user_id=' + response
                }
            }
        })
    }
}

// ajax删除用户
function ajax_delete_user() {
    // 输入框数据
    let input_search_user = document.getElementById('input_search_user').value;

    // 判断输入是否有效
    if (input_search_user) {
        // 发送ajax请求
        $.ajax({
            type: "GET",
            url: "/ajax/delete_user/",
            data: 'input_delete_user_id=' + input_search_user,
            success: function (response) {
                if (response === 'false') {
                    toastr.error('删除失败！')
                } else {
                    toastr.error('删除成功！')
                }
            }
        })
    }
}
