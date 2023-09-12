import json

class JsonFileReader:
    def __init__(self, filename):
        self.data = None

        with open(filename, 'r') as config_file:
            self.data = json.load(config_file)

    def get_browser(self):
        if 'browser' not in self.data.keys():
            raise Exception("Browser option is not present in the config file")
        return self.data['browser']

    def get_wait_time(self):
        if 'wait_time' not in self.data.keys():
            raise Exception("Wait_time option is not present in the config file")
        return int(self.data['wait_time'])

    def get_email(self, user_section):
        if 'email' not in self.data.keys():
            raise Exception(f"Email option is not present in the {user_section} section of the config file")
        return int(self.data[user_section]['email'])

    def get_password(self, user_section):
        if 'password' not in self.data.keys():
            raise Exception(f"Password option is not present in the {user_section} section of the config file")
        return int(self.data[user_section]['password'])

