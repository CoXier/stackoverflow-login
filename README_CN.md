# stackoverflow-login

连续登录了二十几天 StackOverflow 断了，又要重新开始登录，要是能有个自动登录的脚本就好了。所以这个脚本就是为了自动登录 StackOverflow。

## 用法

**Docker 启动（推荐）：**

你可以选择自己打包镜像，或者直接使用我的 [yujiangshui/stackoverflow-login](https://cloud.docker.com/u/yujiangshui/repository/docker/yujiangshui/stackoverflow-login)。

运行 `docker run -e EMAIL="你的邮箱" -e PASS="你的密码" -d yujiangshui/stackoverflow-login`。 

或者使用 Docker Compose：

创建 `docker-compose.yml` 文件并写入：

```
version: '3.1'

services:

  stackoverflow-login:
    image: yujiangshui/stackoverflow-login
    restart: always
    environment:
      EMAIL: 你的邮箱
      PASS: 你的密码
```

之后执行 `docker-compose up -d` 即可启动。

**常规用法：**

安装相关依赖，设置系统变量：

* `EMAIL` 你的 StackOverflow 注册邮箱
* `PASS` 你的 StackOverflow 注册密码
* `APPPATH` 指向当前应用在服务器上的目录，例如：`export APPPATH=/root/apps/stackoverflow-login`

之后执行 crontab 设置定时任务。

```bash
crontab -e
# put below command to new tab
0 0 * * * project_path/stackoverflow-login/dev_script/robot.sh
```
