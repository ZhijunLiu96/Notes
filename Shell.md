# Shell

## Access Management

- check user and group info
查看user、group、user在的group ID
```
cat /etc/passwd
cat /etc/group
dscl . -read /Users/<userName> PrimaryGroupID
```
查看每个组下的用户
```
dscl . -list /groups GroupMembership
```
### User
- create user, the id should be unique; delete user
创建user，ID要唯一；删除用户
```
dscl . -create /Users/<userName> UniqueID <uniqueID e.g 888>
dscl . -delete /Users/<userName>
```

- change the password to 1234
修改用户密码为 1234
```
dscl . -passwd /Users/newuser 1234
```

### Group
- create new group
创建组newGroup：
```
dscl . -create /Groups/<groupName>
dscl . -create /Groups/<groupName> GroupMembership <userName>
dscl . -create /Groups/<groupName> PrimaryGroupID <groupID>
```
- add new user to a group
将用户newuser添加到组newGroup
```
dscl . -append /Groups/<groupName> GroupMembership <userName> 
```
- delete a group
删除group
```
dscl . -delete /Groups/<groupName>
```

### access management

```
chown -R USER:GROUP DIRECTORY
chmod -R 770 directory
chown USER:GROUP FILENAME
chmod 770 filename
```

---


## Vim Tutor

- ```vimtutor```: 打开vim教程

### 保存退出
- ```:q!```: 不保存退出
- ```:wq```: 保存退出
- ```:w FILENAME``` 写到一个路径
- ```v <motion> :'<,'>w TEST```  将高亮部分储存至TEST文件中 ```v motion :w FILENAME```


### 删除
- ```x```: 删除字母
- ```dw```: 删除单词，光标不在首字母就不删除首字母
- ```de```: 从当前光标删除到单词末尾。
- ```d$```: 从当前光标删除到行末。
- ```d2w```: 以删除两个大写字母单词
- ```dd```: 删除该行
- ```2dd```: 删除2行

### 输入、插入
- ```i```: 光标前
- ```a```: 光标后
- ```A```: 句子后
- ```:r FILENAME```: 在光标下插入另一个文件的内容
- ```o```: 在光标 **下方** 打开新的一行
- ```O```: 在光标 **上方** 打开新的一行

### 光标移动(数字可自由改变)
- ```w```: 移动到单词开头, ```2w```: 向前移动两个单词
- ```e```: 移动到单词结尾, ```3e```: 向前移动到第三个单词的末尾
- ```0```:移动光标到行首

### 跳行
- ```CTRL-G```: 显示当前状态，包括行数
- ```gg```: 跳去第一行
- ```G```: 跳去最后一行
- ```100G```: 跳去第100行

### 撤销、返回
- ```u```: undo
- ```U```: 恢复到该行的原始状态
- ```CTRL-R```: 撤消掉撤消命令

### 粘贴、替换、修改
- ```dd <Enter> p <Enter>```: 在下方插入被删除的行
- ```r<char>```: 替换当前字符
- ```R```: 替换
- ```cw```: 删除光标位置至词尾 并键入
- ```ce```: 删除整个单词并键入
- ```c$```: change 这一行剩下的部分
- ```v <motion> y j$ p```: 复制粘贴 


### 查看帮助文档
- ```:help w```
- ```:help c_CTRL-D``` 
- ```:help insert-index``` 
- ```:help user-manual```
- ```:q```: 退出

### 运行外部命令
- ```:!```: 然后紧接着输入一个外部命令可以执行该外部命令, e.g. ```:!ls```
- 

### 查找
- 查找 ```/keyword``` 用n和N进行前后遍历，```:set ic``` ignore case,```:set noic``` cancel case ignore, ```:set hls is``` highlight, ```:nohlsearch``` remove highlight, ```/ignore\c```仅一次查找中忽略大小写
- % 可以查找配对的括号 )、]、}
- ```:s/thee/the <回车> ```。请注意该命令只改变光标所在行的第一个匹配串。
- ```:s/thee/the/g``` 则是替换全行的匹配串
- 在两行内替换所有的字符串 old 为新的字符串 new，请输入  :#,#s/old/new/g
- 在文件内替换所有的字符串 old 为新的字符串 new，请输入  :%s/old/new/g
- 进行全文替换时询问用户确认每个替换需添加 c 标志        :%s/old/new/gc

---

## 其他常用

### 打开外部软件
- ```open <Path/AppName>```: e.g. ```open /Applications/iTerm.app```

### 路径相关
- ```pwd```: print working directory
- ```ls```: list segments, ```ls -a```, ```ls --all```, ```ls -l```, ```ls 'folder'```
- ```cd```: change directory
- ```sudo```: super user do
- ```rm``` remove file, ```rm -r``` remove directory

### 终止
- ```ctrl-C``` : keyboard interrupt

### git
- ```git log```
- ```git log --graph```

### search
- ```grep 'keywords key' file```: search for lines with certain keywords in the file
- ```echo 'regex' file```

### forget
- ```emacs path```:
- control + X + S, control+X+C
- ```man ls```, q to quit
- chsh change shell
- diff -bB file1 file2
- diff -bB dir1 dir2