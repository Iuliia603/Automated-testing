from behave import given, when, then
from config.config_reader import ConfigReader
import os
from Test_Tasks.Wrapper_YouTube.Home_Page import HomePage
from Test_Tasks.Wrapper_YouTube.Search_result import SearchPage
from Test_Tasks.Wrapper_YouTube.Browser import Browser
from Test_Tasks.Wrapper_YouTube.Video import VideoPlayer
import time

URL = "https://www.youtube.com/"
file_path = os.path.join("/Users/iuliia603/PycharmProjects/pythonProject/Test_Tasks/Youtube_Test/steps/config.ini")
configs = ConfigReader(file_path)


@given('user opens website youtube.com')
def user_opens_website(context):
    browser = Browser(URL, configs.get_browser(), configs.get_wait_time())
    context.browser = browser
    context.homepage = HomePage(context.browser)
    context.homepage.get_homepage_title()
    time.sleep(5)


@given('user Enter search request in the input field')
def enter_request_in_input_field(context):
    context.homepage.click_search_field()
    context.homepage.input_request('breakfast burrito')
    time.sleep(2)
    context.homepage.enter_request()
    time.sleep(5)


@when('find in results video name')
def find_in_results_video_name(context):
    context.searchpage = SearchPage(context.browser)
    context.searchpage.get_name_video_title()


@when('user clicks on the video')
def user_clicks_on_video(context):
    context.searchpage.click_video()
    time.sleep(25)


@then('video started to play after opening')
def video_started_to_play(context):
    pass


@when('user clicks on 1/3')
def user_clicks_on_mini_player(context):
    time.sleep(35)
    context.video = VideoPlayer(context.browser)
    context.video.click_mini_player()
    time.sleep(5)


@then('the video continues to play')
def video_continues_to_play(context):
    pass
