import json

import requests
from django.shortcuts import render
from scanner.sdn_interfaces import SwitchApi
from RedmoteWEB import settings

from django.http import HttpResponse, JsonResponse


def index(request):
    # context = {'devices': [{'id': 1}, {'id': 2}, {'id': 3}, {'id': 4}]}
    context = {
        'devices': switches_info()["data"],
        'layer2': layer2_info()["data"],
        'layer3': layer3_info()["data"],
    }

    return render(request, 'scanner/device-list.html', context)


def json_switches_info(request):
    api = SwitchApi()
    data = {"switches": ""}
    if not settings.DEBUG:
        data = api.get_switch_info()
    else:
        success = False
        attemps = 0
        while not success and attemps < 10:
            try:
                data = json.loads(requests.get("http://34.65.206.200/json/switches_info").content)
                success = True
            except:
                data = {"data": "data not available"}
                attemps += 1
        print(data)
        # data = requests.get("http://34.65.206.200/json/switches_info")
        # data = {'data': list(requests.get("http://34.65.206.200/json/switches_info").content)}
        # data = data.content
        # print(data)

    return JsonResponse(data)


def switches_info():
    if settings.DEBUG:
        return {
            "status_code": 200, "data": [{"id": 1, "desc_data": {"hw_desc": "Open vSwitch", "dp_desc": "s1",
                                                                 "serial_num": "None", "sw_desc": "2.5.5",
                                                                 "mfr_desc": "Nicira, Inc."}, "flow_data": [
                {"duration_sec": 1024, "match": {"nw_dst": "192.168.0.1", "dl_type": 2048}, "table_id": 0,
                 "hard_timeout": 0, "cookie": 1, "packet_count": 0, "byte_count": 0, "duration_nsec": 748000000,
                 "flags": 0,
                 "idle_timeout": 0, "actions": ["OUTPUT:CONTROLLER"], "priority": 2, "length": 96},
                {"duration_sec": 1024, "match": {"nw_dst": "192.168.0.1", "dl_type": 2048}, "table_id": 0,
                 "hard_timeout": 0, "cookie": 1, "packet_count": 0, "byte_count": 0, "duration_nsec": 747000000,
                 "flags": 0,
                 "idle_timeout": 0, "actions": ["OUTPUT:CONTROLLER"], "priority": 1037, "length": 96},
                {"duration_sec": 545, "match": {"nw_dst": "192.168.0.2", "dl_type": 2048}, "table_id": 0,
                 "hard_timeout": 0,
                 "cookie": 2, "packet_count": 0, "byte_count": 0, "duration_nsec": 967000000, "flags": 0,
                 "idle_timeout": 0,
                 "actions": ["OUTPUT:CONTROLLER"], "priority": 2, "length": 96},
                {"duration_sec": 545, "match": {"nw_dst": "192.168.0.2", "dl_type": 2048}, "table_id": 0,
                 "hard_timeout": 0,
                 "cookie": 2, "packet_count": 0, "byte_count": 0, "duration_nsec": 965000000, "flags": 0,
                 "idle_timeout": 0,
                 "actions": ["OUTPUT:CONTROLLER"], "priority": 1037, "length": 96},
                {"duration_sec": 371, "match": {"nw_dst": "192.168.0.10", "dl_type": 2048}, "table_id": 0,
                 "hard_timeout": 0, "cookie": 3, "packet_count": 0, "byte_count": 0, "duration_nsec": 671000000,
                 "flags": 0,
                 "idle_timeout": 0, "actions": ["OUTPUT:CONTROLLER"], "priority": 2, "length": 96},
                {"duration_sec": 371, "match": {"nw_dst": "192.168.0.10", "dl_type": 2048}, "table_id": 0,
                 "hard_timeout": 0, "cookie": 3, "packet_count": 0, "byte_count": 0, "duration_nsec": 670000000,
                 "flags": 0,
                 "idle_timeout": 0, "actions": ["OUTPUT:CONTROLLER"], "priority": 1037, "length": 96},
                {"duration_sec": 1024, "match": {"nw_dst": "192.168.0.1", "dl_type": 2048, "nw_src": "192.168.0.1"},
                 "table_id": 0, "hard_timeout": 0, "cookie": 1, "packet_count": 0, "byte_count": 0,
                 "duration_nsec": 746000000, "flags": 0, "idle_timeout": 0, "actions": ["OUTPUT:NORMAL"],
                 "priority": 36,
                 "length": 104},
                {"duration_sec": 545, "match": {"nw_dst": "192.168.0.2", "dl_type": 2048, "nw_src": "192.168.0.2"},
                 "table_id": 0, "hard_timeout": 0, "cookie": 2, "packet_count": 0, "byte_count": 0,
                 "duration_nsec": 965000000, "flags": 0, "idle_timeout": 0, "actions": ["OUTPUT:NORMAL"],
                 "priority": 36,
                 "length": 104},
                {"duration_sec": 371, "match": {"nw_dst": "192.168.0.10", "dl_type": 2048, "nw_src": "192.168.0.10"},
                 "table_id": 0, "hard_timeout": 0, "cookie": 3, "packet_count": 0, "byte_count": 0,
                 "duration_nsec": 670000000, "flags": 0, "idle_timeout": 0, "actions": ["OUTPUT:NORMAL"],
                 "priority": 36,
                 "length": 104},
                {"duration_sec": 3360, "match": {"dl_type": 2054}, "table_id": 0, "hard_timeout": 0, "cookie": 0,
                 "packet_count": 0, "byte_count": 0, "duration_nsec": 27000000, "flags": 0, "idle_timeout": 0,
                 "actions": ["OUTPUT:CONTROLLER"], "priority": 1, "length": 88},
                {"duration_sec": 3360, "match": {"dl_type": 2048}, "table_id": 0, "hard_timeout": 0, "cookie": 0,
                 "packet_count": 0, "byte_count": 0, "duration_nsec": 27000000, "flags": 0, "idle_timeout": 0,
                 "actions": [], "priority": 1, "length": 64},
                {"duration_sec": 3360, "match": {}, "table_id": 0, "hard_timeout": 0, "cookie": 0, "packet_count": 0,
                 "byte_count": 0, "duration_nsec": 27000000, "flags": 0, "idle_timeout": 0,
                 "actions": ["OUTPUT:NORMAL"],
                 "priority": 0, "length": 80}]}, {"id": 2, "desc_data": {"hw_desc": "Open vSwitch", "dp_desc": "s2",
                                                                         "serial_num": "None", "sw_desc": "2.5.5",
                                                                         "mfr_desc": "Nicira, Inc."}, "flow_data": [
                {"duration_sec": 3360, "match": {"dl_type": 2054}, "table_id": 0, "hard_timeout": 0, "cookie": 0,
                 "packet_count": 3, "byte_count": 180, "duration_nsec": 45000000, "flags": 0, "idle_timeout": 0,
                 "actions": ["OUTPUT:CONTROLLER"], "priority": 1, "length": 88},
                {"duration_sec": 3360, "match": {"dl_type": 2048}, "table_id": 0, "hard_timeout": 0, "cookie": 0,
                 "packet_count": 0, "byte_count": 0, "duration_nsec": 45000000, "flags": 0, "idle_timeout": 0,
                 "actions": [], "priority": 1, "length": 64},
                {"duration_sec": 3360, "match": {}, "table_id": 0, "hard_timeout": 0, "cookie": 0, "packet_count": 0,
                 "byte_count": 0, "duration_nsec": 45000000, "flags": 0, "idle_timeout": 0,
                 "actions": ["OUTPUT:NORMAL"],
                 "priority": 0, "length": 80}]}, {"id": 3, "desc_data": {"hw_desc": "Open vSwitch", "dp_desc": "s3",
                                                                         "serial_num": "None", "sw_desc": "2.5.5",
                                                                         "mfr_desc": "Nicira, Inc."}, "flow_data": [
                {"duration_sec": 3360, "match": {"dl_type": 2054}, "table_id": 0, "hard_timeout": 0, "cookie": 0,
                 "packet_count": 0, "byte_count": 0, "duration_nsec": 57000000, "flags": 0, "idle_timeout": 0,
                 "actions": ["OUTPUT:CONTROLLER"], "priority": 1, "length": 88},
                {"duration_sec": 3360, "match": {"dl_type": 2048}, "table_id": 0, "hard_timeout": 0, "cookie": 0,
                 "packet_count": 0, "byte_count": 0, "duration_nsec": 56000000, "flags": 0, "idle_timeout": 0,
                 "actions": [], "priority": 1, "length": 64},
                {"duration_sec": 3360, "match": {}, "table_id": 0, "hard_timeout": 0, "cookie": 0, "packet_count": 0,
                 "byte_count": 0, "duration_nsec": 57000000, "flags": 0, "idle_timeout": 0,
                 "actions": ["OUTPUT:NORMAL"],
                 "priority": 0, "length": 80}]}, {"id": 4, "desc_data": {"hw_desc": "Open vSwitch", "dp_desc": "s4",
                                                                         "serial_num": "None", "sw_desc": "2.5.5",
                                                                         "mfr_desc": "Nicira, Inc."}, "flow_data": [
                {"duration_sec": 3360, "match": {"dl_type": 2054}, "table_id": 0, "hard_timeout": 0, "cookie": 0,
                 "packet_count": 0, "byte_count": 0, "duration_nsec": 72000000, "flags": 0, "idle_timeout": 0,
                 "actions": ["OUTPUT:CONTROLLER"], "priority": 1, "length": 88},
                {"duration_sec": 3360, "match": {"dl_type": 2048}, "table_id": 0, "hard_timeout": 0, "cookie": 0,
                 "packet_count": 0, "byte_count": 0, "duration_nsec": 72000000, "flags": 0, "idle_timeout": 0,
                 "actions": [], "priority": 1, "length": 64},
                {"duration_sec": 3360, "match": {}, "table_id": 0, "hard_timeout": 0, "cookie": 0, "packet_count": 0,
                 "byte_count": 0, "duration_nsec": 72000000, "flags": 0, "idle_timeout": 0,
                 "actions": ["OUTPUT:NORMAL"],
                 "priority": 0, "length": 80}]}]}
    else:
        return SwitchApi().get_switch_info()


