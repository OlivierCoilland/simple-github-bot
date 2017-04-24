from github import GitHub

import config
import strategy
import task

github = GitHub(config.token)
repository = github.get_repo(config.repository)

strategy = strategy.LastCommentStrategy()
warn_task = task.WarnTask()
close_task = task.CloseTask()

issues = repository.get_issues()
for issue in issues:
    if strategy.should_close(issue):
        close_task.close(issue)
        continue
    if strategy.should_warn(issue):
        warn_task.warn(issue)
        continue
