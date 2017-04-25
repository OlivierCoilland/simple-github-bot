import config
import utils

def warn(issue):
    text = utils.format_message(issue, config.warning_message)
    issue.add_comment(text)

def close(issue):
    text = utils.format_message(issue, config.closing_message)
    issue.add_comment(text)
    issue.close()
