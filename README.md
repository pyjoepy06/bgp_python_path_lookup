# Use Python to lookup BGP Paths over the Internet

Recently ran into a scenario where AWS Cloud loss Internet Connectivity within two regions and started to look into a network-as-code options for running API calls to return BGP routes from a public accessiable BGP router.

Going to create a few functions that can take a Public IP (From client or a Cloud) and identify the summary routes, the AS-PATH(s) available, and anything else I can use that can help a network engineer find this type of information fast without using a router/firewall show ip bgp commands

To run the script, you will need to have Python 3.6+ installed.  
Dependencies are listed in **requirements.txt**. You can install them using:  
`pip3 install -r requirements.txt`  

### How to use the script main.py
```
python3 main.py
```

## API Source:
https://bgpview.docs.apiary.io/
