"""
论文爬取模块
从arXiv等学术平台获取最新AI论文
"""

import arxiv
import logging
from typing import List, Dict
from config.sources import ARXIV_CATEGORIES, REPORT_CONFIG

logger = logging.getLogger(__name__)


def fetch_arxiv_papers() -> List[Dict]:
    """
    从arXiv获取最新的AI相关论文
    """
    papers = []
    
    # 使用 OR 逻辑，匹配任意一个AI分类
    search_query = " OR ".join([f"cat:{cat}" for cat in ARXIV_CATEGORIES])

    try:
        # 创建搜索对象
        search = arxiv.Search(
            query=search_query,
            max_results=REPORT_CONFIG['max_papers'] * 2,
            sort_by=arxiv.SortCriterion.SubmittedDate,
            sort_order=arxiv.SortOrder.Descending
        )

        client = arxiv.Client()
        results = client.results(search)

        # 直接获取结果，不再严格限制日期（防止因时差或更新延迟导致0数据）
        for result in results:
            paper = {
                'title': result.title,
                'authors': [author.name for author in result.authors[:5]],
                'abstract': result.summary,
                'url': result.entry_id,
                'pdf_url': result.pdf_url,
                'published': result.published.strftime('%Y-%m-%d %H:%M:%S'),
                'categories': result.categories,
                'primary_category': result.primary_category,
            }
            papers.append(paper)

            # 取够数量就停止
            if len(papers) >= REPORT_CONFIG['max_papers']:
                break

        logger.info(f"成功获取 {len(papers)} 篇arXiv论文")

    except Exception as e:
        logger.error(f"获取arXiv论文失败: {str(e)}")

    return papers


def format_paper_for_report(paper: Dict) -> str:
    """格式化单篇论文"""
    title = paper['title']
    authors = ', '.join(paper['authors'])
    categories = ', '.join(paper.get('categories', [])[:3])
    url = paper['url']
    abstract = paper['abstract']

    if len(abstract) > 500:
        abstract = abstract[:500] + '...'

    return f"""
**{title}**

👤 **Authors**: {authors}

📅 **Published**: {paper['published']} | 📚 **Category**: {categories}

📝 **Abstract**:
{abstract}

🔗 **[View Paper]({url})** | **[PDF]({paper['pdf_url']})**

---
"""