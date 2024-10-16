#!/bin/bash

# Ensure .profile is in the home directory
if [ ! -f ~/.profile ]; then
    cp /etc/skel/.bashrc ~/.profile
    chmod 644 ~/.profile
fi

# Start SSH service
sudo /usr/sbin/sshd -D
