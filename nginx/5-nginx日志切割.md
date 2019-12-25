### nginx日志切割
1. 将原先的log mv到需要备份的目录
		- [ ] mv操作不会影响已经打开文件的写入操作（不会改变文件iNode），所以mv操作不会丢失日志
2. 执行`nginx -s reopen`
3. 以上过程需要手动执行，不如写成脚本放到crontab中

```shell
crontab -l
0 0 1 * * root /usr/local/openresty/nginx/logs/rotate.sh

cat /usr/local/openresty/nginx/logs/rotate.sh
#!/bin/bash
#Rotate the Nginx logs to prevent a single logfile from consuming too mush disk space.
LOGS_PATH=/usr/local/openresty/nginx/logs/history
CUR_LOGS_PATH=/usr/local/openresty/nginx/logs
#以2018-11-27的形式，显示昨天日期2018-11-26
YESTERDAY=$(date -d "yesterday" +%Y-%m-%d)
mv ${CUR_LOGS_PATH}/xufeng_access.log ${LOGS_PATH}/xufeng_access_${YESTERDAY}.log
mv ${CUR_LOGS_PATH}/error.log ${LOGS_PATH}/error_${YESTERDAY}.log

#向Nginx主进程发送USR1信号，USR1信号是重新打开日志文件（相当于nginx -s reopen）
kill -USR1 $(cat /usr/local/openresty/nginx/logs/nginx.pid)
```