# datascience
## GitHub Basic Operations
- **Update Files**
  `git add .`同步全部文件夹 或者 `git add file` 同步某个文件
  `git commit -m “XXX”` 通过commit指令，确认要上传同步的内容，”XXX"内容任意
  `git push` 将内容push上去
- **Download Files**
  - `git clone <仓库URL>`
    1. 下载整个仓库的所有内容
	2. 自动设置远程跟踪分支
	3. 创建并切换到主分之
  - `git pull origin <分之名>`
    1. 从远程仓库获取最新的提交
	2. 自动将这些更改合并到当前本地分支
  - `git fetch origin`
    1. 从远程仓库获取最新的提交
	2. 不会自动合并到本地分支
	3. 允许在合并前检查更改
  使用场景区分：
	- 对于新项目，使用`git clone`
	- 日常更新，如果确定没有冲突，可以直接使用`git pull`
	- 如果希望在合并前检查更改，使用`git fetch`后再手动合并
  
  