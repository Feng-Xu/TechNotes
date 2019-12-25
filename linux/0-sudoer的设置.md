### sudoer的设置
普通用户通过sudo来临时获取root权限，必须在sudoer配置文件中定义。定义有两种方法：
1. 在命令行中敲visudo
2. 修改配置文件`/etc/sudoers`，其实visudo打开的就是`/etc/sudoers`
**不过，系统文档推荐的做法，不是直接修改_etc_sudoers文件，而是将修改写在_etc_sudoers.d/目录下的文件中。**
在`/etc/sudoers`配置文件的最后的配置中包含了`/etc/sudoers.d`目录的文件。
```
## Read drop-in files from /etc/sudoers.d (the # here does not mean a comment)
#includedir /etc/sudoers.d
```
_其中#includedir必须这样写_ 
所以直接在`/etc/sudoers.d`目录中添加文件就可以使普通用户拥有root权限。

### /etc/sudoers.d配置
```
cat user_conf
ansible       ALL=(ALL)       NOPASSWD: ALL
%vk-root       ALL=(ALL)       NOPASSWD: ALL
```
%vk-root 表示vk-root用户组中，可以不用密码在任何地方执行任务命令。

具体含义：
```
授权项(每行一个授权项)：
        who    where=（whom）    commands
        谁   通过哪些主机 以谁的身份 执行什么命令
        root    ALL=(ALL)   ALL 
        %wheel  ALL=(ALL)   ALL     
                
        who:用户
            username:单个用户；
            #uid：单个用户的ID号；
            %groupname：组内的所有用户；
            %#gid：组内的所有用户；
            user_alias：用户别名；支持将多个用户定义为一组用户，称之为用户别名；

        where：主机地址
            IP或hostname：单个主机；
            NetAddr：网络地址；
            host_alias：主机别名；

        whom：
            username
            #uid 
            runas_alias：以谁的身份运行；

        command：
            command：单个命令；
            directory：指定目录内的所有应用程序；
            sudoedit：特殊权限，可用于向其它用户授予sudo权限；
            cmnd_alias：命令别名；

        例：只允许fedora用户以sudo权限运行useradd,usermod两个命令；
            # useradd fedora
            # visudo        #或者放到/etc/sudoers.d/目录下；
              fedora ALL=(root)  /usr/sbin/useradd,/usr/sbin/usermod
        常用标签：
            NOPASSWD:   # sudo时不需要密码；后面加冒号(:);
            PASSWD:     # sudo时需要密码；

        定义别名的方法：
            ALIAS_TYPE  NAME=item1, item2, item3, ...
                ALIAS_TYPE:别名类型
                    User_Alias      # 用户别名
                    Host_Alias      # 主机别名
                    Runas_Alias     # sudo用户别名
                    Cmnd_Alias      # 命令别名
                NAME：别名名称，必须使用全大写字符；不同即可；
        例：为用户user1,user2添加sudo，除关机和visudo,su,passwd,userdel以外的其他所有操作
        useradd user1
        useradd user2
        ~]# visudo     #vim /etc/sudoers
        把
        %wheel  ALL=(ALL)   ALL
        改为
        User_Alias  USERADMINS=user1,user2
        Cmnd_Alias  CMDSHUTDOWN=/usr/sbin/halt,/usr/sbin/shutdown,/usr/sbin/poweroff,/usr/sbin/reboot,/usr/sbin/init
        Cmnd_Alias  CMDDANGER=/usr/sbin/visudo,/usr/bin/su,/usr/bin/passwd,/usr/sbin/userdel
        USERADMINS  ALL=(root)  NOPASSWD:ALL,!CMDSHUTDOWN,!CMDDANGER
```
### 禁止root用户和禁止密码登录
前提是配置好了key登录后，检查可以使用可以登录，在进行以下配置修改，要不然会造成server不能登录。
在sshd配置文件中`/etc/ssh/sshd_config`修改一下配置：
```
PermitRootLogin no
PasswordAuthentication no
```
最后重启sshd服务`service sshd restart`
