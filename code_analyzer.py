"""
Script to analyze code from a cloned extension repository
"""

import csv
import subprocess
import os
import re

analysis_patterns = ["crypto", "dns", "fs", "http", "os",
                     "path", "tls", "dgram", "zlib", "cluster", "process"]

repo_regex = re.compile(".*/(.*)")

subprocess.run(["rm", "-rf", "repos"])
os.mkdir("repos")
os.chdir("repos")

with open("../full_allextensions_info.csv", newline="") as csvfile:
    with open("../code_analysis.csv", mode="x") as output:
        cvsdata = csv.reader(csvfile, delimiter=",", quoting=csv.QUOTE_ALL)
        cvsout = csv.writer(output, delimiter=",", quoting=csv.QUOTE_ALL)

        cvsout.writerow(["Display Name", "Extension Name",
                        "Install Name"] + analysis_patterns)

        for row in cvsdata:
            (
                display_name,
                extension_name,
                install_name,
                publisher,
                verified,
                stats,
                repository,
            ) = row

            folder = repository.replace(".git", "")
            folder = repo_regex.search(folder)
            if folder == None:
                print("FAILURE: " + display_name)
                continue
            folder = folder.group(1)

            subprocess.run(["git", "clone", repository,
                           "--depth=1"], capture_output=True)

            results = []
            for pattern in analysis_patterns:
                o = subprocess.run(
                    [
                        "grep", "-r", "--include=*\.[jt]s", "--exclude-dir=*test*",  "--exclude-dir=*tst*", "--exclude-dir=*build*",
                        "--exclude-dir=*types*", "--exclude-dir=\.github*", pattern, folder
                    ],
                    capture_output=True
                )
                matched = len(o.stdout) != 0
                results.append(matched)

                if matched:
                    print(folder + ", " + pattern)
                    print(o.stdout)
                    print()

            subprocess.run(["rm", "-rf", folder])

            cvsout.writerow([display_name, extension_name,
                            install_name] + results)
            output.flush()
