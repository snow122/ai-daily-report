"""
系统测试脚本
验证各个模块的基本功能
"""

import sys
import os

# 添加项目根目录到路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def test_imports():
    """测试所有模块是否可以正常导入"""
    print("测试模块导入...")

    try:
        from config.sources import ARXIV_CATEGORIES, NEWS_SOURCES, AI_KEYWORDS, REPORT_CONFIG
        print("✓ config.sources 导入成功")
        print(f"  - arXiv分类: {len(ARXIV_CATEGORIES)} 个")
        print(f"  - 新闻源: {len(NEWS_SOURCES)} 个")
        print(f"  - AI关键词: {len(AI_KEYWORDS)} 个")

        from src.paper_fetcher import fetch_arxiv_papers, format_paper_for_report
        print("✓ src.paper_fetcher 导入成功")

        from src.news_fetcher import fetch_all_news, format_news_for_report
        print("✓ src.news_fetcher 导入成功")

        from src.report_generator import generate_daily_report, generate_summary_for_message, save_report_to_file
        print("✓ src.report_generator 导入成功")

        from src.notifier import WeWorkNotifier, DingTalkNotifier, send_notification
        print("✓ src.notifier 导入成功")

        from src.scheduler import generate_and_send_report, start_scheduler
        print("✓ src.scheduler 导入成功")

        return True

    except ImportError as e:
        print(f"✗ 导入失败: {e}")
        return False


def test_report_generation():
    """测试报告生成功能"""
    print("\n测试报告生成...")

    try:
        from src.report_generator import generate_daily_report, save_report_to_file

        # 模拟数据
        mock_papers = [
            {
                'title': 'Test Paper 1: Advances in Large Language Models',
                'authors': ['Author A', 'Author B'],
                'abstract': 'This paper presents a novel approach to...',
                'url': 'https://arxiv.org/abs/1234.5678',
                'pdf_url': 'https://arxiv.org/pdf/1234.5678.pdf',
                'published': '2026-04-27 10:00:00',
                'categories': ['cs.AI', 'cs.CL'],
                'primary_category': 'cs.AI',
            }
        ]

        mock_news = {
            'technology': [
                {
                    'title': 'OpenAI Releases New Model',
                    'summary': 'OpenAI announced a breakthrough in...',
                    'url': 'https://example.com/news1',
                    'source': 'Test Source',
                    'category': 'technology',
                    'published': '2026-04-27',
                }
            ],
            'market': [
                {
                    'title': 'AI Startup Raises $100M',
                    'summary': 'A leading AI startup secured funding...',
                    'url': 'https://example.com/news2',
                    'source': 'Test Source',
                    'category': 'market',
                    'published': '2026-04-27',
                }
            ]
        }

        # 生成报告
        report = generate_daily_report(mock_papers, mock_news)
        print(f"✓ 报告生成成功 (长度: {len(report)} 字符)")

        # 保存报告
        filepath = save_report_to_file(report, 'test_report.md')
        print(f"✓ 报告已保存到: {filepath}")

        # 验证文件存在
        if os.path.exists(filepath):
            print(f"✓ 文件验证成功")
            os.remove(filepath)  # 清理测试文件
            print("✓ 测试文件已清理")

        return True

    except Exception as e:
        print(f"✗ 报告生成测试失败: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_notifier():
    """测试通知模块"""
    print("\n测试通知模块...")

    try:
        from src.notifier import WeWorkNotifier, DingTalkNotifier

        # 创建实例(不实际发送)
        wework = WeWorkNotifier()
        print("✓ WeWorkNotifier 实例化成功")

        dingtalk = DingTalkNotifier()
        print("✓ DingTalkNotifier 实例化成功")

        print("⚠ 注意: 需要配置 .env 文件才能实际发送消息")

        return True

    except Exception as e:
        print(f"✗ 通知模块测试失败: {e}")
        return False


def main():
    """运行所有测试"""
    print("=" * 60)
    print("AI Daily Report - 系统测试")
    print("=" * 60)

    results = []

    # 测试1: 模块导入
    results.append(("模块导入", test_imports()))

    # 测试2: 报告生成
    results.append(("报告生成", test_report_generation()))

    # 测试3: 通知模块
    results.append(("通知模块", test_notifier()))

    # 汇总结果
    print("\n" + "=" * 60)
    print("测试结果汇总:")
    print("=" * 60)

    passed = sum(1 for _, result in results if result)
    total = len(results)

    for name, result in results:
        status = "✓ 通过" if result else "✗ 失败"
        print(f"{name}: {status}")

    print("=" * 60)
    print(f"总计: {passed}/{total} 测试通过")

    if passed == total:
        print("\n🎉 所有测试通过! 系统可以正常使用。")
        print("\n下一步:")
        print("1. 复制 .env.example 为 .env")
        print("2. 在 .env 中配置企业微信或钉钉 Webhook URL")
        print("3. 运行: python main.py --now (测试运行)")
        print("4. 运行: python main.py (启动定时任务)")
    else:
        print("\n⚠️ 部分测试失败,请检查错误信息。")

    return passed == total


if __name__ == '__main__':
    success = main()
    sys.exit(0 if success else 1)
