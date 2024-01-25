def scrape_github_readme(github_url, output_folder):
    response = requests.get(github_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extracting content from the README
    readme_content = soup.find(id='readme')
    print(f"readme_content:: {readme_content}")
    if readme_content:
        readme_text = readme_content.get_text()
        print (f"readme_text:: {readme_text}")
        # with open(os.path.join(output_folder, 'README.md'), 'w', encoding='utf-8') as readme_file:
        #     readme_file.write(readme_text)
        # print("README.md file written successfully!")

        # Extracting and downloading images
        image_tags = readme_content.find_all('img')
        for image_tag in image_tags:
            image_url = urljoin(github_url, image_tag['src'])
            download_image(image_url, output_folder)
        print("Images downloaded successfully!")
    return readme_text