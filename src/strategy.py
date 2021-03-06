import config
import utils

class Strategy(object):

    def remove_bot_comments(self, comments):
        return [comment for comment in comments if '#ignore' not in comment['body']]

    def get_last_comment(self, comments):
        sorted(comments, key=lambda comment: comment['created_at'])
        return comments[-1] if comments else None

    def get_last_warning(self, comments):
        warnings = [comment for comment in comments if '#warning' in comment['body']]
        sorted(warnings, key=lambda comment: comment['created_at'])
        return warnings[-1] if warnings else None

class LastCommentStrategy(Strategy):

    def should_warn(self, issue):
        comments = issue.get_comments()
        last_warning = self.get_last_warning(comments)
        if last_warning is not None:
            return False
        created_at = issue.data['created_at']
        comments = self.remove_bot_comments(comments)
        last_comment = self.get_last_comment(comments)
        if last_comment is not None:
            created_at = last_comment['created_at']
        age = utils.calculate_age_from_iso(created_at)
        return age > config.days_before_warning

    def should_close(self, issue):
        comments = issue.get_comments()
        last_warning = self.get_last_warning(comments)
        if last_warning is None:
            return False
        created_at = last_warning['created_at']
        age = utils.calculate_age_from_iso(created_at)
        return age > config.days_between_warning_and_closing
