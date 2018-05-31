import requests

from hussh.api.constants import file_url

def upload_file(auth_token, content, file_id):
    headers = {
        'Content-Type': 'text/plain; charset=utf-8',
        'Authorization': 'Bearer ' + auth_token,
        #'X-Hasura-Role': 'admin',
    }
    url = file_url.format(file_id=file_id)
    return requests.post(url, data=content, headers=headers)

def download_file(auth_token, file_id):
    headers = {
        'Authorization': 'Bearer ' + auth_token,
    }
    url = file_url.format(file_id=file_id)
    data = requests.get(url, headers=headers)
    return data.content.decode("utf-8")