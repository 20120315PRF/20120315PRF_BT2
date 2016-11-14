#!/usr/bin/env python

import subprocess


def run_command(command):
	return subprocess.Popen('/bin/bash',
                          stdin=subprocess.PIPE, 
                          stdout=subprocess.PIPE, 
                          shell=True).communicate(command)[0].rstrip('\r\n').strip()

def run_check_nodes(folder_lisk_rake, num_server_to_check_forge):
	#command1 = 'cd '+folder_lisk_rake+' > /dev/null \n'
	command2 = 'rake check_nodes servers='+num_server_to_check_forge
	return run_command(command2)

result = run_check_nodes('$HOME/lisk-rake','1')

def is_forging():
	command = 'echo \"'+result+'\" | egrep "Forging" | cut -d : -f2'
	return run_command(command) 

def get_productivity():
	command = 'echo \"'+result+'\" |egrep "Productivity" | cut -d : -f2'
	return run_command(command)

def get_rank():
	command = 'echo \"'+result+'\" | egrep "Rank" | cut -d : -f2'
	return run_command(command)

def get_name_delegate():
	command = 'echo \"'+result+'\" | egrep "Delegate" | cut -d ":" -f2 | cut -d ")" -f2 | cut -d "[" -f1'
	return run_command(command)

print("Delegado: "+get_name_delegate())
print("Esta forjando: "+is_forging())
print("Productividad: "+get_productivity())
print("Ranking: "+get_rank())

