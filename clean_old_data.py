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

# read in the OLD dataset
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


with open("cleaned_full_allextensions_info.csv", "w", newline="") as csvfile:
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

    previous_repo = "N/A"
    for i in range(len(install_names)):

        display_name = display_names[i]
        extension_name = extension_names[i]
        install_name = install_names[i]
        publisher = publishers[i]
        verified = verified_exts[i]
        stats = installs[i]
        repository = repositories[i]

        if repository == previous_repo:
            print(f"found duplicated repo: {install_name}")
            new_repository = "N/A"
        else:
            # Reset the "previous repository" because we aren't in duplicate land anymore
            previous_repo = repository
            # Save the actual repository name
            new_repository = repository

        spamwriter.writerow(
            [
                display_name,
                extension_name,
                install_name,
                publisher,
                verified,
                stats,
                new_repository,
            ]
        )
