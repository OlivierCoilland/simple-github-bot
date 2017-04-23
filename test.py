from github import GitHub

import config
import strategy

def warn(issue):
    text = format_message(issue, config.warning_message)
    issue.add_comment(text)

def close(issue):
    text = format_message(issue, config.closing_message)
    issue.add_comment(text)
    issue.close()

def format_message(issue, text):
    issue_author_login = issue.data['user']['login']
    return text.format(login=issue_author_login)

github = GitHub(config.token)
repository = github.get_repo(config.repository)

strategy = strategy.LastCommentStrategy()
issues = repository.get_issues()
for issue in issues:
    if strategy.should_close(issue):
        close(issue)
        continue
    if strategy.should_warn(issue):
        warn(issue)
        continue
