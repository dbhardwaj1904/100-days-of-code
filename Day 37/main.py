import requests
from datetime import datetime

ENDPOINT = "https://pixe.la"
# Token can be some random chars [different for different users]
token = "RANDOM_ALPHANUMERIC_NO_CAPS"
username = "USERNAME"

# Create Users
create_users = ENDPOINT + "/v1/users"
params = {
    "token": token,
    "username": username,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
create_users_response = requests.post(create_users, json=params)

# Create Graph for user
create_graph = create_users + "/" + username + "/graphs"
graph_id = "graph1"
graph_name = "Cycling Graph"
unit = "Km"
unit_type = "float"
color = "momiji"
params = {
    "id": graph_id,
    "name": graph_name,
    "unit": unit,
    "type": unit_type,
    "color": color,
}
headers = {
    "X-USER-TOKEN": token
}
create_graph_response = requests.post(create_graph, json=params, headers=headers)

# Post pixel for user
post_pixel = create_users + "/" + username + "/graphs/" + graph_id
date = (datetime.now()).strftime("%Y%m%d")
quantity = "9.74"
params = {
    "date": date,
    "quantity": quantity,
}
post_pixel_response = requests.post(post_pixel, json=params, headers=headers)

# Change posted pixel data i.e. quantity in current case
change_posted_pixel_data = post_pixel + "/" + date
quantity = "10.74"
params = {
    "quantity": quantity,
}
change_posted_pixel_data_response = requests.put(change_posted_pixel_data, json=params, headers=headers)

# Delete posted pixel
delete_pixel = change_posted_pixel_data
delete_pixel_response = requests.delete(delete_pixel, headers=headers)
print(change_posted_pixel_data_response.json())
