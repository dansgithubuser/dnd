import code
import os
import re
from urllib.error import URLError
from urllib.request import Request, urlopen

#===== consts =====#
TERMINAL_WIDTH = 80

#===== functions =====#
def ls():
    return sorted(os.listdir())

def match_extensions(path, extensions):
    if not extensions: return True
    for extension in extensions:
        if path.endswith('.' + extension):
            return True
    return False

def fzf(path, extensions=None):
    l = ls() + ['..']
    for i in l:
        if i == path and match_extensions(i, extensions):
            return i
    if re.match("'.*'$", path):
        pat = path[1:-1]
    else:
        pat = '.*'.join(path)
    for i in l:
        if re.match(pat, i) and match_extensions(i, extensions):
            return i
    else:
        print(f'nothing matched {path}')

def post(path):
    try:
        urlopen(Request(f'http://localhost:8000/{path}', method='POST'))
    except URLError as e:
        print(e)

#===== user functions =====#
def user_ls():
    l = ls()
    col_size = max(len(i) for i in l) + 4
    fmt = f'{{:>{col_size}}}'
    x = 0
    for i in l:
        print(fmt.format(i), end='')
        x += col_size
        if x + col_size >= 80:
            print('')
            x = 0
    print('')

def user_cd(path):
    path = fzf(path)
    if not path: return
    os.chdir(path)
    print(os.getcwd())
    print()
    user_ls()

def user_fullscreen():
    post('fullscreen')

user_f = user_fullscreen

def user_present(path):
    path = fzf(path, ['jpg', 'png'])
    if not path: return
    path = os.path.abspath(path)
    post(f'present?path={path}')

user_p = user_present

#===== main =====#
def main(args):
    code.interact(local={
        k.removeprefix('user_'): v
        for k, v in globals().items()
        if k.startswith('user_')
    })
