# AWS EC2 & EBS Daily Inventory Pipeline
## 📌 Project Overview

The AWS EC2 & EBS Daily Inventory Pipeline is an EC2-hosted Apache Airflow pipeline that collects daily inventory data for EC2 instances and EBS volumes across multiple AWS regions and stores the results in Amazon S3.

The pipeline runs on an AWS EC2 instance using Dockerized Airflow services and is designed to:

Track EC2 and EBS inventory on a daily basis

Identify unused EBS volumes

Maintain historical snapshots for auditing and cost optimization

Demonstrate real-world Airflow deployment on AWS EC2

## 🏗️ Architecture Overview

Workflow:

Apache Airflow runs on an EC2 instance

DAG executes a Python task

Boto3 queries EC2 and EBS resources across regions

Pandas structures the extracted data

AWS Wrangler writes Parquet files to Amazon S3

Airflow logs execution and success state

## 🧰 Tech Stack
Layer	Technology
Compute	AWS EC2
Orchestration	Apache Airflow
Containerization	Docker & Docker Compose
SDK	Boto3
Processing	Pandas
Storage	Amazon S3
File Format	Parquet
AWS Helper Library	AWS Wrangler


## 📁 Project Structure

```text
ec2_airflow/
│
├── dags/
│   ├── ec2_extract.py
│   └── ec2_dags.py
│
├── config/
├── logs/
├── plugins/
│
├── docker-compose.yaml
├── Dockerfile
├── requirements.txt
└── README.md

