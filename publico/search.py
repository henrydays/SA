from __future__ import annotations
import json
from typing import Union
from urllib.parse import urlparse
import requests
from lxml import html
 
class Hit:
    def __init__(self, title, date, desc):
        self.title = title
        self.date = date
        self.desc = desc
    def __str__(self):
        return "[{title}, {date}, {desc}]"
        

def search(tag, num_pages):
    tag = tag.replace(" ", "-").lower()
    
    page_number = 1

    collected_news = []
    
    while (
        response := requests.get(
            f"https://www.publico.pt/api/list/{tag}?page={page_number}"
        ).text
    ) != "[]" and page_number < num_pages:

        data = json.loads(response)

        for hit in data:
            collected_news.append(Hit(hit["titulo"],hit["data"],hit["descricao"]))
     
        page_number += 1

    return collected_news
