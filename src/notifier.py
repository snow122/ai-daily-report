"""
消息推送模块
支持飞书、企业微信和钉钉机器人推送
"""

import requests
import hmac
import hashlib
import base64
import time
import json
import logging
import os
from dotenv import load_dotenv
from typing import Optional

logger = logging.getLogger(__name__)

# 加载环境变量
load_dotenv()


class FeishuNotifier:
    """飞书机器人推送"""

    def __init__(self, webhook_url: str = None):
        self.webhook_url = webhook_url or os.getenv('FEISHU_WEBHOOK_URL')

        if not self.webhook_url:
            logger.warning("飞书 Webhook URL 未配置")

    def send_text(self, content: str) -> bool:
        """
        发送文本消息

        Args:
            content: 消息内容

        Returns:
            bool: 是否发送成功
        """
        if not self.webhook_url:
            logger.error("飞书 Webhook URL 未配置")
            return False

        try:
            data = {
                "msg_type": "text",
                "content": {
                    "text": content
                }
            }

            response = requests.post(
                self.webhook_url,
                json=data,
                headers={'Content-Type': 'application/json'},
                timeout=10
            )
            response.raise_for_status()

            result = response.json()
            if result.get('StatusCode') == 0 or result.get('code') == 0:
                logger.info("飞书消息发送成功")
                return True
            else:
                logger.error(f"飞书消息发送失败: {result}")
                return False

        except Exception as e:
            logger.error(f"发送飞书消息异常: {str(e)}")
            return False

    def send_post(self, title: str, content_items: list) -> bool:
        """
        发送富文本消息(POST类型)

        Args:
            title: 消息标题
            content_items: 内容项列表

        Returns:
            bool: 是否发送成功
        """
        if not self.webhook_url:
            logger.error("飞书 Webhook URL 未配置")
            return False

        try:
            zh_cn_content = {
                "title": title,
                "content": [content_items]
            }

            data = {
                "msg_type": "post",
                "content": {
                    "post": {
                        "zh_cn": zh_cn_content
                    }
                }
            }

            response = requests.post(
                self.webhook_url,
                json=data,
                headers={'Content-Type': 'application/json'},
                timeout=10
            )
            response.raise_for_status()

            result = response.json()
            if result.get('StatusCode') == 0 or result.get('code') == 0:
                logger.info("飞书富文本消息发送成功")
                return True
            else:
                logger.error(f"飞书富文本消息发送失败: {result}")
                return False

        except Exception as e:
            logger.error(f"发送飞书富文本消息异常: {str(e)}")
            return False

    def send_card(self, title: str, content: str, color: str = "blue") -> bool:
        """
        发送卡片消息(推荐,支持Markdown)

        Args:
            title: 卡片标题
            content: Markdown格式的内容
            color: 主题颜色 (blue/green/orange/red/purple)

        Returns:
            bool: 是否发送成功
        """
        if not self.webhook_url:
            logger.error("飞书 Webhook URL 未配置")
            return False

        try:
            data = {
                "msg_type": "interactive",
                "card": {
                    "header": {
                        "title": {
                            "tag": "plain_text",
                            "content": title
                        },
                        "template": color
                    },
                    "elements": [
                        {
                            "tag": "div",
                            "text": {
                                "tag": "lark_md",
                                "content": content
                            }
                        }
                    ]
                }
            }

            response = requests.post(
                self.webhook_url,
                json=data,
                headers={'Content-Type': 'application/json'},
                timeout=10
            )
            response.raise_for_status()

            result = response.json()
            if result.get('StatusCode') == 0 or result.get('code') == 0:
                logger.info("飞书卡片消息发送成功")
                return True
            else:
                logger.error(f"飞书卡片消息发送失败: {result}")
                return False

        except Exception as e:
            logger.error(f"发送飞书卡片消息异常: {str(e)}")
            return False


class WeWorkNotifier:
    """企业微信机器人推送"""

    def __init__(self, webhook_url: str = None):
        self.webhook_url = webhook_url or os.getenv('WEWORK_WEBHOOK_URL')

        if not self.webhook_url:
            logger.warning("企业微信 Webhook URL 未配置")

    def send_text(self, content: str, mentioned_list: list = None) -> bool:
        """
        发送文本消息

        Args:
            content: 消息内容
            mentioned_list: 需要@的成员列表

        Returns:
            bool: 是否发送成功
        """
        if not self.webhook_url:
            logger.error("企业微信 Webhook URL 未配置")
            return False

        try:
            data = {
                "msgtype": "text",
                "text": {
                    "content": content,
                    "mentioned_list": mentioned_list or []
                }
            }

            response = requests.post(
                self.webhook_url,
                json=data,
                headers={'Content-Type': 'application/json'},
                timeout=10
            )
            response.raise_for_status()

            result = response.json()
            if result.get('errcode') == 0:
                logger.info("企业微信消息发送成功")
                return True
            else:
                logger.error(f"企业微信消息发送失败: {result}")
                return False

        except Exception as e:
            logger.error(f"发送企业微信消息异常: {str(e)}")
            return False

    def send_markdown(self, content: str) -> bool:
        """
        发送Markdown消息

        Args:
            content: Markdown格式的消息内容

        Returns:
            bool: 是否发送成功
        """
        if not self.webhook_url:
            logger.error("企业微信 Webhook URL 未配置")
            return False

        try:
            data = {
                "msgtype": "markdown",
                "markdown": {
                    "content": content
                }
            }

            response = requests.post(
                self.webhook_url,
                json=data,
                headers={'Content-Type': 'application/json'},
                timeout=10
            )
            response.raise_for_status()

            result = response.json()
            if result.get('errcode') == 0:
                logger.info("企业微信Markdown消息发送成功")
                return True
            else:
                logger.error(f"企业微信Markdown消息发送失败: {result}")
                return False

        except Exception as e:
            logger.error(f"发送企业微信Markdown消息异常: {str(e)}")
            return False


