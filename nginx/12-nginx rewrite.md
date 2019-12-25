### nginx rewrite
#### rewrite方法
```nginx
# 是将url1重写成url2
rewrite url1 url2 last/break;  
# 将以 /a开头的url重写成 /(.*)
# 也就是/a/q1/w2e3重写成了/q1/w2e3
rewrite /a/(.*) /$1 break;
# 上面rewrite执行后，下面的url就会变成 /q1/w2e3，而不是之前的 /a/q1/w2e3了
```  
#### last和break
1. 在location之外    
在location之外，两者的作用一致，需要注意，两者都会跳过之后的rewrite指令，去匹配location
```shell
rewrite url1 url2 last; ①
rewrite url3 url4 last; ②
rewrite url5 url6 last; ③

location  ~  url2     ④
location  ~  url4     ⑤
location  ~  url6     ⑥
```
当①生效后，之后的②③就不会做操作，直接去4、5和6中匹配了。    
2. 在location内部   
Last：使用last命令，rewrite后会跳出location作用域，重新开始再走一次刚刚的行为  
break：使用break命令，rewrite后不会跳出location作用域，它的生命也会在这个location中终结。
```shell
rewrite xxx1 yyy last; ⑦
rewrite xxx2 yyy last; ⑧
rewrite xxx3 yyy last; ⑨
rewrite xxx4 yyy last; ⑩

location ~  url1
{
    rewrite url1 url2 last; ①
}

location ~  url2
{
    rewrite url3 url4 break; ②
    fastcgi_pass 127.0.0.1:9000;
}
```
第一个location，rewrite处理完之后就会跳出location，在重新判断7-10  
第二个location，rewrite处理完之后，不会跳出location，不会重新判断7-10，而是将信息传递给后面的fastcgi_pass或者proxy_pass等指令。
#### permanent和redirect
Permanent：大家公认的信息，永久性重定向。请求日志中状态码301  
Redirect：大家公认的信息，临时性重定向，请求日志中状态码为302  
从实现功能的角度来看，permanent和redirect都一样，不存在好坏和性能上的问题。只不过从SEO角度来看，有影响。
#### last、break、permanent和redirect
permanent和redirect的状态码是301和302，而last和break的状态码为200.  
它们的区别是301和302这样的行为，浏览器重新获取一个新的url，然后对这个新的url进行访问。所以配置了permanent和redirect，对一个URL的访问，落到服务器上是2次。  
而配置了last或者break，最终的url确定下来，不会讲这个URL返回给浏览器，而将其扔给了proxy_pass处理，请求一个URL，落在服务器上是一次。
