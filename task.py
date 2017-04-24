import utils
import config

class Task(object):

    pass

class WarnTask(Task):

    def warn(self, issue):
        text = utils.format_message(issue, config.warning_message)
        issue.add_comment(text)

class CloseTask(Task):

    def close(self, issue):
        text = utils.format_message(issue, config.closing_message)
        issue.add_comment(text)
        issue.close()
