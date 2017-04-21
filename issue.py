from core import GitHubObject

class Issue(GitHubObject):

    def __init__(self, session, data):
        super().__init__(session, data)
        self.COMMENTS_URL = data['comments_url']

    def add_comment(self, body):
        url = self.COMMENTS_URL
        data = {'body': body}
        r = self.session.post(url, json=data)
        r.raise_for_status()
