import os
import shutil

from config import sync


def is_file_hidden(p):
    if os.name== 'nt':
        import win32api, win32con
        attribute = win32api.GetFileAttributes(p)
        return attribute & (win32con.FILE_ATTRIBUTE_HIDDEN | win32con.FILE_ATTRIBUTE_SYSTEM)
    else:
        return p.startswith('.') #linux-osx


def ignore_func(path, files):
    ignored = []
    for f in files:
        filepath = os.path.join(path, f)
        if is_file_hidden(filepath):
            ignored.append(filepath)

    return ignored

def sync_up():
    for x in sync:
        s = x['watch']
        d = x['sync_to']
        print(f'Syncing {s} to {d}')
        shutil.copytree(s, d, symlinks=False, ignore=ignore_func, dirs_exist_ok=True)


if __name__ == '__main__':
    sync_up()
    print('Done')
    input('Press Enter to quit...')
    exit()
