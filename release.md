
# fully automated

    $ ./release.sh 1.8.0

# semi automated
To make a new release
```
# update reacton/_version.py
$ git add -u && git commit -m 'Release v1.8.0' && git tag v1.8.0 && git push upstream master v1.8.0
```


If a problem happens, and you want to keep the history clean
```
# do fix
$ git rebase -i HEAD~3
$ git tag v1.8.0 -f &&  git push upstream master v1.8.0 -f
```
