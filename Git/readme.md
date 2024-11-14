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
