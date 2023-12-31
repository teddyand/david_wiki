# david_wiki
wiki in gollum that can be converted to docx whick published on wechat public

### INSTALL
1. [install nvm and ruby](https://teddyand.github.io/2022-07-15/jadeI)
2. [install gem ](https://rubygems.org/pages/download)
3.  安装指定版本gollum
```
gem i  gollum '>=?'
```
4. 克隆仓库
```
git clone git@github.com:teddyand\david_wiki.git
```
5. make a new directory
6. 拷贝仓库文件到新文件夹(每次 git pull 后的文件重新拷贝一下)
```
cp -rf ~/david_wiki ~/(new directory)/
```
7.在新文件夹中运行gollum （该文件夹无远程仓库连接，仅作为本地浏览使用）
```
cd (new directory)
git init
git add .
git commit -m "blabla"
gollum -c config.rb -h 0.0.0.0
```



[for more please see:]()
