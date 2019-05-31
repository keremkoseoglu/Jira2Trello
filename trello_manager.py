from config import Config
from trello import TrelloApi
from jira.resources import Issue
from jira_manager import JiraManager


class TrelloManager:

    def __init__(self, c: Config):
        self._config = c
        self._trello = TrelloApi(self._config.trello_api_key)
        self._trello.set_token(self._config.trello_token)

    def create_card(self, issue: Issue, jira_man: JiraManager):

        try:
            title_key = issue.fields.parent.key
        except:
            title_key = issue.key

        title = title_key + " - " + issue.fields.summary

        new_card_json = self._trello.cards.new(
            title,
            self._config.trello_list,
            desc=issue.fields.description,
            pos=1)

        new_card_id = new_card_json["id"]

        for i in range(self._config.trello_comment_count):
            comment_idx = issue.fields.comment.total - 1 - i
            if comment_idx < 0:
                break
            current_comment = issue.fields.comment.comments[comment_idx]
            self._trello.cards.new_action_comment(new_card_id, current_comment.body)

        self._trello.cards.new_attachment(new_card_id, url=jira_man.get_url(issue.key))

        checklist_json = self._trello.cards.new_checklist(new_card_id, name="İşler")
        checklist_id = checklist_json["id"]

        self._trello.cards.new_checklist_checkItem_idChecklist(checklist_id, new_card_id, "İlerlet", 1)
        self._trello.cards.new_checklist_checkItem_idChecklist(checklist_id, new_card_id, "İncele", 2)
        self._trello.cards.new_checklist_checkItem_idChecklist(checklist_id, new_card_id, "Todo", 3)
        self._trello.cards.new_checklist_checkItem_idChecklist(checklist_id, new_card_id, "Activate", 4)
        self._trello.cards.new_checklist_checkItem_idChecklist(checklist_id, new_card_id, "EPC & Release", 5)
        self._trello.cards.new_checklist_checkItem_idChecklist(checklist_id, new_card_id, "İlerlet & not yaz", 6)

        ##todo
        pass