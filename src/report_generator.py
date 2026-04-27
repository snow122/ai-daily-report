"""
报告生成模块
将收集的论文和新闻整合成结构化报告
"""

from datetime import datetime
from typing import Dict, List
from src.paper_fetcher import format_paper_for_report
from src.news_fetcher import format_news_for_report


def generate_daily_report(papers: List[Dict], news: Dict[str, List[Dict]]) -> str:
    """
    生成每日AI进展报告(中英双语)

    Args:
        papers: 论文列表
        news: 按类别分组的新闻列表

    Returns:
        str: 完整的报告内容(Markdown格式)
    """
    today = datetime.now()
    date_str = today.strftime('%Y年%m月%d日')
    date_en = today.strftime('%B %d, %Y')
    weekday_cn = today.strftime('%A')

    # 报告头部
    report = f"""# 🤖 AI Daily Report / AI领域日报

**Date**: {date_en} | **日期**: {date_str}

---

## 📊 Summary / 概览

- **Papers Today / 今日论文**: {len(papers)} 篇
- **Tech Updates / 技术动态**: {len(news.get('technology', []))} 条
- **Market News / 市场资讯**: {len(news.get('market', []))} 条

---
"""

    # 第一部分:最新研究论文
    report += "## 📚 Latest Research Papers / 最新研究论文\n\n"

    if papers:
        for paper in papers:
            report += format_paper_for_report(paper)
    else:
        report += "*No new papers found today / 今日无新论文*\n\n"

    # 第二部分:技术进展
    report += "\n## 💻 Technology Updates / 技术进展\n\n"
    tech_news = news.get('technology', [])
    if tech_news:
        for i, item in enumerate(tech_news, 1):
            report += f"**{i}. {item['title']}**\n"
            if item.get('summary'):
                summary = item['summary'][:300]
                report += f"{summary}...\n"
            report += f"📌 Source: {item['source']} | 🔗 [Read More]({item['url']})\n\n"
    else:
        report += "*No technology updates today / 今日无技术更新*\n\n"

    # 第三部分:市场动态
    report += "\n## 📈 Market Dynamics / 市场动态\n\n"
    market_news = news.get('market', [])
    if market_news:
        for i, item in enumerate(market_news, 1):
            report += f"**{i}. {item['title']}**\n"
            if item.get('summary'):
                summary = item['summary'][:300]
                report += f"{summary}...\n"
            report += f"📌 Source: {item['source']} | 🔗 [Read More]({item['url']})\n\n"
    else:
        report += "*No market news today / 今日无市场资讯*\n\n"

    # 报告尾部
    report += f"""
---

*Report generated at {today.strftime('%Y-%m-%d %H:%M:%S')} | 报告生成时间: {today.strftime('%Y-%m-%d %H:%M:%S')}*

*This is an automated report. For questions or suggestions, please contact the administrator.*

*这是自动化生成的报告。如有疑问或建议,请联系管理员。*
"""

    return report


def generate_summary_for_message(papers: List[Dict], news: Dict[str, List[Dict]]) -> str:
    """
    生成简短摘要(用于即时消息推送)

    Args:
        papers: 论文列表
        news: 按类别分组的新闻列表

    Returns:
        str: 简短的报告摘要
    """
    today = datetime.now()
    date_str = today.strftime('%Y-%m-%d')

    summary = f"🤖 AI Daily Report - {date_str}\n\n"

    # 论文统计
    summary += f"📚 Latest Papers / 最新论文: {len(papers)} 篇\n"
    if papers:
        for i, paper in enumerate(papers[:3], 1):
            title = paper['title']
            if len(title) > 60:
                title = title[:60] + '...'
            summary += f"  {i}. {title}\n"

    summary += f"\n💻 Tech Updates / 技术动态: {len(news.get('technology', []))} 条"
    summary += f"\n📈 Market News / 市场资讯: {len(news.get('market', []))} 条\n"

    summary += f"\n完整报告已生成,请查看文件或使用Web界面浏览。"

    return summary


def save_report_to_file(report: str, filename: str = None) -> str:
    """
    将报告保存到文件

    Args:
        report: 报告内容
        filename: 文件名(可选,默认使用日期)

    Returns:
        str: 保存的文件路径
    """
    if not filename:
        filename = f"ai_report_{datetime.now().strftime('%Y%m%d')}.md"

    filepath = f"reports/{filename}"

    # 确保目录存在
    import os
    os.makedirs('reports', exist_ok=True)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(report)

    return filepath


if __name__ == '__main__':
    # 测试代码
    from src.paper_fetcher import fetch_arxiv_papers
    from src.news_fetcher import fetch_all_news

    print("Fetching papers...")
    papers = fetch_arxiv_papers()

    print("Fetching news...")
    news = fetch_all_news()

    print("Generating report...")
    report = generate_daily_report(papers, news)

    # 保存报告
    filepath = save_report_to_file(report)
    print(f"\nReport saved to: {filepath}")
    print(f"\nFirst 500 characters:\n{report[:500]}")
