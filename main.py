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

import lib.boot as boot
import lib.file as file
import lib.lib as lib

def main() -> None:
    # 创建必须的系统需要的第三方库列表
    lib_list = ['tqdm','shutil','requests']

    # 创建必须的第三方库列表文件`lib/requirements.txt`,并写入lib_list的内容
    with file.file('lib/requirements.txt','w') as f:
        f.write('\n'.join(lib_list))

    # 判断`install.mux`文件是否存在,如果不存在则判定未安装系统，
    # 并在调用boot().run()时，传入install=True的参数
    if not file.file('install.mux','r').exists():
        boot.boot(install=True).run()
    else:
        boot.boot().run()
    return None

# lib模块测试
def test_lib() -> None:
    import lib.log as log

    # lib.log模块测试
    log.log(f'APP').error('This is an error message')
    log.log(f'APP').info('This is an info message')
    log.log(f'APP').debug('This is a debug message')
    log.log(f'APP').warning('This is a warning message')

    return None

if __name__ == '__main__':
    test_lib()