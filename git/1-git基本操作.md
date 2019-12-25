### 创建git仓库
两种方式：  
1. 用Git之前已经有项目代码
```shell
cd 项目代码所在的目录
git init
```
2. 用Git之前还没有项目代码
```shell
cd 某个目录
git init your_project	#会在当前目录下创建和项目名称同名的目录
cd your_project
```
### git 基本操作
```shell
# git操作流程
工作目录--->git add files--->暂存区--->git commit--->版本历史--->git push--->远端仓库
# git 修改文件名
git mv oldname newname
# git会在暂存区修改，然后通过commit到本地仓库，在push在远程仓库。

# git log查看提交的历史记录
git log --graph # 以图形的方式查看
git log --graph -n4 # 以图形的方式查看最后四次提交记录
```