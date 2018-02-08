import requests
import base64

OAUTH_URL = 'https://www.bungie.net/platform/app/oauth/token/'


class OAuth:

    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret

    def get_public_access_token(self, code):
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        payload = {'grant_type': 'authorization_code', 'client_id': self.client_id, 'code': code}
        r = requests.post(OAUTH_URL, data=payload, headers=headers)
        return r.json()

    def get_confidential_access_token(self, code):
        headers = {'Content-Type': 'application/x-www-form-urlencoded',
                   'Authorization': 'Basic {}'.format(base64.b64encode(self.client_id+':'+self.client_secret))}
        payload = {'grant_type': 'authorization_code', 'code': code}
        r = requests.post(OAUTH_URL, data=payload, headers=headers)
        return r.json()

    def refresh_token(self, refresh_token):
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        payload = {'grant_type': 'refresh_token',
                   'client_id': self.client_id,
                   'client_secret': self.client_secret,
                   'refresh_token': refresh_token}
        r = requests.post(OAUTH_URL, data=payload, headers=headers)
        return r.json()

