#!/usr/bin/env python

from IPython.core.display import display, HTML
display(HTML("<style>.container { width:100% !important; }</style>"))

import requests

from pprint import pprint


from cloudmesh.common.Printer import Printer


order=["full_name", "description",  "open_issues", "created_at", "updated_at"]


def repos(organization):
    entries = []

    page = 0
    while True:
        path = f"https://api.github.com/orgs/{organization}/repos?page={page}&per_page=500"
        r = requests.get(path)
        d = r.json()
        if len(d) == 0:
            break
        else:
            entries.extend(d)
        page = page + 1

    print(Printer.flatwrite(entries, order=order, output='table'))

    print()
    print ("Number of entries:", len(entries))


repos("cloudmesh-community")
repos("cloudmesh")
repos("bigdata-i523")
