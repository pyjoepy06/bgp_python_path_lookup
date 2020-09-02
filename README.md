# Use Python to lookup BGP Paths over the Internet

Recently ran into a scenario where AWS Cloud loss Internet Connectivity within two regions and started to look into a network-as-code options for running API calls to return BGP routes from a public accessiable BGP router.

Going to create a few functions that can take a Public IP (From client or a Cloud) and identify the summary routes, the AS-PATH(s) available, and anything else I can use that can help a network engineer find this type of information fast without using a router/firewall show ip bgp commands

## API Source:
https://bgpview.docs.apiary.io/
