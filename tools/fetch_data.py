import requests

def fetch_data(url):
    """
    Fetches JSON data from a given URL.

    Args:
        url (str): The URL to retrieve JSON data from.

    Returns:
        dict or None: Parsed JSON data if the request is successful (status code 200), otherwise None.
    """
    response = requests.get(url)

    if response.status_code == 200:
        json_data = response.json()
        return json_data