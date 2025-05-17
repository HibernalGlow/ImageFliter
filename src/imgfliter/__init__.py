"""
ImgFilter - 强大的图片过滤工具包

提供多种图片过滤功能：
- 小图检测
- 灰度图检测
- 重复图片检测
- 文本图片检测
- 水印检测

既可以单独使用每个检测器，也可以使用综合的ImageFilter类进行批量处理。
"""

from imgfilter.core.filter import ImageFilter
from imgfilter.detectors import (
    WatermarkDetector,
    CVTextImageDetector,
    DuplicateImageDetector,
    SmallImageDetector,
    GrayscaleImageDetector,
)

# 方便直接访问的API
__all__ = [
    "ImageFilter",
    "WatermarkDetector", 
    "CVTextImageDetector", 
    "DuplicateImageDetector", 
    "SmallImageDetector", 
    "GrayscaleImageDetector",
]

# 版本信息
__version__ = "1.0.0"