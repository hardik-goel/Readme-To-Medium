import base64

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import os

def download_image(image_url, output_folder):
    try:
        image_response = requests.get(image_url)
        image_name = os.path.basename(urlparse(image_url).path)
        image_path = os.path.join(output_folder, image_name)
        with open(image_path, 'wb') as image_file:
            image_file.write(image_response.content)
        return image_path
    except Exception as e:
        print(f"Error downloading image: {e}")
        return None


def create_image_url(readme_content,github_url,output_folder):
    image_tags = readme_content.find_all('img')
    for image_tag in image_tags:
        image_url = urljoin(github_url, image_tag['src'])
        download_image(image_url, output_folder)
    print("Images downloaded successfully!")


def scrape_github_readme(github_url,output_folder):
    try:
        # Get repository owner and name from GitHub URL
        parts = github_url.split("/")
        owner, repo = parts[-2], parts[-1]

        # Fetch README using GitHub API
        api_url = f"https://api.github.com/repos/{owner}/{repo}/readme"
        response = requests.get(api_url)
        print(f"response:{response}")

        if response.status_code == 200:
            readme_content = response.json().get("content", "")
            print (f"readme_content::{readme_content}")
            # Decode base64-encoded content
            readme_text = base64.b64decode(readme_content).decode("utf-8")
            # Extracting and downloading images
            create_image_url(readme_content,github_url,output_folder)
            return readme_text

    except Exception as e:
        print(f"Error scraping GitHub README: {e}")


