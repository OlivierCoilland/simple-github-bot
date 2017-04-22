import config
from github import GitHub

github = GitHub(config.token)
repository = github.get_repo(config.repository)
issue = repository.get_issue(1)

def warn_before_closing(issue):
    text = "Hi {login}!\nThis issue looks inactive\nI'm about to close it!"
    issue_author_login = issue.data['user']['login']
    text = text.format(login=issue_author_login)
    issue.add_comment(text)

warn_before_closing(issue)
# issue.close()
