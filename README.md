# stackoverflow-login
English version | [中文](README_CN.md)

This project is for a consecutive visit on https://stackoverflow.com/. If you visit https://stackoverflow.com/ for 30 consecutive days, you can earn `Enthusiast` badge. And 100 days, `Fanatic` badge.

## Usage

**By Docker (recommend):**

You can build the Docker Image yourself, or use my Image [yujiangshui/stackoverflow-login](https://cloud.docker.com/u/yujiangshui/repository/docker/yujiangshui/stackoverflow-login).

Run `docker run -e EMAIL="your-email" -e PASS="your-password" -d yujiangshui/stackoverflow-login`.

Or, use Docker Compose. Create `docker-compose.yml` and type the following:

```
version: '3.1'

services:

  stackoverflow-login:
    image: yujiangshui/stackoverflow-login
    restart: always
    environment:
      EMAIL: your-email
      PASS: your-pass
```

After that, run `docker-compose up -d`.

**By Python**

First, install the dependencies in `requirements.txt`, then, setting up Environment Variables:

* `EMAIL` your StackOverflow Account Email
* `PASS` your StackOverflow Account Password
* `APPPATH` point to this application's path, e.g, `export APPPATH=/root/apps/stackoverflow-login`

After that, you can choose to set a schedule task by crontab:

```bash
crontab -e
# put below command to new tab
0 0 * * * project_path/stackoverflow-login/dev_script/robot.sh
```
