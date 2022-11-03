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

# Download repository
# Would need to swap these out dependent on the chosen language
git clone https://github.com/ShaifArfan/react-todo-app

# Move into repository
# Will need to save previous choice to move into correct directory
cd react-todo-app/

# Start VSCode
# Kali needed code-oss so this might depend on architecture
code . &

# Wait for VSCode to start
# This is unreliable... might want to just make this annoyingly large for testing
sleep 4

# Open new file
ctrl N

# Open command window
# ctrl_shift P

# Write some code
str "Hello World"

# Wait to make sure new file is made
sleep 4

# Save project
ctrl S

# Wait for file explorer to pop up
sleep 4

# Name new file
str "test.md"

# Save file
enter