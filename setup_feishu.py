"""
飞书配置助手
帮助用户快速配置和测试飞书推送
"""

import os
import sys


def print_banner():
    """打印欢迎横幅"""
    print("\n" + "=" * 60)
    print("🤖 AI Daily Report - 飞书配置助手")
    print("=" * 60)


def check_env_file():
    """检查.env文件"""
    print("\n📋 步骤1: 检查配置文件")
    print("-" * 60)

    if not os.path.exists('.env'):
        print("❌ 未找到 .env 文件")
        print("   正在从模板创建...")
        if os.path.exists('.env.example'):
            import shutil
            shutil.copy('.env.example', '.env')
            print("   ✓ .env 文件已创建")
        else:
            print("   ❌ 未找到 .env.example 模板文件")
            return False
    else:
        print("   ✓ .env 文件存在")

    # 读取并检查内容
    with open('.env', 'r', encoding='utf-8') as f:
        content = f.read()

    if '请在这里填入你的飞书webhook_key' in content or 'YOUR_' in content:
        print("   ⚠️  Webhook URL 尚未配置")
        return False
    else:
        print("   ✓ Webhook URL 已配置")
        return True


def get_webhook_from_user():
    """从用户获取 Webhook URL"""
    print("\n📝 步骤2: 配置飞书 Webhook URL")
    print("-" * 60)
    print("\n请按以下步骤操作:")
    print("1. 打开飞书,进入一个群聊")
    print("2. 点击右上角 '...' → '添加机器人'")
    print("3. 选择 '自定义机器人',设置名称为 'AI日报'")
    print("4. 复制显示的 Webhook URL")
    print("\nWebhook URL 格式:")
    print("https://open.feishu.cn/open-apis/bot/v2/hook/xxxxx\n")

    webhook_url = input("请粘贴你的飞书 Webhook URL: ").strip()

    if not webhook_url:
        print("❌ 未输入任何内容")
        return False

    if not webhook_url.startswith('https://open.feishu.cn/open-apis/bot/v2/hook/'):
        print("❌ Webhook URL 格式不正确")
        print("   应该以 https://open.feishu.cn/open-apis/bot/v2/hook/ 开头")
        return False

    # 写入 .env 文件
    env_content = f"# 飞书 Webhook URL\nFEISHU_WEBHOOK_URL={webhook_url}\n"

    with open('.env', 'w', encoding='utf-8') as f:
        f.write(env_content)

    print("✓ Webhook URL 已保存到 .env 文件")
    return True


def test_connection():
    """测试飞书连接"""
    print("\n🧪 步骤3: 测试飞书连接")
    print("-" * 60)

    try:
        from dotenv import load_dotenv
        load_dotenv()

        from src.notifier import FeishuNotifier

        notifier = FeishuNotifier()

        test_message = """🤖 AI Daily Report - 配置测试

✅ 恭喜!飞书推送配置成功!

这是一条测试消息,用于验证配置是否正确。
明天早晨8点开始,你将每天收到AI领域的最新进展。

---
*配置时间: 刚刚*
"""

        print("\n📤 正在发送测试消息...")
        success = notifier.send_card("✅ 配置成功!", test_message, "green")

        if success:
            print("✓ 测试消息发送成功!")
            print("\n请在飞书群聊中查看消息。")
            return True
        else:
            print("❌ 发送失败")
            return False

    except ImportError as e:
        print(f"❌ 缺少依赖包: {e}")
        print("\n请先安装依赖:")
        print("pip install -r requirements.txt")
        return False
    except Exception as e:
        print(f"❌ 测试失败: {str(e)}")
        return False


def start_scheduler():
    """询问是否启动定时任务"""
    print("\n⏰ 步骤4: 启动定时任务")
    print("-" * 60)
    print("\n你可以选择:")
    print("1. 立即启动定时任务 (每天早晨8点自动推送)")
    print("2. 稍后手动启动 (运行 python main.py)")
    print()

    choice = input("请选择 (1/2, 默认2): ").strip()

    if choice == '1':
        print("\n正在启动定时任务...")
        print("⚠️  重要: 不要关闭这个终端窗口!\n")

        try:
            from src.scheduler import start_scheduler
            start_scheduler(hour=8, minute=0)
        except KeyboardInterrupt:
            print("\n\n定时任务已停止")
            print("如需重新启动,运行: python main.py")
    else:
        print("\n好的,稍后可以运行以下命令启动定时任务:")
        print("  python main.py")


def main():
    """主函数"""
    print_banner()

    # 步骤1: 检查配置文件
    env_exists = check_env_file()

    # 步骤2: 获取 Webhook URL (如果需要)
    if not env_exists:
        success = get_webhook_from_user()
        if not success:
            print("\n❌ 配置失败,请重试")
            sys.exit(1)

    # 步骤3: 测试连接
    test_success = test_connection()

    if not test_success:
        print("\n❌ 测试失败,请检查:")
        print("  1. Webhook URL 是否正确")
        print("  2. 机器人是否在群聊中")
        print("  3. 网络连接是否正常")
        print("\n查看帮助文档: FEISHU_GUIDE.md")
        sys.exit(1)

    # 步骤4: 启动定时任务
    print("\n" + "=" * 60)
    print("🎉 配置完成!")
    print("=" * 60)
    print("\n你现在可以:")
    print("  • 运行 'python main.py --now' 生成真实报告")
    print("  • 运行 'python main.py' 启动定时任务")
    print("  • 查看 'CHECKLIST.md' 了解完整步骤")

    # 询问是否立即启动
    start_scheduler()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n程序已退出")
        sys.exit(0)
