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

    def get_user1_email(self):
        if 'email' not in self.data.keys():
            raise Exception("email option is not found in user1 section")
        return self.data['email']

    def get_user1_password(self):
        if 'password' not in self.data.keys():
            raise Exception("password option is not found in iser1 section")
        return self.data['password']

    def get_url(self):
        if 'url' not in self.data.keys():
            raise Exception("URL option is not present in the config file")
        return self.data['url']

