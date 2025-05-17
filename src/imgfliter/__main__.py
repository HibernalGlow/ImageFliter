"""
ImgFilter命令行工具入口点
"""
import sys
import argparse
from imgfilter.cli import commands

def main():
    """执行命令行功能"""
    parser = argparse.ArgumentParser(description="ImgFilter - 图片过滤工具")
    commands.setup_parser(parser)
    args = parser.parse_args()
    
    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())