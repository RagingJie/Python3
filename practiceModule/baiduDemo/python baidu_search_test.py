# -*- coding: utf-8 -*-
"""
Python Web自动化测试示例脚本
功能：百度搜索自动化测试
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


def test_baidu_search():
    """百度搜索自动化测试函数"""

    # 1. 初始化浏览器
    print("正在启动浏览器...")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    try:
        # 2. 打开百度首页
        print("正在访问百度首页...")
        driver.get("https://www.baidu.com")

        # 3. 验证页面是否正确加载
        assert "百度" in driver.title, "百度首页加载失败"
        print("百度首页加载成功")

        # 4. 定位搜索框并输入关键词
        print("正在输入搜索关键词...")
        # 使用显式等待，最多等待10秒，直到搜索框可被定位
        search_box = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "chat-textarea"))
        )
        search_box.clear()  # 清空搜索框
        search_box.send_keys("Python自动化测试")

        # 5. 执行搜索（按下回车键）
        print("正在执行搜索...")
        search_box.send_keys(Keys.RETURN)

        # 6. 等待搜索结果加载
        print("等待搜索结果加载...")
        # 等待搜索结果页面加载完成，最多等待15秒
        WebDriverWait(driver, 40).until(
            EC.title_contains("Python自动化测试")
        )

        # 7. 验证搜索结果
        print("验证搜索结果...")
        assert "Python自动化测试" in driver.title, "搜索结果页面标题不正确"

        # 8. 验证搜索结果数量
        result_stats = driver.find_element(By.ID, "content_left")
        print(f"搜索结果统计: {result_stats.text}")

        # 9. 截图保存搜索结果
        screenshot_name = f"baidu_search_result_{int(time.time())}.png"
        driver.save_screenshot(screenshot_name)
        print(f"搜索结果已保存为: {screenshot_name}")

        print("百度搜索自动化测试执行成功！")

    except Exception as e:
        print(f"测试过程中出现错误: {str(e)}")
        # 出错时截图保存
        error_screenshot = f"error_screenshot_{int(time.time())}.png"
        driver.save_screenshot(error_screenshot)
        print(f"错误截图已保存为: {error_screenshot}")

    finally:
        # 10. 关闭浏览器
        print("正在关闭浏览器...")
        time.sleep(3)  # 等待3秒，方便查看结果
        driver.quit()
        print("浏览器已关闭")


if __name__ == "__main__":
    test_baidu_search()