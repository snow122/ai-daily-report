# 🧪 飞书推送测试指南

## 测试前准备

### 1. 确保已配置 Webhook URL

编辑 `.env` 文件,填入你的飞书 Webhook URL:

```env
FEISHU_WEBHOOK_URL=https://open.feishu.cn/open-apis/bot/v2/hook/你的实际key
```

### 2. 安装依赖(如果还没安装)

```bash
pip install -r requirements.txt
```

---

## 测试方法

### 方法一: 使用测试脚本(推荐)

```bash
python test_feishu.py
```

这个脚本提供两种测试模式:

**模式1: 简单测试**
- 发送一条测试消息
- 验证飞书连接是否正常
- 快速确认配置是否正确

**模式2: 完整测试**
- 获取真实的论文和新闻
- 生成完整的报告摘要
- 发送到飞书
- 模拟真实运行流程

### 方法二: 直接运行主程序

```bash
python main.py --now
```

这会立即生成一份真实的AI日报并推送到飞书。

---

## 预期结果

### ✅ 成功的情况

1. **终端输出**:
   ```
   ✓ 检测到 Webhook URL
   📤 正在发送测试消息到飞书...
   ✅ 测试成功!
   ```

2. **飞书群聊**:
   - 收到一条蓝色卡片消息
   - 标题: "🧪 测试消息 - Test Message" 或 "🤖 AI Daily Report"
   - 内容包含测试文本或报告摘要

### ❌ 失败的情况

**错误1: 未配置 Webhook URL**
```
❌ 错误: 未找到 FEISHU_WEBHOOK_URL 环境变量
```
**解决**: 编辑 `.env` 文件,填入正确的 Webhook URL

**错误2: Webhook URL 无效**
```
❌ 发送失败
飞书消息发送失败: {...}
```
**解决**:
- 检查 Webhook URL 是否完整
- 确认机器人仍在群聊中
- 重新创建机器人获取新的 Webhook URL

**错误3: 网络问题**
```
❌ 发生错误: Connection timeout
```
**解决**:
- 检查网络连接
- 确认能访问 open.feishu.cn
- 检查防火墙设置

---

## 常见问题排查

### Q1: 收不到消息怎么办?

**检查清单**:
- [ ] `.env` 文件存在且配置正确
- [ ] Webhook URL 完整无误
- [ ] 机器人在群聊中(未被移除)
- [ ] 网络连接正常
- [ ] 查看了 `logs/ai_report.log` 日志

### Q2: 如何查看日志?

```bash
# Windows
type logs\ai_report.log

# Linux/Mac
cat logs/ai_report.log
```

### Q3: 如何重新获取 Webhook URL?

1. 在群聊中移除旧机器人
2. 重新添加自定义机器人
3. 复制新的 Webhook URL
4. 更新 `.env` 文件

### Q4: 可以测试多次吗?

当然可以!随时运行:
```bash
python test_feishu.py
```
或
```bash
python main.py --now
```

---

## 测试通过后的下一步

### 1. 生成真实报告测试

```bash
python main.py --now
```

这会在飞书发送一份包含真实论文和新闻的报告。

### 2. 启动定时任务

```bash
python main.py
```

**重要**: 这个命令会持续运行,每天早晨8点自动推送。

⚠️ **不要关闭终端窗口!**

### 3. (可选)后台运行

**Windows PowerShell**:
```powershell
Start-Process python -ArgumentList "main.py" -WindowStyle Hidden
```

**Linux/Mac**:
```bash
nohup python main.py > /dev/null 2>&1 &
```

---

## 消息样式预览

### 测试消息
```
┌──────────────────────────────────────┐
│ 🧪 测试消息 - Test Message           │
├──────────────────────────────────────┤
│                                      │
│ 🤖 AI Daily Report - 测试消息        │
│                                      │
│ 这是一条测试消息...                  │
│ 如果收到此消息,说明配置成功! ✅      │
│                                      │
└──────────────────────────────────────┘
```

### 真实报告
```
┌──────────────────────────────────────┐
│ 🤖 AI Daily Report                   │
├──────────────────────────────────────┤
│                                      │
│ 📚 Latest Papers: 8 篇               │
│   1. GPT-5 Technical Report          │
│   2. Advances in Computer Vision     │
│                                      │
│ 💻 Tech Updates: 5 条                │
│ 📈 Market News: 4 条                 │
│                                      │
│ 完整报告已生成...                    │
│                                      │
└──────────────────────────────────────┘
```

---

## 需要帮助?

- 查看详细配置: `FEISHU_GUIDE.md`
- 查看快速开始: `QUICKSTART.md`
- 查看完整文档: `README.md`

---

**祝你测试顺利! 🎉**
