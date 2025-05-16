import os
import logging
import json
from typing import List, Set, Dict, Tuple
from nodes.pics.filter.duplicate_image_detector import DuplicateImageDetector
from nodes.record.logger_config import setup_logger
config = {
    'script_name': 'pics.filter.duplicate_image_detector',
    'console_enabled': True
}
logger, config_info = setup_logger(config)
def _load_hash_file(hash_file):
    """加载哈希文件"""
    if not hash_file:
        return {}
        
    # 移除可能存在的额外引号
    clean_path = hash_file.strip('"\'')
    
    try:
        if not os.path.exists(clean_path):
            logger.error(f"[#hash_calc]哈希文件不存在: \"{clean_path}\"")
            return {}
                
        with open(clean_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        logger.info(f"成功加载哈希文件: {clean_path}")
        hash_cache_data = data.get('hashes', {})
        print(hash_cache_data)
        return hash_cache_data
    except Exception as e:
        logger.error(f"[#hash_calc]加载哈希文件失败: {e}")
        return {}
_load_hash_file(r"E:\1EHV\[23.4ド (イチリ)]\image_hashes.json")