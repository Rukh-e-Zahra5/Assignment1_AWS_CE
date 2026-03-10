\# Assignment1\_AWS\_CE



\## AWS EC2 Flask Deployment



This project demonstrates how to deploy a Python Flask application on an AWS EC2 instance and access it through a public IP address.



---



\# Project Overview



The application fetches event data from an external API and displays it in JSON format.

The Flask application is deployed on an AWS EC2 instance and accessed through the internet using the EC2 public IP address.



---



\# Technologies Used



\* Python

\* Flask

\* AWS EC2

\* GitHub

\* Linux (Amazon Linux)



---



\# Project Structure



Assignment1\_AWS\_CE

│

├── app.py

├── requirements.txt

├── templates/

├── static/

└── README.md



---



\# Step 1: Create EC2 Instance



1\. Login to AWS Console

2\. Open EC2 Dashboard

3\. Click \*\*Launch Instance\*\*

4\. Select \*\*Amazon Linux\*\*

5\. Choose instance type \*\*t2.micro\*\*

6\. Create a key pair (`univent-key.pem`)

7\. Launch the instance



---



\# Step 2: Configure Security Group



Add inbound rules:



| Type       | Port |

| ---------- | ---- |

| SSH        | 22   |

| HTTP       | 80   |

| Custom TCP | 5000 |



Source: `0.0.0.0/0`



---



\# Step 3: Connect to EC2 using SSH



Run the following command:



ssh -i univent-key.pem ec2-user@13.211.240.100



---



\# Step 4: Install Python and Dependencies



Update system:



sudo yum update -y



Install Python:



sudo yum install python3 -y



Install project requirements:



pip3 install -r requirements.txt



---



\# Step 5: Run Flask Application



Start the Flask server:



python3 app.py



The server runs on:



http://0.0.0.0:5000



---



\# Step 6: Access the Application



Open the browser and visit:



http://13.211.240.100:5000



The application will return event data in JSON format.



---



\# Result



The Flask application was successfully deployed on AWS EC2 and accessed through the public IP address.



---



\# Screenshots



(Add screenshots here)



\* EC2 instance running

\* Security group inbound rules

\* Terminal running Flask server

\* Browser accessing the application



