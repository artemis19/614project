Project TODO
-------------

1. Jasmine: Automate analysis of repositories
	1. Generate possible list for manual analysis
2. Kaitlyn: Extension automation stuff
	1. Get all possible extensions from the marketplace - done
	2. Look for potential typosquating in extension names - done
	3. Generate list of extensions where name/publisher differs from that of repo name?
3. Jason
	1. List of potential things to look for in repositories that might be doing weird stuff
	2. Data analysis?
4. Do experiments
5. Data analysis
	1. Highlight key result/analysis points for paper
	2. Graphics to display results
	3. % of extensions that are verified vs not
	4. % of extensions where repo names did not match extension install names
		1. What portion of these are not verified?
		2. Install counts?
	5. Some of these extensions are no longer maintained and/or source repos no longer exist -> Should be removed from the store!

# Extensions

1. CSV of all extensions from the Marketplace as of Nov-19-2022: `full_allextensions_info.csv`
2. List of similar extensions based on 1-2 character differences: `similar_extensions`

# Workflow Automation - Environment Setup (NEED TO UPDATE)

VSCode Linux Setup: [https://code.visualstudio.com/docs/setup/linux](https://code.visualstudio.com/docs/setup/linux)

Open it once with a random folder or file to accept the "Workspace Trust" pop-up.

Fresh install of [Visual Studio Code](https://code.visualstudio.com/)

Install automation tool:

```sh
sudo apt install xautomation
```

Scripts for setup & start-up:

```sh
setup.sh
start.sh
```
