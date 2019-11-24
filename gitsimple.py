#!/usr/bin/env python
import locale
import subprocess
from pathlib import Path
import inspect
import os
import sys

def get_script_dir(follow_symlinks=True):
    if getattr(sys, 'frozen', False): # py2exe, PyInstaller, cx_Freeze
        path = os.path.abspath(sys.executable)
    else:
        path = inspect.getabsfile(get_script_dir)
    if follow_symlinks:
        path = os.path.realpath(path)
    return Path(path).parent

CWD = get_script_dir()
git_path = str(CWD / r'git/cmd/git.exe')


# locale.set(locale.getpreferredencoding())
# print(locale.getpreferredencoding())
# print(sys.getdefaultencoding())
# print (sys.stdout.encoding)
def git_process(*args):
    print(args)
    print(all(map(isinstance, *args)))
    subprocess.run([git_path, *args], cwd=CWD, shell=False, check=True, encoding='utf8')

class Git:
    def __init__(self, repo_path):
        os.chdir(repo_path)

    def commit(self, args):
        git_process('commit', args)

    def init(self):
        git_process('init')

if __name__ == '__main__':
    git = Git(r'D:\pylerning\yandex_test\repo')
    git.init()