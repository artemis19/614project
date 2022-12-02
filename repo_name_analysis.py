"""
Script to look for extensions where source code repository link does not contain extension or publisher names
"""

import csv

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

total_extensions_looped_over = 0
# Start with ALL of the new extensions base
for i in range(len(install_names)):

    total_extensions_looped_over += 1

    # Grab the install name to use as a key for both old and new datasets
    extension = extension_names[i].lower()
    publisher = publishers[i].lower()
    install = install_names[i].lower()
    verified_ext = verified_exts[i]
    row = rows[i]
    repository = repositories[i].lower()
    ext_pieces = []
    # But grab the NEW repository for this extension entry

    if repository != "n/a":
        if verified_ext == "False":
            # print(verified_ext)
            if not extension in repository:
                ext_pieces += publisher.split()
                ext_pieces += publisher.split(".")
                ext_pieces += publisher.split("-")
                ext_pieces += install.split()
                ext_pieces += install.split(".")
                ext_pieces += install.split("-")
                ext_pieces += extension.split()
                ext_pieces += extension.split(".")
                ext_pieces += extension.split("-")
                good = False
                # print(repository)
                for piece in ext_pieces:
                    # print(piece)
                    if piece in repository:
                        good = True
                        continue
                if not good:
                    print(row)
