#!/usr/bin/env python3

from geoip import geolite2
from datetime import datetime
import subprocess
import re

SYSLOG = "/home/student/syslog.log"
IP = re.compile(r"Failed password.*from (?P<ip>\d+\.\d+\.\d+\.\d+)")
DICT = {}

def parse_syslog(filename):
    # parse the syslog file to analyze logins
   
    # graceful error handling
    try: 
        # opens the file (and closes when done)
        with open(filename) as file:

            # iterate through each line in the file
            for line in file:
            
                regex = IP.search(line)
                if regex:
                    ip = regex.group("ip")
                    if not(ip in DICT):
                        DICT[ip] = 1
                    else:
                        DICT[ip] += 1
    
    # captures FNF exception
    except FileNotFoundError:
        print("That file does not exist!")

def find_country(ip):
    # finds the country from an ip address

    match = geolite2.lookup(ip)
    country = match.country
    
    return country


def main():

    # clear the terminal before starting 
    subprocess.call("clear", shell=True)

    # prints header
    today = datetime.now().strftime('%B %d, %Y')
    print("\033[31m\033[1mAttacker Report -\033[0m", today, "\n")

    # prints columns 
    print("\033[32m\033[1mCOUNT\tIP ADDRESS\tCOUNTRY\033[0m")

    # calls parsing function to read syslog    
    parse_syslog(SYSLOG)
    
    # sorts the dictionary by values (login attempts)
    my_list = sorted(DICT.items(), key=lambda x:x[1])
    my_dict = dict(my_list)

    # iterate over the sorted dictionary
    for key in my_dict:
        if (my_dict[key] >= 10):
            print(my_dict[key], "\t", key, "\t", find_country(key), sep="")

if __name__ == "__main__":
    main()
