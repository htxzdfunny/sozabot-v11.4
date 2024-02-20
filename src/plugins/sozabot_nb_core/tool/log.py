import datetime
import os
import sys


class Log:
    def __init__(self, original_stdout, log_file):
        self.original_stdout = original_stdout
        self.log_file = log_file

    def write(self, message):
        self.original_stdout.write(message)  # 不做任何修改，保留原始 print 的换行符
        timestamp = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        with open(self.log_file, "a") as f:
            # 在写入日志文件时去除末尾的换行符，并自己添加格式化的日期时间前缀
            if message.endswith("\n"):
                formatted_message = f"{timestamp}: {message[:-1]}"
            else:
                formatted_message = f"{timestamp}: {message}"
            f.write(formatted_message + "\n")  # 添加一个换行符以保证日志记录之间的间隔

    def flush(self):
        self.original_stdout.flush()


def log_decorator(func):
    """
    记录被修饰方法的运行日志

    Args:
        func: 要修饰的方法

    Returns:
        修饰后的方法
    """

    def wrapper(*args, **kwargs):
        # 获取当前日期和时间
        now = datetime.datetime.now()
        date_str = now.strftime("%Y-%m-%d")

        # 创建或打开当天的日志文件
        log_file_path = os.path.join("log", f"{date_str}.txt")
        if not os.path.exists(os.path.dirname(log_file_path)):
            os.makedirs(os.path.dirname(log_file_path))

        with open(log_file_path, "a") as f:
            f.write(f"\n{now.strftime('%Y/%m/%d %H:%M:%S')}: 函数 {func.__name__} 开始执行\n")

        # 替换 stdout 为 TeeStdout 对象
        original_stdout = sys.stdout
        tee_stdout = Log(original_stdout, log_file_path)
        sys.stdout = tee_stdout

        try:
            result = func(*args, **kwargs)
        except Exception as e:
            # 记录函数执行异常
            with open(log_file_path, "a") as f:
                f.write(
                    f"{now.strftime('%Y/%m/%d %H:%M:%S')}: 函数 {func.__name__} 执行异常: {str(e)}\n"
                )
            raise e

        # 恢复原 stdout
        sys.stdout = original_stdout

        # 记录函数执行结束
        with open(log_file_path, "a") as f:
            f.write(f"{now.strftime('%Y/%m/%d %H:%M:%S')}: 函数 {func.__name__} 执行结束\n")

        return result

    return wrapper
