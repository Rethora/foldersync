import shutil

from config import sync


def sync_up():
    for x in sync:
        s = x['watch']
        d = x['sync_to']
        print(f'Syncing {s} to {d}')
        shutil.copytree(s, d, symlinks=False, ignore=shutil.ignore_patterns('*.psd', '*.psdc'))


if __name__ == '__main__':
    sync_up()
    print('Done')
    input('Press Enter to quit...')
    exit()
