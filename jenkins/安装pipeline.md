### 安装pipeline
Jenkins安装后是全新的。需要安装pipeline插件才可以使用pipeline。
`系统管理——插件管理——advanced——update Site`
默认的update site是被墙的，更换为清华的源：`https://mirrors.tuna.tsinghua.edu.cn/jenkins/updates/update-center.json`
在available标签中，搜索pipeline，选中pipeline安装即可。
安装过程过程中，会提示部分插件安装错误，那是因为部分插件需要重启Jenkins才可以生效，所以重新启动下Jenkins即可