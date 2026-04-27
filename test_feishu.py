"""
飞书推送测试脚本
用于验证飞书机器人配置是否正确
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from src.notifier import FeishuNotifier
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()


def test_feishu_connection():
    """测试飞书连接"""
    print("=" * 60)
    print("飞书推送功能测试")
    print("=" * 60)

    # 检查环境变量
    webhook_url = os.getenv('FEISHU_WEBHOOK_URL')

    if not webhook_url:
        print("\n❌ 错误: 未找到 FEISHU_WEBHOOK_URL 环境变量")
        print("\n请按以下步骤配置:")
        print("1. 在飞书群中创建自定义机器人")
        print("2. 复制 Webhook URL")
        print("3. 编辑 .env 文件,填入:")
        print("   FEISHU_WEBHOOK_URL=你的webhook地址")
        return False

    print(f"\n✓ 检测到 Webhook URL: {webhook_url[:50]}...")

    # 创建飞书通知器
    notifier = FeishuNotifier(webhook_url)

    # 测试消息
    test_message = """🤖 AI Daily Report - 测试消息

这是一条测试消息,用于验证飞书推送功能是否正常。

如果收到此消息,说明配置成功! ✅

---
*发送时间: 测试中*
"""

    print("\n📤 正在发送测试消息到飞书...")

    try:
        # 发送卡片消息
        success = notifier.send_card(
            title="🧪 测试消息 - Test Message",
            content=test_message,
            color="blue"
        )

        if success:
            print("\n✅ 测试成功!")
            print("\n请在飞书群聊中查看消息。")
            print("如果看到卡片消息,说明配置完全正确!")
            return True
        else:
            print("\n❌ 发送失败")
            print("\n可能的原因:")
            print("1. Webhook URL 不正确或已失效")
            print("2. 机器人已被移除群聊")
            print("3. 网络连接问题")
            print("\n请检查 .env 文件中的 Webhook URL 是否正确")
            return False

    except Exception as e:
        print(f"\n❌ 发生错误: {str(e)}")
        return False


def test_full_workflow():
    """测试完整工作流程"""
    print("\n" + "=" * 60)
    print("完整工作流程测试")
    print("=" * 60)

    try:
        from src.paper_fetcher import fetch_arxiv_papers
        from src.news_fetcher import fetch_all_news
        from src.report_generator import generate_summary_for_message

        print("\n📚 步骤1: 获取最新论文...")
        papers = fetch_arxiv_papers()
        print(f"   ✓ 获取到 {len(papers)} 篇论文")

        print("\n📰 步骤2: 获取新闻资讯...")
        news = fetch_all_news()
        tech_count = len(news.get('technology', []))
        market_count = len(news.get('market', []))
        print(f"   ✓ 技术资讯: {tech_count} 条")
        print(f"   ✓ 市场资讯: {market_count} 条")

        print("\n📝 步骤3: 生成报告摘要...")
        summary = generate_summary_for_message(papers, news)
        print(f"   ✓ 摘要长度: {len(summary)} 字符")

        print("\n📤 步骤4: 发送到飞书...")
        notifier = FeishuNotifier()
        success = notifier.send_card("🤖 AI Daily Report", summary, "blue")

        if success:
            print("   ✓ 发送成功!")
            print("\n✅ 完整流程测试通过!")
            return True
        else:
            print("   ❌ 发送失败")
            return False

    except ImportError as e:
        print(f"\n⚠️  缺少依赖包: {e}")
        print("\n请先安装依赖:")
        print("pip install -r requirements.txt")
        return False
    except Exception as e:
        print(f"\n❌ 测试失败: {str(e)}")
        import traceback
        traceback.print_exc()
        return False


def main():
    """主函数"""
    print("\n请选择测试模式:")
    print("1. 简单测试 - 只发送测试消息")
    print("2. 完整测试 - 生成真实报告并发送")
    print()

    choice = input("请输入选项 (1/2, 默认1): ").strip()

    if choice == '2':
        print("\n开始完整测试...\n")
        success = test_full_workflow()
    else:
        print("\n开始简单测试...\n")
        success = test_feishu_connection()

    print("\n" + "=" * 60)
    if success:
        print("🎉 测试完成! 配置正确!")
        print("\n下一步:")
        print("1. 运行 'python main.py --now' 生成真实报告")
        print("2. 运行 'python main.py' 启动定时任务(每天8点)")
    else:
        print("⚠️  测试未通过,请检查配置")
        print("\n帮助文档:")
        print("- 查看 FEISHU_GUIDE.md 了解详细配置步骤")
        print("- 查看 QUICKSTART.md 了解快速开始指南")
    print("=" * 60)


if __name__ == '__main__':
    main()
