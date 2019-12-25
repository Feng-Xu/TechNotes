### nginx命令行
1. 格式：nginx -s reload
2. 帮助：nginx -h/-?
3. 使用指定配置文件： -c
4. 配置指令：-g
    - 在nginx.conf中有很多指令，如果需要在命令行中覆盖，则需要使用nginx -g xxxx
5. 指定运行目录：-p
    - 替换掉之前定义好的运行目录
6. 发送信号：-s
    - stop：立刻停止服务
    - quit：优雅的停止服务（平缓停止）
    - reload：重新加载配置文件（优雅的停止服务）
    - reopen：重新开始记录日志文件。比如说换一个nginx的log文件，reopen会新打开一个日志文件，从头开始记录
7. 测试配置文件是否错误：-t -T
8. 打印nginx的版本信息、编译信息等：-v -V

### ngixn的kill -USR1、-USR2、-HUP和-QUIT
1.  `kill -USR1 pid`:日志切割的，对应reopen命令，推荐`nginx -s reopen`来进行日志切割，更不易犯错 。
2.  `kill -USR2 pid`：是热部署升级nginx用的，它会以子进程的方式启动另一个nginx
3.  `kill -HUP pid`：对应`nginx -s reload`命令，它会在没有worker进程时启动worker进程。
4.  `kill -QUIT pid`：对应`nginx -s quit`命令，平滑停掉nginx进程。