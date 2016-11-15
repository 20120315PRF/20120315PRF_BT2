#!/usr/bin/env python
import subprocess

from models import delegate_info

def run_command(command):
    return subprocess.Popen('/bin/bash',
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                shell=True).communicate(command)[0].rstrip('\r\n').strip()

def run_check_nodes(folder_lisk_rake, num_server_to_check_forge):
    command2 = 'rake check_nodes servers='+num_server_to_check_forge
    return run_command(command2)

def is_forging(result):
    command = 'echo \"'+result+'\" | egrep "Forging" | cut -d : -f2'
    return run_command(command)

def get_productivity(result):
    command = 'echo \"'+result+'\" |egrep "Productivity" | cut -d : -f2'
    return run_command(command)

def get_rank(result):
    command = 'echo \"'+result+'\" | egrep "Rank" | cut -d : -f2'
    return run_command(command)

def get_name_delegate(result):
    command = 'echo \"'+result+'\" | egrep "Delegate" | cut -d ":" -f2 | cut -d ")" -f2 | cut -d "[" -f1'
    return run_command(command)

## Execute the rake query
def execute_rake_query():
    result = run_check_nodes('$HOME/lisk-rake','1')
    delegate_status = delegate_info.DelegateInfoFactory().generate_delegate(get_name_delegate(result))
    delegate_status['position'] = get_rank(result)
    delegate_status['uptime'] = get_productivity(result)
    delegate_status['status'] = is_forging(result)
    return delegate_status

# Mock rake query for testing
def execute_rake_query_mock():
    delegateStatusMock = delegate_info.DelegateInfoFactory().generate_delegate("theredhawk")
    delegateStatusMock['position'] = '23'
    delegateStatusMock['uptime'] = '99'
    delegateStatusMock['approval'] = '4.3'
    delegateStatusMock['status'] = delegate_info.DelegateInfoStatus.STATUS_CYCLE_LOST
    return delegateStatusMock

