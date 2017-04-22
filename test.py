from github import GitHub

import config
import strategy

github = GitHub(config.token)
repository = github.get_repo(config.repository)

strategy = strategy.LastCommentStrategy()
issues = repository.get_issues()
for issue in issues:
    print(strategy.should_warn(issue))
    print(strategy.should_close(issue))

# def warn_before_closing(issue):
#     text = "Hi {login}!\nThis issue looks inactive\nI'm about to close it!"
#     issue_author_login = issue.data['user']['login']
#     text = text.format(login=issue_author_login)
#     issue.add_comment(text)

# warn_before_closing(issue)
# issue.close()
