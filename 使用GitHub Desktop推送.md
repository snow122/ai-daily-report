# 🚀 使用GitHub Desktop推送代码 - 超简单指南

## 🎯 为什么用GitHub Desktop?

- ✅ **不需要命令行**
- ✅ **图形界面,点点鼠标就行**
- ✅ **自动处理Git配置**
- ✅ **自动处理认证**
- ✅ **5分钟搞定**

---

## 📋 详细步骤

### 第1步: 下载GitHub Desktop

1. **访问**: https://desktop.github.com/
2. **点击**: "Download for Windows"
3. **等待下载完成**
4. **运行安装程序** (GitHubDesktopSetup.exe)
5. **等待安装完成**(会自动启动)

---

### 第2步: 登录GitHub账号

1. GitHub Desktop启动后,会看到登录界面
2. **点击**: "Sign in to GitHub.com"
3. **输入用户名**: `snow122`
4. **输入密码**: 你的GitHub密码
5. **点击**: "Sign in"
6. 如果浏览器弹出授权页面,点击 **"Authorize desktop"**

---

### 第3步: 添加本地仓库

1. 登录后,点击左上角的 **File** 菜单
2. 选择 **"Add local repository..."**
3. 点击 **"Choose..."** 按钮
4. **导航到**: `d:\桌面\项目\ai-daily-report`
5. **点击**: "选择文件夹"
6. 如果提示 "This directory does not appear to be a Git repository"
7. **点击**: **"create a repository"**
8. 在弹出的窗口中:
   - Name: `ai-daily-report`
   - Description: (可选) AI Daily Report System
   - **点击**: "Create Repository"

---

### 第4步: 发布到GitHub

1. 现在你会看到主界面,左侧显示文件列表
2. **点击右上角的绿色按钮**: "Publish repository"
3. 在弹出的窗口中:
   - Name: `ai-daily-report` (应该已自动填写)
   - Description: (可选)
   - **勾选**: ⚫ "Keep this code private" (重要!设为私有)
   - **不要勾选**: "Include all branches"
4. **点击**: "Publish repository"
5. 等待上传完成(底部会显示进度)

**✅ 完成!代码已推送到GitHub!**

---

### 第5步: 验证

1. **打开浏览器**
2. **访问**: https://github.com/snow122/ai-daily-report
3. 你应该能看到所有文件
4. 如果看到了,说明成功! 🎉

---

### 第6步: 配置Secrets

1. 在GitHub仓库页面
2. **点击顶部导航栏**: Settings
3. **左侧菜单**: Secrets and variables → Actions
4. **点击**: New repository secret
5. **填写**:
   - Name: `FEISHU_WEBHOOK_URL`
   - Value: `https://open.feishu.cn/open-apis/bot/v2/hook/da523c13-8176-4d7b-bdbb-73eaf37633fb`
6. **点击**: Add secret

---

### 第7步: 测试

1. **点击顶部导航栏**: Actions
2. 应该能看到 "AI Daily Report" 工作流
3. **点击右侧**: Run workflow
4. **点击绿色按钮**: Run workflow
5. **等待1-2分钟**
6. **查看飞书**是否收到消息

---

## 🎊 完成!

从现在开始:
- ✅ 每天北京时间下午4点自动执行
- ✅ 无论你的电脑是否开机
- ✅ 准时推送到飞书
- ✅ 完全免费

---

## 💡 以后如何更新代码?

如果以后修改了代码,想同步到GitHub:

1. 打开GitHub Desktop
2. 左侧会显示修改的文件
3. 在左下角填写:
   - Summary: 简短描述(如 "更新配置")
4. **点击**: "Commit to main"
5. **点击右上角**: "Push origin"

**完成!** 就这么简单!

---

## ❓ 常见问题

### Q1: 下载很慢怎么办?

A: GitHub Desktop文件不大(约100MB),如果慢可以:
- 使用VPN加速
- 或使用国内镜像下载

### Q2: 登录失败怎么办?

A: 
- 确认用户名和密码正确
- 如果开启了两步验证,需要使用Personal Access Token
- 获取Token: https://github.com/settings/tokens

### Q3: 发布时提示错误?

A:
- 确认网络连接正常
- 确认仓库名称未被占用
- 尝试刷新页面重新登录

---

## 🎯 总结

**只需3步**:
1. ✅ 下载安装GitHub Desktop
2. ✅ 登录并添加仓库
3. ✅ 发布到GitHub

**然后配置Secrets,就完成了!**

**现在就下载GitHub Desktop开始吧! 🚀**

下载地址: https://desktop.github.com/
