import requests
from repository import Repository

class GitHub():

    API_ROOT = 'https://api.github.com'

    def __init__(self, token):
        session = requests.Session()
        session.headers.update({
            'Authorization': 'token ' + token
        })
        self.session = session

    def get_repo(self, name):
        r = self.session.get(GitHub.API_ROOT + '/repos/' + name)
        r.raise_for_status()
        return Repository(self.session, r.json())
