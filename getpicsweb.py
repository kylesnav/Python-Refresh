from flask import Flask, render_template_string, url_for
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

url = "https://blueskyweb.xyz/"

def get_links(url, domain, visited_links):
    links = []
    response = requests.get(url)
    content_type = response.headers.get('Content-Type', '').lower()
    parser = 'lxml-xml' if 'xml' in content_type else 'html.parser'
    soup = BeautifulSoup(response.text, parser)
    for a in soup.find_all('a', href=True):
        link = urljoin(domain, a['href'])
        if link.startswith(domain) and link not in visited_links:
            links.append(link)
            visited_links.add(link)
    return links

def get_images(url):
    images = []
    response = requests.get(url)
    content_type = response.headers.get('Content-Type', '').lower()
    parser = 'lxml-xml' if 'xml' in content_type else 'html.parser'
    soup = BeautifulSoup(response.text, parser)
    img_tags = soup.find_all('img')
    for img_tag in img_tags:
        img_url = urljoin(url, img_tag.get('src'))
        images.append(img_url)
    return images

def scrape(url, domain, visited_links):
    links = get_links(url, domain, visited_links)
    images = set()
    for link in links:
        link_images = get_images(link)
        images.update(link_images)
        images.update(scrape(link, domain, visited_links))
    return list(images)

def main():
    domain = url
    visited_links = set()
    return scrape(url, domain, visited_links)

app = Flask(__name__)

@app.route('/')
def landing_page():
    images = main()
    template = """
    <!DOCTYPE html>
    <html>
        <head>
            <title>Images</title>
            <style>
                .image-gallery {
                    display: grid;
                    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
                    grid-gap: 10px;
                    padding: 10px;
                }
                .image-gallery img {
                    width: 100%;
                    height: auto;
                    object-fit: cover;
                }
            </style>
        </head>
        <body>
            <div class="image-gallery">
                {% for image in images %}
                    <img src="{{ image }}">
                {% endfor %}
            </div>
        </body>
    </html>"""
    return render_template_string(template, images=images)

if __name__ == '__main__':
    app.run()
