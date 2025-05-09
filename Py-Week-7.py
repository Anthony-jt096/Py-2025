import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import time
from datetime import datetime
#Ex-1


#url = "https://www.w3schools.com/python/"
#try:
#    response = requests.get(url)
#    response.raise_for_status()  
#    soup = BeautifulSoup(response.text, "html.parser")
#    headline = soup.find("h1")
#    if headline:
#        print(headline.get_text(strip=True))
#    else:
#        print("No headline found.")
#except requests.RequestException as e:
#    print(f"Request failed: {e}")

           
#Ex-2
'''


url = "https://www.timeanddate.com/weather/usa/oklahoma-city"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# The temperature is inside a div with id="qlook"
temp_div = soup.find("div", id="qlook")
if temp_div:
    temp = temp_div.find("div", class_="h2")
    if temp:
        print("Temperature in Oklahoma City:", temp.text.strip())
    else:
        print("Temperature not found.")
else:
    print("Weather info not found.")
'''

#Ex-3
'''
url = "https://www.thewhiskyexchange.com/c/35/japanese-whisky"
driver = webdriver.Chrome()  
driver.get(url)
time.sleep(1)  

soup = BeautifulSoup(driver.page_source, "html.parser")
products = soup.find_all("li", class_="product-grid__item")

for product in products:
    name_tag = product.find("p", class_="product-card__name")
    name = name_tag.text.strip() if name_tag else "N/A"
    print("Spirit:", name)
    print("---")
'''

#Ex-4
'''
base_url = "https://quotes.toscrape.com"
url = "/"
while url:
    response = requests.get(base_url + url)
    soup = BeautifulSoup(response.text, "html.parser")
    quotes = soup.find_all("div", class_="quote")
    for quote in quotes:
        text = quote.find("span", class_="text").text.strip()
        author = quote.find("small", class_="author").text.strip()
        tags = [tag.text for tag in quote.find_all("a", class_="tag")]
        print(f"Quote: {text}")
        print(f"Author: {author}")
        print(f"Tags: {', '.join(tags)}")
        print("-" * 100)
    next_btn = soup.find("li", class_="next")
    url = next_btn.a["href"] if next_btn else None
'''

#Ex-5
'''
print("Top five movies:")


url = "https://www.imdb.com/chart/top"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

movies = soup.select("td.titleColumn")[:5]

for i, movie in enumerate(movies, 1):
    title = movie.a.text
    year = movie.span.text.strip("()")
    movie_url = "https://www.imdb.com" + movie.a["href"]

  
    movie_response = requests.get(movie_url)
    movie_soup = BeautifulSoup(movie_response.text, "html.parser")

   
    director_tag = movie_soup.find("a", attrs={"data-testid": "title-pc-principal-credit"})
    director = director_tag.text if director_tag else "N/A"

   
    actors = []
    actor_tags = movie_soup.select('a[data-testid="title-cast-item__actor"]')
    for actor_tag in actor_tags[:3]:
        actors.append(actor_tag.text)
    actors_str = ", ".join(actors) if actors else "N/A"

    print(f"\n{i}. {title} ({year})")
    print(f"Director: {director}")
    print(f"Main Actors: {actors_str}")
'''


#Ex-6

'''

def get_today_soccer_scores():
    today = datetime.now().strftime("%Y-%m-%d")
    url = f"https://www.thesportsdb.com/api/v1/json/1/eventsday.php?d={today}&s=Soccer"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
    except Exception as e:
        print(f"Failed to fetch data: {e}")
        return

    print("Today's Soccer Scores:")
    events = data.get("events")
    if events:
        for event in events[:5]:
            home = event.get("strHomeTeam", "Unknown")
            away = event.get("strAwayTeam", "Unknown")
            home_score = event.get("intHomeScore")
            away_score = event.get("intAwayScore")
            home_score = home_score if home_score is not None else "N/A"
            away_score = away_score if away_score is not None else "N/A"
            print(f"{home} {home_score} - {away_score} {away}")
    else:
        print("No events found.")

get_today_soccer_scores()
'''



































