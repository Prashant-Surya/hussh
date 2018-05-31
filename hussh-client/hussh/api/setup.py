import requests, json

from hussh.api.constants import BASE_URL

headers = {
    'Content-Type': 'application/json'
}

def setup(api_key, username, password):
    setup_api =  BASE_URL + "/setup"
    data = {
        'api_key': api_key,
        'username': username,
        'password': password,
    }
    #print("PRINT ", setup_api)
    response = requests.post(setup_api, json=data, headers=headers)
    return response

def share_auth(api_key, username):
    share_auth_url = BASE_URL + "/share-auth"
    data = {
        'api_key': api_key,
        'username': username,
    }
    response = requests.post(share_auth_url, json=data, headers=headers)
    response = response.json()
    return response['auth_token']

def create_hash(api_key, hash, os_user, ip):
    create_hash_url = BASE_URL + "/create-hash"
    data = {
        'api_key': api_key,
        'hash': hash,
        'os_user': os_user,
        'ip': ip,
    }
    response = requests.post(create_hash_url, json=data, headers=headers)
    return response.json()

def get_hash(hash):
    get_hash_url = BASE_URL + "/get-hash?hash={0}".format(hash)
    response = requests.get(get_hash_url, headers=headers)
    return response.json()