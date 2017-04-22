class GitHubObject(object):

    def __init__(self, session, data):
        super(GitHubObject, self).__init__()
        self.session = session
        self.data = data
