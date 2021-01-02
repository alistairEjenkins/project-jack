import requests
from datetime import datetime,timedelta

TOKEN = 'AlexJackGeo3'
USERNAME = 'alistair'
GRAPH_ID = 'graph1'

pixela_endpoint = 'https://pixe.la/v1/users'

user_params = {

    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',

}
# response = requests.post(url=pixela_endpoint, json=user_params)
#
# print(response.text)

graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs'
graph_params = {

    'id': GRAPH_ID,
    'name': 'Reading Graph',
    'unit': 'pages',
    'type': 'int',
    'color': 'momiji',
}

headers = {

    'X-USER-TOKEN': TOKEN,
}


# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response.text)
today = datetime.now() # - timedelta(1)
TODAY = today.strftime("%Y%m%d")
post_pixel_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}'


post_pixel_params = {
    'date' : TODAY,
    'quantity' : '33'
}

# response = requests.post(url=post_pixel_endpoint, json=post_pixel_params, headers=headers)
# print(response.text)

put_pixel_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{TODAY}'

put_pixel_params = {
    'quantity' : '100',
}

# response = requests.put(url=put_pixel_endpoint, json=put_pixel_params, headers=headers)
# print(response.text)

delete_pixel_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{TODAY}'

response = requests.delete(url=delete_pixel_endpoint, headers=headers)
print(response.text)