"""
BadZipFliter - 压缩文件完整性检查工具入口点

此工具用于检测压缩文件是否损坏，并将损坏的文件重命名为.tdel后缀
"""
import sys
from src.badzipfliter import run_check

if __name__ == "__main__":
    # 执行检查函数并获取返回的状态码
    exit_code = run_check()
    # 将状态码作为程序的退出码
    sys.exit(exit_code)

