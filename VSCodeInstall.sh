`#!/bin/bash
curl -fsSL https://code-server.dev/install.sh > install.sh && chmod +x install.sh
./install.sh
sudo systemctl enable --now code-server@$USER
echo ‘’'bind-addr: 0.0.0.0:8081
auth: password
password: abcd1234
cert: false’’' > ./.config/code-server/config.yaml
