from core import GitHubObject

class Issue(GitHubObject):

    def __init__(self, session, data):
        super().__init__(session, data)
        self.ISSUE_URL = data['url']
        self.COMMENTS_URL = data['comments_url']
        self.LABELS_URL = data['labels_url'].replace('{/name}', '')
        self.LABEL_URL = data['labels_url'].replace('{/name}', '/{}')

    def add_comment(self, body):
        data = {'body': body}
        r = self.session.post(self.COMMENTS_URL, json=data)
        r.raise_for_status()

    def add_label(self, label):
        data = [ label ]
        r = self.session.post(self.LABELS_URL, json=data)
        r.raise_for_status()

    def close(self):
        data = {'state': 'closed'}
        r = self.session.patch(self.ISSUE_URL, json=data)
        r.raise_for_status()
