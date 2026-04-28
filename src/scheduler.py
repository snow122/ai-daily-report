"""
定时任务调度模块
"""

import logging
import os
import sys
from datetime import datetime

# 导入其他模块
from src.paper_fetcher import fetch_arxiv_papers
from src.news_fetcher import fetch_all_news
from src.report_generator import generate_daily_report, generate_summary_for_message, save_report
from src.notifier import send_notification

logger = logging.getLogger(__name__)

def run_once():
    """执行一次报告生成和发送"""
    logger.info("开始生成报告...")
    try:
        # 1. 获取数据
        papers = fetch_arxiv_papers()
        news = fetch_all_news()
        
        # 2. 生成报告 (Markdown 用于日志/文件, HTML 用于网页)
        # save_report 会生成 public/index.html
        save_report(papers, news)
        
        # 3. 生成飞书消息摘要
        summary = generate_summary_for_message(papers, news)
        
        # 4. 发送飞书通知
        logger.info("准备发送飞书通知...")
        success = send_notification(summary)
        
        if success:
            logger.info("飞书发送成功!")
        else:
            logger.error("飞书发送失败，请检查 Webhook URL Secret")
            
    except Exception as e:
        logger.error(f"执行过程中出错: {e}")
        raise

def start_scheduler(hour=16, minute=0):
    """启动定时任务 (本地运行使用)"""
    import time
    import schedule
    logger.info(f"启动定时任务调度器 (每天 {hour:02d}:{minute:02d} 执行)")
    
    schedule.every().day.at(f"{hour:02d}:{minute:02d}").do(run_once)
    
    try:
        while True:
            schedule.run_pending()
            time.sleep(60)
    except KeyboardInterrupt:
        logger.info("程序已停止")

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    if len(sys.argv) > 1 and sys.argv[1] == '--now':
        run_once()
    else:
        start_scheduler()