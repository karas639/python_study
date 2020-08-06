import requests

def get_access_token():
    global a
    tistory_url = 'https://www.tistory.com'
    access_token = None

    login_url = '{}/auth/login'.format(tistory_url)
    print(login_url)
    login_data = {
        'loginId':'karas639@gmail.com',
        'password':'dwkimsec135@$^',
        'redirectUrI':'https://www.tistory.com/oauth/authorize?client_id=a1f11d9eb54d53fcdb19da6026fa0fa7&redirect_uri=https://kkamagistory.tistory.com&response_type=token'
    }
    a = requests.post(login_url, login_data)
    return a.url