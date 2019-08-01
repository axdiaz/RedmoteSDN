from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    # context = {'devices': [{'id': 1}, {'id': 2}, {'id': 3}, {'id': 4}]}
    api_result = [
        {
            'id': '1',
            'data': {
                'dp_desc': 's1',
                'sw_desc': '2.5.5',
                'hw_desc': 'Open vSwitch',
                'serial_num': 'None',
                'mfr_desc': 'Nicira, Inc.'
            }
        },
        {
            'id': '2',
            'data': {
                'dp_desc': 's2',
                'sw_desc': '2.5.5',
                'hw_desc': 'Open vSwitch',
                'serial_num': 'None',
                'mfr_desc': 'Nicira, Inc.'
            }
        },
        {
            'id': '3',
            'data': {
                'dp_desc': 's3',
                'sw_desc': '2.5.5',
                'hw_desc': 'Open vSwitch',
                'serial_num': 'None',
                'mfr_desc': 'Nicira, Inc.'
            }
        },
        {
            'id': '4',
            'data': {
                'dp_desc': 's4',
                'sw_desc': '2.5.5',
                'hw_desc': 'Open vSwitch',
                'serial_num': 'None',
                'mfr_desc': 'Nicira, Inc.'
            }
        }]

    return render(request, 'scanner/device-list.html', {"devices": api_result})
