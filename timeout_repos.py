"""
Script to look for repositories that have 404s
"""

import csv
import requests

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

for row in rows:
    repository = repositories[rows.index(row)]
    if repository != "N/A" and repository != "Source Code":
        if "git+ssh://git@" in repository:
            repository = repository.replace("git+ssh://git@", "https://")
        if "ssh://" in repository:
            repository = repository.replace("ssh://", "")
        if "git://" in repository:
            repository = repository.replace("git://", "https://")
        if "git@" in repository:
            repository = repository.replace("git@", "https://")
        if "github.com:" in repository:
            repository = repository.replace("github.com:", "github.com/")
        if "git+" in repository:
            repository = repository.replace("git+", "")
        if (
            "https://github.com/git@github.com:UncleBill/vscode-prisme.git.git"
            in repository
        ):
            repository = repository.replace(
                "https://github.com/git@github.com:UncleBill/vscode-prisme.git.git",
                "https://github.com/UncleBill/vscode-prisme.git",
            )
        try:
            r = requests.get(repository, timeout=10)
            print(row)
        except requests.TimeoutError:
            pass
