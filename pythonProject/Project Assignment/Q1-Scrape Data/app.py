from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)


def scrape_google_image(query):
    response = requests.get(f"""https://www.google.com/search?q={query}&sxsrf=AJOqlzUuff1RXi2mm8I_OqOwT9VjfIDL7w:1676996143273&source=lnms
                            &tbm=isch&sa=X&ved=2ahUKEwiq-qK7gaf9AhXUgVYBHYReAfYQ_AUoA3oECAEQBQ&biw=1920&bih=937&dpr=1#imgrc=1th7VhSesfMJ4M""")
    soap = BeautifulSoup(response.content, 'html.parser')
    # file_path = "output.html"
    # with open(file_path, 'w', encoding='utf-8') as file:
    #     file.write(str(soap))
    # print(soap)

    img_urls = []
    images_tags = soap.find_all("img")
    del images_tags[0]
    counter = 0
    for x in images_tags:
        if counter < 10:
            counter += 1
            image_url = x["src"]
            img_urls.append({'title': 'Image '+str(counter), 'link': image_url})
        else:
            break
    return img_urls

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/search')
def search():
    query = request.args.get('query', 'Default')
    image_results = scrape_google_image(query)
    return render_template('search_results.html', image_results=image_results, query=query)
    # return render_template('search_results.html', youtube_results=youtube_results, amazon_results=amazon_results)

if __name__ == '__main__':
    app.run(host="0.0.0.0")
