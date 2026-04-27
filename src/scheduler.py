"""
定时任务调度模块
每天早晨8点自动执行报告生成和推送
"""

import schedule
import time
import logging
import sys
from datetime import datetime
from src.paper_fetcher import fetch_arxiv_papers
from src.news_fetcher import fetch_all_news
from src.report_generator import generate_daily_report, generate_summary_for_message, save_report_to_file
from src.notifier import send_notification

logger = logging.getLogger(__name__)


def generate_and_send_report():
    """
    生成报告并发送通知的主函数
    """
    logger.info("=" * 50)
    logger.info(f"开始生成AI日报 - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    logger.info("=" * 50)

    try:
        # 步骤1: 获取最新论文
        logger.info("步骤1: 获取最新研究论文...")
        papers = fetch_arxiv_papers()
        logger.info(f"成功获取 {len(papers)} 篇论文")

        # 步骤2: 获取新闻资讯
        logger.info("步骤2: 获取技术和市场资讯...")
        news = fetch_all_news()
        tech_count = len(news.get('technology', []))
        market_count = len(news.get('market', []))
        logger.info(f"成功获取技术资讯 {tech_count} 条, 市场资讯 {market_count} 条")

        # 步骤3: 生成完整报告
        logger.info("步骤3: 生成完整报告...")
        report = generate_daily_report(papers, news)

        # 步骤4: 保存报告到文件
        logger.info("步骤4: 保存报告文件...")
        report_file = save_report_to_file(report)
        logger.info(f"报告已保存到: {report_file}")

        # 步骤5: 生成简短摘要
        logger.info("步骤5: 生成消息摘要...")
        summary = generate_summary_for_message(papers, news)

        # 步骤6: 发送通知
        logger.info("步骤6: 发送通知...")
        success = send_notification(summary, report_file)

        if success:
            logger.info("✅ 报告生成和推送完成!")
        else:
            logger.warning("⚠️ 报告已生成,但推送失败")

    except Exception as e:
        logger.error(f"❌ 生成报告时发生错误: {str(e)}", exc_info=True)
        return False

    return True


def run_once():
    """
    立即执行一次报告生成(用于测试或手动触发)
    """
    logger.info("手动触发报告生成...")
    generate_and_send_report()


def start_scheduler(hour=8, minute=0):
    """
    启动定时任务调度器

    Args:
        hour: 执行时间的小时(默认8点)
        minute: 执行时间的分钟(默认0分)
    """
    # 设置每天指定时间执行
    schedule.every().day.at(f"{hour:02d}:{minute:02d}").do(generate_and_send_report)

    logger.info(f"定时任务已设置: 每天 {hour:02d}:{minute:02d} 执行")
    logger.info("按 Ctrl+C 停止程序")

    # 持续运行
    try:
        while True:
            schedule.run_pending()
            time.sleep(60)  # 每分钟检查一次
    except KeyboardInterrupt:
        logger.info("程序已停止")


if __name__ == '__main__':
    # 配置日志
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('logs/ai_report.log', encoding='utf-8'),
            logging.StreamHandler(sys.stdout)
        ]
    )

    # 检查命令行参数
    if len(sys.argv) > 1 and sys.argv[1] == '--now':
        # 立即执行一次
        run_once()
    else:
        # 启动定时任务(每天8点)
        start_scheduler(hour=8, minute=0)
