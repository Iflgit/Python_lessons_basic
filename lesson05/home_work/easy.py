import os


def md(root_dir, dirname):
    _md = os.path.join(root_dir, dirname)
    try:
        os.mkdir(_md)
        print(f'+{_md} created')
    except FileExistsError:
        print(f'directory {_md} exist')


def rd(root_dir, dirname):
    _rd = os.path.join(root_dir, dirname)
    try:
        os.rmdir(_rd)
        print(f'-{_rd} deleted')
    except FileNotFoundError:
        print(f'directory {_rd} not found')
    except PermissionError:
        print(f'directory {_rd} permission error')


def cd(root_dir, dirname):
    _cd = os.path.join(root_dir, dirname)
    try:
        os.chdir(_cd)
        print(f'path changed to {_cd}')
    except FileNotFoundError:
        print(f'directory {_cd} not found')


def dir(dirname):
    for file in os.listdir(dirname):
        print(file)


def quit(code):
    exit(0)
