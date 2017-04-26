# simple-github-bot

A simple bot for GitHub, developed as a POC for GitHub API. It detects inactive issues in a repository, adds a warning and closes them if no answer is made.

## features

- Detects inactive issues in a repository
- Adds a comment to warn of imminent closing
- Closes the issue if no answer

## Usage (as of now)

- Clone the repository
- Copy `src/config.py.example` to `src/config.py` and update it

```
token = 'CHANGE_ME'
repository = 'USER/REPO'
```
- Run `src/main.py`
