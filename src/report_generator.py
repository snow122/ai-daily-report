"""
报告生成模块
将收集的论文和新闻整合成结构化报告和网页
"""

from datetime import datetime
from typing import Dict, List
import os

def generate_daily_report(papers: List[Dict], news: Dict[str, List[Dict]]) -> str:
    """生成 Markdown 格式报告"""
    today = datetime.now()
    report = f"# 🤖 AI Daily Report - {today.strftime('%Y-%m-%d')}\n\n"
    report += f"## 📚 Papers ({len(papers)})\n"
    for p in papers:
        report += f"- **{p['title']}**\n  - Authors: {', '.join(p['authors'][:3])}\n  - {p['url']}\n"
    report += f"\n## 💻 Tech ({len(news.get('technology', []))})\n"
    for n in news.get('technology', []):
        report += f"- **{n['title']}**\n  - {n['url']}\n"
    return report

def generate_html_report(papers: List[Dict], news: Dict[str, List[Dict]]) -> str:
    """生成 HTML 网页报告"""
    today = datetime.now().strftime('%Y-%m-%d')
    
    # 论文 HTML
    papers_html = ""
    if papers:
        for p in papers:
            papers_html += f"""
            <div class="card">
                <h3>📄 {p['title']}</h3>
                <p class="authors">👤 {', '.join(p['authors'][:3])}</p>
                <p class="abstract">📝 {p['abstract'][:300]}...</p>
                <a href="{p['url']}" target="_blank" class="btn">View Paper</a>
                <a href="{p['pdf_url']}" target="_blank" class="btn">PDF</a>
            </div>"""
    else:
        papers_html = "<p>今日暂无最新论文</p>"

    # 新闻 HTML
    news_html = ""
    for item in news.get('technology', []) + news.get('market', []):
        news_html += f"""
        <div class="news-item">
            <h4>🔹 {item['title']}</h4>
            <p>{item.get('summary', '')[:150]}...</p>
            <a href="{item['url']}" target="_blank">Read More →</a>
        </div>"""

    html = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>AI Daily Report - {today}</title>
    <style>
        body {{ font-family: -apple-system, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; background: #f5f5f5; color: #333; }}
        .header {{ background: #2563eb; color: white; padding: 20px; border-radius: 8px; margin-bottom: 20px; }}
        .card {{ background: white; padding: 15px; border-radius: 8px; margin-bottom: 15px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }}
        .btn {{ display: inline-block; padding: 5px 10px; background: #2563eb; color: white; text-decoration: none; border-radius: 4px; margin-right: 5px; font-size: 12px; }}
        .news-item {{ background: white; padding: 10px; border-radius: 6px; margin-bottom: 10px; border-left: 4px solid #10b981; }}
        h3 {{ margin-top: 0; }}
    </style>
</head>
<body>
    <div class="header">
        <h1>🤖 AI Daily Report</h1>
        <p>Date: {today}</p>
    </div>
    
    <h2>📚 Latest Papers ({len(papers)})</h2>
    {papers_html}
    
    <h2>📰 News & Updates</h2>
    {news_html}
</body>
</html>"""
    return html

def save_report(papers: List[Dict], news: Dict[str, List[Dict]]):
    """保存 Markdown 和 HTML 报告"""
    os.makedirs('public', exist_ok=True)
    
    # 保存 HTML 到 public 目录 (用于发布网页)
    html_content = generate_html_report(papers, news)
    with open('public/index.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
        
    return html_content

def generate_summary_for_message(papers, news):
    """生成飞书消息摘要"""
    summary = f"🤖 AI Daily Report - {datetime.now().strftime('%Y-%m-%d')}\n\n"
    summary += f"📚 Papers: {len(papers)} 篇\n"
    for i, p in enumerate(papers[:3], 1):
        summary += f"  {i}. {p['title'][:40]}...\n"
    
    summary += f"\n📰 News: {len(news.get('technology', [])) + len(news.get('market', []))} 条\n"
    
    # 添加网页链接
    summary += f"\n🌐 **完整报告**: https://snow122.github.io/ai-daily-report/"
    return summary