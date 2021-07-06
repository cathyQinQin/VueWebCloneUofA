from selenium import webdriver
import json
import pathlib
from datetime import date
from bs4 import BeautifulSoup
from flask import Flask
from flask import jsonify
app = Flask(__name__)

@app.route("/")
def get_data():
    def fetch_webpage():
        path = 'chromedriver.exe'
        driver = webdriver.Chrome(executable_path = path)
        driver.set_window_position(0, 0)
        driver.set_window_size(1920, 1080)
        driver.get('https://www.ualberta.ca/index.html')
        with open("cache.html", 'w', encoding='utf-8') as f:
            f.write(driver.page_source)
        driver.quit()

    def get_text(tag,css):
        result = tag.select(css)
        if not len(result):
            return None
        contents = result[0].contents
        if not len(contents):
            return None
        return contents[0]    

    path = pathlib.Path('cache.html')
    if not (path.exists() and date.fromtimestamp(path.stat().st_ctime) == date.today()):
        fetch_webpage()

    with open("cache.html", 'r', encoding='utf-8') as f:
        page = f.read()

    soup = BeautifulSoup(page, 'html.parser')
    columns = []
    for col in soup.select('.latest-stories>.story-list>.story-column'):
        stories = []
        for story_tag in col.select("div.story"):
            story = {}
            story["cover_image"] = story_tag.select("img.story-image")[0]["src"]
            story["cover_logo"] = story_tag.select(".story-image-wrapper>.container>img")[0]["src"]
            story["category"] = get_text(story_tag,"div.story-category")
            story["title_link"] = story_tag.select(".story a.stretched-link")[0]["href"]
            story["title_text"] = story_tag.select(".story a.stretched-link")[0].string
            story["story_teaser"] =get_text(story_tag,"div.story-teaser")
            story["story_date"] =story_tag.select("div.story-date")[0].string
            stories.append(story)
        columns.append(stories)
    with open('data.json', 'w') as outfile:
        json.dump(columns, outfile)
    return jsonify(columns)


