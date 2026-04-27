"""
论文爬取模块
从arXiv等学术平台获取最新AI论文
"""

import arxiv
import logging
from datetime import datetime, timedelta
from typing import List, Dict
from config.sources import ARXIV_CATEGORIES, REPORT_CONFIG

logger = logging.getLogger(__name__)


def fetch_arxiv_papers() -> List[Dict]:
    """
    从arXiv获取最新的AI相关论文

    Returns:
        List[Dict]: 论文列表,包含标题、作者、摘要、链接等信息
    """
    papers = []
    today = datetime.now()
    yesterday = today - timedelta(days=1)

    # 构建搜索查询 - 获取最近一天的论文
    search_query = " OR ".join([f"cat:{cat}" for cat in ARXIV_CATEGORIES])

    try:
        # 创建搜索对象
        search = arxiv.Search(
            query=search_query,
            max_results=REPORT_CONFIG['max_papers'] * 2,  # 获取更多以便筛选
            sort_by=arxiv.SortCriterion.SubmittedDate,
            sort_order=arxiv.SortOrder.Descending
        )

        # 执行搜索
        client = arxiv.Client()
        results = client.results(search)

        for result in results:
            # 检查是否是昨天或今天提交的
            if result.published.date() >= yesterday.date():
                paper = {
                    'title': result.title,
                    'authors': [author.name for author in result.authors[:5]],  # 最多5个作者
                    'abstract': result.summary,
                    'url': result.entry_id,
                    'pdf_url': result.pdf_url,
                    'published': result.published.strftime('%Y-%m-%d %H:%M:%S'),
                    'categories': result.categories,
                    'primary_category': result.primary_category,
                }
                papers.append(paper)

                # 达到最大数量限制
                if len(papers) >= REPORT_CONFIG['max_papers']:
                    break

        logger.info(f"成功获取 {len(papers)} 篇arXiv论文")

    except Exception as e:
        logger.error(f"获取arXiv论文失败: {str(e)}")

    return papers


def format_paper_for_report(paper: Dict) -> str:
    """
    格式化单篇论文为报告格式(中英双语)

    Args:
        paper: 论文字典

    Returns:
        str: 格式化后的论文信息
    """
    # 提取关键信息
    title = paper['title']
    authors = ', '.join(paper['authors'])
    categories = ', '.join(paper.get('categories', [])[:3])
    url = paper['url']
    abstract = paper['abstract']

    # 截断过长的摘要
    if len(abstract) > 500:
        abstract = abstract[:500] + '...'

    formatted = f"""
**{title}**

👤 **Authors**: {authors}

📅 **Published**: {paper['published']} | 📚 **Category**: {categories}

📝 **Abstract**:
{abstract}

🔗 **[View Paper]({url})** | **[PDF]({paper['pdf_url']})**

---
"""
    return formatted


if __name__ == '__main__':
    # 测试代码
    logging.basicConfig(level=logging.INFO)
    papers = fetch_arxiv_papers()
    print(f"\n获取到 {len(papers)} 篇论文:\n")
    for i, paper in enumerate(papers[:3], 1):
        print(f"{i}. {paper['title']}")
        print(f"   Authors: {', '.join(paper['authors'][:3])}")
        print(f"   URL: {paper['url']}\n")
