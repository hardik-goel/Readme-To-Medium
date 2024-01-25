TOKEN = "<Your Token>"

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.5",
    "Connection": "keep-alive",
    "Host": "api.medium.com",
    "Authorization": "Bearer {}".format(TOKEN),
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0"
}

readme_path = "https://github.com/hardik-goel/Audio-Summariser/blob/master/README.md"
output_file_path_for_images = "resources/images"
title = "CustomerEchoEase—an advanced solution offering streamlined text summarization, sentiment analysis, " \
        "and impactful visualizations "
tags = "sentiment,summariser"
pub = "draft"
MODEL_NAME = "gemini-pro"
API_KEY = "<Your API Key>"
