# https://github.com/nikolaik/docker-python-nodejs
FROM nikolaik/python-nodejs:python3.8-nodejs13

MAINTAINER Albert King <jindaixang@163.com>

#RUN pip install akshare -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host=mirrors.aliyun.com  --upgrade
RUN pip install akshare --upgrade
