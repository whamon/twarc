#!/usr/bin/env python

"""
Print out the URLs in a tweet json stream.
"""
from __future__ import print_function

import sys
import json
import fileinput

for line in fileinput.input():
    tweet = json.loads(line)
    for url in tweet["entities"]["urls"]:
        if 'unshortened_url' in url:
            sys.stdout.write(url['unshortened_url'] + "\n")
        elif url.get('expanded_url'):
            sys.stdout.write(url['expanded_url'] + "\n")
        elif url.get('url'):
            sys.stdout.write(url['url'] + "\n")
