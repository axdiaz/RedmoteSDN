import requests


class SwitchApi:

    def __init__(self):
        base_url = "http://localhost:8080/stats/"

        # number of switches and dpid
        # switch info
        # # switch flow
        # response = requests.get(base_url + "flow/" + str(swtich_data[0]))
        # switch_flow = response.json()
        #
        # print("switches: ", swtich_data)
        # print("switch flow: ", {item: str(switch_flow['1'][0][item]) for item in switch_flow['1'][0]})

        def __headers__(response):
            return {"status_code": response.status_code,
                    "data": None}

        def __get_switches__():
            response = requests.get(base_url + "switches")
            switch_data = response.json()
            switch_info = __headers__(response)
            filter_switches = []

            for switch in switch_data:
                switch_response = requests.get(base_url + "desc/" + str(switch))
                filter_switches.append(dict(
                    [
                        ("id", switch),
                        ("data", switch_response.json()[str(switch)])
                    ]))

            switch_info['data'] = filter_switches
            return switch_info
