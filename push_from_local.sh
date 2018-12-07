# Push content from my computer to GH pages
pelican content -o output -s publishconf.py
ghp-import output
git push -f origin gh-pages:master