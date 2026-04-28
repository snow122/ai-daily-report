"""
定时任务调度模块
"""

import sys
import os
import logging
from datetime import datetime

# 添加根目录到路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from src.paper_fetcher import fetch_arxiv_papers
from src.news_fetcher import fetch_all_news
from src.report_generator import generate_daily_report, generate_summary_for_message, save_report
from src.notifier import send_notification

logger = logging.getLogger(__name__)

def generate_and_send_report():
    """生成报告并发送的主函数"""
    logger.info("开始生成报告...")
    
    try:
        # 1. 获取数据
        papers = fetch_arxiv_papers()
        news = fetch_all_news()
        
        # 2. 保存 HTML 报告到 public/ 目录 (用于网页)
        # 注意：这里不再需要 markdown 文件路径，我们直接生成 HTML 用于网页
        save_report(papers, news)
        
        # 3. 生成飞书消息摘要
        summary = generate_summary_for_message(papers, news)
        
        # 4. 发送飞书通知
        # send_notification 内部会自动读取 FEISHU_WEBHOOK_URL 环境变量
        logger.info("准备发送飞书通知...")
        success = send_notification(summary)
        
        if success:
            logger.info("飞书发送成功!")
        else:
            logger.error("飞书发送失败，请检查 Webhook URL Secret")
            
    except Exception as e:
        logger.error(f"执行过程中出错: {e}")
        raise

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    if len(sys.argv) > 1 and sys.argv[1] == '--now':
        generate_and_send_report()
    else:
        # 如果是本地运行且无参数，启动定时任务
        from src.scheduler import start_scheduler # 防止循环导入
        start_scheduler()