import requests
import csv
import json


def request_pages(page_num=1, page_size=800):
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

extensions = request_pages(1)["results"][0]["extensions"]

with open("extensions_top800.csv", "w", newline="") as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=",", quoting=csv.QUOTE_ALL)
    spamwriter.writerow(
        ["Extension Name", "Publisher", "Verified", "Install Count", "Source Code"]
    )

    for extension in extensions:
        publisher = extension["publisher"]["displayName"]
        verified = extension["publisher"]["isDomainVerified"]
        display_name = extension["displayName"]
        stats = extension["statistics"][0]["value"]
        properties = extension["versions"][0]["properties"]
        repository = "N/A"

        for i in properties:
            if i["key"].endswith(".Source"):
                repository = i["value"]
                break

        spamwriter.writerow([display_name, publisher, verified, stats, repository])
