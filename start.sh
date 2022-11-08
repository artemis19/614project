#!/bin/bash

# Defining functions for mouse/keyboard input
function alt_tab(){
	xte "keydown Alt_L" "keydown Tab" "keyup Alt_L" "keyup Tab"
	sleep 0.5
}

function ctrl(){
	xte "keydown Control_L" "key $1" "keyup Control_L"
}

function ctrl_shift(){
	xte "keydown Control_L" "keydown Shift_L" "key $1" "keyup Shift_L" "keyup Control_L"
}

function str(){
	xte "str $1"
}

function enter(){
	xte "keydown Return" "keyup Return"
}

function tab(){
	xte "keydown Tab" "keyup Tab"
}

function arrow_down(){
	xte "keydown Down" "keyup Down"
}

# Extensions to test
extensions=("ms-python.python" "ms-toolsai.jupyter" "ms-python.vscode-pylance" "ms-vscode.cpptools" "ms-toolsai.jupyter-keymap" "ms-toolsai.jupyter-renderers" "ritwickdey.LiveServer" "esbenp.prettier-vscode" "VisualStudioExptTeam.vscodeintellicode" "dbaeumer.vscode-eslint" "redhat.java" "MS-CEINTL.vscode-language-pack-zh-hans" "ms-azuretools.vscode-docker" "ms-dotnettools.csharp" "eamodio.gitlens" "vscjava.vscode-java-debug" "vscjava.vscode-maven" "ms-vscode-remote.remote-wsl" "vscjava.vscode-java-test" "formulahendry.code-runner" "vscjava.vscode-java-pack" "vscjava.vscode-java-dependency" "ms-vscode-remote.remote-containers" "PKief.material-icon-theme" "twxs.cmake" "ms-vscode.cmake-tools" "ms-vscode-remote.remote-ssh" "vscode-icons-team.vscode-icons" "ecmel.vscode-html-css" "ms-vscode.cpptools-themes" "ms-vscode-remote.remote-ssh-edit" "octref.vetur" "formulahendry.auto-rename-tag" "ms-vscode.cpptools-extension-pack" "MS-vsliveshare.vsliveshare" "xabikos.JavaScriptSnippets" "redhat.vscode-yaml" "jeff-hykin.better-cpp-syntax" "msjsdiag.debugger-for-chrome" "cschlosser.doxdocgen" "HookyQR.beautify" "abusaidm.html-snippets" "formulahendry.auto-close-tag" "christian-kohler.path-intellisense" "GitHub.vscode-pull-request-github" "ms-toolsai.vscode-jupyter-cell-tags" "ms-toolsai.vscode-jupyter-slideshow" "golang.Go" "xdebug.php-debug" "bmewburn.vscode-intelephense-client" "donjayamanne.githistory" "ms-vscode.PowerShell" "techer.open-in-browser" "dsznajder.es7-react-js-snippets" "zhuangtongfa.Material-theme" "EditorConfig.EditorConfig" "eg2.vscode-npm-script" "VisualStudioExptTeam.intellicode-api-usage-examples" "GitHub.github-vscode-theme" "Dart-Code.dart-code" "streetsidesoftware.code-spell-checker" "Zignd.html-css-class-completion" "CoenraadS.bracket-pair-colorizer-2" "ms-mssql.mssql" "yzhang.markdown-all-in-one" "batisteo.vscode-django" "Dart-Code.flutter" "christian-kohler.npm-intellisense" "tht13.python" "ms-vscode.azure-account" "MS-CEINTL.vscode-language-pack-ja" "wholroyd.jinja" "MS-vsliveshare.vsliveshare-audio" "dracula-theme.theme-dracula" "naumovs.color-highlight" "TabNine.tabnine-vscode" "austin.code-gnu-global" "DavidAnson.vscode-markdownlint" "vscodevim.vim" "Angular.ng-template" "oderwat.indent-rainbow" "DotJoshJohnson.xml" "donjayamanne.python-extension-pack" "aaron-bond.better-comments" "akamud.vscode-theme-onedark" "mhutchie.git-graph" "ms-vscode.vscode-typescript-tslint-plugin" "pranaygp.vscode-css-peek" "xdebug.php-pack" "shd101wyy.markdown-preview-enhanced" "Shan.code-settings-sync" "johnpapa.Angular2" "magicstack.MagicPython" "redhat.vscode-xml" "mikestead.dotenv" "njpwerner.autodocstring" "MS-CEINTL.vscode-language-pack-es" "lonefy.vscode-JS-CSS-HTML-formatter" "awwsky.csharpfixformatfixed" "KevinRose.vsc-python-indent" "ms-vscode-remote.vscode-remote-extensionpack" "msjsdiag.vscode-react-native" "ms-python.isort" "wayou.vscode-todo-highlight" "rebornix.Ruby" "alefragnani.project-manager" "humao.rest-client" "platformio.platformio-ide")

# Projects to test
# projects=("https://github.com/MubertAI/Mubert-Text-to-Music" "https://github.com/snyk-labs/nodejs-goof" "https://github.com/microsoft/calculator" "https://github.com/jenkins-docs/simple-java-maven-app" "https://github.com/farzadForoozanfar/MineSweeper" "https://github.com/Kao19/GUI-Bash-Calculator")

# read answer

# choice=${projects[$answer]}

# # echo "$choice"

# output_dir="test"

# # Download repository
# git clone $choice $output_dir

# # Move into repository
# # Will need to save previous choice to move into correct directory
# cd $output_dir

for i in {0..${#extensions[@]}}
do
	# Install given extension
	# code --install-extension ${extensions[$i]}

	# Start VSCode
	code . &

	# # Wait for VSCode to start
	# # This is unreliable... might want to just make this annoyingly large for testing
	sleep 4

	# # Open extension
	ctrl_shift X

	# Search for extension
	str ${extensions[$i]}

	# Select extension box
	tab

	# Select top result
	arrow_down

	# Select "Instal" option
	tab

	# Install extension
	enter

	# Sleep
	sleep 20

	# Close VSCode
	ctrl Q

	# Uninstall extension through CLI
	code --uninstall-extension ${extensions[$i]}
done