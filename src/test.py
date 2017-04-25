import config
from api.github import GitHub

class SimpleTest(object):

    def __init__(self):
        super(SimpleTest, self).__init__()
        self.github = GitHub(config.token)
        self.repository = self.github.get_repo(config.repository)

    def print_repository_data(self):
        print(self.repository.data)

if __name__ == '__main__':
    test = SimpleTest()
    test.print_repository_data()
