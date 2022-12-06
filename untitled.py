import requests

repository = "https://github.com/ovsky/vscode-csharpfixformat"
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
    try:
        r = requests.get(repository, timeout=10)
        print(r.status_code)
        if r.status_code == 404:
            print(repository)
    except:
        print(repository)
