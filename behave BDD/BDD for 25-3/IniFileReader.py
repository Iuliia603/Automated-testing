from configparser import ConfigParser

class IniFileReader:
    def __init__(self, filename):
        self.data = None

        with open(filename, 'r') as config_file:
            self.data = ConfigParser()
            self.data.read_file(config_file)

    def get_browser(self):
        value = self.data.get('environment', 'browser', fallback=None)
        if value is None:
            raise Exception("Browser option is not present in the config file")
        return value

    def get_wait_time(self):
        value = self.data.get('environment', 'wait', fallback=None)
        if value is None:
            raise Exception("Wait_time option is not present in the config file")
        return int(value)

    def get_email(self, user_section):
        if not self.data.has_option(user_section, 'email'):
            raise Exception(f"Email option is not present in the {user_section} section of the config file")
        return self.data.get(user_section, 'email')

    def get_password(self, user_section):
        if not self.data.has_option(user_section, 'password'):
            raise Exception(f"Password option is not present in the {user_section} section of the config file")
        return self.data.get(user_section, 'password')

    def get_user1_email(self):
        if not self.data.has_option('user1', 'email'):
            raise Exception("Email option is not present in the 'user1' section of the config file")
        return self.data.get('user1', 'email')

    def get_user1_password(self):
        if not self.data.has_option('user1', 'password'):
            raise Exception("Password option is not present in the 'user1' section of the config file")
        return self.data.get('user1', 'password')

    def get_user2_email(self):
        if not self.data.has_option('user2', 'email'):
            raise Exception("Email option is not present in the 'user1' section of the config file")
        return self.data.get('user2', 'email')

    def get_user2_password(self):
        if not self.data.has_option('user2', 'password'):
            raise Exception("Password option is not present in the 'user1' section of the config file")
        return self.data.get('user2', 'password')

    def get_url(self):
        value = self.data.get('environment', 'url', fallback=None)
        if value is None:
            raise Exception("URL option is not found in environment section")
        return value
