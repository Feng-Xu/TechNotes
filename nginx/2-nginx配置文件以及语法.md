### nginx配置文件&配置语法
```shell
user					nginx;
worker_processes  			auto;
error_log  				/var/log/nginx/error.log;
pid        				log/nginx.pid;
worker_rlimit_nofile    		102400;
events {
    use					epoll;
    worker_connections			10240;
}

http {
    server_tokens 			off;
    include         			mime.types;
    default_type    			application/octet-stream;

    log_format  main  '$time_local|$hostname|$server_port|$remote_addr|$upstream_addr|$request_time|$upstream_response_time|$upstream_connect_time|'
        '$status|$upstream_status|-|$bytes_sent|-|-|$remote_user|$request|$http_user_agent|$http_referer|$host|second|^_^|'
        '$scheme|$request_method|$request_trace_id|$request_trace_seq|^_^|'
        '$http_x_forwarded_for|$http_Authorization|$cookie_parentId|$cookie_studentId|$cookie_mbparentid|$cookie_mbstudentid|$http_vk_session_id';
    log_format  xxxx_main  '$time_local|$hostname|$remote_addr|$upstream_addr|$request_time|$upstream_response_time|$upstream_connect_time|'
        '$status|$upstream_status|-|$bytes_sent|-|-|$remote_user|$request|$http_user_agent|$http_referer|$host|second|^_^|'
        '$scheme|$request_method|$request_trace_id|$request_trace_seq|^_^|'
        '$http_x_forwarded_for|$http_Authorization|$cookie_parentId|$cookie_studentId|$cookie_mbparentid|$cookie_mbstudentid|$http_vk_session_id|$proxy_add_x_forwarded_for|$http_x_real_ip|$http_x_client_ip';

    access_log  			/var/log/nginx/access.log  main;
}
```
1. 配置文件由指令和指令块构成
    - 指令：`include	mime.types;`
    - 指令块：`http { }`
2. 每条指令以;号结尾，指令与参数间以空格符号分隔
3. 指令块中已{}大括号将多条指令组织在一起
4. include允许组合多个配置文件以提升可读性
    - mime.type：很多不同文件后缀名与HTTP协议中mime格式对照表，定义了http中支持的文件类型，与nginx语法关联不大，通过include来引入，增加可读性。
5. 使用#符号来注释
6. 使用$来使用变量
    - $status、$upstream_status等变量是nginx框架提供
7. 部分指令的参数支持正则表达式
    - location后面的参数支持正则表达式
8. 配置参数（时间为单位）
    - ms：milliseconds 毫秒
    - s：seconds 秒
    - m：minutes 分钟
    - h：hours 小时
    - d：day 天
    - w：weeks 周
    - M：Month 月
    - y：years 年
9. 配置参数（空间为单位）
    - 什么都不写：bytes 字节
    - k/K：kilobytes 千字节
    - m/M：megabytes 兆字节
    - g/G：gigabyte 
10. 指令块
    - http
    - server：一个域名或一组域名
    - location：url
    - upstream：与tomcat、Django等等企业内网其他服务交互