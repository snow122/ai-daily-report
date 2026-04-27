"""
新闻资讯爬取模块
从各大AI资讯源获取最新的技术和市场动态
"""

import feedparser
import requests
from bs4 import BeautifulSoup
import logging
from datetime import datetime, timedelta
from typing import List, Dict
from config.sources import NEWS_SOURCES, AI_KEYWORDS, REPORT_CONFIG

logger = logging.getLogger(__name__)


def fetch_rss_feed(source: Dict) -> List[Dict]:
    """
    从RSS源获取新闻

    Args:
        source: 数据源配置字典

    Returns:
        List[Dict]: 新闻列表
    """
    news_items = []

    try:
        # 解析RSS feed
        feed = feedparser.parse(source['url'])

        for entry in feed.entries[:10]:  # 最多获取10条
            # 检查发布时间(最近24小时)
            published_time = None
            if hasattr(entry, 'published_parsed') and entry.published_parsed:
                published_time = datetime(*entry.published_parsed[:6])
            elif hasattr(entry, 'updated_parsed') and entry.updated_parsed:
                published_time = datetime(*entry.updated_parsed[:6])

            if published_time:
                hours_ago = (datetime.now() - published_time).total_seconds() / 3600
                if hours_ago > 48:  # 超过48小时的跳过
                    continue

            # 提取内容
            title = entry.get('title', '')
            summary = entry.get('summary', '') or entry.get('description', '')
            link = entry.get('link', '')

            # 简单的关键词过滤
            content_lower = (title + ' ' + summary).lower()
            if not any(keyword.lower() in content_lower for keyword in AI_KEYWORDS):
                continue

            news_item = {
                'title': title,
                'summary': summary[:300] if summary else '',  # 限制摘要长度
                'url': link,
                'source': source['name'],
                'category': source['category'],
                'published': published_time.strftime('%Y-%m-%d %H:%M:%S') if published_time else '',
            }

            news_items.append(news_item)

    except Exception as e:
        logger.error(f"获取RSS源 {source['name']} 失败: {str(e)}")

    return news_items


def fetch_web_news(source: Dict) -> List[Dict]:
    """
    从网页获取新闻(简化版,实际可能需要更复杂的爬虫)

    Args:
        source: 数据源配置字典

    Returns:
        List[Dict]: 新闻列表
    """
    news_items = []

    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        response = requests.get(source['url'], headers=headers, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'lxml')

        # 尝试提取文章标题和链接(通用规则,可能需要针对每个网站定制)
        articles = soup.find_all('article') or soup.find_all('div', class_=lambda x: x and 'post' in x.lower())

        for article in articles[:5]:
            title_elem = article.find('h2') or article.find('h3') or article.find('a')
            if title_elem:
                title = title_elem.get_text(strip=True)
                link = title_elem.get('href', '') if title_elem.name == 'a' else ''

                if not link:
                    link_elem = article.find('a', href=True)
                    if link_elem:
                        link = link_elem['href']

                # 确保是完整URL
                if link and not link.startswith('http'):
                    from urllib.parse import urljoin
                    link = urljoin(source['url'], link)

                if title and len(title) > 10:  # 过滤太短的标题
                    news_items.append({
                        'title': title,
                        'summary': '',
                        'url': link,
                        'source': source['name'],
                        'category': source['category'],
                        'published': datetime.now().strftime('%Y-%m-%d'),
                    })

    except Exception as e:
        logger.error(f"获取网页 {source['name']} 失败: {str(e)}")

    return news_items


def fetch_all_news() -> Dict[str, List[Dict]]:
    """
    从所有数据源获取新闻

    Returns:
        Dict[str, List[Dict]]: 按类别分组的新闻列表
    """
    all_news = {
        'technology': [],  # 技术进展
        'market': [],      # 市场动态
    }

    for source in NEWS_SOURCES:
        logger.info(f"正在获取: {source['name']}")

        if source['type'] == 'rss':
            items = fetch_rss_feed(source)
        else:
            items = fetch_web_news(source)

        # 按类别分组
        category = source['category']
        if category in all_news:
            all_news[category].extend(items)

    # 去重和限制数量
    for category in all_news:
        # 基于标题去重
        seen_titles = set()
        unique_news = []
        for item in all_news[category]:
            if item['title'] not in seen_titles:
                seen_titles.add(item['title'])
                unique_news.append(item)

        # 限制数量
        all_news[category] = unique_news[:REPORT_CONFIG['max_news_per_category']]

    logger.info(f"获取完成 - 技术: {len(all_news['technology'])} 条, 市场: {len(all_news['market'])} 条")

    return all_news


def format_news_for_report(news_list: List[Dict], category: str) -> str:
    """
    格式化新闻为报告格式

    Args:
        news_list: 新闻列表
        category: 类别名称

    Returns:
        str: 格式化后的新闻内容
    """
    if not news_list:
        return f"\n**{category}**: No updates today\n\n**{category}**: 今日无更新\n\n"

    category_cn = "技术进展" if category == "technology" else "市场动态"
    category_en = "Technology Updates" if category == "technology" else "Market Dynamics"

    formatted = f"\n### 📰 {category_en} / {category_cn}\n\n"

    for i, news in enumerate(news_list, 1):
        formatted += f"**{i}. {news['title']}**\n"
        if news.get('summary'):
            formatted += f"{news['summary'][:200]}...\n"
        formatted += f"📌 Source: {news['source']} | 🔗 [Read More]({news['url']})\n\n"

    return formatted


if __name__ == '__main__':
    # 测试代码
    logging.basicConfig(level=logging.INFO)
    news = fetch_all_news()
    print(f"\n技术进展 ({len(news['technology'])} 条):")
    for item in news['technology'][:3]:
        print(f"  - {item['title']}")
    print(f"\n市场动态 ({len(news['market'])} 条):")
    for item in news['market'][:3]:
        print(f"  - {item['title']}")
