import requests

base_url = "http://localhost:8080/stats/"

# number of switches and dpid
response = requests.get(base_url + "switches")
swtich_data = response.json()

# switch info
response = requests.get(base_url + "desc/" + str(swtich_data[0]))
switch_info = response.json()

# switch flow
response = requests.get(base_url + "flow/" + str(swtich_data[0]))
switch_flow = response.json()

print("switches: ", swtich_data)
print("switch info: ", {item + " : " + switch_info['1'][item] for item in switch_info['1']})
print("switch flow: ", {item + " : " + str(switch_flow['1'][0][item]) for item in switch_flow['1'][0]})

