from dataclasses import dataclass
import requests
from src.config import NOTION_API_TOKEN, NOTION_DATABASE_ID

# Create a dataclass for question
@dataclass
class Question:
    id: str
    title: str
    url: str
    tag: str
    hint: str
    level: str
    done: bool
    must_know: bool
    blind_75: bool
    memorize: bool

class NotionImporter:
    NOTION_VERSION = "2022-06-28"
    API_URL = f"https://api.notion.com/v1/databases/{NOTION_DATABASE_ID}/query"

    def __init__(self):
        self.headers = {
            "Authorization": f"Bearer {NOTION_API_TOKEN}",
            "Notion-Version": self.NOTION_VERSION,
            "Content-Type": "application/json",
        }

    def fetch_from_api(self):
        data = []

        start_cursor = None

        while True:
            payload = {"page_size": 100}
            if start_cursor:
                payload["start_cursor"] = start_cursor

            try:
                response = requests.post(self.API_URL, headers=self.headers, json=payload)
                response.raise_for_status()
                res_json = response.json()
            except requests.RequestException as e:
                print(f"Error fetching data from Notion API: {e}")
                return []

            data.extend(res_json.get("results", []))
            if res_json.get("has_more"):
                start_cursor = res_json.get("next_cursor")
            else:
                break
            
        if not data:
            print("No data found in Notion database.")
            return []
        
        print(f"Fetched {len(data)} items from Notion database.")

        return self._transform(data)

    def _transform(self, data):
        questions = []
        
        for page in data:
            props = page.get("properties", {})

            # skip the page if not done
            if not props["Done"]["checkbox"]:
                continue

            # Extract fields with safe defaults
            title = props["Question"]["title"][0]["plain_text"]
            url = props["Question Link"]["url"]
            tag = props["Tag"]["multi_select"][0]["name"]
            hint = props["Remark"]["rich_text"][0]["plain_text"] if props["Remark"]["rich_text"] else ""
            level = props["Level"]["select"]["name"]
            done = props["Done"]["checkbox"]
            must_know = props["Must-know"]["checkbox"]
            blind_75 = props["Blind-75"]["checkbox"]
            memorize = props["Memorize"]["checkbox"]

            question: Question = {
                "id": page["id"],
                "title": title,
                "url": url,
                "tag": tag,
                "hint": hint,
                "level": level,
                "done": done,
                "must_know": must_know,
                "blind_75": blind_75,
                "memorize": memorize,
            }   

            questions.append(question)

        print(f"Transformed {len(questions)} questions from Notion api data.")

        return questions
