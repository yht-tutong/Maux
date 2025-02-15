"""
Copyright (c) [2025] [Maux Studio of copyright holder]
[Software Maux] is licensed under Mulan PSL v2.
You can use this software according to the terms and conditions of the Mulan PSL v2.
You may obtain a copy of Mulan PSL v2 at:
         http://license.coscl.org.cn/MulanPSL2
THIS SOFTWARE IS PROVIDED ON AN "AS IS" BASIS, WITHOUT WARRANTIES OF ANY KIND,
EITHER EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO NON-INFRINGEMENT,
MERCHANTABILITY OR FIT FOR A PARTICULAR PURPOSE.
See the Mulan PSL v2 for more details.
"""

# import lib.boot as boot
# import lib.file as file
# import lib.lib as lib

import os

def main() -> None:
    os.system('cls')

    print("\033[33mCopyright (c) [2025] [Maux Studio of copyright holder]\n\033[32mWelcome to JHS beta version 0.2\033[1;37m")
    
    # 判断`system.wsl`文件是否存在,如果不存在则判定未安装系统，
    # 并在调用boot().run()时，传入install=True的参数
    #if not file.file('system.wsl','r').exists():
    #    boot.boot(install=True).run()
    #else:
    #    boot.boot().run()
    #return None

    if input("该程序会直接下载ubuntu系统!输入小写\"y\"以继续") == "y":
        install()

def install():
    print("\033[31m请不要关闭程序!")
    os.system("wsl --install")
    print("安装成功!请打开本目录下的.wsl文件!")
    input("按下确认键来结束程序!")
    os.system("quit")

# lib模块测试
# def test_lib() -> None:
#     import lib.log as log

#     # lib.log模块测试
#     log.log(f'APP').error('This is an error message')
#     log.log(f'APP').info('This is an info message')
#     log.log(f'APP').debug('This is a debug message')
#     log.log(f'APP').warning('This is a warning message')

#     return None

if __name__ == '__main__':
    # test_lib()
    main()