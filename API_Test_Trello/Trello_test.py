import requests


APIKEY = "2919653692730f574379db8cf074a945"
TOKEN = "ATTA2927f7481e176cd94d47aa11fadcb3cf2d4eac8e1b52fba40edf607d0d18cb0b0C3B5384"
URL = "https://api.trello.com/"


def get_user_boards():
    endpoint = "1/members/me/boards"
    params = {
        'key': APIKEY,
        'token': TOKEN
    }

    response = requests.get(url=URL + endpoint, params=params)
    assert response.status_code == 200
    assert response.reason == "OK"
    assert response.ok
    response_json = response.json()
    return response_json


def get_board_id(name):
    id = None
    response = get_user_boards()
    for board in response:
        if board['name'] == name:
            id = board['id']
            break

    if id is None:
        print("No board found with the name: {}".format(name))
    return id


def update_board(name, **kwargs):
    board_id = get_board_id(name)

    endpoint = "{}1/boards/{}".format(URL, board_id)
    params = {
        'key': APIKEY,
        'token': TOKEN,
        'name': name
    }
    for key, value in kwargs.items():
        params[key] = value

    response = requests.request(
        "PUT",
        endpoint,
        params=params
    )
    assert response.status_code == 200
    assert response.reason == "OK"
    assert response.ok
    response_json = response.json()
    print(response_json)


def delete_board(name):
    board_id = get_board_id(name)
    endpoint = "{}1/boards/{}".format(URL, board_id)
    params = {
        'key': APIKEY,
        'token': TOKEN,
        'name': name
    }

    response = requests.request(
        "DELETE",
        endpoint,
        params=params
    )
    assert response.status_code == 200
    assert response.reason == "OK"
    assert response.ok
    response_json = response.json()
    print(response_json)


def create_new_board(name):
    endpoint = "1/boards/"
    params = {
        'key': APIKEY,
        'token': TOKEN,
        'name': name
    }
    response = requests.post(url=URL + endpoint, json=params)
    assert response.status_code == 200
    assert response.reason == "OK"
    assert response.ok
    response_json = response.json()
    print(response_json)


def create_new_list(name, list_name):
    board_id = get_board_id(name)

    endpoint = "{}1/boards/{}/lists".format(URL, board_id)
    headers = {
        "Accept": "application/json"
    }

    params = {
        'key': APIKEY,
        'token': TOKEN,
        'name': list_name
    }

    response = requests.request(
        "POST",
        endpoint,
        headers=headers,
        params=params
    )
    assert response.status_code == 200
    assert response.reason == "OK"
    assert response.ok
    response_json = response.json()
    print(response_json)

def get_user_list(name):
    board_id = get_board_id(name)
    endpoint = "{}1/boards/{}/lists".format(URL, board_id)
    headers = {
        "Accept": "application/json"
    }

    params = {
        'key': APIKEY,
        'token': TOKEN,
        }

    response = requests.get(url=endpoint, headers=headers, params=params)
    assert response.status_code == 200
    assert response.reason == "OK"
    assert response.ok
    response_json = response.json()
    return response_json

def get_list_id(name, list_name):
    list_id = None
    response = get_user_list(name)
    for list in response:
        if list['name'] == list_name:
            list_id = list['id']
            break

    if list_id is None:
        print("No list found with the name: {}".format(list_name))
    return list_id


def create_new_card(name, list_name, card_name):
    board_id = get_board_id(name)
    list_id = get_list_id(name, list_name)

    endpoint = "{}1/cards".format(URL)
    headers = {
        "Accept": "application/json"
    }

    params = {
        'key': APIKEY,
        'token': TOKEN,
        'name': card_name,
        'idList': list_id
    }

    response = requests.request(
        "POST",
        endpoint,
        headers=headers,
        params=params
    )
    assert response.status_code == 200
    assert response.reason == "OK"
    assert response.ok
    response_json = response.json()
    print(response_json)


def update_card(card_name, **kwargs):
    card_id = "Pfz6uUnX"
    endpoint = "{}1/cards/{}".format(URL, card_id)
    params = {
        'key': APIKEY,
        'token': TOKEN,
        'name': card_name
    }

    for key, value in kwargs.items():
        params[key] = value

    response = requests.request(
        "PUT",
        endpoint,
        params=params
    )
    assert response.status_code == 200
    assert response.reason == "OK"
    assert response.ok
    response_json = response.json()
    print(response_json)


def delete_card(card_name):
    card_id = "Pfz6uUnX"
    endpoint = "{}1/cards/{}".format(URL, card_id)
    params = {
        'key': APIKEY,
        'token': TOKEN,
        'name': card_name
    }

    response = requests.request(
        "DELETE",
        endpoint,
        params=params
    )
    assert response.status_code == 200
    assert response.reason == "OK"
    assert response.ok
    response_json = response.json()
    print(response_json)


def archive_list(name, list_name):
    board_id = get_board_id(name)
    list_id = get_list_id(name, list_name)
    endpoint = "{}1/boards/{}/lists/{}/closed".format(URL, board_id, list_id)
    headers = {
        "Accept": "application/json"
    }

    params = {
        'key': APIKEY,
        'token': TOKEN
    }

    response = requests.get(url=endpoint, headers=headers, params=params)
    assert response.status_code == 200
    assert response.reason == "OK"
    assert response.ok
    response_json = response.json()
    return response_json


if __name__ == "__main__":
   get_user_boards()
   create_new_board("Test Automation10")
   update_board("Test Automation10", desc="Add items to finish automation")
   delete_board("Test Automation")
   create_new_list("Test Automation10", "My_list")
   create_new_card("Test Automation10", "My_list", "My_Card")
   get_user_list("Test Automation10")
   get_list_id("Test Automation10", "My_list")
   update_card("My_Card", desc="My Update")
   delete_card("My_Card")
   archive_list("Test Automation10", "My_list")

