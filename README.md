# 🤖 AI Daily Report - AI领域自动化日报系统

一个自动化的工作流系统,每天汇总AI领域的最新进展和行业论文,从技术和市场两个维度跟进AI行业发展。

## ✨ 功能特性

- 📚 **自动获取最新研究论文** - 从arXiv等平台抓取AI相关论文
- 💻 **技术动态追踪** - 收集Hugging Face、OpenAI、Google AI等技术博客
- 📈 **市场资讯监控** - 跟踪MIT Technology Review、VentureBeat等市场新闻
- 🌐 **中英双语报告** - 自动生成结构化的双语报告
- 📱 **即时推送** - 支持企业微信和钉钉机器人推送
- ⏰ **定时执行** - 每天早晨8点准时生成并发送报告
- 📄 **报告存档** - 自动保存完整报告到文件

## 📋 系统要求

- Python 3.7+
- 网络连接(用于获取数据)
- 企业微信或钉钉账号(用于接收通知)

## 🚀 快速开始

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 配置通知渠道

复制环境变量模板:

```bash
cp .env.example .env
```

编辑 `.env` 文件,配置以下任一方式:

#### 方式一: 飞书机器人 (推荐)

1. 在飞书群中添加自定义机器人
2. 获取 Webhook URL
3. 在 `.env` 中配置:
   ```
   FEISHU_WEBHOOK_URL=https://open.feishu.cn/open-apis/bot/v2/hook/YOUR_KEY
   ```

#### 方式二: 企业微信机器人

1. 在企业微信群中添加群机器人
2. 获取 Webhook URL
3. 在 `.env` 中配置:
   ```
   WEWORK_WEBHOOK_URL=https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=YOUR_KEY
   ```

#### 方式三: 钉钉机器人

1. 在钉钉群中添加自定义机器人
2. 获取 Webhook URL 和 Secret
3. 在 `.env` 中配置:
   ```
   DINGTALK_WEBHOOK_URL=https://oapi.dingtalk.com/robot/send?access_token=YOUR_TOKEN
   DINGTALK_SECRET=YOUR_SECRET
   ```

### 3. 运行程序

#### 测试运行(立即生成一次报告)

```bash
python main.py --now
```

#### 正式运行(启动定时任务)

```bash
python main.py
```

程序将在每天下午16:00(4点)自动执行。

## 📁 项目结构

```
ai-daily-report/
├── config/
│   └── sources.py          # 数据源配置
├── src/
│   ├── paper_fetcher.py    # 论文爬取模块
│   ├── news_fetcher.py     # 新闻爬取模块
│   ├── report_generator.py # 报告生成模块
│   ├── notifier.py         # 消息推送模块
│   └── scheduler.py        # 定时任务模块
├── reports/                # 报告存储目录(自动生成)
├── logs/                   # 日志目录(自动生成)
├── main.py                 # 主入口文件
├── requirements.txt        # Python依赖
├── .env.example           # 环境变量模板
└── README.md              # 说明文档
```

## 🔧 自定义配置

### 修改执行时间

编辑 `main.py`,修改启动调度器的参数:

```python
start_scheduler(hour=7, minute=30)  # 改为7:30执行
```

### 添加新的数据源

编辑 `config/sources.py`,在 `NEWS_SOURCES` 列表中添加:

```python
{
    'name': 'Your News Source',
    'url': 'https://example.com/feed',
    'type': 'rss',  # 或 'web'
    'category': 'technology'  # 或 'market'
}
```

### 调整报告内容

在 `config/sources.py` 中修改 `REPORT_CONFIG`:

```python
REPORT_CONFIG = {
    'max_papers': 15,              # 最多收录15篇论文
    'max_news_per_category': 8,    # 每类最多8条新闻
    'language': 'bilingual',       # 双语报告
    'include_abstract': True,      # 包含摘要
}
```

## 📊 报告示例

报告包含以下部分:

1. **概览** - 今日论文和资讯数量统计
2. **最新研究论文** - arXiv最新AI论文(标题、作者、摘要、链接)
3. **技术进展** - 各大技术平台的最新动态
4. **市场动态** - AI行业市场和商业资讯

## 🔍 故障排查

### 问题: 收不到推送消息

- 检查 `.env` 文件是否正确配置了 Webhook URL
- 确认企业微信/钉钉机器人已正确添加到群组
- 查看 `logs/ai_report.log` 日志文件了解详细错误

### 问题: 获取不到论文或新闻

- 检查网络连接是否正常
- 确认数据源URL是否可访问
- 查看日志文件中的错误信息

### 问题: 定时任务不执行

- 确保程序持续运行(不要关闭终端)
- 检查系统时间是否正确
- 考虑使用系统级定时任务(如cron或Task Scheduler)

## 🛠️ 高级用法

### 使用系统定时任务(推荐生产环境)

#### Linux/macOS (cron)

```bash
# 编辑crontab
crontab -e

# 添加以下行(每天8点执行)
0 8 * * * cd /path/to/ai-daily-report && python main.py --now >> logs/cron.log 2>&1
```

#### Windows (Task Scheduler)

1. 打开"任务计划程序"
2. 创建基本任务
3. 设置触发器: 每天 8:00
4. 设置操作: 启动程序 `python.exe`,参数 `main.py --now`

### 后台运行

```bash
# Linux/macOS
nohup python main.py > /dev/null 2>&1 &

# 或使用screen/tmux
screen -S ai-report
python main.py
# Ctrl+A, D 脱离会话
```

## 📝 许可证

MIT License

## 🤝 贡献

欢迎提交 Issue 和 Pull Request!

---

**Enjoy your daily AI insights! 🚀**
