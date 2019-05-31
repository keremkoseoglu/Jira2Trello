from config import Config
from trello_manager import TrelloManager
from jira_manager import JiraManager
import sys

desired_issue = sys.argv[1]
#desired_issue="VOL-6370"

my_config = Config()
my_jira_manager = JiraManager(my_config)
my_trello_manager = TrelloManager(my_config)

issue = my_jira_manager.get_issue(desired_issue)
my_trello_manager.create_card(issue, my_jira_manager)