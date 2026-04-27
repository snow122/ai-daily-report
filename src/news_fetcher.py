"""
新闻资讯爬取模块
从各大AI资讯源获取最新的技术和市场动态
"""

import feedparser
import requests
from bs4 import BeautifulSoup
import logging
from datetime import datetime
from typing import List, Dict
from config.sources import NEWS_SOURCES, REPORT_CONFIG

logger = logging.getLogger(__name__)


def fetch_rss_feed(source: Dict) -> List[Dict]:
    """从RSS源获取新闻"""
    news_items = []

    try:
        feed = feedparser.parse(source['url'])

        for entry in feed.entries[:10]:
            # 提取内容
            title = entry.get('title', '')
            summary = entry.get('summary', '') or entry.get('description', '')
            link = entry.get('link', '')
            
            # 获取时间
            published_time = None
            if hasattr(entry, 'published_parsed') and entry.published_parsed:
                published_time = datetime(*entry.published_parsed[:6])
            
            # 只要标题不为空就收录，不再强制过滤关键词和时间
            if title:
                news_items.append({
                    'title': title,
                    'summary': summary[:300] if summary else '',
                    'url': link,
                    'source': source['name'],
                    'category': source['category'],
                    'published': published_time.strftime('%Y-%m-%d') if published_time else '',
                })

    except Exception as e:
        logger.error(f"获取RSS源 {source['name']} 失败: {str(e)}")

    return news_items


def fetch_web_news(source: Dict) -> List[Dict]:
    """从网页获取新闻"""
    news_items = []
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(source['url'], headers=headers, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'lxml')
        
        articles = soup.find_all('article') or soup.find_all('div', class_=lambda x: x and 'post' in str(x).lower())
        
        for article in articles[:5]:
            title_elem = article.find('h2') or article.find('h3') or article.find('a')
            if title_elem:
                title = title_elem.get_text(strip=True)
                link = title_elem.get('href', '')
                if not link:
                    link_elem = article.find('a', href=True)
                    if link_elem: link = link_elem['href']
                
                if title and len(title) > 5:
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
    """获取所有新闻"""
    all_news = {'technology': [], 'market': []}

    for source in NEWS_SOURCES:
        items = fetch_rss_feed(source) if source['type'] == 'rss' else fetch_web_news(source)
        category = source['category']
        if category in all_news:
            all_news[category].extend(items)

    # 去重和限制数量
    for category in all_news:
        seen = set()
        unique = []
        for item in all_news[category]:
            if item['title'] not in seen:
                seen.add(item['title'])
                unique.append(item)
        all_news[category] = unique[:REPORT_CONFIG['max_news_per_category']]

    return all_news