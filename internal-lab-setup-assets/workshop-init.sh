#!/bin/bash

echo "clab:$CX23_LAB_PASSWORD" | chpasswd

echo "clab ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/clab
chmod 0440 /etc/sudoers.d/clab

echo "syntax on" > /home/clab/.vimrc

/sbin/sysctl -w net.ipv6.conf.all.disable_ipv6=1
/sbin/sysctl -w net.ipv6.conf.default.disable_ipv6=1
/sbin/sysctl -w net.ipv6.conf.lo.disable_ipv6=1

/usr/sbin/sshd -D
