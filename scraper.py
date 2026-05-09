import requests
from bs4 import BeautifulSoup
import sqlite3

def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS content 
                 (url TEXT PRIMARY KEY, title TEXT, status TEXT)''')
    conn.commit()
    conn.close()

def scrape_tools_info():
    url = "https://ai.ealimni.info/qr/" # مثال
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # استخراج أول مقال لم يتم معالجته
    articles = soup.find_all('article')
    for art in articles:
        link = art.find('a')['href']
        title = art.find('h2').text
        
        # التحقق من قاعدة البيانات
        conn = sqlite3.connect('database.db')
        if not conn.execute("SELECT url FROM content WHERE url=?", (link,)).fetchone():
            conn.execute("INSERT INTO content VALUES (?, ?, 'pending')", (link, title))
            conn.commit()
            conn.close()
            return {"title": title, "link": link}
    return None
  
