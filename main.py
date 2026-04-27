"""
AI Daily Report - 主入口文件
自动化生成和推送AI领域每日进展报告
"""

import sys
import os
import logging

# 添加项目根目录到路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from src.scheduler import start_scheduler, run_once


def main():
    """主函数"""
    # 配置日志
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

    # 确保必要目录存在
    os.makedirs('logs', exist_ok=True)
    os.makedirs('reports', exist_ok=True)

    # 检查命令行参数
    if len(sys.argv) > 1:
        if sys.argv[1] == '--now':
            logger.info("立即执行一次报告生成...")
            run_once()
        elif sys.argv[1] == '--help':
            print("""
AI Daily Report - 使用说明

用法:
  python main.py              启动定时任务(每天8点自动执行)
  python main.py --now        立即执行一次报告生成
  python main.py --help       显示帮助信息

配置步骤:
  1. 复制 .env.example 为 .env
  2. 在 .env 中配置飞书/企业微信/钉钉 Webhook URL
  3. 运行程序

功能说明:
  - 自动从arXiv获取最新AI论文
  - 从各大资讯源获取技术和市场动态
  - 生成中英双语报告
  - 通过飞书/企业微信/钉钉推送通知
  - 保存完整报告到文件

支持平台:
  - 飞书 (推荐): FEISHU_WEBHOOK_URL
  - 企业微信: WEWORK_WEBHOOK_URL
  - 钉钉: DINGTALK_WEBHOOK_URL + DINGTALK_SECRET
            """)
        else:
            logger.error(f"未知参数: {sys.argv[1]}")
            print("使用 --help 查看帮助")
    else:
        logger.info("启动定时任务调度器 (每天16:00执行)")
        start_scheduler(hour=16, minute=0)


if __name__ == '__main__':
    main()
