Project TODO
-------------

1. Jasmine: Automate analysis of repositories
	1. Generate list of potentially suspicious repos
2. Kaitlyn: Extension automation stuff
	1. Get all possible extensions from the marketplace - Nov 21, 2022
	2. Look for potential typosquating by extension and install names - done
	3. Generate list of extensions where name/publisher differs from that of repo name?
3. Jason
	1. Upload findings from similar extension comparisons
	2. Continue finer-grained analysis
4. Data analysis
	1. Highlight key result/analysis points for paper
		1. Extensions that possibly go against use policy (i.e. illegal movie downloads?)
		2. % of similar extensions by install name -- need to manually verify
		3. Any interesting ones Jason found and overall counts for stuff he pulled out
	2. Graphics / Tables
		1. General counts of the VSCode marketplace extension landscape
		2. Workflow figure
		3. Figures of VSCode extensions that are similar (i.e. kinda show form of typosquatting?) -> Comparison of install counts between pairs?
	3. % of extensions that are verified vs not
	4. % of extensions where repo names did not match extension install names
		1. What portion of these are not verified?
		2. Install counts?
	5. Some of these extensions are no longer maintained and/or source repos no longer exist -> Should be removed from the store!

# Extensions

1. CSV of all extensions from the Marketplace as of Nov-19-2022: `full_allextensions_info.csv`
2. List of similar extensions based on 1-2 character differences for the extension name: `similar_extensions_by_ext_name`
3. List of similar extensions based on 1-2 character differences for the install name: `similar_ext_by_install_name`
4. List of extensions that are deprecated or unmaintained `deprecated_extensions`
5. List of extensions where the extension name, install name, and publisher do not appear in the source code repository listed (when available): `repo_name_analysis`

## Workflow Automation - Environment Setup (OLD)

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
