# UniEvent AWS Deployment

Name: Rukh-e-Zahra


##  Project Overview

This project demonstrates the deployment of a web application on AWS using EC2 instances and an Application Load Balancer. The goal is to achieve high availability by distributing traffic across multiple servers.

---

## Setup Details

* **Cloud Platform:** AWS
* **Instances:** 2 EC2 instances (Amazon Linux)
* **Instance Type:** t3.micro
* **Load Balancer:** Application Load Balancer
* **Target Group Port:** 5000
* **Application:** Flask (Python)
* **Ports Used:** 22 (SSH), 80 (HTTP), 5000 (Flask), 9000 (File transfer)

---

##  Deployment Steps

1. Launched two EC2 instances.
2. Installed Python and Flask on both servers.
3. Deployed the same Flask application on both instances.
4. Configured Security Groups to allow HTTP traffic.
5. Created a Target Group with port 5000.
6. Registered both instances in the Target Group.
7. Created an Application Load Balancer.
8. Linked Load Balancer with Target Group.
9. Verified health checks for both instances.

---

##  Application URL

http://<your-load-balancer-dns>

*(Replace with your actual Load Balancer DNS)*

---

##  Application Behavior

The Flask application returns a unique message from each server:

* Hello from UniEvent Server 1
* Hello from UniEvent Server 2

This allows verification that traffic is being distributed between both servers.

---

##  Load Balancing Result

When accessing the Load Balancer URL and refreshing multiple times, the response alternates between:

* Hello from UniEvent Server 1
* Hello from UniEvent Server 2

This confirms that traffic is successfully distributed across both servers.

---

##  Screenshots

The following screenshots are included in the submission folder:

1. EC2 Instances running
2. Security Group configuration
3. Target Group health status
4. Load Balancer configuration
5. Application output (Server 1 & Server 2)

---

##  Key Concepts

* Load Balancing distributes traffic across multiple servers
* Target Groups manage registered instances
* Health Checks ensure only healthy servers receive traffic
* Improves availability and reliability

---

##  Conclusion

This project successfully demonstrates load balancing using AWS. By distributing traffic across multiple EC2 instances, the system ensures high availability, scalability, and fault tolerance.

---

##  Note

AWS resources were terminated after testing to avoid additional charges.
