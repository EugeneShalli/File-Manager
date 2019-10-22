import win32file, win32api
import os

import win32con


class Manager:

    def __init__(self):
        pass

    # Get drives
    def process1(self):
        drivebits = win32file.GetLogicalDrives()
        drives = win32api.GetLogicalDriveStrings()
        drives = drives.split('\000')[:-1]
        print(drives)
        print(bin(drivebits), "\n")

    # Get info about drive
    def process2(self):
        drivetype = {
            0: 'DRIVE_UNKNOWN',
            1: 'DRIVE_NO_ROOT_DIR',
            2: 'DRIVE_REMOVABLE',
            3: 'DRIVE_FIXED',
            4: 'DRIVE_REMOTE',
            5: 'DRIVE_CDROM',
            6: 'DRIVE_RAMDISK'
        }
        type = win32file.GetDriveType(win32api.GetLogicalDriveStrings())
        print(drivetype[type], "\n")

        volume = win32api.GetVolumeInformation(win32api.GetLogicalDriveStrings())
        print(volume, "\n")

        space = win32file.GetDiskFreeSpace(win32api.GetLogicalDriveStrings())
        print(space, '\n')

    # Manipulate the directory
    def process3(self):

        answer3 = 5

        while answer3 != '10':
            print('1 - To create directory\n'
                  '2 - To remove directory\n'
                  '10 - To exit to menu')

            answer3 = input()

            if answer3 == '1':
                print("Enter the name of directory\n")
                directory = input()
                win32file.CreateDirectory(directory, None)

            elif answer3 == '2':
                print("Enter the name of directory to delete\n")
                directory = input()
                win32file.RemoveDirectory(directory, None)
        answer = 9

    # Creating new files
    def process4(self):
        print("Enter the name of file to create\n")
        win32file.CreateFile(input(),
                             win32file.GENERIC_WRITE,
                             0,
                             None,
                             win32con.CREATE_NEW,
                             0,
                             None)

    # Manipulate files
    def process5(self):
        answer5 = 5

        while answer5 != '10':
            print('1 - To copy file\n'
                  '2 - To move file\n'
                  '3 - '
                  '10 - To exit to menu')

            answer5 = input()

            if answer5 == '1':
                print("Enter the name of file to copy and the name of new file\n")
                win32api.CopyFile(input(), input(), 0)

            elif answer5 == '2':
                print("Enter the name of file and the directory to move\n")
                win32api.MoveFile(input(), input())

    def process6(self):
        pass

    def dispatch(self, value):
        method_name = 'process' + str(value)
        method = getattr(self, method_name)
        return method()


answer = 9

X = Manager()

while answer != 0:

    print("Choose option:\n"
          "1 - To see drives list\n"
          "2 - To see info about the drive\n"
          "3 - To create and delete directories\n"
          "4 - To create files\n"
          "5 - To copy and move files\n"
          "6 - To analyse changes in attributes\n"
          "0 - To exit\n")

    answer = input()

    try:
        X.dispatch(answer)
    except ValueError as e:
        raise ValueError('Undefined unit: {}'.format(e.args[0]))
