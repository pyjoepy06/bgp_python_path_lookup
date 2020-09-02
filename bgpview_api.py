#https://bgpview.docs.apiary.io/#
#All functions are converted in JSON format
import urllib3
import requests
urllib3.disable_warnings()

#Funciton to lookup a specific IP
#Example: bgp_ip_lookup('148.45.67.8') - Not used just provides a prefix return back 148.32.0.0/12 therefore no entity owns this
def bgp_ip_lookup(ip):
    response = requests.get('https://api.bgpview.io/ip/' + str(ip))
    #Convert Response to JSON/Dictionary to read/view data better
    res_dict = response.json()

    #Check if response has a error message
    if res_dict['status'] == 'ok':
        return (res_dict)
    else:
        print ('Invalid IP Address provide: ' + str(ip))

#Who Owns this ASN#
#Example: bgp_asn_prefix('14618') - ASN #
def bgp_asn_lookup(asn):
    response = requests.get('https://api.bgpview.io/asn/' + str(asn))
    #Convert Response to JSON/Dictionary to read/view data better
    res_dict = response.json()

    #Check if response has a error message
    if res_dict['status'] == 'ok':
        return (res_dict)
    else:
        print ('Invalid IP Address provide: ' + str(ip))

#Will return all Asscioated Prefixes for a ASN#
#Example: bgp_asn_prefix('14618') - This AWS ASN # therefore we will get a lot of routes back as they are the cloud
def bgp_asn_prefix(asn):
    response = requests.get('https://api.bgpview.io/asn/' + str(asn) +'/prefixes')
    #Convert Response to JSON/Dictionary to read/view data better
    res_dict = response.json()

    #Check if response has a error message
    if res_dict['status'] == 'ok':
        return (res_dict)
    else:
        print ('Invalid IP Address provide: ' + str(ip))

#Example: bgp_asn_prefix(14618) - This AWS ASN # what is this ASN Peer'd with
def bgp_asn_peers(asn):
    response = requests.get('https://api.bgpview.io/asn/' + str(asn) +'/peers')
    #Convert Response to JSON/Dictionary to read/view data better
    res_dict = response.json()

    #Check if response has a error message
    if res_dict['status'] == 'ok':
        return (res_dict)
    else:
        print ('Invalid IP Address provide: ' + str(ip))

#Function to lookup who the ASN ISP/BGP Peers are
#bgp_asn_upstreams(14618) - Who is the upstream provider i.e ISP Peers can also provide a cool ipv4_graph to view on your browser
def bgp_asn_upstreams(asn):
    response = requests.get('https://api.bgpview.io/asn/' + str(asn) +'/upstreams')
    #Convert Response to JSON/Dictionary to read/view data better
    res_dict = response.json()

    #Check if response has a error message
    if res_dict['status'] == 'ok':
        return (res_dict)
    else:
        print ('Invalid IP Address provide: ' + str(ip))
