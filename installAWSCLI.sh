#!/usr/bin/env bash

rm -f '/pathTo/awscliv2.zip'
rm -rf '/pathTo/aws'

curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install

aws sts get-caller-identity
