### location、proxy_pass和rewrite
1. location中匹配顺序
优先级：等号（=） > 类型表达式（^~） > 正则匹配（ ~：匹配大小写，~*：忽略大小写 ） > 常规字符串匹配

2. location中只是匹配path，不会匹配path中的参数

```nginx
    location ~* ^/api/v1/gift {
        rewrite ^/api/v1/gift/(.*) /$1 break;
        proxy_pass http://api_gw;
    }
```
如上面，假如请求url是`/api/v1/gift/1231/teacher?id=123`这样，`rewrite ^/api/v1/gift/(.*) /$1 break;`后，请求的url变成了`1231/teacher?id=123`，这种重写是带参数的。
```nginx
    location ~* ^/api/v1/gift/(.*) {
        #rewrite ^/api/v1/gift/(.*) /$1 break;
    }
```
以上location中的(.*)只有path，不带参数，也就是只有`1231/teacher`，没有后面的参数：`?id=123`  
   
3. proxy_pass中有path
```nginx
location ^~ /api/gw/ {
    proxy_pass http://10.0.0.1:8080/new/;
}
```
假如请求是`/api/gw/test1/123?asdaxxx`，那么经过上面配置后，打到后端server是`/new/test1/123?asdaxxx`，也就是只要upstream后面有’/‘，则就会把location中的path去掉，然后向后拼接。
  
4. location中使用^~匹配path，也可以使用rewrite来修改url
```nginx
    location ^~ /api/pc/service/reader/ {
        rewrite /api/pc/service/reader/(.*) /dl-service-provider/$1 break;
        proxy_pass http://api_gateway;
        proxy_set_header   Host             $host;
        proxy_redirect     off;
        proxy_set_header   X-Real-IP        $remote_addr;
        proxy_set_header   X-Forwarded-For  $proxy_add_x_forwarded_for;
        proxy_set_header   X-Request-ID     $request_trace_id;
        proxy_set_header   X-Request-Seq    $request_trace_seq;
    }
```
  
5. Location中有如果使用正则（使用~ 或者~*匹配path），那么proxy_pass中处理的请求url必须是经过一个或者多个变量改造过的，且proxy_pass结尾不以`/`结尾。   
1）直接在proxy_pass中使用变量改造
假设后端只接收处理`/api/gw`开头的请求，并且location中path要传到后端处理。
```nginx
location ~ ^/([A-Za-z0-9]+) {
    proxy_pass http://upstream_name/api/gw/$1;
}
```
2）在rewrite中使用变量改造
```nginx
location ~ ^/([A-Za-z0-9]+) {
    rewrite ^/([A-Za-z0-9]+) /api/gw/$1 break; 
    # 此时url已经变成了/api/gw/xxx，后续都按照这个处理
    proxy_pass http://upstream_name;
}
```
以上两种方式根据实际情况来决定用那种，常用第二种rewrite方式。
