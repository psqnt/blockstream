import requests


BASE_URL = 'https://blockstream.info/api/'

def call_api(endpoint):
    """
    Build the API URL and request data
    :param str endpoint: specific api endpoint to hit
    :return response: server's reponse to the request
    """
    url = BASE_URL + endpoint
    try:  # try to get json data
        response = requests.get(url).json()
    except ValueError:  # if bytes, convert to str
        response = requests.get(url).content.decode('utf-8')
    except Exception as e:
        response = e
    return handle_response(response)


def handle_response(response):
    """
    Responses from blockstream's API are returned in json or str
    :param response: http response object from requests library
    :return response: decoded response from api
    """
    if isinstance(response, Exception):
        print(response)
        return response
    else:
        return response
