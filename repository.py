from core import GitHubObject
from issue import Issue

class Repository(GitHubObject):

    def __init__(self, session, data):
        super(Repository, self).__init__(session, data)
        self.issues_url = data['issues_url'].replace('{/number}', '')
        self.issue_url = data['issues_url'].replace('{/number}', '/{}')

    def get_issues(self):
        r = self.session.get(self.issues_url)
        r.raise_for_status()
        return [Issue(self.session, data) for data in r.json()]

    def get_issue(self, id):
        url = self.issue_url.format(id)
        r = self.session.get(url)
        r.raise_for_status()
        return Issue(self.session, r.json())
