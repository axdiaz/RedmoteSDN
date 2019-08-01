import requests


class SwitchApi:

    def __init__(self):
        base_url = "http://localhost:8080/stats/"
        base_url_router = "http://localhost:8080/router/"

        def __headers__(response):
            return {"status_code": response.status_code}

        # GETTERS
        def __get_switch_info__():
            response = requests.get(base_url + "switches")

            # setting headers
            switch_info = __headers__(response)
            # setting info
            filter_switches = []

            for switch in response.json():
                switch_desc_response = requests.get(base_url + "desc/" + str(switch))
                switch_flow_response = requests.get(base_url + "flow/" + str(switch))
                filter_switches.append(dict(
                    [
                        ("id", switch),
                        ("desc_data", switch_desc_response.json()[str(switch)]),
                        ("flow_data", switch_flow_response.json()[str(switch)])
                    ]))

            switch_info['data'] = filter_switches

            print(switch_info)

            return switch_info

        def __get_switch_layer_two_info__():
            response = requests.get(base_url + "switches")
            ports_desc_switches = []
            switch_info = __headers__(response)

            for switch in response.json():
                ports_desc_response = requests.get(base_url + "portdesc/" + str(switch))
                ports_desc_switches.append(dict([
                    ("id", switch),
                    ("port_data", ports_desc_response.json()[str(switch)])
                ]))

            print(ports_desc_switches)
            switch_info['data'] = ports_desc_switches
            print(switch_info)

        def __get_switch_layer_three_info__(router_id):
            response = requests.get(
                base_url_router + ("000000000000000" + router_id) if router_id is not None else "all/all")
            layer_two_response = __headers__(response)
            layer_two_response['data'] = response.json()

            for item in layer_two_response['data']:
                item['switch_id'] = item['switch_id'][-1]

            print(layer_two_response)
            return layer_two_response

        # SETTERS
        def __set__adress__(switch_id, address):
            response = requests.post(base_url_router + "000000000000000" + switch_id, json=dict([("address", address)]))
            set_address_response = __headers__(response)
            set_address_response['data'] = response.json()
            print(set_address_response)
            return set_address_response

        # def __set_default_switch__(dpid):
        #     response = requests.post(base_url + "flowentry/add", json=dict([
        #         ("dpid", dpid),
        #         ("cookie", 1),
        #         ("cookie_mask", 1),
        #         ("table_id", dpid),
        #         ("idle_timeout", 30),
        #         ("hard_timeout", 30),
        #         ("priority", 11111),
        #         ("flags", 1)]))
        #
        #     # setting headers
        #     switch_info = __headers__(response)
        #
        #     print(switch_info)
        #
        #     return switch_info
