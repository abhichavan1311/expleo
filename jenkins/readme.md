

---

# Jenkins Tasks for ExpleoGroup

Welcome to the **ExpleoGroup Jenkins Task Documentation**! This document provides a comprehensive guide to understanding, setting up, and executing Jenkins tasks tailored to the needs of ExpleoGroup. Whether you're a beginner or an experienced Jenkins user, this guide ensures a seamless experience.

---

## Table of Contents

1. [Introduction](#introduction)  
2. [Setup and Prerequisites](#setup-and-prerequisites)  
3. [Task Overview](#task-overview)  
4. [Task Execution Steps](#task-execution-steps)  
5. [Best Practices](#best-practices)  
6. [Troubleshooting](#troubleshooting)  
7. [Additional Resources](#additional-resources)

---

## Introduction

Jenkins is a powerful automation server used to build, deploy, and automate various aspects of the software development lifecycle. This documentation will walk you through specific Jenkins tasks designed for ExpleoGroup's workflow, highlighting their importance and detailing how to implement them effectively.  

> **Why Jenkins?**  
> Jenkins provides continuous integration (CI) and continuous delivery (CD) capabilities that ensure seamless and automated workflows.

---

## Setup and Prerequisites  

To begin, ensure the following prerequisites are met:  


### **1. Prerequisites** 
**Minimum hardware requirements:**
256 MB of RAM

1 GB of drive space (although 10 GB is a recommended minimum if running Jenkins as a Docker container)

**Recommended hardware configuration for a small team:**
4 GB+ of RAM,
50 GB+ of drive space

### **2. Jenkins Installation**  
- Download and install Jenkins from the [official Jenkins website](https://www.jenkins.io/).  
- Ensure Java is installed on your system [java requirement](https://www.jenkins.io/doc/book/platform-information/support-policy-java/) 
- setup JAVA_HOME
 

### **3. Plugins Required**  
Install the following plugins:  
- **Git Plugin**: For managing code repositories.  
- **Pipeline Plugin**: To create Jenkins pipelines.  
- **Blue Ocean**: For an improved UI experience.  
- **Maven IntegrationVersion**: provides a deep integration between Jenkins and Maven.

### **4. Jenkins installation using linux**

ubuntu@ip-172-31-26-103:~$ history

sudo apt-get update

sudo apt-get install openjdk-21-jdk -y

java --version

which java

sudo update-alternatives --config java

sudo wget -O /usr/share/keyrings/jenkins-keyring.asc https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key

echo "deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] https://pkg.jenkins.io/debian-stable binary/" | sudo tee /etc/apt/sources.list.d/jenkins.list > /dev/null

sudo apt-get update

sudo apt-get install jenkins

jenkins --version

sudo vi /etc/default/jenkins

sudo systemctl restart jenkins

sudo systemctl status jenkins

Now hit, IP-Address:8080 on web browser

![Jenkins Installation](images/jenkins_installation1.jpg)


**Why Set JAVA_HOME for Jenkins?
Explicit Java Version Control:**

Jenkins depends on Java, and specifying JAVA_HOME ensures that Jenkins uses the correct version of Java installed on your system. This is particularly important when multiple versions of Java are installed.

1. Prevent Startup Errors:

    If JAVA_HOME is not set, Jenkins might fail to start or use an incorrect Java version, which could lead to runtime errors or incompatibility issues.
2. Consistency Across Users and Processes:

    Setting JAVA_HOME ensures that any Jenkins jobs, plugins, or scripts that rely on Java use the same environment configuration.
3. Custom Java Options:

    Some advanced Jenkins configurations or plugins require additional Java options. By setting JAVA_HOME, you can more easily configure JAVA_OPTS or JENKINS_JAVA_OPTIONS.

**How to Set JAVA_HOME for Jenkins**
1. Verify Java Installation
Ensure Java is installed and locate its installation directory:



    sudo update-alternatives --config java

    (Copy the Java installation path, e.g., /usr/lib/jvm/java-21-openjdk-amd64.)

2.Set JAVA_HOME in a way that Jenkins can use it:
    
     sudo vi /etc/default/jenkins
and set 
     JAVA_HOME="/usr/lib/jvm/java-21-openjdk-amd64"

     sudo systemctl restart jenkins


---



## Task Overview  


### **Task 1: Build Automation**  
Automate the process of building a software application. This ensures consistency and reduces manual effort.  

### **Task 2: Test Automation**  
Run automated tests to ensure the quality of the software.  

### **Task 3: Deployment**  
Automate the deployment process to production or staging environments.  

### **Task 4: Monitoring and Feedback**  
Set up alerts and feedback mechanisms to monitor the build and deployment processes.  

---

Let me know the specifics you'd like to include or edit, and I'll update accordingly!