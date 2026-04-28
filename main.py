"""
AI Daily Report - 主入口文件
"""

import sys
import os
import logging

# 添加根目录到路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from src.scheduler import start_scheduler, run_once

def main():
    # 1. 【最重要】必须先创建文件夹，否则写日志会报错
    os.makedirs('logs', exist_ok=True)
    os.makedirs('reports', exist_ok=True)
    os.makedirs('public', exist_ok=True)

    # 2. 然后再配置日志
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('logs/ai_report.log', encoding='utf-8'),
            logging.StreamHandler(sys.stdout)
        ]
    )

    logger = logging.getLogger(__name__)
    logger.info("🤖 AI Daily Report System Starting...")

    # 3. 检查命令行参数
    if len(sys.argv) > 1:
        if sys.argv[1] == '--now':
            logger.info("立即执行一次报告生成...")
            run_once()
        elif sys.argv[1] == '--help':
            print("Usage: python main.py [--now|--help]")
        else:
            logger.error(f"Unknown argument: {sys.argv[1]}")
    else:
        logger.info("启动定时任务调度器 (每天 16:00 执行)")
        start_scheduler(hour=16, minute=0)

if __name__ == '__main__':
    main()