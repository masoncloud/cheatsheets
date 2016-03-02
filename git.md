# Git

## Installation

### Install Git on Ubuntu/Debian

    sudo apt-get install git

### Initialize a Git Repository in the Current Directory

    git init
    
### Add a Remote Repository Alias

For convenience, you can create an alias to reference a remote repository.

    # Example: git remote add origin https://github.com/LAHacknight/cheatsheets.git
    git remote add <alias> <git_url>
    
### Clone a Repository Into a Specific Directory

    git clone https://github.com/LAHacknight/cheatsheets.git path/to/place/repo/content
    
### Remove Git Tracking Within a Project

This will destroy all Git tracking metadata. Yes, this is that "rm -rf" you've been warned above... use with care. 

    cd project/directory
    rm -rf .git
    
## Tagging

### List Available Tags

    # See all
    git tag
    
    # See only those matching pattern
    git tag -l "v1.*"
    
### Inspect a Tag

    git show <tag>
    
### Create Annotated Tag

    # New tag with message
    git tag -a <tag> -m <message>
    
    # New GPG-signed tag, using default e-email address's key, along with message
    git tag -as <tag> -m <message>
    
### Create Lightweight Tag

    git tag <tag>
    
### Push Tags to Remote Repo

By default, push does not include tags. To include:
    
    # Pushes all tags
    git push origin --tags
    
    # Push a specific tag
    git push origin <tag>
    
## Log / History

### View Tidy Text Graph of Git Log

    git log --graph --oneline --decorate

## Remote Repositories

### Difference between fetch and pull

`fetch` will download any changes from the remote branch, updating your repository data, but leaving your local branch unchanged. `pull` will perform a `fetch` and additionally `merge` the changes into your local branch. What's the difference? `pull` updates your local branch with changes from the pulled branch. A `fetch` does not advance your local branch. [Source](http://stackoverflow.com/questions/14894768/git-fetch-vs-pull-merge-vs-rebase)