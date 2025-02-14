import lib.file as file
import os,time

class log:
    """
    :class:`log` 类用于日志记录。
    :param app_name: 应用名，用于生成日志文件名。
    :param console: 是否输出到控制台。
    :param file: 是否输出到文件。

    此类用于各个应用模块的日志记录，日志信息会被写入到日志文件中，并根据日志级别
    输出到控制台或文件中。
    
    日志级别包括: ERROR, WARNING, INFO, DEBUG, SUCCESS。
    日志信息必须是字符串。

    日志输出可以选择输出到控制台或文件中，可以通过设置`console`和`file`参数来控制。
    例如: `log.info("This is a info message.", console=True, file=True)`
    
    输出格式一般为: `[时间.日志级别.模块名] - [日志信息]` 或 `[日志级别/模块名] - [日志信息]`
    例如: 
    `[UTC-0800 2025-01-01 12:00:00.INFO.App] - This is a info message.`
    `[INFO/App] - This is a info message.`(控制台输出)
    
    输出文件一般位于log/目录下，文件名为`log/[应用名]/[应用名]_[自动生成的日志编号].log`，
    例如`log/App/App_20250101010101.log`。
    """
    ERROR = ["ERROR",0]
    WARNING = ["WARNING",1]
    INFO = ["INFO",2]
    DEBUG = ["DEBUG",3]
    SUCCESS = ["SUCCESS",4]

    # 日志级别颜色
    level_color = {
        "ERROR": "\033[31m",
        "WARNING": "\033[33m",
        "INFO": "\033[32m",
        "DEBUG": "\033[34m",
        "SUCCESS": "\033[36m"
    }

    def __init__(self, app_name, console=True, file=True):
        self.app_name = app_name
        self.console = console
        self.file = file
        self.log_dir = os.path.join(os.getcwd(), f"log/{app_name}/")
        self.log_file = os.path.join(self.log_dir, f"{app_name}_{time.strftime('%Y%m%d%H%M%S', time.localtime())}.log")
        if not os.path.exists(self.log_dir):
            os.makedirs(self.log_dir)
        if not os.path.exists(self.log_file):
            with open(self.log_file, "w", encoding="utf-8") as f:
                f.write("")

    def _write_log(self, level, module, message):
        
        # 写入日志文件
        if self.file:
            with open(self.log_file, "a", encoding="utf-8") as f:
                # 格式化日志信息，自动对齐前面的`[`和`]``
                data = f"[{time.strftime('%Y.%m.%d %H:%M:%S', time.localtime())}.{level}.{module}] - {message}\n"
                for line in data.split("\n"):
                    f.write(line.ljust(40) + "\n")
        
        # 输出到控制台
        if self.console:
            print(f"{log.level_color[level]}{level}/{module} - {message}\033[0m")

    def error(self, message, module="App"):
        """
        输出错误日志。
        :param message: 日志信息。
        :param module: 日志模块。
        """
        self._write_log(log.ERROR[0], module, message)

    def warning(self, message, module="App"):
        """
        输出警告日志。
        :param message: 日志信息。
        :param module: 日志模块。
        """
        self._write_log(log.WARNING[0], module, message)

    def info(self, message, module="App"):
        """
        输出信息日志。
        :param message: 日志信息。
        :param module: 日志模块。
        """
        self._write_log(log.INFO[0], module, message)

    def debug(self, message, module="App"):
        """
        输出调试日志。
        :param message: 日志信息。
        :param module: 日志模块。
        """
        self._write_log(log.DEBUG[0], module, message)

    def success(self, message, module="App"):
        """
        输出成功日志。
        :param message: 日志信息。
        :param module: 日志模块。
        """
        self._write_log(log.SUCCESS[0], module, message)

    def print_log(self, log_file):
        """
        输出日志文件内容。
        :param log_file: 日志文件路径。
        """
        if os.path.exists(log_file):
            with open(log_file, "r", encoding="utf-8") as f:
                print(f.read())
        else:
            print(f"日志文件 {log_file} 不存在！")