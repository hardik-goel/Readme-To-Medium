import requests
import argparse
import subprocess

from conf.configs import headers, pub, title, tags


def read_file(filepath):
    f = open(filepath, 'r')
    content = f.read()
    if not f.closed: f.close()

    if filepath.find('.') < 0:
        file_ext = ""
    else:
        file_ext = filepath[filepath.find(".")+1:]
    if file_ext == "md": file_ext = "markdown"
    return {"content": content, "contentFormat": file_ext}

def prep_data(**kwargs):
    data = {
        "title": kwargs.get('title', ''),
    }
    data = {**data, **read_file(kwargs.get('filepath', ''))}
    if kwargs.get('tags'):
        data['tags'] = [t.strip() for t in kwargs['tags'].split(',')]
    data['publishStatus'] = 'draft'
    if kwargs.get('pub'):
        data['publishStatus'] = kwargs['pub']
    return data

def get_author_id():
    response = requests.get("https://api.medium.com/v1/me", headers=headers, params={"Authorization": "Bearer {}".format(TOKEN)})
    if response.status_code == 200:
        return response.json()['data']['id']
    return None

def post_article(data):
    author_id = get_author_id()
    url = "https://api.medium.com/v1/users/{}/posts".format(author_id)
    response = requests.post(url, headers=headers, data=data)
    if response.status_code in [200, 201]:
        response_json = response.json()
        # get URL of uploaded post
        pub_url = response_json["data"]["url"]
        return pub_url
    return None

def copy_to_clipboard(to_copy):
    if not to_copy: return
    process = subprocess.Popen('pbcopy', env={'LANG': 'en_US.UTF-8'}, stdin=subprocess.PIPE)
    process.communicate(to_copy.encode('utf-8'))


def execute(filepath):
    data = prep_data(filepath=filepath,title=title,tags=tags,pub=pub)
    post_url = post_article(data)
    copy_to_clipboard(post_url) # copy url to clipboard for further usecases
    print(post_url)
    return post_url