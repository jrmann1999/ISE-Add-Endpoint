#!/usr/bin/env python

from pyiseers import ERS
import argparse
import logging

logger = logging.getLogger('ISE_ADD')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler('ISE_ADD_DEBUG.log')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

def add_device(args):

    ise = ERS(ise_node=args.host, ers_user=args.username, ers_pass=args.password, verify=False, disable_warnings=True)
    
    exist = ise.get_endpoint(args.mac)['response']
    if 'not found' in exist:
        grp = ise.get_endpoint_group('FILLMEIN')['response']
        res = ise.add_endpoint(name=args.name, mac=args.mac, description=args.description, group_id=grp['id'])
        print(res['response'])
        logger.debug("ADD")
        logger.debug(res)
    else:
        print(exist['mac'] + " already exists")
        print(exist['link']['href'])
        logger.debug("EXIST")
        logger.debug(exist)


if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("mac", help = "Mac Address of Endpoint", type=str)
    parser.add_argument("-host", "--host", help="ISE Server IP or Name", required=True)
    parser.add_argument("-user", "--username", help="ERS Login UserName", required=True)
    parser.add_argument("-password", "--password", help="ERS Login Password", required=True)
    parser.add_argument("-name", "--name", help="Name of Endpoint", default='Default Name')
    parser.add_argument("-desc", "--description", help="Description of Endpoint", default='Default Description')
    args = parser.parse_args()

    add_device(args)