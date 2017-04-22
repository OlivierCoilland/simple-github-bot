from core import GitHubObject

class Issue(GitHubObject):

    def __init__(self, session, data):
        super(Issue, self).__init__(session, data)
        self.issue_url = data['url']
        self.comments_url = data['comments_url']
        self.labels_url = data['labels_url'].replace('{/name}', '')
        self.label_url = data['labels_url'].replace('{/name}', '/{}')

    def add_comment(self, body):
        data = {'body': body}
        r = self.session.post(self.comments_url, json=data)
        r.raise_for_status()

    def add_label(self, label):
        data = [label]
        r = self.session.post(self.labels_url, json=data)
        r.raise_for_status()

    def close(self):
        data = {'state': 'closed'}
        r = self.session.patch(self.issue_url, json=data)
        r.raise_for_status()
