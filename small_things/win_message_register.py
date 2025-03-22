import win32gui
import win32api
import random
import string
# 使用程序后电脑如果出问题，重启即可
for i in range(16384):
    msg_name = "msg"+str(i)
    msg_id = win32gui.RegisterWindowMessage("msg"+str(i))
    if msg_id == 0:
        error_code = win32api.GetLastError()
        print(f"无法使用 '{msg_name}'注册消息 错误代码: {error_code}")# 错误代码8: ERROR_NOT_ENOUGH_MEMORY
    else:
        print(f"成功使用'{msg_name}' 注册了 {msg_id} 号消息")
