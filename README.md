# stackoverflow-login
English version | [中文](README_CN.md)

This project is for consecutive visit on https://stackoverflow.com/ .If you visit https://stackoverflow.com/ for 30 consecutive days, you can earn `Enthuiast` bage. And 100 days, `Fanatic` bage.

# Usage

Setting your `email` and `password` by the environments `EMAIL` and `PASS` respectively.

Then you should better put this project on a server because it can login automatically every day. Here is a script `robot.sh` in `stackoverflow-login/dev_script/robot.sh`.

An example for schedule job. **Note: the path of bash script**. 
 
```bash
crontab -e
# put below command to new tab
0 0 * * * project_path/stackoverflow-login/dev_script/robot.sh
```
