"""
All news sources used in the project are defined here.
"""

KNOWN_NEWS_SOURCES = {
    "The Hindu": {
        "home": "https://www.thehindu.com/",
        "india": "https://www.thehindu.com/news/national/",
        "page1": "",
        "pages": "https://www.thehindu.com/news/national/?page={}"
    },
    "NDTV": {
        "home": "https://www.ndtv.com/",
        "india": "https://www.ndtv.com/india",
        "page1": "",
        "pages": "https://www.ndtv.com/india/page-{}"
    },
    "Times of India": {
        "home": "https://timesofindia.indiatimes.com/",
        "india": "https://timesofindia.indiatimes.com/india/",
        "page1": "https://timesofindia.indiatimes.com/india/",
        "pages": "https://timesofindia.indiatimes.com/india/{}"
    },
}