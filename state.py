#!/usr/bin/env python

import sys
import json
from pprint import pprint

def main():
    state = None

    with open(sys.argv[1]) as f:
        state = json.load(f)

    with open(sys.argv[2]) as f:
        update_functions = json.load(f)

    for key, f_str in update_functions.items():
        f = eval(f_str)
        try:
            state[key] = f(state[key])
        except KeyError:
            state[key] = f(None)

    pprint(json.dumps(state))

if __name__ == '__main__':
    main()
