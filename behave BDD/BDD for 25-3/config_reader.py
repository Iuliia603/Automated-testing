from config.JsonFileReader import JsonFileReader
from config.IniFileReader import IniFileReader


class ConfigReader:
    def __init__(self, filename):
        self.reader = None

        if filename.endswith(".json"):
            self.reader = JsonFileReader(filename)
        elif filename.endswith(".ini"):
            self.reader = IniFileReader(filename)
        else:
            raise Exception("File format is not supported")

    def get_browser(self):
        return self.reader.get_browser()

    def get_wait_time(self):
        return self.reader.get_wait_time()

    def get_email(self):
        return self.reader.get_email()

    def get_password(self):
        return self.reader.get_password()

    def get_user1_email(self):
        return self.reader.get_user1_email()

    def get_user1_password(self):
        return self.reader.get_user1_password()

    def get_user2_email(self):
        return self.reader.get_user2_email()

    def get_user2_password(self):
        return self.reader.get_user2_password()

    def get_url(self):
        return self.reader.get_url()
