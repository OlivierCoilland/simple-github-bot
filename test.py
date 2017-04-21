import config
from github import GitHub

github = GitHub(config.token)
repository = github.get_repo(config.repository)
issue = repository.get_issue(1);

def warnBeforeClosing(issue):
    issue.add_comment("This issue looks inactive, I'm about to close it!")

warnBeforeClosing(issue)
issue.close()
