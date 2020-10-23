# importing os module
import os

# Get all files of the "_route" path
def list_directory(_route):
    files = [a for a in os.listdir(_route)]
    return files

# Sort files by date
def orderByDate(_route):
    files = [a for a in os.listdir(_route)]
    files.sort(key=os.path.getctime)
    return files

# Sort files alphabetically
def orderByName(_route):
    files = [a for a in os.listdir(_route)]
    files.sort()
    return files

# Get directory containing file
def getDirectory(_route):
    _route = os.getcwd()
    _route = _route.strip("/")
    _route = _route.split("/")
    _route = _route[-1]
    return _route