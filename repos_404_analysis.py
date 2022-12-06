"""
Script to look for repositories that have 404s, timeouts, or weird values for their listed source
"""

import csv
import requests
from requests import ReadTimeout, ConnectTimeout, HTTPError, Timeout, ConnectionError
import time

display_names = []
extension_names = []
install_names = []
publishers = []
verified_exts = []
installs = []
repositories = []
similar_exts = {}
rows = []

with open("full_allextensions_info.csv", newline="") as csvfile:

    spamreader = csv.reader(csvfile, delimiter=",", quoting=csv.QUOTE_ALL)

    for row in spamreader:
        (
            display_name,
            extension_name,
            install_name,
            publisher,
            verified,
            stats,
            repository,
        ) = row

        rows.append(str(row))

        display_names.append(display_name)
        extension_names.append(extension_name)
        install_names.append(install_name)
        publishers.append(publisher)
        verified_exts.append(verified)
        installs.append(stats)
        repositories.append(repository)

for i, row in enumerate(rows):
    if i < 34438:
        continue
    repository = repositories[rows.index(row)]
    # repository = "git clone https://daniele_mabiloft@bitbucket.org/mabiloft/grapes-vscode-extension.git"
    if repository != "N/A" and repository != "Source Code":
        if "git+ssh://git@" in repository:
            repository = repository.replace("git+ssh://git@", "https://")
        if "ssh://git@" in repository:
            repository = repository.replace("ssh://git@", "https://")
        if "ssh://" in repository:
            repository = repository.replace("ssh://", "")
        if "git://" in repository:
            repository = repository.replace("git://", "https://")
        if "svn://" in repository:
            repository = repository.replace("svn://", "https://")
        if "github:" in repository:
            repository = repository.replace("github:", "")
        # if "git@" in repository:
        #     repository = repository.replace("git@", "https://")
        # if "github.com:" in repository:
        #     repository = repository.replace("github.com:", "github.com/")
        if "git+" in repository:
            repository = repository.replace("git+", "")
        if "git:" in repository:
            repository = repository.replace("git:", "")
        if "at:" in repository:
            repository = repository.replace("at:", "at/")
        # if ".com:" in repository:
        #     repository = repository.replace(".com:", ".com/")
        if "git@github.com:" in repository:
            repository = repository.replace("git@github.com:", "")
        if "https: //" in repository:
            repository = repository.replace("https: //", "https://")
        if "hhttp" in repository:
            repository = repository.replace("hhttp", "http")
        if "http:/https://" in repository:
            repository = repository.replace("http:/https://", "https://")
        if "https:www" in repository:
            repository = repository.replace("https:www.", "https://")
        if "git@code.byted.org:" in repository:
            repository = repository.replace("git@code.byted.org:", "")
        if "com:" in repository:
            repository = repository.replace("com:", "com/")
        if "git@ssh." in repository:
            repository = repository.replace("git@ssh.", "")
        if "git@gitee.com:" in repository:
            repository = repository.replace("git@gitee.com:", "")
        if "git remote add origin " in repository:
            repository = repository.replace("git remote add origin ", "")
        if "git clone " in repository:
            repository = repository.replace("git clone ", "")
        if (
            "https://github.com/git@github.com:UncleBill/vscode-prisme.git.git"
            in repository
        ):
            repository = repository.replace(
                "https://github.com/git@github.com:UncleBill/vscode-prisme.git.git",
                "https://github.com/UncleBill/vscode-prisme.git",
            )
        if "https:/example.com" in repository:
            repository = repository.replace("https:/example.com", "https://example.com")
        if "https:/github.com/cdonke/github-explorer" in repository:
            repository = repository.replace(
                "https:/github.com/cdonke/github-explorer",
                "https://github.com/cdonke/github-explorer",
            )
        if repository.startswith("github.com"):
            repository = "https://" + repository
        # print(repository)
        if "http" not in repository:
            print(row)
            continue
        time.sleep(0.1)
        try:
            r = requests.get(repository, timeout=10)
            # print(r.status_code)
            if r.status_code == 404:
                print(row)
        except (Timeout, requests.exceptions.ConnectionError) as e:
            print(row)
