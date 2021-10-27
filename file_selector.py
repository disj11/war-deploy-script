from os import listdir
from os.path import isfile, join


class FileSelector(object):
    def __init__(self, directory):
        self.directory = directory

    def _print(self):
        for i, f in enumerate(self.get_files()):
            print('{:3d}. {:30s}'.format(i + 1, f))
        print('{:3d}. {:30s}'.format(0, 'exit'))

    def _get_count_number_of_files(self):
        return len(self.get_files())

    def _get_absolute_path(self, file):
        return join(self.directory, file)

    def get_files(self):
        return [f for f in listdir(self.directory) if isfile(self._get_absolute_path(f))]

    def get_all(self):
        return listdir(self.directory)

    def select(self, text):
        print('___________________________________________')
        self._print()
        print('___________________________________________')
        number = int(input(text))
        if number == 0:
            exit()
        return self._get_absolute_path(self.get_files()[number - 1])
