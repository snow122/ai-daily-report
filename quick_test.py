"""快速测试飞书推送"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from dotenv import load_dotenv
load_dotenv()

from src.notifier import FeishuNotifier

notifier = FeishuNotifier()

test_msg = """🤖 AI Daily Report - 配置测试

✅ 恭喜!飞书推送配置成功!

明天早晨8点开始,你将每天收到AI领域的最新进展。

---
*测试时间: 刚刚*
"""

print("正在发送测试消息到飞书...")
success = notifier.send_card("✅ 配置成功!", test_msg, "green")

if success:
    print("✅ 测试成功!请查看飞书群聊")
else:
    print("❌ 测试失败")
