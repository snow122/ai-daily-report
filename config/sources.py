"""
数据源配置模块
定义AI领域相关的论文和资讯来源
"""

# arXiv AI相关分类
ARXIV_CATEGORIES = [
    'cs.AI',      # 人工智能
    'cs.CL',      # 计算与语言
    'cs.CV',      # 计算机视觉
    'cs.LG',      # 机器学习
    'cs.NE',      # 神经与进化计算
    'cs.RO',      # 机器人学
]

# AI新闻和技术资讯源
NEWS_SOURCES = [
    {
        'name': 'Hugging Face Blog',
        'url': 'https://huggingface.co/blog',
        'type': 'rss',
        'category': 'technology'
    },
    {
        'name': 'OpenAI News',
        'url': 'https://openai.com/news',
        'type': 'web',
        'category': 'technology'
    },
    {
        'name': 'Google AI Blog',
        'url': 'https://ai.googleblog.com/feeds/posts/default',
        'type': 'rss',
        'category': 'technology'
    },
    {
        'name': 'Meta AI Research',
        'url': 'https://ai.facebook.com/blog/',
        'type': 'web',
        'category': 'technology'
    },
    {
        'name': 'MIT Technology Review - AI',
        'url': 'https://www.technologyreview.com/topic/artificial-intelligence/feed',
        'type': 'rss',
        'category': 'market'
    },
    {
        'name': 'VentureBeat AI',
        'url': 'https://venturebeat.com/category/ai/feed/',
        'type': 'rss',
        'category': 'market'
    },
]

# 关键词过滤(用于筛选相关内容)
AI_KEYWORDS = [
    'artificial intelligence',
    'machine learning',
    'deep learning',
    'large language model',
    'LLM',
    'GPT',
    'transformer',
    'neural network',
    'computer vision',
    'natural language processing',
    'NLP',
    'generative AI',
    'diffusion model',
    'reinforcement learning',
    '人工智能',
    '大模型',
    '深度学习',
]

# 报告配置
REPORT_CONFIG = {
    'max_papers': 10,          # 每日最多收录论文数
    'max_news_per_category': 5, # 每类新闻最多收录数
    'language': 'bilingual',   # 双语报告
    'include_abstract': True,  # 包含摘要
}
