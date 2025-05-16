import time
import threaded
import logging
import pytest
from concurrent.futures import wait

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ThreadedTester:
    def __init__(self):
        self.max_worker = 4
        # 配置全局线程池
        threaded.ThreadPooled.configure(max_workers=self.max_worker)
        
    @threaded.ThreadPooled
    def process_item(self, item):
        """模拟耗时操作"""
        logger.info(f"Processing item {item} in thread")
        time.sleep(1)  # 模拟耗时操作
        return f"Processed {item}"
        
    def process_items(self, items):
        """批量处理items"""
        futures = []
        for item in items:
            future = self.process_item(item)
            futures.append(future)
            
        # 等待所有任务完成
        done, _ = wait(futures)
        # 获取结果
        processed_results = [future.result() for future in done]
        return processed_results

@pytest.fixture
def tester():
    return ThreadedTester()

def test_single_thread(tester):
    """测试单线程执行时间"""
    items = list(range(5))
    start = time.time()
    for item in items:
        time.sleep(1)
    duration = time.time() - start
    assert duration >= 5.0
    
def test_multi_thread(tester):
    """测试多线程执行时间"""
    items = list(range(5))
    start = time.time()
    results = tester.process_items(items)
    duration = time.time() - start
    
    # 验证多线程执行更快
    assert duration < 5.0
    # 验证结果正确性
    assert len(results) == 5
    assert all(isinstance(r, str) for r in results)
    assert all('Processed' in r for r in results)

def main():
    """手动测试入口"""
    tester = ThreadedTester()
    items = list(range(10))
    
    # 测试单线程执行时间
    start = time.time()
    for item in items:
        time.sleep(1)
    print(f"单线程执行时间: {time.time() - start:.2f}秒")
    
    # 测试多线程执行时间
    start = time.time()
    results = tester.process_items(items)
    print(f"多线程执行时间: {time.time() - start:.2f}秒")
    print("处理结果:", results)

if __name__ == "__main__":
    main()