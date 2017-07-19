#! python3

# File Handling Re-writes: 4
# Times I swore 'This is the last time': 2

"""Functions for writing user input to files, and updating entry_count data"""

from __future__ import print_function

import json
import os
import sys
import shutil


class FileIO(object):
    """Mixin class for context managed file read/write operations"""

    @classmethod
    def json_io(cls, write_data=None):
        """write_data is written to file_information.json if provided,
        otherwise, data stored in file_information.json is returned"""
        if not write_data:
            with open(Directory.JSON_PATH, 'r') as f:
                return json.load(f)
        else:
            with open(Directory.JSON_PATH, 'w') as f:
                json.dump(write_data, f, indent=4, sort_keys=True)

    @classmethod
    def standard_io(cls, io_method, write_data=None, file=None):
        """Writes data if write_data is provided, else, file contents returned"""
        if not file:
            file = Directory.get_entry_path()

        with open(file, 'w+') as f:
            io_methods = {'read': f.read, 'readlines': f.readlines,
                          'write': f.write, 'writelines': f.writelines}
            if not write_data:
                return io_methods[io_method]()
            else:
                io_methods[io_method](write_data)


class DataValidation(FileIO):
    @classmethod
    def check_all(cls):
        """Method for performing all checks under DataValidation"""
        cls._check_json()
        cls._check_entry_path()

    @classmethod
    def _check_json(cls):
        """Generates missing json_data directory and file_information.json if they do not exist"""

        if not os.path.exists(os.path.dirname(Directory.JSON_PATH)):
            os.mkdir(os.path.dirname(Directory.JSON_PATH))

        if not os.path.isfile(Directory.JSON_PATH):
            print(">>Program data file not detected | generating new object now.")
            data = {"entry_count": 0, "entry_path": "{}".format(Directory.ENTRY_DEFAULT)}
            cls.json_io(write_data=data)

    @classmethod
    def _check_entry_path(cls):
        """Returns true if entry path folder exists in file_information.json,
        otherwise, default path is set for user in working directory for
        program and method returns False"""

        if not os.path.exists(cls.json_io()['entry_path']):
            print(">>Entry folder location not detected | folder set to: {}"
                  .format(Directory.ENTRY_DEFAULT))
            os.mkdir(Directory.ENTRY_DEFAULT)


class Directory(FileIO):
    """Handles retrieval and updating of file paths"""

    ENTRY_DEFAULT = os.path.abspath(os.path.join(
        os.path.dirname(sys.argv[0]), 'Entries'))

    JSON_PATH = os.path.join(os.path.dirname(sys.argv[0]),
                             'json_data\\file_information.json')

    @classmethod
    def get_entry_path(cls):
        """Returns path of entry folder"""
        return cls.json_io()['entry_path']

    @classmethod
    def set_entry_path(cls, user_path=None, reset_path=False):
        """Changes path to entry folder and copies all current entries to that
        new folder.

        Args:
            user_path (str): contains path to new folder location
            reset_path (bool): if True, path is reset to default entry path

        """
        if reset_path:
            UpdateData.update_data(entry_path=cls.ENTRY_DEFAULT)
            return print("Entry folder reset to: {}".format(cls.ENTRY_DEFAULT))

        if os.path.isdir(user_path) and not reset_path:
            shutil.copytree(Directory.get_entry_path(), user_path)
            UpdateData.update_data(entry_path=user_path)
            return print("Entry folder updated to: {}".format(user_path))


class UpdateData(FileIO):
    """Class for managing file_information.json"""

    @classmethod
    def update_data(cls, entries=0, entry_path=None):
        """Performs action based on passed entry_count or entry_path arguments

        Args:
            entries  (int): Int value of 0 or 1 depending if new entry added
            entry_path (str): string containing path to entry files

        """
        file_data = cls.json_io()

        file_data['entry_count'] += entries
        if entry_path:
            file_data['entry_path'] = entry_path

        cls.json_io(write_data=file_data)

    @classmethod
    def save_entry(cls, entry):
        """Writes user's journal entry and datetime information to a .txt file and
        calls update_data() from UpdateData() to iterate entry count by 1

        Args:
            entry (obj): Object containing formatted text header and filename

        """

        UpdateData().update_data(entries=1)

        filename = os.path.join(Directory.get_entry_path(), entry.filename)
        cls.standard_io('writelines', write_data=entry.document, file=filename)

        print("Entry saved to {}".format(Directory.get_entry_path()))


if __name__ == '__main__':
    # test case(s)
    pass
