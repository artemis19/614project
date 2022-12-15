# Identifying Anomalies in the VSCode Marketplace

This repo contains all of scripts and datasets that we used to perform our experiments and analyses. Below is an outline of the important files that contain the specific extension data.

## Findings & Results

1. CSV of all extensions from the Marketplace as of Nov-21-2022: `full_allextensions_info.csv`
2. List of similar extensions based on 1-2 character differences for the extension name ONLY: `similar_extensions_by_ext_name`
3. List of similar extensions based on 1-2 character differences for the install name: `similar_ext_by_install_name`
4. Manual analysis of similar extensions: `Data Analysis.xlsx`
5. List of extensions where the extension name, install name, and publisher do not appear in the source code repository listed (when available): `repo_name_analysis_new`
6. 404's, timeouts, unavailable repos: `repos_404_timesouts_final`
	1. This link was used for multiple extensions: `ssh://git@gitlab.xiaxuechao.com:902/vscode/laravel-extension-pack.git`
	2. Weird source: `https://www.520stone.com`
	3. Empty repo but does resolve: `github.com/jakubDoka/metaflow`
7. Analysis of source code for top-800 extensions: `top_800_code_analysis.csv`