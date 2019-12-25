### pipeline step

```
pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'echo "Hello World"'
                sh '''
                    echo "Multiline shell steps works too"
                    ls -lah
                '''
            }
        }
    }
}
```
在Linux, BSD, 和 Mac OS (类Unix) 系统中的shell命令， 对应于Pipeline中的一个 sh 步骤（step）

### 超时、重试和更多
```
pipeline {
    agent any
    stages {
        stage('Deploy') {
            steps {
                retry(3) {
                    sh './flakey-deploy.sh'
                }

                timeout(time: 3, unit: 'MINUTES') {
                    sh './health-check.sh'
                }
            }
        }
    }
}
```
“Deploy”阶段（stage）重试运行` flakey-deploy.sh` 脚本3次，然后等待 `health-check.sh` 脚本最多执行3分钟。 如果 `health-check.sh `脚本在3分钟内没有完成，Pipeline将会标记在“Deploy”阶段失败。

```
pipeline {
    agent any
    stages {
        stage('Deploy') {
            steps {
                timeout(time: 3, unit: 'MINUTES') {
                    retry(5) {
                        sh './flakey-deploy.sh'
                    }
                }
            }
        }
    }
}
```
重试部署任务5次，但是总共花费的时间不能超过3分钟。

### 完成时的动作
当Pipeline运行完成时，你可能需要做一些清理工作或者基于Pipeline的运行结果执行不同的操作， 这些操作可以放在 post 部分。
```
pipeline {
    agent any
    stages {
        stage('test') {
            steps {
                retry(3) {
                    sh 'echo "hello world"'
                }
                
            }
        }
    }
    post {
        always {
            echo 'This will always run'
        }
        success {
            echo 'This will run only if successful'
        }
        failure {
            echo 'This will run only if failed'
        }
        unstable {
            echo 'This will run only if the run was marked as unstable'
        }
        changed {
            echo 'This will run only if the state of the Pipeline has changed'
            echo 'For example, if the Pipeline was previously failing but is now successful'
        }
    }
}
```

打印hello world和post中的always、success信息，执行结果如下：
```
Started by user root
Running in Durability level: MAX_SURVIVABILITY
[Pipeline] node
Running on Jenkins in /root/.jenkins/workspace/test
[Pipeline] {
[Pipeline] stage
[Pipeline] { (test)
[Pipeline] retry
[Pipeline] {
[Pipeline] echo
hello world
[Pipeline] }
[Pipeline] // retry
[Pipeline] }
[Pipeline] // stage
[Pipeline] stage
[Pipeline] { (Declarative: Post Actions)
[Pipeline] echo
This will always run
[Pipeline] echo
This will run only if successful
[Pipeline] }
[Pipeline] // stage
[Pipeline] }
[Pipeline] // node
[Pipeline] End of Pipeline
Finished: SUCCESS
```

将pipeline中的sh改成`sh 'echo “fail！”; exit 1'`，运行结果就不一样了。retry(3)起作用了，打印了post中的always、changed和failure。如下：
```
Started by user root
Replayed #8
Running in Durability level: MAX_SURVIVABILITY
[Pipeline] node
Running on Jenkins in /root/.jenkins/workspace/test
[Pipeline] {
[Pipeline] stage
[Pipeline] { (test)
[Pipeline] retry
[Pipeline] {
[Pipeline] sh
+ echo 'fail!'
fail!
+ exit 1
[Pipeline] }
ERROR: script returned exit code 1
Retrying
[Pipeline] {
[Pipeline] sh
+ echo 'fail!'
fail!
+ exit 1
[Pipeline] }
ERROR: script returned exit code 1
Retrying
[Pipeline] {
[Pipeline] sh
+ echo 'fail!'
fail!
+ exit 1
[Pipeline] }
[Pipeline] // retry
[Pipeline] }
[Pipeline] // stage
[Pipeline] stage
[Pipeline] { (Declarative: Post Actions)
[Pipeline] echo
This will always run
[Pipeline] echo
This will run only if the state of the Pipeline has changed
[Pipeline] echo
For example, if the Pipeline was previously failing but is now successful
[Pipeline] echo
This will run only if failed
[Pipeline] }
[Pipeline] // stage
[Pipeline] }
[Pipeline] // node
[Pipeline] End of Pipeline
ERROR: script returned exit code 1
Finished: FAILURE
```