# Title:
# Description: Create Ingress Rule
# Author: Ayo Salawu
# Date: February 27, 2020
# ===============================================================================

# Import required modules

import argparse, json, datetime, threading

# Date and Header
date = datetime.datetime.now()

# Add some color
BLUE = "\033[1;34m"
GREEN = "\033[1;32m"
RED = "\033[1;31m"
YELLOW = "\033[1;33m"
NORMAL = "\033[0;0m"
BOLD = "\033[1m"


def create_dictionary(file_name):
    with open(file_name) as k:
        param_dict = json.load(k)
    return param_dict
param_dict = create_dictionary('params.json')
print(param_dict)


# Fancy animation (tweaked from Stack..)
done = False
def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write(YELLOW + '\rParsing ' + c + NORMAL)
        sys.stdout.flush()
        time.sleep(0.1)
    #sys.stdout.write(GREEN + '\rDone. ' + NORMAL)

t = threading.Thread(target=animate)

# Output what is going to happen
print(BLUE + "The Files you requested are above: " + NORMAL + BOLD + NORMAL)