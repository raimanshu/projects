
'''
✅ - okay need to read onece
❌ - need to understand
⭐ - asked in interview
👉- think important 
'''

# https://www.geeksforgeeks.org/git/git-interview-questions-and-answers/


# ✅What is Git?
'''used to track changes in source code during software development. It permits multiple developers to work on a project together without interrupting each other's changes'''
# ✅What is a repository in Git?
'''file structure that stores all the files for a project. It continues to track changes made to these files over time, helping teams work together evenly. Git can control both local repositories (on your own machine) and remote repositories (usually hosted on platforms like GitHub, GitLab, or Bitbucket), allowing teamwork and backup.'''
# ✅What is difference between Git and GitHub?
'''
- Git is a version control system used to track changes in files over time while Github is a platform where Git repositories can be stored and shared
- Git runs locally on your computer while Github is cloud-based service
- Git can be used offline, as it operates locally on your machine while GitHub requires an internet connection because it is hosted on the web'''
# ✅👉What is origin in Git?
'''default name offered to the remote repository from which local repository was cloned.'''
# ✅What is the purpose of the .gitignore file?
'''tells Git which files and folders to ignore when tracking changes. It is used to avoid attaching unneeded files (like logs, temporary files, or compiled code) to your repository. '''
# ✅What is a version control system (VCS)?
'''records the work of developers coordinating on projects. It keeps the history of code changes, permitting developers to add new code, fix bugs, and run tests securely.'''
# ✅What is the git push command? - used to share local repository changes to a remote repository
# ✅What is the git pull command? - updates the current local branch with changes from a remote repository and combining it with a local repository.
# ✅What does git clone do? - forms a copy of a remote repository upon your local machine.
# ✅What are the advantages of using GIT?
'''
- It assists teamwork by supporting multiple developers to work on the same project together.
- Each developer has a local copy of the repository, improving performance and enabling offline work.
- Free and widely supported.
- Git supports work on various types of projects.
- Each repository has only one Git directory.'''
# ✅What is the difference between git init and git clone? 
'''git init develops a new, empty Git repository in the present directory, while 'git clone' copies an existing remote repository, containing all files and history, to a local directory.'''
# ✅What is git add? -  tells Git which files to involve in the later update, making them ready to be saved in the repository.
# ✅What is git status? - tells you which files have changed, which ones are ready to be committed, and which ones are new and unobserved.
# ✅What is a commit in Git? - denotes a snapshot of changes made to files in a repository. Each commit has a unique message explaining what was done. 
# ✅What is the purpose of the git clean command? - clean up the workspace by deleting files that are not being saved by Git, checking a clean state with only observed files present.
# ✅What is a 'conflict' in git? 
'''conflicts occur when two branches edit the same line or when one branch deletes a file that another edits.'''
# ✅👉What is the meaning of 'Index' in GIT?
''' 'Index' (also called as the "Staging Area") is a place where alterations are temporarily store before committing them to the repository. It permits you to select and prepare specific alterations from your working directory before properly saving them as part of the project's history.'''
# ✅How do you change the last commit in git? - git commit --amend
# ✅What is `git checkout`? - switch between branches or return files to a previous state
# ✅How do you switch branches in Git? - git switch
# ✅Name some popular Git hosting services? - GitHub, GitLab, Bitbucket
# ❌What are the different types of Git repositories?
'''
- Bare Repository: A repository without a working directory, typically used for sharing projects remotely.
- Non-Bare Repository: A repository that includes a working directory where developers can modify and track files.'''
# ✅How does Git handle file deletion? 
'''Git provides the git rm command to remove files from the working directory and the staging area. If you only want to remove a file from Git but keep it in the working directory, use:  git rm --cached <file_name>'''
# ✅How can you create an alias in Git? - git config --global alias.<alias_name> '<git_command>'
# ✅How do you rename a branch in Git? - git branch -m <new_branch_name>    or  git branch -m <old_branch_name> <new_branch_name>
# ✅👉What is the difference between git fetch and git pull?
'''
git fetch - Retrieves updates from a remote repository but does not merge them into the local repository. This allows reviewing changes before integrating them.
git pull - Fetches updates from a remote repository and immediately merges them into the current local branch. Equivalent to git fetch followed by git merge.'''
# ❌👉⭐Explain Git rebase and when do you use it?
'''The Git rebase is a process to combine alterations from one branch into another. It forms a linear history, avoiding merge commits. Use it to clean up commit history, keep a project history sequential, and make feature branches up-to-date before uniting.'''
# ✅How will you create a git repository?
# ✅What differentiates between the commands git remote and git clone?
'''
git remote - Manages connections to remote repositories. It allows users to add, remove, and view remote repositories linked to a local project. However, it does not download any files.
git clone - Creates a local copy of an existing remote repository, including all its files, branches, and commit history. This allows developers to start working on a project immediately.'''
# ✅What are the benefits of using a pull request in a project? - Code Review, Collaboration, Version Control
# ❌What is a Git bundle?
'''A Git bundle is a collective file that wraps all data from Git repository, such as commits, branches, and tags. It acts as a handy approach for relocating a repository offline or sharing upgrades when network connection is not available. To form a git bundle, perform the following command:  git bundle create <bundle_file> <refs> '''
# ✅What are the advantages of Git over SVN? - Distributed Version Control, Faster Performance, Branching and Merging, Offline Work, Better Conflict Resolution
# ✅👉What is git stash?
'''used to temporarily save changes that are not yet ready to be committed. It allows developers to switch branches or work on something else without losing their progress.'''
# ❌👉How do you revert a commit that has already been pushed and made public?
'''
git checkout <branch-name>
git log
git revert <commit-hash>
git push origin <branch-name>'''
# ✅👉Explain the difference between reverting and resetting?
'''
git reset - Moves the HEAD pointer to a previous commit, removing changes from the commit history. It can modify staged and working directory changes.
git revert - Creates a new commit that undoes changes from a previous commit without modifying commit history. It is safer when working in a shared repository.'''
# ❌👉What is the difference between git reflog and log?
'''
Purpose - reflog tracks movements of HEAD and branch changes while log shows commit history.
Visibility - reflog shows all references, even those not in branch history while log only shows commits in the current branch history
Recoverability - reflog can help recover lost commits while log does not track changes outside commit history
Use Case - reflog used to restore lost branches or commits while log used to review past commits and changes
'''
# ✅👉What is the HEAD in Git?
'''
- HEAD in Git is a reference to the latest commit on the currently checked-out branch.
- It determines which commit and branch you are working on.
- When switching branches, HEAD updates to point to the latest commit of the new branch.
- If in a detached HEAD state, it means you are working on a specific commit instead of a branch.'''
# ✅What is the purpose of 'git tag -a'?
'''used to create an annotated tag in Git. Annotated tags store additional metadata such as the tagger’s name, email, date, and a message describing the tag. These tags are useful for marking important points in a repository, such as software releases.
git tag -a v1.0 -m "Version 1.0 Release"'''
# ❌What is the difference between 'HEAD', 'working tree' and 'index' in Git?
'''
- HEAD -  A reference to the current commit or branch you are working on. It points to the tip of the current branch. Represents the current branch or commit you are on. Located in .git/HEAD.
- Working Tree - The directory where your project files reside. It reflects the actual state of files on your filesystem and includes changes made but not yet staged. Contains the actual files, including any modifications or additions not yet staged. The local directory in your project.
- Index(Staging Area) - A file (also called the staging area) that acts as a buffer between the working tree and the repository. Files staged here are ready to be committed. Holds changes that you want to commit to the repository. Located in .git/index.'''
# ✅How to resolve a conflict in Git?
# ❌👉⭐Explain the difference between 'git merge' and 'git rebase' and when you would use each?
'''| **Feature**      | **git merge**                                                      | **git rebase**                                                        |
|------------------|---------------------------------------------------------------------|------------------------------------------------------------------------|
| **What it does** | Combines branches, creates a merge commit.                         | Reapplies commits on top of another branch, creates linear history.   |
| **Commit History**| Keeps history intact, includes a merge commit.                     | Rewrites history to make it linear.                                   |
| **Result**       | New merge commit, preserves branch structure.                      | Clean, straight history without merge commits.                        |
| **When to use**  | To preserve both branches' histories and structure.                | To get a clean, linear commit history.                                |
| **Best for**     | Team collaboration, integrating feature branches.                  | Personal branches, squashing, cleanup before pushing.                 |
| **Merge Commit** | Yes, merge commit is created.                                      | No, history is rewritten.                                             |'''
# ✅What language is used in GIT? - C programming language.
# ✅How do you add a file to the staging area? - git add <file>, git add .
# ✅What is 'git diff? - shows the differences between files or commits
# ✅What is a Git commit hash?
'''unique identifier (SHA-1) for each commit. It helps to reference and track specific commits in the repository.'''
# ✅👉What is a detached HEAD state?
'''detached HEAD state occurs when you check out a specific commit rather than a branch. In this state, commits are not attached to any branch, meaning they may be lost if not properly managed.'''
# ✅How can you delete a remote Git branch? - git push origin --delete <branch-name>
# ❌👉What is the purpose of git cherry-pick?
'''
- Selective Commit Application: Applies changes from a specific commit to the current branch.
- No Full Branch Merge: Useful when you want to incorporate changes from a branch without merging the entire branch.
- Clean Commit History: Helps maintain a clean history by including only selected changes.
- Bug Fixes: Ideal for bringing specific bug fixes or features from one branch to another.
- New Commit: The changes are applied as a new commit on the current branch, preserving the original commit's content.'''
# ❌What does git ls-files do? - displays the files in both the working directory and the staging area.
# ✅How do you fetch all remote branches? - git fetch --all
# What is the Git object model?
'''
- Blobs: Store the file data (the contents of files).
- Trees: Represent directory structures and contain references to blobs (files) and other trees (subdirectories).
- Commits: Store snapshots of the repository at a particular point in time, along with metadata like author, timestamp, and parent commit references.
- Tags: Store references to specific commits, typically used for marking important points in the repository's history, such as releases.'''
# Explain 'git rebase' and when you would use each?
'''❌
git rebase moves or reapplies commits from one branch onto another, creating a linear commit history.
When to use:
- Clean Commit History: To avoid merge commits and keep a straight line of history.
- Sync with Latest Changes: To update your branch with the latest changes from another branch.
- Squashing Commits: To combine multiple commits into one before merging.'''
# ❌What is a git hook and how might you use it?
'''
A Git hook is a script that runs automatically at certain points in the Git workflow, like before or after a commit, merge, or push.
Use cases:
- Pre-commit: Check code quality or run tests before committing.
- Post-commit: Automate tasks like notifications after a commit.
- Pre-push: Ensure tests pass before pushing changes.
'''
# ✅👉Explain the difference between git reset, git revert, and git checkout?
'''
- git reset: Moves HEAD to different commit, potentially changing history.
- git revert: Undoes exact commit by making new commit with inverse changes.
- git checkout: Switches branches or checks out files from commit, putting you in "detached HEAD" state for direct commits.'''
# ✅How do you handle large files with Git?
'''
To handle large files with Git, use Git LFS (Large File Storage). It replaces large files in the repository with pointers, while the actual file content is stored externally.
Steps:
1. Install Git LFS:
git lfs install
2. Track large files:
git lfs track "*.psd"
3. Commit and push as usual. Git LFS will handle the large file storage automatically.'''
# ❌What is ‘bare repository’ in Git?
'''repository that doesn't have a working directory. It only contains the Git data, such as branches, tags, and commits, without the actual project files.'''
# ✅👉What is branching in Git?
'''Branching in Git permits forming separate lines of development. It allows users to work on features or fixes separately from the main codebase, helping parallel development and simpler integration of changes.'''
# ❌👉What is a Git submodule?
'''
A Git submodule is a repository embedded inside another Git repository. It allows you to keep track of an external repository as part of your project. Submodules are useful when you want to include external libraries or dependencies while keeping their history separate.'''
# ✅How can you undo a commit that hasn’t been pushed to the remote repository?
'''
- To keep changes in the working directory:
git reset --soft HEAD~1
- To remove changes from both the commit and working directory:
git reset --hard HEAD~1'''
# ❌How do you squash multiple commits into one using Git rebase? - git rebase -i HEAD~<number-of-commits>
# ✅How do you reset a commit to a previous commit without losing changes in the working directory? - git reset --soft <commit-hash>
# ❌What is the difference between git reset --hard and git clean -fd?
'''
- git reset --hard: Resets the commit history, the staging area, and the working directory to a specific commit, discarding any changes.
- git clean -fd: Removes untracked files and directories from the working directory but does not affect the commit history or staged changes.'''
# ✅How do you apply a patch from a remote Git repository?
'''
git fetch <remote> <branch>
git apply <patch-file>'''
# ✅How do you configure a Git repository to use a specific user for a particular project?
'''
git config user.name "Your Name"
git config user.email "your.email@example.com"'''
# ✅👉What is a Git reflog, and how is it useful?
'''
reflog tracks the history of changes to the HEAD and branches, including changes that are not part of the commit history (e.g., resets, rebase). It allows you to recover lost commits by providing references to previous states.
git reflog'''
# ✅How do you manage multiple remotes in a Git repository?
'''
- Add a new remote:
git remote add <remote-name> <remote-url>
- View remotes:
git remote -v
- Remove a remote:
git remote remove <remote-name>'''
# ❌How do you configure and use Git hooks for pre-commit checks?
'''
Go to the .git/hooks directory.
Rename or copy pre-commit.sample to pre-commit.
Write your script to check code style, run tests, etc.
Make the hook script executable:
chmod +x .git/hooks/pre-commit'''
# How do you manage large binary files in Git without using Git LFS? - can store large files in a separate repository and reference them using Git submodules
# How do you fetch changes from multiple remotes in Git? - git fetch --all
# ❌🤔How do you perform a Git bisect to find the commit that introduced a bug?
