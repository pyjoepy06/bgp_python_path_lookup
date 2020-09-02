#Functions for code are located in bgpview_api.py
#Example of me using multiple functions to output helpful Data
import bgpview_api
import sys
import ipaddress

def ipaddress_check():
    input_ip = input('Please provide IPv4 or IPv6 Public IP address to run search against: ')
    try:
        ip = ipaddress.ip_address(input_ip)
        print('%s is a correct IP%s address.' % (ip, ip.version))
        print('Proceeding with gathering API Data\n')
        return(input_ip)
    except ValueError:
        print('\nAddress is invalid: %s' % input_ip)
        print('Exiting code, please retry with a valid IPv4 or IPv6 address')
        sys.exit()
    except:
        print('Usage : %s  ip' % ip)


def main():
    ip_data = ipaddress_check()

    ip_lookup = bgpview_api.bgp_ip_lookup(ip_data)

    if ip_lookup['status'] == 'ok':
        print(ip_lookup['status_message'])

        #Gather how many prefix routes are seen over BGP for IP
        count_bgp_routes = len(ip_lookup['data']['prefixes'])

        print('There is '+ str(count_bgp_routes) + ' BGP routes/paths present for ' + str(ip_data))
        print('\n')

        #Loop through route/prefix and find ISP for each
        #Pending better iteration rebuild
        for i in range(count_bgp_routes):
            cidr=ip_lookup['data']['prefixes'][i]['prefix']
            asn=ip_lookup['data']['prefixes'][i]['asn']['asn']

            print(cidr + ' is managed by ASN#: ' + str(asn))

            #Run function using ASN # to find ISPs this client/Public prefix uses
            asn_peers = bgpview_api.bgp_asn_upstreams(asn)

            #Will need to consider rebuilding for IPv6 logic versus IPv4 logic
            isp_peers = len(asn_peers['data']['ipv4_upstreams'])
            print('Which is peered with the following ' + str(isp_peers) + ' ISP providers\n')

            for peer in range(isp_peers):
                isp = asn_peers['data']['ipv4_upstreams'][peer]['name']
                isp_asnum = asn_peers['data']['ipv4_upstreams'][peer]['asn']
                print (isp + ' AS#: ' + str(isp_asnum))
    else:
        print('No BGP Route for provided IP address')



if __name__ == '__main__':
    main()
