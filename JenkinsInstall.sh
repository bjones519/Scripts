#!/bin/bash
# Step 1: Import Jenkins Key
curl -fsSL https://pkg.jenkins.io/debian/jenkins.io-2023.key | sudo tee \
  /usr/share/keyrings/jenkins-keyring.asc > /dev/null
# Step 2: Add Jenkins to the sources.list (NOTE: echo command to output the provided text which is our Jenkins APT repo)
echo deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] \
  https://pkg.jenkins.io/debian binary/ | sudo tee \
  /etc/apt/sources.list.d/jenkins.list > /dev/null
# Step 3: Update the package list
sudo apt-get update
# Step 4: Install fontconfig and openjdk-17-jre
sudo apt-get install -y fontconfig openjdk-17-jre
# Step 5: Install Jenkins
sudo apt-get install -y jenkins
echo “All of your packages for Jenkins have been downloaded!”
