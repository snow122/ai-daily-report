# 🚀 AI日报 - 3分钟快速配置(电脑可正常开关机)

## ✅ 最佳方案: Windows定时任务

**优势**:
- ✅ 电脑可以正常关机/重启
- ✅ 无需保持任何窗口开启
- ✅ 系统级别自动化,稳定可靠
- ✅ 每天下午4点自动推送到飞书

---

## 📋 配置步骤(只需2步!)

### 第1步: 确保已配置飞书Webhook

检查 `.env` 文件是否包含你的飞书 Webhook URL:
```env
FEISHU_WEBHOOK_URL=https://open.feishu.cn/open-apis/bot/v2/hook/da523c13-8176-4d7b-bdbb-73eaf37633fb
```

✅ 你已经配置好了!可以跳过这一步。

---

### 第2步: 设置Windows定时任务

**右键点击** `setup_task.bat`,选择 **"以管理员身份运行"**

等待提示 "✅ 定时任务创建成功!"

**完成!** 🎉

---

## ⏰ 明天下午4点会发生什么?

如果电脑是开着的:
1. Windows自动触发任务
2. 获取最新AI论文和资讯
3. 生成报告并推送到你的飞书群
4. 保存报告到 `reports/` 目录
5. 任务结束(无任何窗口残留)

如果电脑是关机的:
- 任务不会执行
- 随时手动运行: `python main.py --now` 补看报告

---

## 🔍 如何确认任务已创建?

### 方法1: 命令行查看
```bash
schtasks /query /tn "AI_Daily_Report"
```

### 方法2: 图形界面查看
1. 按 `Win + R`,输入 `taskschd.msc`
2. 找到 "AI_Daily_Report" 任务
3. 可以看到下次运行时间

---

## 🧪 立即测试(可选)

想现在就看看效果?

**方法1**: 双击运行 `一键安装依赖.bat`

**方法2**: 在CMD中运行:
```bash
cd /d "d:\桌面\项目\ai-daily-report"
python main.py --now
```

你会在飞书群聊中收到一份完整的AI日报!

---

## 💡 常用命令

### 查看任务状态
```bash
schtasks /query /tn "AI_Daily_Report"
```

### 立即执行一次(测试用)
```bash
schtasks /run /tn "AI_Daily_Report"
```

### 临时禁用任务
```bash
schtasks /change /tn "AI_Daily_Report" /disable
```

### 重新启用任务
```bash
schtasks /change /tn "AI_Daily_Report" /enable
```

### 删除任务
```bash
schtasks /delete /tn "AI_Daily_Report" /f
```

---

## 📚 更多文档

- **定时任务说明.md** - 详细的定时任务配置指南
- **FEISHU_GUIDE.md** - 飞书配置指南
- **TEST_GUIDE.md** - 测试指南
- **CHECKLIST.md** - 完整检查清单

---

## ❓ 常见问题

### Q: 如果下午4点电脑没开机怎么办?
A: 任务不会执行。开机后随时运行 `python main.py --now` 手动生成报告。

### Q: 可以修改推送时间吗?
A: 可以!查看 `定时任务说明.md` 中的"修改执行时间"章节。

### Q: 如何知道任务是否成功执行?
A: 查看 `logs/ai_report.log` 日志文件和 `reports/` 目录的报告文件。

---

## 🎉 总结

你只需要:
1. ✅ 飞书 Webhook 已配置
2. ✅ 右键运行 `setup_task.bat`(管理员身份)

**就完成了!每天下午4点飞书见!** 🚀
