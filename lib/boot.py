import lib

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

class boot:
    install = False
    def __init__(self,install:bool = install) -> None:
        self.install = install
        return None

    def run(self) -> None:
        # 
        if self.install is True:
            with lib.file.file(f'install.mux','w') as f:
                f.write(f'')
        else:
            pass
        return None