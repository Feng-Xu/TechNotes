### nginx热部署
```shell
[root@l-test-xufeng1.ops.dev.ali.dm sbin]# ps -ef|grep nginx
root     26254     1  0 22:45 ?        00:00:00 nginx: master process nginx
nginx    26255 26254  0 22:45 ?        00:00:00 nginx: worker process
nginx    26256 26254  0 22:45 ?        00:00:00 nginx: worker process
nginx    26257 26254  0 22:45 ?        00:00:00 nginx: cache manager process
root     26469 17557  0 22:46 pts/0    00:00:00 grep nginx
```
1. 备份现有的nginx二进制文件
    - `cd /usr/sbin; cp nginx nginx.old`
2. 将编译好的最新版本的二进制nginx文件，拷贝到nginx的目录中，替换掉正在运行的进程所使用的二进制文件
    - `[root@l-test-xufeng1.ops.dev.ali.dm sbin]# cp -rf /root/nginx-1.14.0/objs/nginx .
`
3. 现在要给正在运行的master进程发送信号，告诉master进程，要进行热部署，做一次版本升级
    - `kill -USR2 pid(现在master的pid)`
    - `kill -USR2 26254`
    - nginx的master进程会新启动一个master进程，新的master进程会使用刚刚copy过来的二进制文件。
    - 老的worker也在运行，新的master会生成新的worker。他们会平滑的把所有的请求过渡到新的nginx进程中。（老的worker会继续处理已有的进程，新的worker会处理新的请求）
```shell
[root@l-test-xufeng1.ops.dev.ali.dm sbin]# ps -ef|grep nginx
root     26254     1  0 22:45 ?        00:00:00 nginx: master process nginx
nginx    26255 26254  0 22:45 ?        00:00:00 nginx: worker process
nginx    26256 26254  0 22:45 ?        00:00:00 nginx: worker process
nginx    26257 26254  0 22:45 ?        00:00:00 nginx: cache manager process
root     26470 26254  0 22:46 ?        00:00:00 nginx: master process nginx
nginx    26471 26470  0 22:46 ?        00:00:00 nginx: worker process
nginx    26472 26470  0 22:46 ?        00:00:00 nginx: worker process
nginx    26473 26470  0 22:46 ?        00:00:00 nginx: cache manager process
nginx    26474 26470  0 22:46 ?        00:00:00 nginx: cache loader process
root     26673 17557  0 22:47 pts/0    00:00:00 grep nginx
```
4. 向老的nginx进程发送winch信号，告诉老的nginx进程，请优雅的关闭你所有worker进程。
    - `kill -WINCH pid(老nginx进程的pid)`
```shell
kill -WINCH 26254
[root@l-test-xufeng1.ops.dev.ali.dm sbin]# ps -ef|grep nginx
root     26254     1  0 22:45 ?        00:00:00 nginx: master process nginx
root     26470 26254  0 22:46 ?        00:00:00 nginx: master process nginx
nginx    26471 26470  0 22:46 ?        00:00:00 nginx: worker process
nginx    26472 26470  0 22:46 ?        00:00:00 nginx: worker process
nginx    26473 26470  0 22:46 ?        00:00:00 nginx: cache manager process
root     27639 17557  0 22:52 pts/0    00:00:00 grep nginx
```
5. 老的master没有worker进程了，说明所有的请求已经切换到新升级好的nginx中。但是新nginx万一有一些问题，需要退回到老版本中，所有老的master进程，我们还可以向它发送reload命令，重新拉起worker进程，再把新版本关掉，所以老的master进程不会自动退出，会保留，允许做版本回退。
    - 如果热部署没有问题，
        1. 使用`kill -QUIT 老进程pid` 来把老的mater进程平滑停掉，热部署升级完成。
    - 如果热部署有问题
        1. 使用`kill -HUP 老进程pid` 重新拉起老master进程的worker进程。
        2. 结束掉新master进程：`kill -QUIT 新master进程`
        3. 将nginx.old文件替换成nginx：`cp nginx.old nginx`
```shell
#重新拉起老master的worker
[root@l-test-xufeng1.ops.dev.ali.dm sbin]# kill -HUP 26254
[root@l-test-xufeng1.ops.dev.ali.dm sbin]# ps -ef|grep nginx
root     26254     1  0 22:45 ?        00:00:00 nginx: master process nginx
root     26470 26254  0 22:46 ?        00:00:00 nginx: master process nginx
nginx    26471 26470  0 22:46 ?        00:00:00 nginx: worker process
nginx    26472 26470  0 22:46 ?        00:00:00 nginx: worker process
nginx    26473 26470  0 22:46 ?        00:00:00 nginx: cache manager process
nginx    30950 26254  0 23:09 ?        00:00:00 nginx: worker process
nginx    30951 26254  0 23:09 ?        00:00:00 nginx: worker process
nginx    30952 26254  0 23:09 ?        00:00:00 nginx: cache manager process
nginx    30953 26254  0 23:09 ?        00:00:00 nginx: cache loader process
root     30955 17557  0 23:09 pts/0    00:00:00 grep nginx

#结束掉新master进程，回退成功
[root@l-test-xufeng1.ops.dev.ali.dm sbin]# kill -QUIT 26470
[root@l-test-xufeng1.ops.dev.ali.dm sbin]# ps -ef|grep nginx
root     26254     1  0 22:45 ?        00:00:00 nginx: master process nginx
nginx    30950 26254  0 23:09 ?        00:00:00 nginx: worker process
nginx    30951 26254  0 23:09 ?        00:00:00 nginx: worker process
nginx    30952 26254  0 23:09 ?        00:00:00 nginx: cache manager process
root     32114 17557  0 23:15 pts/0    00:00:00 grep nginx
```