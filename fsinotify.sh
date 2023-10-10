#!/bin/bash

current_watches=$(sysctl fs.inotify.max_user_watches | awk '{print $3}')
current_instances=$(sysctl fs.inotify.max_user_instances | awk '{print $3}')

# Check if either value is less than 4000
value_changed=false
if [ $current_watches -lt 4000 ]; then
  sysctl -w fs.inotify.max_user_watches=4000
  current_watches=4000
  value_changed=true
fi

if [ $current_instances -lt 4000 ]; then
  sysctl -w fs.inotify.max_user_instances=4000
  current_instances=4000
  value_changed=true
fi

# Output the values to a file if the values were changed
if [ "$value_changed" = true ]; then
  echo "fs.inotify.max_user_watches=$current_watches" > output.txt
  echo "fs.inotify.max_user_instances=$current_instances" >> output.txt
fi
