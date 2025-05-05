"""
BadZipFliter - 压缩文件完整性检查工具

这个包提供了检测和处理损坏压缩文件的工具，
可以检查指定目录下的所有压缩文件，将损坏的文件重命名为.tdel后缀。
"""

from .archive_checker import check_archive, process_directory, get_archive_files
from .path_handler import get_paths_from_clipboard, get_valid_paths
from .history_manager import load_check_history, save_check_history, update_file_history
from .logger_module import setup_logger

__all__ = [
    'check_archive', 
    'process_directory', 
    'get_archive_files',
    'get_paths_from_clipboard', 
    'get_valid_paths',
    'load_check_history', 
    'save_check_history', 
    'update_file_history',
    'setup_logger'
]

__version__ = '1.0.0'