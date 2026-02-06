import feedparser, json, time, random, os

TRENDS_URL = "https://trends.google.com/trends/trendingsearches/daily/rss?geo=AU"
FILE = "inventory.json"

def run():
    time.sleep(random.uniform(1, 5)) # Human jitter
    feed = feedparser.parse(TRENDS_URL)
    if not feed.entries: return

    try: 
        with open(FILE, 'r') as f: data = json.load(f)
    except: data = []

    # Add new trends
    for entry in feed.entries[:3]:
        if not any(d['trend'] == entry.title for d in data):
            data.append({
                "id": str(int(time.time())), 
                "trend": entry.title,
                "product": f"The {entry.title} Guide"
            })

    with open(FILE, 'w') as f: json.dump(data[-20:], f)

if __name__ == "__main__": run()

