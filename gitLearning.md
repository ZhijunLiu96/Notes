[git learning](https://github.com/pcottle/learnGitBranching)

- ```git branch <new branch>```
- ```git checkout <new branch/master>```: switch to new branch or master
- ```git commit```: save the branch to a child node
- ```git commit --amend```: resubmit a copy at the same level  

---

- ```git checkout <branch>; git merge master```: merge master to ```<branch>```

---

- ```git rebase```: ```checkout <branch>; rebase master``` <br/>
	== merge master to branch <br/>
	== ```git rebase master branch```

---

- ```git checkout c1```: prev - head -> master -> c1; now - head -> c1
- ```git checkout HEAD^```
- ```HEAD^```, ```HEAD^^```, ```HEAD~4```
- ```git checkout -b <branch> <hash value>```: new a branch at a specific position

---

- ```git branch -f <branch name> <node>```

---

- ```git reset HEAD~1```: go back
- ```git revert HEAD```: submit a new one
- ```git rebase -i HEAD~number```: interactive rebase

---

- ```git tag <tag> node```: later we can directly checkout the tag
- ```git describe```

---

- ```git checkout <master^2/master^/master~/master~2>``` <br/>
== ```git checkout <HEAD^2^~~2>```

---

**o/master -> local**
- ```git clone```
- ```git fetch```: update local
- ```git pull``` == ```git fetch; git merge 0/master```: then everything will be merged to master

---

- ```git fakeTeamwork```: simulate teamwork created on remote branch
- ```git frkeTeamwork <branch> 3: add three teamwork```

---

**not consistent case:**
- ```git fetch; git rebase o/master; git push```
- ```git fetch; git merge o/master; git push```
- ```git pull --rebase; git push```

---

**track method:**
- ```git checkout -b <new branch> o/master```
- ```git branch -u o/master <new branch>```

---

- ```git push <remote> <place>```
- ```git push <remote> <source>:<destination>```
- ```git fetch origin foo```: just fetch the foo branch from the remote

---

- ```git fetch <origin> <source>:<destination>```
- ```git push origin (empty):<source>```: delete
- ```git fetch origin (empty):<source>```: add
- ```git pull origin master``` == ```git fetch origin master; git merge o/master```
- ```git pull origin master:foo``` == ```git fetch origin master:foo; git merge foo```

---
 
**删除当前缓存重新添加：**

```git rm -r --cached .```
