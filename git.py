git config --global user.name "YOUR NAME"
git config --global user.email "YOUR EMAIL ADDRESS"

git clone https://github.com/libgit2/libgit2
git clone https://github.com/libgit2/libgit2 mylibgit

git init #If you’re starting to track an existing project in Git, you need to go to the project’s directory and type:
git add *.c
git add LICENSE
git commit -m 'initial project version'

git status #check out the status of the repository
git add *** # start tracking file , *** file name or directory
git status -s # short version of git status

.gitignore # to ignore the file
# no .a files
*.a

# but do track lib.a, even though you're ignoring .a files above
!lib.a

# only ignore the TODO file in the current directory, not subdir/TODO
/TODO

# ignore all files in the build/ directory
build/

# ignore doc/notes.txt, but not doc/server/arch.txt
doc/*.txt

# ignore all .pdf files in the doc/ directory
doc/**/*.pdf

git commit -m "***" # commit the files with comments

git rm *** # remove the file from the tracked files and hard drive
git rm --cached *** # remove the file from the tracked files but not the hard drive

git push origin master # push the file in the HEAD to the repository
