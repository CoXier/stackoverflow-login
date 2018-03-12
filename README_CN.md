# stackoverflow-login

连续登录了二十几天 StackOverflow 断了，又要重新开始登录，要是能有个自动登录的脚本就好了。所以这个脚本就是为了自动登录 StackOverflow。

# 用法
在 `config/account.json` 中填写你的邮箱和密码。

```bash
{
  "email": "your_email",
  "password": "your_password"
}
```
你可以把这个脚本放在服务器上，每天自动登录一次。参考脚本，**请注意脚本所在的路径**，替换即可。

```bash
crontab -e
# put below command to new tab
0 0 * * * project_path/stackoverflow-login/dev_script/robot.sh
```
