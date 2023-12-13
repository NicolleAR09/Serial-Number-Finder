### Serial Number Finder
This is a Serial Number Finder, which consists of a program that is responsible for searching for serial numbers that meet a certain format, within a tree of folders.

The program will go through all the files and subfolders in a root directory (in this case the .zip), and look for any string that matches a serial number pattern.

Used the os module to open and iterate through the directory, and regular expressions to find the correct serial number format.

For the purposes of this exercise, these are the formatting conditions that findings must meet:
- [N] + [three characters of text] + [-] + [5 numbers]
