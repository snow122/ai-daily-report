# 🚀 GitHub Actions 配置指南 - 10分钟实现24小时在线

## 🎯 这是什么?

GitHub Actions 是 GitHub 提供的自动化服务,可以让你的代码在云端运行。

**优势**:
- ✅ **完全免费**(每月2000分钟运行时间,你用不完)
- ✅ 24小时在线,无论你的电脑是否开机
- ✅ 每天下午4点准时推送到飞书
- ✅ 无需维护服务器
- ✅ 可靠性极高(GitHub基础设施)

---

## 📋 配置步骤(超简单!)

### 第1步: 创建GitHub仓库 (2分钟)

1. 访问 https://github.com/new
2. 填写信息:
   - Repository name: `ai-daily-report`
   - 选择 **Private**(私有,保护你的Webhook URL)
3. 点击 **Create repository**

---

### 第2步: 上传代码到GitHub (3分钟)

打开CMD或PowerShell,运行:

```bash
cd "d:\桌面\项目\ai-daily-report"

# 初始化Git仓库
git init

# 添加所有文件
git add .

# 提交
git commit -m "AI日报系统"

# 关联GitHub仓库(替换YOUR_USERNAME为你的GitHub用户名)
git remote add origin https://github.com/YOUR_USERNAME/ai-daily-report.git

# 推送到GitHub
git push -u origin main
```

**如果遇到Git未安装**:
- 下载Git: https://git-scm.com/download/win
- 或使用GitHub Desktop(图形界面): https://desktop.github.com/

---

### 第3步: 配置Secrets (2分钟)

1. 在GitHub仓库页面,点击顶部导航栏的 **Settings**
2. 左侧菜单找到 **Secrets and variables** → **Actions**
3. 点击 **New repository secret**
4. 填写:
   - **Name**: `FEISHU_WEBHOOK_URL`
   - **Value**: `https://open.feishu.cn/open-apis/bot/v2/hook/da523c13-8176-4d7b-bdbb-73eaf37633fb`
5. 点击 **Add secret**

---

### 第4步: 验证配置 (1分钟)

1. 在GitHub仓库页面,点击顶部的 **Actions** 标签
2. 你应该能看到 "AI Daily Report" 工作流
3. 点击右侧的 **Run workflow** → **Run workflow**(手动测试)
4. 等待几分钟,查看飞书是否收到消息

---

### 第5步: 完成! 🎉

从现在开始:
- ✅ 每天北京时间下午4点自动执行
- ✅ 无论你的电脑是否开机
- ✅ 准时推送到你的飞书群

---

## 🔍 如何确认正在运行?

### 查看执行历史

1. 访问 GitHub 仓库的 **Actions** 标签
2. 左侧看到 "AI Daily Report"
3. 点击可以看到每次执行的记录
4. 绿色✓表示成功,红色✗表示失败

### 查看日志

点击任意一次执行记录,可以看到:
- 执行的每一步
- 输出日志
- 错误信息(如果有)

---

## 💡 常见问题

### Q1: 推送失败了怎么办?

**检查**:
1. Actions标签中查看错误日志
2. 确认Secrets中的Webhook URL正确
3. 确认requirements.txt包含所有依赖

**重新运行**:
点击 **Run workflow** 手动触发一次

### Q2: 可以修改执行时间吗?

可以!编辑 `.github/workflows/daily_report.yml`:

```yaml
schedule:
  # cron表达式: 分 时 日 月 周
  # 当前: UTC 8:00 = 北京时间 16:00
  - cron: '0 8 * * *'
```

改为其他时间(UTC时间):
- 早上9点北京: `cron: '0 1 * * *'`
- 晚上8点北京: `cron: '0 12 * * *'`

### Q3: GitHub Actions真的免费吗?

是的!GitHub为每个账户提供:
- 每月2000分钟运行时间
- 你的任务每次运行约1-2分钟
- 每天1次 = 每月约60分钟
- **完全够用!**

### Q4: 我的代码安全吗?

非常安全!
- 仓库设置为Private(私有)
- Webhook URL存储在Secrets中(加密)
- 只有你能看到
- GitHub是世界最大的代码平台,安全性极高

### Q5: 如果我想暂停怎么办?

**方法1**: 在Actions页面禁用工作流
**方法2**: 删除或重命名 `.github/workflows/daily_report.yml`
**方法3**: 删除整个仓库

---

## 📊 执行流程

```
每天 UTC 8:00 (北京 16:00)
        ↓
GitHub Actions 自动触发
        ↓
启动 Ubuntu 虚拟机
        ↓
克隆你的代码
        ↓
安装 Python 3.11
        ↓
安装依赖包
        ↓
执行 python main.py --now
        ↓
获取最新AI论文和资讯
        ↓
生成报告并推送到飞书
        ↓
保存报告到Artifact
        ↓
虚拟机关闭
        ↓
完成!(耗时约1-2分钟)
```

---

## 🎁 额外功能

### 下载报告

每次执行后,报告会保存为Artifact:
1. 在Actions中找到对应的执行记录
2. 页面底部有 "Artifacts" 区域
3. 点击下载 `ai-reports`
4. 解压查看所有历史报告

### 手动触发

随时可以手动执行:
1. Actions → AI Daily Report
2. 点击 **Run workflow**
3. 立即执行一次

### 通知设置

可以在仓库Settings中配置:
- 执行失败时邮件通知
- Slack/Discord通知等

---

## 📞 需要帮助?

如果遇到问题:
1. 查看Actions中的错误日志
2. 确认Secrets配置正确
3. 检查 `.env` 文件(本地测试用)
4. 查看 `logs/ai_report.log`(本地日志)

---

## 🎉 总结

**只需4步**:
1. ✅ 创建GitHub私有仓库
2. ✅ 上传代码
3. ✅ 配置Secrets(Webhook URL)
4. ✅ 手动测试一次

**完成后**:
- 🌍 24小时在线
- ⏰ 每天下午4点准时推送
- 💻 你的电脑可以全年关机
- 💰 完全免费
- 🔒 安全可靠

**现在就行动吧!10分钟后就能实现24小时在线了! 🚀**
