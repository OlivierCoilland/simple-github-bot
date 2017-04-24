from github import GitHub

import config
import strategy
import task

class SimpleGitHubBot(object):

    def __init__(self):
        super(SimpleGitHubBot, self).__init__()
        self.github = GitHub(config.token)
        self.repository = self.github.get_repo(config.repository)

    def monitor_issues_inactivity(self):
        inactivity_strategy = strategy.LastCommentStrategy()
        warn_task = task.WarnTask()
        close_task = task.CloseTask()
        issues = self.repository.get_issues()
        for issue in issues:
            if inactivity_strategy.should_close(issue):
                close_task.close(issue)
            elif inactivity_strategy.should_warn(issue):
                warn_task.warn(issue)

if __name__ == '__main__':
    bot = SimpleGitHubBot()
    bot.monitor_issues_inactivity()
