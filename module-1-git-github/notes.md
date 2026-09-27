# Module 1 — Git & GitHub

****Student:**** Jazper Escoto

****Date:**** September 28, 2026

---

## What is Git? What is GitHub? (explain like you're teaching a friend who's never used either)

Git is a tool that tracks changes in files. It helps us save different versions of our work and makes it easier to go back if something goes wrong.

GitHub is a website where Git repositories can be stored online. Git is used to track changes on the computer, while GitHub is used to store and share the repository online.

---

## Key vocabulary (in your own words)

- repository: a folder that contains a project and its files tracked by Git.

- commit: a saved version of changes in the repository.

- branch: a separate version of the project where we can work on changes.

- push / pull: push sends changes from the computer to GitHub, while pull gets changes from GitHub.

- pull request: a request to add changes from one branch to another branch.

- merge conflict: a problem that happens when Git cannot automatically combine different changes.

---

## Walking through what I did

I created my repository from the provided GitHub template. I worked on my own branch called `Jazper-Act`. I edited the files in VS Code, saved my changes, committed them, and pushed them to GitHub. I also created a pull request from `Jazper-Act` to `main`.

```bash
# check the current status
git status

# add a file
git add module-2-python-basics/lesson4-functions.py

# save the changes as a commit
git commit -m "Add lesson on functions in Python"

# push the changes to my branch
git push origin Jazper-Act
```

---

## A mistake I made (or one I want to avoid)

One mistake I made was getting confused about which branch I was working on. I learned that I should check my current branch using `git status` before making changes or pushing them.

I also learned that seeing a file in VS Code does not always mean Git detected a change. The `git status` command shows if a file was modified or if there are changes that still need to be committed.

---

## How this connects to something else

Git and GitHub connect to programming projects because they help keep track of changes. They are also useful when working with other people because each person can work on their own branch and use a pull request to combine their changes.
