import os, requests, json
from PIL import Image, ImageDraw, ImageFont

TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHANNEL_ID"]

with open("inventory.json", 'r') as f: data = json.load(f)
trend = data[-1]['trend']

# 1. Draw Image
img = Image.new('RGB', (1080, 1080), (10,10,10))
draw = ImageDraw.Draw(img)
draw.rectangle([20,20,1060,1060], outline=(0,255,100), width=15)
try: font = ImageFont.load_default()
except: pass
draw.text((100,500), f"TREND ALERT:\n{trend.upper()}", fill="white")
draw.text((100,800), "LINK IN BIO", fill=(0,255,100))
img.save("post.png")

# 2. Send to Channel
url = f"https://api.telegram.org/bot{TOKEN}/sendPhoto"
requests.post(url, data={'chat_id': CHAT_ID, 'caption': f"🔥 {trend} is trending!"}, files={'photo': open("post.png", 'rb')})

