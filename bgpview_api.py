#!/usr/bin/env python
"""
Refer to https://bgpview.docs.apiary.io/#
All functions are converted in JSON format
"""
import urllib3
import requests
urllib3.disable_warnings()

def bgp_ip_lookup(ip_addres):
    #Function to lookup a specific IP
    response = requests.get('https://api.bgpview.io/ip/' + str(ip_addres))
    res_dict = response.json()

    #Check if response has a error message
    if res_dict['status'] == 'ok':
        pass
    else:
        res_dict = None
    return res_dict

def bgp_asn_lookup(asn):
    response = requests.get('https://api.bgpview.io/asn/' + str(asn))

    res_dict = response.json()

    #Check if response has a error message
    if res_dict['status'] == 'ok':
        pass
    else:
        res_dict = None
    return res_dict


def bgp_asn_prefix(asn):
    response = requests.get('https://api.bgpview.io/asn/' + str(asn) +'/prefixes')

    res_dict = response.json()

    #Check if response has a error message
    if res_dict['status'] == 'ok':
        pass
    else:
        res_dict = None
    return res_dict



def bgp_asn_peers(asn):
    response = requests.get('https://api.bgpview.io/asn/' + str(asn) +'/peers')
    #Convert Response to JSON/Dictionary to read/view data better
    res_dict = response.json()

    #Check if response has a error message
    if res_dict['status'] == 'ok':
        pass
    else:
        res_dict = None
    return res_dict



def bgp_asn_upstreams(asn):
    response = requests.get('https://api.bgpview.io/asn/' + str(asn) +'/upstreams')
    #Convert Response to JSON/Dictionary to read/view data better
    res_dict = response.json()

    #Check if response has a error message
    if res_dict['status'] == 'ok':
        pass
    else:
        res_dict = None
    return res_dict
