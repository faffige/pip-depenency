import os, random, string
from pathlib import Path

#create a new random dir
def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

#Get the current directory
dirpath = os.getcwd()
#Get the parent directory
parentDir = Path(dirpath).parent
#Generate a random string for a folder name
folderName = randomString()
#Build string of the new path
newDir = "{}/{}".format(parentDir, folderName)

# Create target Directory if don't exist
if not os.path.exists(newDir):
  os.mkdir(newDir)
  print("Directory " , newDir ,  " Created ")
else:    
  print("Directory " , newDir ,  " already exists")

#Change to the temp directory
os.chdir(newDir)

#Build commands that need to be run
venv = 'virtualenv venv'
pipInstall = 'pip install requests'
freeze = 'pip freeze > requirements.txt'

#Start running commands
os.system(venv)
activate_this_file = "{}/venv/bin/activate_this.py".format(newDir)

with open(activate_this_file) as f:
    code = compile(f.read(), activate_this_file, 'exec')
    exec(code)

os.system(pipInstall)
os.system(freeze)
os.system('deactivate')

#Read the result of pip freeze
f=open("requirements.txt", "r")
if f.mode == 'r':
    contents =f.read()
    print(contents)

# remove target directory if it exists
if os.path.exists(newDir):
  os.rmdir(newDir)
  print("Directory " , newDir ,  " removed ")
else:    
  print("Directory " , newDir ,  " does not exist")

#Return the contents
return contents