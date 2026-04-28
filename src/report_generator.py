"""
报告生成模块
将收集的论文和新闻整合成结构化报告
"""

from datetime import datetime
from typing import Dict, List


def generate_daily_report(papers: List[Dict], news: Dict[str, List[Dict]]) -> str:
    """
    生成每日AI进展报告(中英双语)
    """
    today = datetime.now()
    date_str = today.strftime('%Y年%m月%d日')
    date_en = today.strftime('%B %d, %Y')

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
            report += f"**{paper['title']}**\n\n"
            report += f"👤 **Authors**: {', '.join(paper['authors'][:3])}\n\n"
            abstract = paper['abstract']
            if len(abstract) > 300: abstract = abstract[:300] + '...'
            report += f"📝 **Abstract**:\n{abstract}\n\n"
            report += f"🔗 [View Paper]({paper['url']}) | [PDF]({paper['pdf_url']})\n\n---\n"
    else:
        report += "*No new papers found today / 今日无新论文*\n\n"

    # 第二部分:技术进展
    report += "\n## 💻 Technology Updates / 技术进展\n\n"
    tech_news = news.get('technology', [])
    if tech_news:
        for i, item in enumerate(tech_news, 1):
            report += f"**{i}. {item['title']}**\n"
            if item.get('summary'):
                report += f"{item['summary'][:200]}...\n"
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
                report += f"{item['summary'][:200]}...\n"
            report += f"📌 Source: {item['source']} | 🔗 [Read More]({item['url']})\n\n"
    else:
        report += "*No market news today / 今日无市场资讯*\n\n"

    report += f"\n---\n*Report generated at {today.strftime('%Y-%m-%d %H:%M:%S')} | 报告生成时间: {today.strftime('%Y-%m-%d %H:%M:%S')}*\n"
    return report


def generate_summary_for_message(papers: List[Dict], news: Dict[str, List[Dict]]) -> str:
    """
    生成简短摘要(用于即时消息推送)
    修改：直接包含标题，不再提示查看文件
    """
    today = datetime.now()
    date_str = today.strftime('%Y-%m-%d')

    summary = f"🤖 AI Daily Report - {date_str}\n\n"

    # 论文列表
    summary += f"📚 Latest Papers / 最新论文: {len(papers)} 篇\n"
    if papers:
        for i, paper in enumerate(papers[:3], 1):
            title = paper['title']
            if len(title) > 50: title = title[:50] + '...'
            summary += f"  {i}. {title}\n"
    else:
        summary += "  (今日暂无最新论文)\n"

    # 技术动态
    summary += f"\n💻 Tech Updates / 技术动态: {len(news.get('technology', []))} 条\n"
    tech_items = news.get('technology', [])
    if tech_items:
        for i, item in enumerate(tech_items[:3], 1):
            title = item['title']
            if len(title) > 50: title = title[:50] + '...'
            summary += f"  {i}. {title}\n"
    else:
        summary += "  (今日暂无技术动态)\n"

    # 市场资讯
    summary += f"\n📈 Market News / 市场资讯: {len(news.get('market', []))} 条\n"
    market_items = news.get('market', [])
    if market_items:
        for i, item in enumerate(market_items[:3], 1):
            title = item['title']
            if len(title) > 50: title = title[:50] + '...'
            summary += f"  {i}. {title}\n"
    else:
        summary += "  (今日暂无市场资讯)\n"

    summary += f"\n---\n*Powered by GitHub Actions | 完整报告见上文*"
    return summary


def save_report_to_file(report: str, filename: str = None) -> str:
    """保存报告到文件"""
    if not filename:
        filename = f"ai_report_{datetime.now().strftime('%Y%m%d')}.md"
    filepath = f"reports/{filename}"
    import os
    os.makedirs('reports', exist_ok=True)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(report)
    return filepath