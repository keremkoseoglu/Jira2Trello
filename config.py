import json, os


class Config:

    _CONFIG_FILE = "/Users/kerem/Dropbox/etc/config/jira2trello.txt" # Check sample_config.txt

    trello_api_key = ""
    trello_token = ""
    trello_board = ""
    trello_list = ""
    trello_comment_count = 0

    jira_base_url = ""
    jira_username = ""
    jira_password = ""

    def __init__(self):

        # Read text file
        script_dir = os.path.dirname(__file__)
        config_path = os.path.join(script_dir, self._CONFIG_FILE)
        txt_file = open(config_path, "r")
        txt_content = txt_file.read()
        txt_file.close()
        json_data = json.loads(txt_content)

        # Parse contents
        self.trello_api_key = json_data["config"]["trello"]["api_key"]
        self.trello_token = json_data["config"]["trello"]["token"]
        self.trello_board = json_data["config"]["trello"]["board"]
        self.trello_list = json_data["config"]["trello"]["list"]
        self.trello_comment_count = int(json_data["config"]["note"]["comment_count"])

        self.jira_base_url = json_data["config"]["jira"]["base_url"]
        self.jira_username = json_data["config"]["jira"]["username"]
        self.jira_password = json_data["config"]["jira"]["password"]