def layer2_info():
    if settings.DEBUG:
        return {
            "status_code": 200, "data": [{"id": 1, "port_data": [
                {"hw_addr": "de:61:a0:28:0a:47", "curr": 0, "supported": 0, "max_speed": 0, "advertised": 0, "peer": 0,
                 "port_no": "LOCAL", "curr_speed": 0, "name": "s1", "state": 1, "config": 1},
                {"hw_addr": "d2:af:e8:2f:16:bb", "curr": 2112, "supported": 0, "max_speed": 0, "advertised": 0,
                 "peer": 0,
                 "port_no": 1, "curr_speed": 10000000, "name": "s1-eth1", "state": 0, "config": 0},
                {"hw_addr": "fa:8f:b3:5a:78:4b", "curr": 2112, "supported": 0, "max_speed": 0, "advertised": 0,
                 "peer": 0,
                 "port_no": 2, "curr_speed": 10000000, "name": "s1-eth2", "state": 0, "config": 0}]},
                                         {"id": 1,
                                          "port_data": [{
                                              "hw_addr": "de:61:a0:28:0a:47",
                                              "curr": 0,
                                              "supported": 0,
                                              "max_speed": 0,
                                              "advertised": 0,
                                              "peer": 0,
                                              "port_no": "LOCAL",
                                              "curr_speed": 0,
                                              "name": "s1",
                                              "state": 1,
                                              "config": 1},
                                              {
                                                  "hw_addr": "d2:af:e8:2f:16:11",
                                                  "curr": 2112,
                                                  "supported": 0,
                                                  "max_speed": 0,
                                                  "advertised": 0,
                                                  "peer": 0,
                                                  "port_no": 1,
                                                  "curr_speed": 10000000,
                                                  "name": "s1-eth1",
                                                  "state": 0,
                                                  "config": 0},
                                              {
                                                  "hw_addr": "fa:8f:b3:5a:78:4b",
                                                  "curr": 2112,
                                                  "supported": 0,
                                                  "max_speed": 0,
                                                  "advertised": 0,
                                                  "peer": 0,
                                                  "port_no": 2,
                                                  "curr_speed": 10000000,
                                                  "name": "s1-eth2",
                                                  "state": 0,
                                                  "config": 0}]},
                                         {"id": 2, "port_data": [
                                             {"hw_addr": "de:61:a0:28:0a:22", "curr": 0, "supported": 0,
                                              "max_speed": 0, "advertised": 0, "peer": 0, "port_no": "LOCAL",
                                              "curr_speed": 0, "name": "s1", "state": 1, "config": 1},
                                             {"hw_addr": "d2:af:e8:2f:16:bb", "curr": 2112, "supported": 0,
                                              "max_speed": 0, "advertised": 0, "peer": 0, "port_no": 1,
                                              "curr_speed": 10000000, "name": "s1-eth1", "state": 0, "config": 0},
                                             {"hw_addr": "fa:8f:b3:5a:78:4b", "curr": 2112, "supported": 0,
                                              "max_speed": 0, "advertised": 0, "peer": 0, "port_no": 2,
                                              "curr_speed": 10000000, "name": "s1-eth2", "state": 0, "config": 0}]},
                                         {"id": 3, "port_data": [
                                             {"hw_addr": "de:61:a0:28:0a:33", "curr": 0, "supported": 0,
                                              "max_speed": 0, "advertised": 0, "peer": 0, "port_no": "LOCAL",
                                              "curr_speed": 0, "name": "s1", "state": 1, "config": 1},
                                             {"hw_addr": "d2:af:e8:2f:16:bb", "curr": 2112, "supported": 0,
                                              "max_speed": 0, "advertised": 0, "peer": 0, "port_no": 1,
                                              "curr_speed": 10000000, "name": "s1-eth1", "state": 0, "config": 0},
                                             {"hw_addr": "fa:8f:b3:5a:78:4b", "curr": 2112, "supported": 0,
                                              "max_speed": 0, "advertised": 0, "peer": 0, "port_no": 2,
                                              "curr_speed": 10000000, "name": "s1-eth2", "state": 0, "config": 0}]},
                                         {"id": 4, "port_data": [
                                             {"hw_addr": "de:61:a0:28:0a:44", "curr": 0, "supported": 0,
                                              "max_speed": 0, "advertised": 0, "peer": 0, "port_no": "LOCAL",
                                              "curr_speed": 0, "name": "s1", "state": 1, "config": 1},
                                             {"hw_addr": "d2:af:e8:2f:16:bb", "curr": 2112, "supported": 0,
                                              "max_speed": 0, "advertised": 0, "peer": 0, "port_no": 1,
                                              "curr_speed": 10000000, "name": "s1-eth1", "state": 0, "config": 0},
                                             {"hw_addr": "fa:8f:b3:5a:78:4b", "curr": 2112, "supported": 0,
                                              "max_speed": 0, "advertised": 0, "peer": 0, "port_no": 2,
                                              "curr_speed": 10000000, "name": "s1-eth2", "state": 0,
                                              "config": 0}]}]}
    else:
        return SwitchApi().get_switch_layer_two_info()


def layer3_info():
    if settings.DEBUG:
        return {
            "status_code": 200, "data": [{"internal_network": [{"address": [
                {"address_id": 3, "address": "192.168.0.10/32"}, {"address_id": 1, "address": "192.168.0.1/32"},
                {"address_id": 2, "address": "192.168.0.2/32"}]}], "switch_id": "1"},
                {"internal_network": [{}], "switch_id": "2"},
                {"internal_network": [{}], "switch_id": "3"},
                {"internal_network": [{}], "switch_id": "4"}]}
    else:
        return SwitchApi().get_switch_layer_three_info()
