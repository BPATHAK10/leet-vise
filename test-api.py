import requests
from dotenv import load_dotenv
import os

load_dotenv()

NOTION_API_TOKEN = os.getenv("NOTION_API_TOKEN")
NOTION_DATABASE_ID = os.getenv("NOTION_DATABASE_ID")

url = f"https://api.notion.com/v1/databases/{NOTION_DATABASE_ID}/query"
headers = {
    "Authorization": f"Bearer {NOTION_API_TOKEN}",
    "Notion-Version": "2022-06-28",
    "Content-Type": "application/json",
}

response = requests.post(url, headers=headers)

res = response.json()

# write the response to a file for inspection
with open("notion_response.json", "w", encoding="utf-8") as f:
    import json
    json.dump(res, f, indent=2)
