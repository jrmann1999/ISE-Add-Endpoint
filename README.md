This is a simple script to add endpoints to an ISE system via MAC address.  Optionally you can specify the name and description of the device as well.

Usage:
    ./ise_add_endpoint.py MACADDRESS -user USERNAME -pass PASSWORD -host ISE_HOST
    
Optional Arguments
    -name DEVICE NAME
    -desc DEVICE DESCRIPTION

All usages of the script will log to ISE_ADD_DEBUG.log file in the same folder as the command was run.