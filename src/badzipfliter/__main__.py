"""
主程序入口模块 - 整合所有功能并提供命令行接口
"""
import os
import sys
import argparse
from pathlib import Path
from loguru import logger

# 导入自定义模块
from badzipfliter.logger_module import setup_logger
from badzipfliter.path_handler import get_valid_paths
from badzipfliter.archive_checker import process_directory

# 尝试导入TUI界面模块（可能在某些环境下不可用）
try:
    from textual_logger import TextualLoggerManager
    TEXTUAL_AVAILABLE = True
except ImportError:
    TEXTUAL_AVAILABLE = False

from badzipfliter.config import TEXTUAL_LAYOUT

def main():
    """主程序入口函数"""
    parser = argparse.ArgumentParser(description='压缩包完整性检查工具')
    parser.add_argument('paths', nargs='*', help='要处理的路径列表')
    parser.add_argument('-c', '--clipboard', action='store_true', help='从剪贴板读取路径')
    parser.add_argument('--no_tui', action='store_true', help='不使用TUI界面，只使用控制台输出')
    parser.add_argument('--force_check', action='store_true', help='强制检查所有文件，忽略已处理记录')
    args = parser.parse_args()

    # 根据是否使用TUI配置日志
    if args.no_tui or not TEXTUAL_AVAILABLE:
        # 重新初始化日志，启用控制台输出
        logger, config_info = setup_logger(app_name="badzipfliter", console_output=True)
        logger.info("使用控制台输出模式")
    else:
        # 初始化日志，不使用控制台输出（将由TUI接管）
        logger, config_info = setup_logger(app_name="badzipfliter", console_output=False)
        # 初始化TextualLogger
        TextualLoggerManager.set_layout(TEXTUAL_LAYOUT, config_info['log_file'], newtab=True)
        logger.info("使用TUI界面模式")
    
    directories = get_valid_paths(args.paths, args.clipboard)
    
    if not directories:
        logger.error("[#error] ❌ 未提供任何有效的路径")
        return

    # 根据命令行参数决定是否跳过已检查的文件
    skip_checked = not args.force_check
    if args.force_check:
        logger.info("[#status] 🔄 强制检查模式：将检查所有文件，包括之前已检查过的")
    else:
        logger.info("[#status] ℹ️ 标准检查模式：将跳过之前已检查且完好的文件")
        
    # 可以根据CPU核心数调整线程数
    max_workers = os.cpu_count() or 4
    
    # 处理每个目录
    total_dirs = len(directories)
    for idx, directory in enumerate(directories):
        dir_progress = int((idx / total_dirs) * 100) if total_dirs > 0 else 100
        logger.info(f"[@progress] 处理目录 ({idx+1}/{total_dirs}) {dir_progress}%")
        logger.info(f"[#status] 📂 开始处理目录: {directory}")
        process_directory(directory, skip_checked, max_workers=max_workers)
        logger.info(f"[#success] ✅ 目录处理完成: {directory}")
    
    # 最终完成
    logger.info(f"[@progress] 处理目录 ({total_dirs}/{total_dirs}) 100%")
    
if __name__ == "__main__":
    main()