import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from pathlib import Path

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

def save_image(url, path):
    if url.startswith('data:'):
        return
    response = requests.get(url, stream=True)
    filename = Path(url).name
    with open(os.path.join(path, filename), 'wb') as out_file:
        for chunk in response.iter_content(chunk_size=128):
            out_file.write(chunk)

def write_tree(link, depth, file):
    indentation = '  ' * depth
    file.write(f'{indentation}{link}\n')
    print(indentation+link)

def scrape(url, domain, visited_links, path, file, depth=0):
    links = get_links(url, domain, visited_links)
    for link in links:
        write_tree(link, depth, file)
        images = get_images(link)
        for image in images:
            save_image(image, path)
        scrape(link, domain, visited_links, path, file, depth + 1)
        
def main():
    domain = url
    visited_links = set()
    path = os.path.join(os.path.expanduser("~"), "Desktop", "images")
    os.makedirs(path, exist_ok=True)
    tree_file_path = os.path.join(path, "link_tree.txt")
    with open(tree_file_path, "w") as tree_file:
        scrape(url, domain, visited_links, path, tree_file)

if __name__ == '__main__':
    main()