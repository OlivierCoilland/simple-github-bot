from core import GitHubObject

class Issue(GitHubObject):

    def __init__(self, session, data):
        super(Issue, self).__init__(session, data)
        self.issue_url = data['url']
        self.comments_url = data['comments_url']
        self.events_url = data['events_url']
        self.labels_url = data['labels_url'].replace('{/name}', '')
        self.label_url = data['labels_url'].replace('{/name}', '/{}')

    def get_comments(self):
        r = self.session.get(self.comments_url)
        r.raise_for_status()
        return r.json()

    def get_events(self):
        r = self.session.get(self.events_url)
        r.raise_for_status()
        return r.json()

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
