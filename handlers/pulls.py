import requests


def get_pulls(state):
    if state in ['open', 'closed']:
        return get_open_close_events(state)
    else:
        return get_accept_need_work_events(state)


def get_accept_need_work_events(current_state):
    result_array = []
    all_params = {'per_page': 100}
    response = requests.get(
        'https://api.github.com/repos/alenaPy/devops_lab/pulls',
        auth=('user', 'password'), params=all_params)

    for item in response.json():
        label = item['labels']

        if len(label) > 0:
            state = [d["name"] for d in label]

            if current_state == state[0]:
                result_array.append(parse_response_item(item))
    return result_array


def get_open_close_events(current_state):
    result_array = []
    all_params = {'state': current_state, 'per_page': 100}
    response = requests.get(
        'https://api.github.com/repos/alenaPy/devops_lab/pulls',
        auth=('user', 'password'), params=all_params)

    for item in response.json():
        result_array.append(parse_response_item(item))
    return result_array


def parse_response_item(item):
    number = item["number"]
    title = item['title']
    link = item['_links']['html']['href']
    return {'num': number, 'title': title, 'link': link}
