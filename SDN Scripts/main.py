import requests


class SwitchApi:

    def _init_(self):
        self.base_url = "http://localhost:8080/stats/"
        self.base_url_router = "http://localhost:8080/router/"

    @staticmethod
    def headers(response):
        return {"status_code": response.status_code}

    # GETTERS
    def get_switch_info(self):
        response = requests.get(self.base_url + "switches")

        # setting headers
        switch_info = SwitchApi.headers(response)
        # setting info
        filter_switches = []

        for switch in response.json():
            switch_desc_response = requests.get(self.base_url + "desc/" + str(switch))
            switch_flow_response = requests.get(self.base_url + "flow/" + str(switch))
            filter_switches.append(dict(
                [
                    ("id", switch),
                    ("desc_data", switch_desc_response.json()[str(switch)]),
                    ("flow_data", switch_flow_response.json()[str(switch)])
                ]))

        switch_info['data'] = filter_switches

        print(switch_info)

        return switch_info

    def get_switch_layer_two_info(self):
        response = requests.get(self.base_url + "switches")
        ports_desc_switches = []
        switch_info = SwitchApi.headers(response)

        for switch in response.json():
            ports_desc_response = requests.get(self.base_url + "portdesc/" + str(switch))
            ports_desc_switches.append(dict([
                ("id", switch),
                ("port_data", ports_desc_response.json()[str(switch)])
            ]))

        print(ports_desc_switches)
        switch_info['data'] = ports_desc_switches
        return switch_info

    def get_switch_layer_three_info(self, router_id):
        response = requests.get(
            self.base_url_router + ("000000000000000" + router_id) if router_id is not None else "all/all")
        layer_three_response = SwitchApi.headers(response)
        layer_three_response['data'] = response.json()

        for item in layer_three_response['data']:
            item['switch_id'] = item['switch_id'][-1]

        print(layer_three_response)
        return layer_three_response

    # SETTERS
    def set__address(self, switch_id, address):
        response = requests.post(self.base_url_router + "000000000000000" + switch_id,
                                 json=dict([("address", address)]))
        set_address_response = SwitchApi.headers(response)
        set_address_response['data'] = response.json()

        for item in set_address_response['data']:
            item['switch_id'] = item['switch_id'][-1]
            print(item['switch_id'])

        return set_address_response

    def set__default_route(self, switch_id, gateway):
        response = requests.post(self.base_url_router + "000000000000000" + switch_id,
                                 json=dict([("gateway", gateway)]))
        set_address_response = SwitchApi.headers(response)
        set_address_response['data'] = response.json()

        for item in set_address_response['data']:
            item['switch_id'] = item['switch_id'][-1]
            print(item['switch_id'])

        return set_address_response

    def set_static_route(self, switch_id, destination, gateway):
        response = requests.post(self.base_url_router + "000000000000000" + switch_id,
                                 json=dict([("destination", destination), ("gateway", gateway)]))
        set_address_response = SwitchApi.headers(response)
        set_address_response['data'] = response.json()

        for item in set_address_response['data']:
            item['switch_id'] = item['switch_id'][-1]
            print(item['switch_id'])

        return set_address_response

    # DELETE
    def delete_address(self, switch_id, address_id):
        response = requests.delete(self.base_url_router + "000000000000000" + switch_id,
                                   json=dict([("address_id", address_id)]))
        set_address_response = SwitchApi.headers(response)
        set_address_response['data'] = response.json()

        for item in set_address_response['data']:
            item['switch_id'] = item['switch_id'][-1]
            print(item['switch_id'])

        return set_address_response

    def delete_static_route(self, switch_id, route_id):
        response = requests.delete(self.base_url_router + "000000000000000" + switch_id,
                                   json=dict([("route_id", route_id)]))
        set_address_response = SwitchApi.headers(response)
        set_address_response['data'] = response.json()

        for item in set_address_response['data']:
            item['switch_id'] = item['switch_id'][-1]
            print(item['switch_id'])

        return set_address_response
