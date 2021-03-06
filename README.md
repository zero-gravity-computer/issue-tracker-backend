# About
A web application backend built with [Django](https://www.djangoproject.com/)!

# Usage
* Install all dependencies/packages: `pipenv install`
* Install python package: `pipenv install <package_name>`
* Start development shell: `pipenv shell`
* Run application: `python manage.py runserver`

# Git Commands
* Copy GitHub Repo to local machine: `git clone <Repo_URL>`
* Display current branch: `git branch`
* Creat new branch: `git checkout -b <intent/issue#_name>`
* Checkout existing branch: `git checkout <existing branch name>`
* View Repo status (more is better): `git status`
* Add file to staging area: `git add <file_name>`
* Add all files to staging area: `git add .`
* Add dir to staging area: `git add <directory name>/*`
* Unstage file: `git reset <file_name>`
* Commit staged files: `git commit -m "<commit message>"`
* Push local changes to origin: `git push`
* List commit log (press "q" to exit log): `git log`
* Import origin changes to local machine: `git pull`
* Merge current branch with master: `git push --set-upstream origin <branch name>`

# Django Snippets 
* Create new model instance: `instance_name = Class(trait, etc)`
  * When new instance has a relationship, another variable is required within trait list