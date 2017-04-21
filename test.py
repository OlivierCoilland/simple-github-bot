import config
from github import GitHub

github = GitHub(config.token)
repository = github.get_repo(config.repository)
issue = repository.get_issue(1);

# issue.add_comment("Hey! I'm a bot :)")
issue.add_label('bug')
