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
'''text

## ⚙️ Airflow Setup on EC2

Apache Airflow is deployed on an AWS EC2 instance using Docker Compose.
All Airflow components run as separate containers to closely mirror a production environment.

Running Services

airflow-webserver

airflow-scheduler

airflow-worker

airflow-triggerer

airflow-dag-processor

postgres

redis

This confirms:

Airflow is successfully running on EC2

All required services are healthy

The environment is stable for scheduled workloads

## 🔐 Accessing the Airflow UI

Airflow is accessible via the EC2 public IP on port 8080:

http://18.175.176.91:8080


The screenshot below shows the Airflow UI running successfully on the EC2 instance, with the DAG visible and operational:

## 🔄 DAG: EC2 & EBS Daily Inventory
DAG Name
ec2_inventory_to_s3

Task
extract_ec2_data

DAG Capabilities

Discovers EC2 instances across multiple AWS regions

Collects EBS volume metadata

Logs region-level processing

Writes daily Parquet snapshots to Amazon S3

Gracefully handles regions with no resources

✅ Successful DAG Execution

The DAG was manually triggered and completed successfully.

Execution Details:

Status: ✅ Success

Duration: ~21 seconds

Task: extract_ec2_data

Triggered by: Airflow user

This confirms that:

The DAG is correctly configured

AWS credentials and permissions are valid

Data extraction and S3 upload completed without errors

## 📦 Data Collected
EC2 Inventory

Region

Instance ID

Instance State

EBS Inventory

Region

Volume ID

Size (GB)

State

Unused EBS volumes can be identified using:

State = available

## 🗂️ S3 Output Structure

Daily inventory snapshots are written to Amazon S3 using date-based naming:

s3://ec2-ebsinstances/zobs_instance/YYYY-MM-DD.parquet
s3://ec2-ebsinstances/zobs_volumes/YYYY-MM-DD.parquet


This structure enables:

Historical trend analysis

Easy Athena integration

Cost and utilization reporting

## 📅 Scheduling

The DAG can be scheduled to run daily

Manual triggering is supported for testing

Logical execution dates are tracked by Airflow

## 🚀 Future Enhancements

Athena external tables for querying Parquet data

Cost estimation for unused EBS volumes

Slack or email alerts for unused resources

IAM role-based authentication (remove static credentials)

Partitioned S3 datasets for performance optimization
