# Use Python to lookup BGP Paths over the Internet

Recently ran into a scenario where AWS Cloud loss Internet Connectivity within two regions and started to look into a network-as-code options for running API calls to return BGP routes from a public accessible BGP router.

Going to create a few functions that can take a Public IP (From client or a Cloud) and identify the summary routes, the AS-PATH(s) available, and anything else I can use that can help a network engineer find this type of information fast without using a router/firewall show ip bgp commands

To run the script, you will need to have Python 3.6+ installed.  
Dependencies are listed in **requirements.txt**. You can install them using:  
```
pip3 install -r requirements.txt
```

### How to use the script main.py

The main.py file is a example script which is entering the arguments needed for the methods inside bgpview_api.py file to execute

```
python3 main.py
Please provide IPv4 or IPv6 Public IP address to run search against: 2620:0:ccb::4
```

High Level Diagram with Example:

![bgp_path_lookup](./docs/BGP_Path_Lookup_High_Level.png?raw=true "BGP Path Lookup High Level")

### How can this help with day-to-day tasks

- Run this script if you just added a new BGP peer to another ISP
- Run this script if you are experience route loss through a ISP
- View the entire API output examples in bgpview_api.py and create your own output

## API Source:
https://bgpview.docs.apiary.io/
