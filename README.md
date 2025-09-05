# Emoji Hub Adapter

## Description

Minimal web app to browse emojis. Backend fetches data from EmojiHub API.
Frontend is HTML + JS.

## Run with Docker

```bash
docker build -t emoji_hub_adapter .
docker run -d --name emoji_hub_adapter -p 8000:8000 -v c:\_work\_nfactorial\ai_engineer_course\test_task\emoji-hub-adapter\backend\app:/app/app -v c:\_work\_nfactorial\ai_engineer_course\test_task\emoji-hub-adapter\frontend:/app/frontend emoji_hub_adapter
```
