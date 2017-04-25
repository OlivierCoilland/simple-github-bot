import config
import strategy
import tasks
from api.github import GitHub

class SimpleGitHubBot(object):

    def __init__(self):
        super(SimpleGitHubBot, self).__init__()
        self.github = GitHub(config.token)
        self.repository = self.github.get_repo(config.repository)

    def monitor_issues_inactivity(self):
        inactivity_strategy = strategy.LastCommentStrategy()
        issues = self.repository.get_issues()
        for issue in issues:
            if inactivity_strategy.should_close(issue):
                tasks.close(issue)
            elif inactivity_strategy.should_warn(issue):
                tasks.warn(issue)

if __name__ == '__main__':
    bot = SimpleGitHubBot()
    bot.monitor_issues_inactivity()
