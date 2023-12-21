from Test_Tasks.Wrapper_YouTube import Browser
from config.config_reader import ConfigReader
import os

def before_all(context):
   file_path = os.path.join("/Users/iuliia603/PycharmProjects/pythonProject/Test_Tasks/Youtube_Test/steps/config.ini")
   configs = ConfigReader(file_path)
   context.configs = configs

def before_scenario(context, scenario):
   configs = context.configs
   browser = Browser(configs.get_url(), configs.get_browser(), configs.get_wait_time())
   context.browser = browser

def after_scenario(context, scenario):
   context.browser.shutdown()