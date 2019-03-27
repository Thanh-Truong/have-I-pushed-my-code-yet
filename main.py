import subprocess
import sys
import os

def have_i_pushed_my_code_yet():
    message = ''
    last_commit_pushed = os.system('test "$(git rev-parse @{u})" = "$(git rev-parse HEAD)"')    
    if last_commit_pushed != 0:
        message = 'ERROR The last commit has not been pushed yet'
    no_unstaged_files = os.system('test "$(git diff --name-only)" = ""')
    if no_unstaged_files != 0:
        message = 'ERROR There are unstaged files'    
    return last_commit_pushed + no_unstaged_files, message

def main():
    errorcode, message = have_i_pushed_my_code_yet()
    if errorcode !=0:
        print(message)
        sys.exit(1)

if __name__ == "__main__":
    main()
