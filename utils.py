import os

def is_windows():
   return os.name == "nt" 

file_regex = r"[\\\/:\*\?\"<>\|]"