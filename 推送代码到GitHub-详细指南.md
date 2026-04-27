# 🔧 Git命令找不到 - 解决方案

## ❓ 问题原因

虽然Git已安装,但系统PATH环境变量中没有包含Git的路径。

---

## ✅ 解决方案(3选1)

### 方案1: 使用Git的完整路径(最快!)

Git通常安装在以下位置,直接使用完整路径:

```bash
"C:\Program Files\Git\cmd\git.exe" --version
```

如果这个命令能显示版本号,就用完整路径来push:

```bash
cd /d "d:\桌面\项目\ai-daily-report"
"C:\Program Files\Git\cmd\git.exe" push -u origin main
```

---

### 方案2: 重新打开CMD(简单!)

有时候PATH环境变量需要刷新:

1. **关闭所有CMD窗口**
2. **按 Win + R**,输入 `cmd`,回车(打开新的CMD)
3. 再试一次:
   ```bash
   git --version
   ```

如果还是不行,继续看方案3。

---

### 方案3: 手动添加Git到PATH(一劳永逸!)

#### 步骤1: 找到Git安装位置

Git通常安装在:
- `C:\Program Files\Git\cmd`
- 或 `C:\Program Files (x86)\Git\cmd`

打开文件资源管理器,检查这些目录是否存在 `git.exe`

#### 步骤2: 添加到PATH

1. **右键点击** "此电脑" → "属性"
2. 点击 **"高级系统设置"**
3. 点击 **"环境变量"**
4. 在"系统变量"中找到 **Path**,双击编辑
5. 点击 **"新建"**
6. 添加: `C:\Program Files\Git\cmd`
7. 点击 **"确定"** 保存所有窗口
8. **关闭并重新打开CMD**
9. 测试: `git --version`

---

### 方案4: 使用GitHub Desktop(最简单!⭐推荐)

如果上面的方法都太复杂,**强烈推荐使用GitHub Desktop**:

#### 优点:
- ✅ 不需要命令行
- ✅ 图形界面,操作简单
- ✅ 自动处理Git和认证
- ✅ 微软官方应用,稳定可靠

#### 配置步骤:

**第1步: 下载GitHub Desktop**
访问: https://desktop.github.com/
点击下载并安装

**第2步: 登录GitHub账号**
- 打开GitHub Desktop
- 点击 "Sign in to GitHub.com"
- 输入你的用户名 `snow122` 和密码

**第3步: 添加本地仓库**
- 点击 **File** → **Add local repository**
- 选择目录: `d:\桌面\项目\ai-daily-report`
- 如果提示 "This directory does not appear to be a Git repository"
- 点击 **"create a repository"**

**第4步: 发布到GitHub**
- 点击右上角 **"Publish repository"**
- Name: `ai-daily-report`
- 勾选 **"Keep this code private"** (私有)
- 点击 **"Publish repository"**

**完成!** 代码已推送到GitHub! 🎉

---

## 🎯 我的建议

**立即使用GitHub Desktop**,因为:
1. ✅ 不需要配置PATH
2. ✅ 不需要记命令
3. ✅ 图形界面,一目了然
4. ✅ 自动处理认证
5. ✅ 以后更新代码也超级简单

**下载安装只需5分钟!**

---

## 📋 如果使用命令行方案

### 快速测试Git路径

在新CMD中依次尝试:

```bash
where git
```

如果显示路径,说明找到了,直接用 `git` 命令即可。

如果显示 "信息: 用提供的模式无法找到文件",说明需要:
1. 重新安装Git: https://git-scm.com/download/win
2. 安装时**务必勾选** "Add Git to PATH"
3. 或者使用上面的方案4(GitHub Desktop)

---

## 💡 提示

如果你选择重新安装Git:
1. 下载: https://git-scm.com/download/win
2. 运行安装程序
3. 在安装选项中,**确保勾选**:
   - ✅ "Git from the command line and also from 3rd-party software"
   - 这会 automatically 添加Git到PATH
4. 完成安装后,重新打开CMD
5. 测试: `git --version`

---

## 🚀 下一步

无论用哪种方法,推送代码后都需要:

1. ✅ 在GitHub创建私有仓库 `ai-daily-report`
2. ✅ 推送代码
3. ✅ 配置Secrets (`FEISHU_WEBHOOK_URL`)
4. ✅ 测试Actions

**推荐使用GitHub Desktop,最简单! 🎯**
