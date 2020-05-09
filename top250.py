
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
import json
import os

option = Options()
option.add_argument('--disable-notifications')

browser = webdriver.Chrome('chromedriver.exe', chrome_options=option)

browser.get('https://www.imdb.com/chart/top')

print('Scraping...')

list_ = browser.find_element_by_class_name('lister-list').find_elements_by_tag_name('tr')
ids = []
imdbLinks = []
smallPoster = []
for movie in list_:
    link = movie.find_element_by_class_name('titleColumn').find_element_by_tag_name('a').get_attribute('href')
    posterLink = movie.find_element_by_class_name('posterColumn').find_element_by_tag_name('a').find_element_by_tag_name('img').get_attribute('src')
    imdbLinks.append(link)
    smallPoster.append(posterLink)
    id_ = link.split('/')[4]
    ids.append(id_)

notseen = []
seen = []

print('Done!')

for id_ in ids:

    apiKey = os.environ['TMDB_API_KEY']
    url = 'https://api.themoviedb.org/3/find/'+id_+'?api_key='+apiKey+'&language=en-US&external_source=imdb_id' 

    response = requests.get(url).json()['movie_results'][0]
    sid = response['id']
    response['imdbLink'] = imdbLinks[ids.index(id_)]
    response['smallPosterLink'] = smallPoster[ids.index(id_)]

    
    ytUrl = 'https://api.themoviedb.org/3/movie/'+str(sid)+'/videos?api_key='+apiKey+'&language=en-US'

    ytResponse = requests.get(ytUrl).json()['results']
    if len(ytResponse) != 0:
        ytLink = 'https://www.youtube.com/watch?v=' + ytResponse[0]['key']
    else:
        ytLink = 'NA'

    response['ytLink'] = ytLink

    response['index'] = ids.index(id_)

    print(response['title'])
    notseen.append(response)

jsonObject = {
    'notseen':notseen,
    'seen':seen
}

with open('list.json', 'w', encoding='utf-8') as f:
    json.dump(jsonObject, f, ensure_ascii=False, indent=4)

print('list.json Created.')

browser.quit()

