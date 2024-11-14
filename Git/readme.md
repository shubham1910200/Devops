#### Git Stash
- Used for Managing the temporary changes
- Scenario: You're working on a feature in new branch and need to switch to another branch without committing your current changes. This is where git stash comes into Play.

1. Create a new branch and make changes: Start by creating a new branch
``` bash
git checkout -b new-branch-feature
```
2. Make some changes to your files. These changes are now in your working directory.
3. Stash The changes: Use git stash to save your changes temporarily.
``` bash
git stash
```
This command will remove the changes from your working directory and save them in stash, allowing you to switch to another branch without lossing progress.
4 Switches to Different branch: switch to different branch where you need to work:
``` bash
git checkout branch_name
```
5. Make some changes and commit them as usual.
6. Pop the stash: once you're done, return to your original branch and apply the stashed changes on the top of new commits.
``` bash
git checkout new-feature-branch git stash pop
```

# Linux Command Cheat-sheet file

## Directory Management
##### 1. ls List directory contents
```bash
ls
```
##### 2. cd [directory] Change the current directory
```bash
cd /path/to/directory
```
##### 3. pwd print the current working directory path
```bash
pwd
```
##### 4. mkdir [directory] Create a new directory
```bash
mkdir new-directory
```
##### 5. rmdir [directory] Remove a empty directory
```bash
rmdir old-directory
```
##### 6. rm [file] Remove a file
```bash
rm file-to-remove.txt
```
##### 7. cp[sources] [distination] Copy file or directory
```bash
cp source-file destination-file
```
##### 8. mv[sources] [distination] Move or rename file or directory
```bash
mv old-name-txt new-name-txt
```
##### 9. touch [file] Create a empty file
```bash
touch file-name
```
### File viewing & Editing
##### 1. cat [file-name] display the contents of the file
```bash
cat file-name
```
##### 2. less [file] view file content page by page
```bash
less file-name
```
##### 3. head [file-name] Display the first 10 line of a file
```bash
head file-name
```
##### 4. tail [file-name] Display the last 10 lines of a file
```bash
tail file-name
```
##### 5. nano [file-name] Edit the file using Nano txt editor
```bash
nano file-name.txt
```
##### 6. vim [file-name] Edit the file using vim txt editor
```bash
vim file-name.txt
```
### Permissions & Ownership
##### 1. chmod [permissions] [file-name] Change the permission.
```bash
chmod 755 file-name.txt
```
##### 2. chown [permissions] [file-name] Change the owner and group
```bash
chown user:group file-name.txt
```
##### 3. ls -l List file with detailed information including permissions and ownership.
```bash
ls -l
```
### System Monitoring & Management
##### 1. top Display active processes
```bash
top
```
##### 2. ps aux List all running processes
```bash
ps aux 
```
##### 3. df -h Display disk space usage
```bash
df -h
```
##### 4. du -sh [directory] Display disk usage of a directory
```bash
du -sh /path/to/directory
```
##### 5. free -h Display memory usage
```bash
free -h
```
##### 6. uptime show system uptime and load average
```bash
uptime 
```
# Git Commands Cheatsheet Basic Commands

##### 1. git init initialize a new git repository
```bash
git init
```
##### 2. git clone [url] clone a repository url
```bash
git clone [url]
```
##### 3. git add [file] Add a file to staging area
```bash
git add file-name
```
##### 4. git commit -m ['message'] commit changes with message
```bash
git commit -m 'commit message'
```
##### 5. git status show the status of changes
```bash
git status
```
##### 6. git log Display commit history
```bash 
git log
```
## Branching and Merging

##### 7. git branch List all branches
```bash 
git branch
```
##### 8. git branch [branch_name] Create a new branch
```bash
git branch new-branch-name
```
##### 9. git checkout [branch_name] Switch to a branch
```bash
git checkout new-branch
```
##### 10. git merge [branch_name] Merge a branch into the current branch
```bash
git merge new-branch
```
##### 11. git rebase [branch_name] rebase the current branch onto another branch
```bash
git rebase new-branch
```
## Stashing 
##### 12. git stash temporarily save changes without committing
```bash
git stash
```
##### 13. git stash pop Apply stashed changes and remove them from the stash
```bash
git stash pop
```
##### 14. git stash list all stash changes
```bash
git stash list
```
##### 15. git stash drop Remove a specific stash.
```bash
git stash drop stash@{0}
```
##### 16. git stash clear Remove all stashes
```bash
git stash clear
```
## Cherry-Picking
##### 1. git cherry-pick [commit_hash] Apply a specific commit from another branch
```bash
git cherry-pick 1232ab3
```

## Conflict Resolution
##### 1. git status show files with conflicts
```bash
git status
```
##### 2. git diff shows differences between conflicting versions
```bash
git diff
```
##### 3. git add [file_name] Stage resolved file for commit
```bash
git add resolved-file.txt
```

# GitHub Tips Cheat-Sheet Repository Management

##### 1. Create a Repository Click "New" on GitHub and follow the prompts.

##### 2. Fork a Repository Click "Fork" on the top-right of the repository page.

3. Clone a Repository Use git clone [url] to copy a repository locally.
```bash
git clone https://github.com/user/repo.git
```

# Collaboration
##### 1. Pull Requests Create a pull request to propose changes. Review and discuss before merging.

##### 2. Issues Use GitHub Issues to track bugs, tasks, and feature requests.

##### 3. Wiki Utilize the GitHub Wiki for project documentation. Branch Protection

##### 4. Enable Branch Protection Prevent force-pushes and require pull request reviews before merging.