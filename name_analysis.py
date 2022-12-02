"""
Script to look for potential typosquatting in VSCode IDE extensions by name and install name
"""
import csv
from Levenshtein import distance as l_distance
import itertools

display_names = []
extension_names = []
install_names = []
publishers = []
verified_exts = []
installs = []
repositories = []
similar_exts = {}

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

        display_names.append(display_name)
        extension_names.append(extension_name)
        install_names.append(install_name)
        publishers.append(publisher)
        verified_exts.append(verified)
        installs.append(stats)
        repositories.append(repository)

for p in itertools.combinations(install_names, 2):
    distance = l_distance(p[0], p[1])
    if distance < 3 and distance != 0:
        if distance not in similar_exts.keys():
            similar_exts[distance] = []
        else:
            similar_exts[distance].append(p)
            print(distance, p)
