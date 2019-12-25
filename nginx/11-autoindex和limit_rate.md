### 目录浏览：autoindex
当一个目录内没有默认主页的文件时，直接访问目录会报 403 Forbidden 错误，而启用目录浏览功能后可以直接列出当前目录下的文件、文件夹  
打开目录浏览功能，默认是关闭的，使用范围：http, server, location

```shell
location / {
    autoindex	on;
}
```

### 限制ng向客户端发送的速度limit_rate

官网关于limit_rate的说明

> Limits the rate of response transmission to a client. The `*rate*` is specified in bytes per second. The zero value disables rate limiting. The limit is set per a request, and so if a client simultaneously opens two connections, the overall rate will be twice as much as the specified limit. 

```shell
Syntax:	limit_rate rate;
Default:	
limit_rate 0;
Context:	http, server, location, if in location
```

eg: `set limit_rate 1k;`每秒传输1k字节到客户端中。

### nginx内置变量

在nginx官方文档——模块：ngx_http_core_module等——embedded variable内置变量

