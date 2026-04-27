# 🚀 快速开始指南

## 第一步: 安装依赖

```bash
cd ai-daily-report
pip install -r requirements.txt
```

如果 `pip` 命令不可用,尝试:
```bash
python -m pip install -r requirements.txt
```

## 第二步: 配置通知渠道

### 选项A: 飞书机器人 (推荐)

1. **创建群机器人**
   - 打开飞书群聊
   - 点击右上角 "..." → "添加机器人"
   - 选择 "自定义机器人"
   - 设置机器人名称(如 "AI日报")和头像
   - 复制 Webhook 地址

2. **配置环境变量**
   ```bash
   cp .env.example .env
   ```
   编辑 `.env` 文件,填入你的 Webhook URL:
   ```
   FEISHU_WEBHOOK_URL=https://open.feishu.cn/open-apis/bot/v2/hook/YOUR_WEBHOOK_KEY_HERE
   ```

### 选项B: 企业微信机器人

1. **创建群机器人**
   - 打开企业微信群聊
   - 点击右上角 "+" → "添加群机器人"
   - 点击 "新创建机器人"
   - 设置机器人名称(如 "AI日报")
   - 复制 Webhook 地址

2. **配置环境变量**
   ```bash
   cp .env.example .env
   ```
   编辑 `.env` 文件,填入你的 Webhook URL:
   ```
   WEWORK_WEBHOOK_URL=https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=YOUR_KEY_HERE
   ```

### 选项C: 钉钉机器人

1. **创建群机器人**
   - 打开钉钉群聊
   - 点击右上角 "..." → "智能群助手" → "添加机器人"
   - 选择 "自定义" (通过Webhook接入)
   - 设置机器人名称和头像
   - 安全设置选择 "加签"
   - 复制 Webhook URL 和 Secret

2. **配置环境变量**
   编辑 `.env` 文件,填入你的配置:
   ```
   DINGTALK_WEBHOOK_URL=https://oapi.dingtalk.com/robot/send?access_token=YOUR_TOKEN_HERE
   DINGTALK_SECRET=YOUR_SECRET_HERE
   ```

## 第三步: 测试运行

立即生成一份报告进行测试:

```bash
python main.py --now
```

你应该看到类似输出:
```
2026-04-27 14:30:00 - __main__ - INFO - 🤖 AI Daily Report System Starting...
2026-04-27 14:30:00 - src.scheduler - INFO - ==================================================
2026-04-27 14:30:00 - src.scheduler - INFO - 开始生成AI日报 - 2026-04-27 14:30:00
2026-04-27 14:30:00 - src.scheduler - INFO - ==================================================
2026-04-27 14:30:00 - src.scheduler - INFO - 步骤1: 获取最新研究论文...
...
```

检查:
- ✅ 在飞书/企业微信/钉钉收到消息推送
- ✅ `reports/` 目录下生成了报告文件(如 `ai_report_20260427.md`)
- ✅ `logs/` 目录下有日志文件

## 第四步: 启动定时任务

确认测试成功后,启动正式的定时任务:

```bash
python main.py
```

程序将持续运行,每天下午 16:00(4点)自动执行。

**重要**: 不要关闭这个终端窗口,否则定时任务会停止。

## 后台运行(可选)

### Windows

使用 PowerShell 后台运行:
```powershell
Start-Process python -ArgumentList "main.py" -WindowStyle Hidden
```

或使用任务计划程序设置开机自启。

### Linux/macOS

```bash
nohup python main.py > /dev/null 2>&1 &
```

或使用 systemd/cron。

## 常见问题

### Q: 收不到消息推送?

A: 检查以下几点:
1. `.env` 文件是否正确配置
2. Webhook URL 是否完整且正确
3. 机器人是否已添加到群聊
4. 查看 `logs/ai_report.log` 了解错误详情

### Q: 如何修改报告发送时间?

A: 编辑 `main.py`,找到最后一行:
```python
start_scheduler(hour=8, minute=0)
```
修改为你想要的时间,例如改为早上7:30:
```python
start_scheduler(hour=7, minute=30)
```

### Q: 如何手动触发一次报告?

A: 随时运行:
```bash
python main.py --now
```

### Q: 如何查看历史报告?

A: 所有报告都保存在 `reports/` 目录下,文件名格式为 `ai_report_YYYYMMDD.md`。
可以使用任何 Markdown 阅读器打开。

### Q: 如何添加更多数据源?

A: 编辑 `config/sources.py`,在 `NEWS_SOURCES` 列表中添加新的数据源:
```python
{
    'name': '你的数据源名称',
    'url': 'https://example.com/feed',
    'type': 'rss',  # 或 'web'
    'category': 'technology'  # 或 'market'
}
```

## 下一步

- 📖 阅读 [README.md](README.md) 了解更多详细功能
- 🔧 查看 `config/sources.py` 自定义数据源和关键词
- 📝 查看生成的报告文件了解报告格式
- 💡 根据需要调整配置参数

---

**祝你使用愉快! 如有问题请查看日志文件。** 🎉
