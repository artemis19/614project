"""
Script to scrape all extensions from VSCode Marketplace
"""

import requests
import csv
import json


def request_pages(page_num=1, page_size=54):
    json_data = {
        "filters": [
            {
                "criteria": [
                    {
                        "filterType": 8,
                        "value": "Microsoft.VisualStudio.Code",
                    },
                    {
                        "filterType": 10,
                        "value": 'target:"Microsoft.VisualStudio.Code" ',
                    },
                    {
                        "filterType": 12,
                        "value": "37888",
                    },
                ],
                "direction": 2,
                "pageSize": page_size,
                "pageNumber": page_num,
                "sortBy": 4,
                "sortOrder": 0,
                "pagingToken": None,
            },
        ],
        "flags": 870,
    }

    response = requests.post(
        "https://marketplace.visualstudio.com/_apis/public/gallery/extensionquery",
        json=json_data,
    )

    return response.json()


extension_num = 0

with open("full_allextensions_info.csv", "w", newline="") as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=",", quoting=csv.QUOTE_ALL)
    spamwriter.writerow(
        [
            "Display Name",
            "Extension Name",
            "Install Name",
            "Publisher",
            "Verified",
            "Install Count",
            "Source Code",
        ]
    )

    for i in range(1, 43):
        extensions = request_pages(i, 1000)["results"][0]["extensions"]

        for extension in extensions:
            publisher = extension["publisher"]["displayName"]
            verified = extension["publisher"]["isDomainVerified"]
            display_name = extension["displayName"]
            publisher_name = extension["publisher"]["publisherName"]
            install_name = publisher_name + "." + extension["extensionName"]
            extension_name = extension["extensionName"]
            stats = 0
            repository = "N/A"
            try:
                stats = extension["statistics"][0]["value"]
            except:
                pass
            try:
                properties = extension["versions"][0]["properties"]
                for i in properties:
                    if i["key"].endswith(".Source"):
                        repository = i["value"]
                        break
            except:
                repository = "N/A"
                pass

            spamwriter.writerow(
                [
                    display_name,
                    extension_name,
                    install_name,
                    publisher,
                    verified,
                    stats,
                    repository,
                ]
            )
