import os.path
import shutil


class Backup(object):
    def __init__(self, source_path, backup_path):
        self.source_path = source_path
        self.backup_path = backup_path

    def start(self):
        if not os.path.exists(self.source_path):
            print('%s is not exist' % self.source_path)
            return False

        print('cp %s %s' % (self.source_path, self.backup_path))
        shutil.copy(self.source_path, self.backup_path)
        return True

