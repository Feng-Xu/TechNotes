### 请求资源root和alias的区别
Root配置范围：http，server，location和if
alias配置范围：location

1. Root的处理结果是：root路径+location路径
::root后面可有可无‘/’，结果都是root+location的路径::
eg：
```
location ^~ /t/ {
		root /www/root/html；
}
```
如果一个请求URL是`/t/a.html`时，web服务器会返回服务器上的`/www/root/html/t/a.html`文件。

下面来看alias的怎么处理

2. alias的处理结果是：使用alias的路径替换location的路径，就是location后的路径直接去alias中去找。
::alias后面必须以‘/’结束::
Eg:
```
location ^~ /t/ {
		alias /www/root/html/；
}
```
如果一个请求URL是`/t/a.html`时，web服务器会返回服务器上的`/www/root/html/a.html`文件。