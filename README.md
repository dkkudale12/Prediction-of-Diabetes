# Prediction-of-Diabetes

# Diabetes_Prediction

# Softwares and tools

[Github](https://github.com)
[VSIDE](https://code.visualstudio.com/)
[GITCLS]

Steps:

First clone git folder
Create new repository of project name
	select add readme,giigonre python, 
Copy code from HTTP path
Open command prompt and select destination whre we want to clone
git clone paste that path

then open visual studio and select that path


1. Create new environment
   " conda create -p venv python==3.7 -y"
2. Activate environment
   " conda activate venv/"
3. create new requirements.txt file and mention all libraries which want to use:
    pandas, numpy,sklearn, flask, matplpotlib, seaborn,...etc
4. install all libraries from txt file
    "pip install -r requirements.txt"
5. Now connect to gitcls to push all docs in git
    " git config --global user.name" DEEPAK" # if already have then only write user.name
    " git config --global user.email"mailid"
6. now add one file:
    " git add requirments.txt"
7. you can see new file and untracked(not added) files.
    to add all this  use " git add ."
8. then see git status
9. now we have to push this from remote to branch
    " git push origin main" it will automatically redirected to sign in and browser
10.Use git hub password to push all and finally refresh github all repositaries will be pushed.