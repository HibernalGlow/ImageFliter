from typing import Dict, List, Any, Optional

class FilterConfig:
    """图片过滤器配置类，用于管理所有过滤参数"""
    
    def __init__(self, config_dict: Dict[str, Any] = None):
        """
        初始化过滤器配置
        
        Args:
            config_dict: 配置字典，如果提供则使用其覆盖默认配置
        """
        # 全局配置
        self.max_workers = None  # 最大工作线程数，默认为None表示使用CPU核心数
        self.hash_file = None    # 哈希文件路径
        
        # 重复图片过滤配置
        self.duplicate_filter = DuplicateFilterConfig()
        
        # 小图过滤配置
        self.small_filter = SmallFilterConfig()
        
        # 灰度图过滤配置
        self.grayscale_filter = GrayscaleFilterConfig()
        
        # 文本图片过滤配置
        self.text_filter = TextFilterConfig()
        
        # 处理自定义配置
        if config_dict:
            self.update_from_dict(config_dict)
    
    def update_from_dict(self, config_dict: Dict[str, Any]) -> None:
        """从字典更新配置"""
        # 更新全局配置
        if 'max_workers' in config_dict:
            self.max_workers = config_dict['max_workers']
            
        if 'hash_file' in config_dict:
            self.hash_file = config_dict['hash_file']
            
        # 更新子配置
        if 'duplicate_filter' in config_dict:
            self.duplicate_filter.update_from_dict(config_dict['duplicate_filter'])
            
        if 'small_filter' in config_dict:
            self.small_filter.update_from_dict(config_dict['small_filter'])
            
        if 'grayscale_filter' in config_dict:
            self.grayscale_filter.update_from_dict(config_dict['grayscale_filter'])
            
        if 'text_filter' in config_dict:
            self.text_filter.update_from_dict(config_dict['text_filter'])
    
    def to_dict(self) -> Dict[str, Any]:
        """将配置转换为字典"""
        return {
            'max_workers': self.max_workers,
            'hash_file': self.hash_file,
            'duplicate_filter': self.duplicate_filter.to_dict(),
            'small_filter': self.small_filter.to_dict(),
            'grayscale_filter': self.grayscale_filter.to_dict(),
            'text_filter': self.text_filter.to_dict()
        }
    
    @classmethod
    def get_default(cls) -> 'FilterConfig':
        """获取默认配置"""
        return cls()

class DuplicateFilterConfig:
    """重复图片过滤配置"""
    
    def __init__(self):
        # 基础配置
        self.enabled = False                # 是否启用重复图片过滤
        self.mode = 'quality'               # 重复过滤模式: 'quality', 'watermark' 或 'hash'
        self.hamming_threshold = 12         # 汉明距离阈值，用于相似图片组检测
        self.ref_hamming_threshold = None   # 哈希文件过滤的汉明距离阈值，None时使用hamming_threshold
        
        # 水印过滤相关
        self.watermark_keywords = []        # 水印关键词列表
    
    def update_from_dict(self, config_dict: Dict[str, Any]) -> None:
        """从字典更新配置"""
        if 'enabled' in config_dict:
            self.enabled = config_dict['enabled']
            
        if 'mode' in config_dict:
            self.mode = config_dict['mode']
            
        if 'hamming_threshold' in config_dict:
            self.hamming_threshold = config_dict['hamming_threshold']
            
        if 'ref_hamming_threshold' in config_dict:
            self.ref_hamming_threshold = config_dict['ref_hamming_threshold']
            
        if 'watermark_keywords' in config_dict:
            self.watermark_keywords = config_dict['watermark_keywords']
    
    def to_dict(self) -> Dict[str, Any]:
        """将配置转换为字典"""
        return {
            'enabled': self.enabled,
            'mode': self.mode,
            'hamming_threshold': self.hamming_threshold,
            'ref_hamming_threshold': self.ref_hamming_threshold,
            'watermark_keywords': self.watermark_keywords
        }

class SmallFilterConfig:
    """小图过滤配置"""
    
    def __init__(self):
        self.enabled = False     # 是否启用小图过滤
        self.min_size = 631      # 最小图片尺寸（宽或高），小于此尺寸的图片将被判定为小图
    
    def update_from_dict(self, config_dict: Dict[str, Any]) -> None:
        """从字典更新配置"""
        if 'enabled' in config_dict:
            self.enabled = config_dict['enabled']
            
        if 'min_size' in config_dict:
            self.min_size = config_dict['min_size']
    
    def to_dict(self) -> Dict[str, Any]:
        """将配置转换为字典"""
        return {
            'enabled': self.enabled,
            'min_size': self.min_size
        }

class GrayscaleFilterConfig:
    """灰度图过滤配置"""
    
    def __init__(self):
        self.enabled = False         # 是否启用灰度图过滤
        self.detect_pure_black = True    # 是否检测纯黑图
        self.detect_pure_white = True    # 是否检测纯白图
        self.detect_grayscale = True     # 是否检测灰度图
    
    def update_from_dict(self, config_dict: Dict[str, Any]) -> None:
        """从字典更新配置"""
        if 'enabled' in config_dict:
            self.enabled = config_dict['enabled']
            
        if 'detect_pure_black' in config_dict:
            self.detect_pure_black = config_dict['detect_pure_black']
            
        if 'detect_pure_white' in config_dict:
            self.detect_pure_white = config_dict['detect_pure_white']
            
        if 'detect_grayscale' in config_dict:
            self.detect_grayscale = config_dict['detect_grayscale']
    
    def to_dict(self) -> Dict[str, Any]:
        """将配置转换为字典"""
        return {
            'enabled': self.enabled,
            'detect_pure_black': self.detect_pure_black,
            'detect_pure_white': self.detect_pure_white,
            'detect_grayscale': self.detect_grayscale
        }

class TextFilterConfig:
    """文本图片过滤配置"""
    
    def __init__(self):
        self.enabled = False     # 是否启用文本图片过滤
        self.threshold = 0.5     # 文本图片检测阈值
    
    def update_from_dict(self, config_dict: Dict[str, Any]) -> None:
        """从字典更新配置"""
        if 'enabled' in config_dict:
            self.enabled = config_dict['enabled']
            
        if 'threshold' in config_dict:
            self.threshold = config_dict['threshold']
    
    def to_dict(self) -> Dict[str, Any]:
        """将配置转换为字典"""
        return {
            'enabled': self.enabled,
            'threshold': self.threshold
        }
