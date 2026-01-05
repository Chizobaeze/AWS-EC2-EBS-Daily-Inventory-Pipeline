# AWS-EC2-EBS-Daily-Inventory-Pipeline
## 📌 Project Overview

The AWS EC2 & EBS Daily Inventory Pipeline is an EC2-hosted Apache Airflow pipeline that collects daily inventory data for EC2 instances and EBS volumes across multiple AWS regions and stores the results in Amazon S3.

The pipeline runs on an AWS EC2 instance using Dockerized Airflow services and is designed to:
1. Track EC2 and EBS inventory on a daily basis

2. Identify unused EBS volumes

3. Maintain historical snapshots for auditing and cost optimization

4. Demonstrate real-world Airflow deployment on AWS EC2