class DingTalkNotifier:
    """钉钉机器人推送"""

    def __init__(self, webhook_url: str = None, secret: str = None):
        self.webhook_url = webhook_url or os.getenv('DINGTALK_WEBHOOK_URL')
        self.secret = secret or os.getenv('DINGTALK_SECRET')

        if not self.webhook_url:
            logger.warning("钉钉 Webhook URL 未配置")

    def _generate_sign(self) -> tuple:
        """
        生成钉钉签名

        Returns:
            tuple: (timestamp, sign)
        """
        timestamp = str(round(time.time() * 1000))
        secret_enc = self.secret.encode('utf-8')
        string_to_sign = f'{timestamp}\n{self.secret}'
        string_to_sign_enc = string_to_sign.encode('utf-8')

        hmac_code = hmac.new(
            secret_enc,
            string_to_sign_enc,
            digestmod=hashlib.sha256
        ).digest()

        sign = base64.b64encode(hmac_code).decode('utf-8')

        return timestamp, sign

    def send_text(self, content: str, at_mobiles: list = None) -> bool:
        """
        发送文本消息

        Args:
            content: 消息内容
            at_mobiles: 需要@的手机号列表

        Returns:
            bool: 是否发送成功
        """
        if not self.webhook_url:
            logger.error("钉钉 Webhook URL 未配置")
            return False

        try:
            # 构建URL(如果需要签名)
            url = self.webhook_url
            if self.secret:
                timestamp, sign = self._generate_sign()
                url = f"{self.webhook_url}&timestamp={timestamp}&sign={sign}"

            data = {
                "msgtype": "text",
                "text": {
                    "content": content
                },
                "at": {
                    "atMobiles": at_mobiles or [],
                    "isAtAll": False
                }
            }

            response = requests.post(
                url,
                json=data,
                headers={'Content-Type': 'application/json'},
                timeout=10
            )
            response.raise_for_status()

            result = response.json()
            if result.get('errcode') == 0:
                logger.info("钉钉消息发送成功")
                return True
            else:
                logger.error(f"钉钉消息发送失败: {result}")
                return False

        except Exception as e:
            logger.error(f"发送钉钉消息异常: {str(e)}")
            return False

    def send_markdown(self, title: str, content: str, at_mobiles: list = None) -> bool:
        """
        发送Markdown消息

        Args:
            title: 消息标题
            content: Markdown格式的消息内容
            at_mobiles: 需要@的手机号列表

        Returns:
            bool: 是否发送成功
        """
        if not self.webhook_url:
            logger.error("钉钉 Webhook URL 未配置")
            return False

        try:
            # 构建URL(如果需要签名)
            url = self.webhook_url
            if self.secret:
                timestamp, sign = self._generate_sign()
                url = f"{self.webhook_url}&timestamp={timestamp}&sign={sign}"

            data = {
                "msgtype": "markdown",
                "markdown": {
                    "title": title,
                    "text": content
                },
                "at": {
                    "atMobiles": at_mobiles or [],
                    "isAtAll": False
                }
            }

            response = requests.post(
                url,
                json=data,
                headers={'Content-Type': 'application/json'},
                timeout=10
            )
            response.raise_for_status()

            result = response.json()
            if result.get('errcode') == 0:
                logger.info("钉钉Markdown消息发送成功")
                return True
            else:
                logger.error(f"钉钉Markdown消息发送失败: {result}")
                return False

        except Exception as e:
            logger.error(f"发送钉钉Markdown消息异常: {str(e)}")
            return False


def send_notification(summary: str, report_file: str = None) -> bool:
    """
    发送通知(自动选择可用的推送方式)

    Args:
        summary: 消息摘要
        report_file: 报告文件路径(可选)

    Returns:
        bool: 是否发送成功
    """
    success = False

    # 优先尝试飞书
    feishu_url = os.getenv('FEISHU_WEBHOOK_URL')
    if feishu_url:
        notifier = FeishuNotifier(feishu_url)
        # 使用卡片消息发送,支持Markdown格式
        if notifier.send_card("🤖 AI Daily Report", summary, "blue"):
            success = True
            logger.info("已通过飞书发送通知")

    # 尝试企业微信
    wework_url = os.getenv('WEWORK_WEBHOOK_URL')
    if wework_url and not success:
        notifier = WeWorkNotifier(wework_url)
        if notifier.send_markdown(summary):
            success = True
            logger.info("已通过企业微信发送通知")

    # 尝试钉钉
    dingtalk_url = os.getenv('DINGTALK_WEBHOOK_URL')
    if dingtalk_url and not success:
        notifier = DingTalkNotifier(dingtalk_url, os.getenv('DINGTALK_SECRET'))
        if notifier.send_markdown("AI Daily Report", summary):
            success = True
            logger.info("已通过钉钉发送通知")

    if not success:
        logger.warning("所有推送方式均失败或未配置")

    return success


if __name__ == '__main__':
    # 测试代码
    logging.basicConfig(level=logging.INFO)

    test_summary = """🤖 AI Daily Report - 2026-04-27

📚 Latest Papers / 最新论文: 5 篇
  1. GPT-5 Technical Report
  2. Advances in Computer Vision...
  3. New Breakthrough in NLP...

💻 Tech Updates / 技术动态: 3 条
📈 Market News / 市场资讯: 4 条

完整报告已生成,请查看附件或链接。
"""

    send_notification(test_summary)
