### git 配置user信息
#### 配置user.name 和user.email   
```shell
git config --global user.name 'your_name'
git config --global user.email 'your_email@domain.com'
```
### config 的三个作用域
#### 设置作用域，缺省等同于local  
```shell
git config --local	#local只对某个仓库有效
git config --global	#global对登录用户所有仓库有效
git config --system	#system对系统的所有用户有效
```
#### 如果要显示config的配置，需要加—list：
```shell
git config --local --list
git config --global --list
git config --system —list
```
#### 清除作用域，使用—unset
```shell
git config --unset --local user.name
git config --unset --global user.name
git config --unset --system user.name
```
#### 作用域的优先级
`local > global > system`