# ✅ 明天下午4点收到报告 - 完整检查清单

## 📋 必须完成的步骤

### ✓ 步骤1: 在飞书中创建机器人 (1分钟)

- [ ] 打开飞书,进入一个群聊
- [ ] 点击右上角 "..." → "添加机器人"
- [ ] 选择 "自定义机器人"
- [ ] 设置名称为 "AI日报"
- [ ] **复制 Webhook URL** (重要!)

Webhook URL 格式:
```
https://open.feishu.cn/open-apis/bot/v2/hook/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
```

---

### ✓ 步骤2: 配置 .env 文件 (30秒)

当前 `.env` 文件内容:
```env
FEISHU_WEBHOOK_URL=https://open.feishu.cn/open-apis/bot/v2/hook/请在这里填入你的飞书webhook_key
```

**你需要做的**:
将 `请在这里填入你的飞书webhook_key` 替换为你从飞书复制的真实 key

**示例**:
```env
FEISHU_WEBHOOK_URL=https://open.feishu.cn/open-apis/bot/v2/hook/a1b2c3d4-e5f6-7890-abcd-ef1234567890
```

---

### ✓ 步骤3: 测试推送 (1分钟)

运行测试命令:
```bash
cd "d:\桌面\项目\ai-daily-report"
python test_feishu.py
```

或直接测试真实报告:
```bash
python main.py --now
```

**预期结果**:
- ✅ 终端显示 "发送成功"
- ✅ 飞书群聊中收到卡片消息

如果失败:
- 检查 `.env` 文件中的 Webhook URL 是否正确
- 查看 `logs/ai_report.log` 了解错误详情

---

### ✓ 步骤4: 启动定时任务 (关键!)

测试成功后,**必须运行这个命令**:

```bash
python main.py
```

你会看到:
```
启动定时任务调度器 (每天8:00执行)
```

⚠️ **极其重要**:
- **不要关闭这个终端窗口!**
- 程序会持续运行,每天早晨8点自动推送
- 如果关闭窗口,定时任务会停止

---

## 🔍 验证清单

在睡觉前,确认以下事项:

- [ ] `.env` 文件已配置正确的 Webhook URL
- [ ] 运行 `python main.py --now` 成功收到测试消息
- [ ] 运行 `python main.py` 启动了定时任务
- [ ] 终端窗口保持打开状态(显示 "启动定时任务调度器")
- [ ] 查看了 `logs/ai_report.log` 确认无错误

---

## ⏰ 明天早晨8点

你应该在飞书群聊中收到:

```
┌──────────────────────────────────────┐
│ 🤖 AI Daily Report                   │
├──────────────────────────────────────┤
│                                      │
│ 📚 Latest Papers / 最新论文: X 篇    │
│   1. [论文标题]                      │
│   2. [论文标题]                      │
│                                      │
│ 💻 Tech Updates / 技术动态: X 条     │
│ 📈 Market News / 市场资讯: X 条      │
│                                      │
└──────────────────────────────────────┘
```

---

## ❓ 如果没收到怎么办?

### 检查1: 程序是否在运行?

查看终端窗口,应该显示:
```
启动定时任务调度器 (每天8:00执行)
```

如果没有,重新运行:
```bash
python main.py
```

### 检查2: 查看日志

```bash
# Windows
type logs\ai_report.log

# 查找是否有错误信息
```

### 检查3: 手动触发测试

```bash
python main.py --now
```

如果能收到,说明配置正确,只是定时任务没运行。

### 检查4: 系统时间

确认你的电脑时间正确:
```bash
# Windows
time

# 确保时区是北京时间 (UTC+8)
```

---

## 💡 提示

1. **首次使用建议**:
   - 先运行 `python test_feishu.py` 进行简单测试
   - 再运行 `python main.py --now` 生成真实报告
   - 最后运行 `python main.py` 启动定时任务

2. **保持程序运行**:
   - 定时任务需要程序持续运行
   - 不要关闭运行 `python main.py` 的终端窗口
   - 如果需要后台运行,参考 README.md

3. **历史记录**:
   - 所有报告保存在 `reports/` 目录
   - 日志保存在 `logs/ai_report.log`
   - 可以随时查阅

---

## 📞 需要帮助?

- 飞书配置: 查看 `FEISHU_GUIDE.md`
- 快速开始: 查看 `QUICKSTART.md`
- 完整文档: 查看 `README.md`
- 测试指南: 查看 `TEST_GUIDE.md`

---

**完成以上步骤,明天早晨8点你就能准时收到AI日报了! 🎉**
