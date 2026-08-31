"""
Telegram Bot Observer for $PLC mentions.
Monitors GitHub, Twitter, Reddit for $PLC activity.
"""

import requests
import time
import json
from datetime import datetime
from typing import List, Dict, Any

# ===== Configuration =====
# Получи токен у @BotFather в Telegram
BOT_TOKEN = "ТВОЙ_ТОКЕН_ОТ_BOTFATHER"
CHAT_ID = "ID_ТВОЕГО_ЧАТА"  # Можно узнать через @userinfobot

# ===== Telegram API =====

def send_message(text: str, chat_id: str = CHAT_ID) -> bool:
    """Send a message to Telegram chat."""
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "Markdown"
    }
    try:
        response = requests.post(url, json=payload, timeout=10)
        return response.status_code == 200
    except Exception as e:
        print(f"Error sending message: {e}")
        return False


def send_mention_update(platform: str, url: str, context: str = "") -> None:
    """Send a formatted update about a $PLC mention."""
    message = f"""
🔍 *New $PLC Mention Detected*

📱 *Platform:* {platform}
🔗 *Link:* {url}
📝 *Context:* {context if context else "N/A"}
🕐 *Time:* {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}

---
_Placeholder Standard ($PLC) Monitor_
"""
    send_message(message)


# ===== Search Functions =====

def check_github() -> List[Dict[str, str]]:
    """Check GitHub for $PLC mentions."""
    results = []
    try:
        # Поиск на GitHub через public API
        url = "https://api.github.com/search/repositories"
        params = {
            "q": "$PLC placeholder standard",
            "sort": "updated",
            "order": "desc"
        }
        response = requests.get(url, params=params, timeout=10)
        if response.status_code == 200:
            data = response.json()
            for item in data.get("items", [])[:3]:
                results.append({
                    "platform": "GitHub",
                    "url": item.get("html_url", ""),
                    "context": f"{item.get('name', '')} - {item.get('description', '')[:50]}"
                })
    except Exception as e:
        print(f"GitHub search error: {e}")
    return results


def check_reddit() -> List[Dict[str, str]]:
    """Check Reddit for $PLC mentions."""
    results = []
    try:
        # Поиск на Reddit
        url = "https://www.reddit.com/search.json"
        params = {
            "q": "$PLC",
            "sort": "new",
            "limit": 3
        }
        response = requests.get(url, params=params, timeout=10)
        if response.status_code == 200:
            data = response.json()
            for child in data.get("data", {}).get("children", []):
                post = child.get("data", {})
                results.append({
                    "platform": "Reddit",
                    "url": f"https://reddit.com{post.get('permalink', '')}",
                    "context": post.get("title", "")[:50]
                })
    except Exception as e:
        print(f"Reddit search error: {e}")
    return results


def check_twitter() -> List[Dict[str, str]]:
    """Check Twitter for $PLC mentions."""
    # Примечание: Twitter API v2 требует OAuth 2.0
    # Для простоты используем публичный поиск через альтернативный сервис
    results = []
    try:
        # Используем анонимный поиск через RSS-агрегатор
        url = "https://nitter.net/search.json"
        params = {"query": "$PLC", "f": "tweets"}
        # Nitter может быть доступен по разным адресам
        # Если не работает, просто пропускаем
    except Exception as e:
        print(f"Twitter search error: {e}")
    return results


def check_news() -> List[Dict[str, str]]:
    """Check news aggregators for $PLC mentions."""
    results = []
    try:
        # Используем Google News RSS
        url = "https://news.google.com/rss/search"
        params = {"q": "$PLC"}
        response = requests.get(url, params=params, timeout=10)
        if response.status_code == 200:
            # Парсинг RSS оставляем для следующей версии
            pass
    except Exception as e:
        print(f"News search error: {e}")
    return results


# ===== Main Loop =====

def monitor_mentions() -> None:
    """Main monitoring loop."""
    print(f"🔍 $PLC Monitor Started")
    print(f"   Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}")
    print("   Checking for new mentions...")
    print("=" * 60)
    
    checks = [
        ("GitHub", check_github),
        ("Reddit", check_reddit)
    ]
    
    for platform_name, check_func in checks:
        try:
            results = check_func()
            for result in results:
                send_mention_update(
                    platform=result.get("platform", platform_name),
                    url=result.get("url", ""),
                    context=result.get("context", "")
                )
        except Exception as e:
            print(f"Error checking {platform_name}: {e}")


def run_monitor(interval_minutes: int = 60) -> None:
    """Run the monitor with specified interval."""
    print(f"🕐 Running every {interval_minutes} minutes")
    
    while True:
        try:
            monitor_mentions()
        except Exception as e:
            print(f"Monitor error: {e}")
            send_message(f"⚠️ Bot error: {e}")
        
        time.sleep(interval_minutes * 60)


# ===== Entry Point =====

if __name__ == "__main__":
    # Отправляем приветствие при запуске
    send_message("🤖 $PLC Monitor started! I'll track mentions of Placeholder Standard.")
    
    # Запускаем мониторинг (каждый час)
    run_monitor(interval_minutes=60)
