mkdir project1 && cd project1 
git init
mkdir myproject
echo >> README.md
git commit -m "point1"
mkdir project1 && cd project1 
git init
git checkout -b first_branch
git status
git add .
git commit -m "point3"
git checkout master
git add .
git commit -m "point4"
git log
git worktree list
git merge first_branch
git add .
git commit -m "merge conflict"

