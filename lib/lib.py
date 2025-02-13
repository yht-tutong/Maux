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

class lib:
    """
    PYPI镜像源
    清华大学TUNA镜像源:tsinghua_mirror_url
    阿里云源:aliyun_mirror_url
    中国科学技术大学镜像源:utsc_mirror_url
    华为云镜像源:huaweicloud_mirror_url
    腾讯云镜像源:tencent_mirror_url
    """

    tsinghua_mirror_url:str = 'https://pypi.tuna.tsinghua.edu.cn/simple'
    aliyun_mirror_url:str = 'https://mirrors.aliyun.com/pypi/simple'
    utsc_mirror_url:str = 'https://mirrors.ustc.edu.cn/pypi/simple/'
    huaweicloud_mirror_url:str = 'https://repo.huaweicloud.com/repository/pypi/simple/'
    tencent_mirror_url:str = 'https://mirrors.cloud.tencent.com/pypi/simple/'
    pypi_url:str = 'https://pypi.org/simple'

    def __init__(self,site:str = tsinghua_mirror_url) -> None:
        self.site = site
        return None

    def check(self,lib:str = 'os') -> bool:
        """
        检查传入参数中的软件包是否存在，例如：
        `lib().check('os')`
        """
        try:
            __import__(f'{lib}')
            return True
        except ImportError:
            return False

    def install(self,*args) -> str:
        """
        安装传入参数中的软件包，例如：
        `lib().install('os','tqdm')`
        如果需要更改安装源，可以传入参数：
        `lib(site='https://pypi.tuna.tsinghua.edu.cn/simple').install('os','tqdm')`
        或者直接传入lib.tsinghua_mirror_url的值
        `lib(lib.tsinghua_mirror_url).install('os','tqdm')`
        """
        try:
            import os
            for i in args:
                try:
                    os.system(f"pip install {i} -i {self.site}")
                    return f"Successful"
                except:
                    print(f"pip install {i} -i {self.site} failed")
                    return f"Failed"
                finally:
                    continue
        except Exception as e:
            return 'Failed'

    def uninstall(self,*args) -> str:
        """
        卸载传入参数中的软件包，例如：
        `lib().uninstall('os','tqdm')`
        """
        try:
            import os
            for i in args:
                try:
                    os.system(f"pip uninstall {i} -y")
                    return f"Successful"
                except:
                    print(f"pip uninstall {i} -y failed")
                    return f"Failed"
                finally:
                    continue
        except Exception as e:
            return 'Failed'

    def info(self,lib:str = 'os') -> dict:
        """
        获取传入参数中的软件包的信息，例如：
        `lib().info('os')`
        """
        try:
            import pip
            from pip._internal.commands.show import search_packages_info
            info = search_packages_info([lib], self.site)
            return info
        except Exception as e:
            return dict('Failed', e)

    def list(self) -> list:
        """
        获取当前镜像源中的所有软件包，例如：
        `lib().list()`
        """
        try:
            import pip
            from pip._internal.commands.list import list_packages
            packages = list_packages(self.site)
            return packages
        except Exception as e:
            return list('Failed', e)

    def help(self) -> None:
        """
        打印帮助信息，例如：
        `lib().help()`
        """
        print("""
        PYPI镜像源
        清华大学TUNA镜像源:tsinghua_mirror_url
        阿里云源:aliyun_mirror_url
        华为云镜像源:huaweicloud_mirror_url
        腾讯云镜像源:tencent_mirror_url
        """)
        return None

# 测试模块
def main():
    lib().install('os','tqdm')

if __name__ == '__main__':
    main()