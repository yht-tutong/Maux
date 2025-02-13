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

import os
import shutil
 
class file:
    """
    文件及目录操作类，封装了文件及目录操作的常用方法
    实现了上下文管理器支持，可以自动关闭文件
    """
    def __init__(self, name, mode) -> None:
        self.name = name
        self.mode = mode
        try:
            if not os.path.exists(self.name) and 'r' in self.mode:
                raise FileNotFoundError(f"The file or directory '{self.name}' does not exist.")
            self.file = open(name, mode)
        except Exception as e:
            print(f"Error opening file: {e}")
 
    def __enter__(self):
        """
        返回文件对象
        """
        return self
 
    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        自动关闭文件
        """
        self.close()

    def create(self,name) -> bool:
        """
        创建文件
        :return: True创建成功，False创建失败
        """
        try:
            with open(name, 'w') as f:
                f.write('')
            return True
        except Exception as e:
            print(f"Error creating file: {e}")
            return False
    def read(self, size=None) -> str:
        """
        读取文件内容
        :size: 读取的字节数，默认为None，表示读取全部内容
        :return: 读取到的内容
        """
        try:
            return self.file.read(size)
        except Exception as e:
            print(f"Error reading file: {e}")
            return 'None'
 
    def write(self, data) -> None:
        """
        写入文件内容，默认模式为“a”（追加）
        :data: 要写入的内容
        """
        try:
            self.file.write(data)
        except Exception as e:
            print(f"Error writing to file: {e}")
        finally:
            self.file.close()
 
    def close(self) -> None:
        """
        关闭文件
        """
        try:
            self.file.close()
        except Exception as e:
            print(f"Error closing file: {e}")
 
    def folder(self) -> bool:
        """
        判断是否为目录
        :return: True为目录，False为文件
        """
        try:
            return os.path.isdir(self.name)
        except Exception as e:
            print(f"Error checking if '{self.name}' is a directory: {e}")
            return False
 
    def exists(self) -> bool:
        """
        判断文件或目录是否存在
        :return: True存在，False不存在
        """
        try:
            return os.path.exists(self.name)
        except Exception as e:
            print(f"Error checking if '{self.name}' exists: {e}")
            return False
 
    def size(self) -> int or None:
        """
        获取文件大小
        :return: 文件大小，单位为字节
        """
        try:
            return os.path.getsize(self.name)
        except Exception as e:
            print(f"Error getting size of '{self.name}': {e}")
            return None
 
    def rename(self, new_name) -> None:
        """
        重命名文件或目录
        :new_name: 新的文件名或目录名
        """
        try:
            os.rename(self.name, new_name)
            self.name = new_name  # 更新文件名
        except Exception as e:
            print(f"Error renaming '{self.name}' to '{new_name}': {e}")
 
    def delete(self) -> None:
        """
        删除文件或目录
        """
        try:
            if self.folder():
                shutil.rmtree(self.name)
            else:
                os.remove(self.name)
        except Exception as e:
            print(f"Error deleting '{self.name}': {e}")
 
    def mkdir(self) -> None:
        """
        创建目录
        """
        try:
            os.mkdir(self.name)
        except Exception as e:
            print(f"Error creating directory '{self.name}': {e}")
 
    def listdir(self) -> list:
        """
        列出目录下的文件和目录
        :return: 目录下的文件和目录列表
        """
        try:
            return os.listdir(self.name)
        except Exception as e:
            print(f"Error listing contents of '{self.name}': {e}")
            return []
 
    def copy(self, new_name) -> None:
        """
        复制文件或目录
        :new_name: 新的文件名或目录名
        """
        try:
            if self.folder():
                shutil.copytree(self.name, new_name)
            else:
                shutil.copy(self.name, new_name)
        except Exception as e:
            print(f"Error copying '{self.name}' to '{new_name}': {e}")
 
    def move(self, new_name) -> None:
        """
        移动文件或目录
        :new_name: 新的文件名或目录名
        """
        try:
            shutil.move(self.name, new_name)
            self.name = new_name  # 更新文件名
        except Exception as e:
            print(f"Error moving '{self.name}' to '{new_name}': {e}")
 
    def zip(self, new_name) -> str or None:
        """
        压缩文件或目录
        :new_name: 压缩后的文件名（不包括“.zip”）
        """
        try:
            return shutil.make_archive(new_name, "zip", self.name)
        except Exception as e:
            print(f"Error zipping '{self.name}': {e}")
            return None
 
    def unzip(self, new_name) -> str or None:
        """
        解压文件
        :new_name: 解压后的目录名
        """
        try:
            return shutil.unpack_archive(self.name, new_name)
        except Exception as e:
            print(f"Error unzipping '{self.name}': {e}")
            return None
 
 
# 测试单元
def main():
    # 上下文管理器测试
    with file('test.txt', 'w') as f:
        f.write('Hello, world!')
    with file('test.txt', 'r') as f:
        print(f.read())
 
 
if __name__ == '__main__':
    main()