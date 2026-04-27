# ✅ GitHub创建仓库的正确方法

## 🎯 问题原因

`https://github.com/new` 可能需要先登录才能访问。

---

## ✅ 正确的操作步骤

### 第1步: 登录GitHub

**访问**: https://github.com/login

输入你的用户名 `snow122` 和密码登录

---

### 第2步: 创建新仓库

登录后,有**3种方法**创建仓库:

#### 方法A: 点击右上角的 "+" 号(推荐)
1. 在GitHub页面右上角,找到 **"+"** 图标
2. 点击它
3. 选择 **"New repository"**

#### 方法B: 访问创建页面
直接访问: https://github.com/new
(这次应该可以正常访问了,因为已经登录)

#### 方法C: 从个人主页创建
1. 点击右上角你的头像
2. 选择 **"Your repositories"**
3. 点击绿色的 **"New"** 按钮

---

### 第3步: 填写仓库信息

在创建页面填写:

- **Repository name**: `ai-daily-report`
- **Description**(可选): AI Daily Report System
- **选择**: ⚫ Private (私有,保护你的Webhook URL)
- **不要勾选**: "Initialize this repository with a README"
- **不要勾选**: 其他任何选项

然后点击绿色的 **"Create repository"** 按钮

---

### 第4步: 推送代码

仓库创建成功后,会显示一些命令。

打开CMD,运行:

```bash
cd /d "d:\桌面\项目\ai-daily-report"
git push -u origin main
```

**如果提示输入认证信息**:
- Username: `snow122`
- Password: 使用Personal Access Token

**获取Token**:
1. 访问: https://github.com/settings/tokens
2. 点击 "Generate new token (classic)"
3. 勾选 "repo" 权限
4. 生成并复制Token
5. 用Token作为密码粘贴到CMD中

---

### 第5步: 配置Secrets

1. 在你的仓库页面(应该是 `https://github.com/snow122/ai-daily-report`)
2. 点击顶部导航栏的 **Settings**
3. 左侧菜单找到 **Secrets and variables** → **Actions**
4. 点击 **New repository secret**
5. 填写:
   - Name: `FEISHU_WEBHOOK_URL`
   - Value: `https://open.feishu.cn/open-apis/bot/v2/hook/da523c13-8176-4d7b-bdbb-73eaf37633fb`
6. 点击 **Add secret**

---

### 第6步: 验证和测试

1. 访问: https://github.com/snow122/ai-daily-report/actions
2. 应该能看到 "AI Daily Report" 工作流
3. 点击右侧 **Run workflow** → **Run workflow**(手动测试)
4. 等待1-2分钟
5. 查看飞书是否收到消息

---

## 📋 快速检查清单

- [ ] 已登录GitHub (https://github.com/login)
- [ ] 已创建私有仓库 `ai-daily-report`
- [ ] 已推送代码 (`git push -u origin main`)
- [ ] 已配置Secret `FEISHU_WEBHOOK_URL`
- [ ] 已手动测试一次 (Actions → Run workflow)
- [ ] 飞书收到测试消息

---

## 💡 提示

### 如果git push失败

**错误**: Authentication failed

**解决**: 使用Personal Access Token
1. https://github.com/settings/tokens
2. Generate new token (classic)
3. 勾选 "repo"
4. 复制Token
5. 用Token作为密码

### 如果想用HTTPS简化认证

```bash
# 设置Git缓存凭证(避免每次都输入)
git config --global credential.helper store

# 然后再次push
git push -u origin main
```

下次只需要输入一次用户名和密码,之后会自动记住。

---

## 🎉 完成后

- ✅ 每天北京时间下午4点自动执行
- ✅ 无论你的电脑是否开机
- ✅ 准时推送到飞书
- ✅ 完全免费
- ✅ 24小时在线

**现在就去登录GitHub开始吧! 🚀**
