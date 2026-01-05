# AWS EC2 & EBS Daily Inventory Pipeline

## 📌 Project Overview

The **AWS EC2 & EBS Daily Inventory Pipeline** is an EC2-hosted **Apache Airflow** pipeline that collects daily inventory data for **EC2 instances** and **EBS volumes** across multiple AWS regions and stores the results in **Amazon S3**.

The pipeline is designed to:

- Track EC2 and EBS inventory on a daily basis  
- Identify unused EBS volumes  
- Maintain historical snapshots for auditing and cost optimization  
- Demonstrate real-world Airflow deployment on AWS EC2  

---

## 🏗️ Architecture Overview

### Workflow

1. Apache Airflow runs on an **EC2 instance**  
2. DAG executes a Python task  
3. **Boto3** queries EC2 and EBS resources across regions  
4. **Pandas** structures the extracted data  
5. **AWS Wrangler** writes **Parquet** files to Amazon S3  
6. Airflow logs execution and success state  

---

## 🧰 Tech Stack

| Layer                | Technology                     |
|---------------------|--------------------------------|
| Compute              | AWS EC2                        |
| Orchestration        | Apache Airflow                 |
| Containerization     | Docker & Docker Compose        |
| SDK                  | Boto3                          |
| Processing           | Pandas                         |
| Storage              | Amazon S3                      |
| File Format          | Parquet                        |
| AWS Helper Library   | AWS Wrangler                   |

---

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
```

---

## ⚙️ Airflow Setup on EC2

Apache Airflow is deployed on an AWS EC2 instance using Docker Compose.  
All Airflow components run as separate containers to closely mirror a production environment.

### Running Services

- airflow-webserver  
- airflow-scheduler  
- airflow-worker  
- airflow-triggerer  
- airflow-dag-processor  
- postgres  
- redis
![Airflow UI](https://github.com/Chizobaeze/AWS-EC2-EBS-Daily-Inventory-Pipeline/blob/9bc5d836aa2df042fb01429a13de990c90e46f79/ec2-ebs-png/files%20used.PNG)


This confirms:

- Airflow is successfully running on EC2  
- All required services are healthy  
- The environment is stable for scheduled workloads  

---
## 🔐 Accessing the Airflow UI

Airflow is accessible via the EC2 public IP on port 8080:

[http://18.175.176.91:8080](http://18.175.176.91:8080)


**DAG Name:** `ec2_inventory_to_s3`  
**Task:** `extract_ec2_data`  


### ✅ Successful DAG Execution

- Status: ✅ Success  
- Duration: ~21 seconds  
- Task: `extract_ec2_data`  
- Triggered by: Airflow user

![Airflow UI](https://github.com/Chizobaeze/AWS-EC2-EBS-Daily-Inventory-Pipeline/blob/cded72b57b9f6e26a6924c783576deb507620f2b/ec2-ebs-png/code%20ran%20perfectly%20well.PNG)


Confirms:

- DAG is correctly configured  
- AWS credentials and permissions are valid  
- Data extraction and S3 upload completed successfully  

---

## 📦 Data Collected

### EC2 Inventory

| Field          |
|----------------|
| Region         |
| Instance ID    |
| Instance State |

### EBS Inventory

| Field    |
|----------|
| Region   |
| Volume ID|
| Size (GB)|
| State    |

**Unused EBS volumes:** `State = available`  

---

## 🗂️ S3 Output Structure

Daily inventory snapshots are written to Amazon S3 using **date-based naming**:

```
s3://ec2-ebsinstances/zobs_instance/YYYY-MM-DD.parquet
s3://ec2-ebsinstances/zobs_volumes/YYYY-MM-DD.parquet
```
![Airflow UI](https://github.com/Chizobaeze/AWS-EC2-EBS-Daily-Inventory-Pipeline/blob/0618ab7b701e7c18c4e67ddba278b4b52f7ba9d7/ec2-ebs-png/s3_bucket%20ec2_ebs_instance.PNG)
Benefits:

- Historical trend analysis  
- Easy **Athena** integration  
- Cost and utilization reporting  

---

## 📅 Scheduling

- DAG can run **daily**  
- Manual triggering supported for testing  
- Logical execution dates tracked by Airflow  

---

## 🚀 Future Enhancements

- Athena **external tables** for querying Parquet data  
- Cost estimation for **unused EBS volumes**  
- Slack or email alerts for unused resources  
- IAM **role-based authentication** (remove static credentials)  
- Partitioned S3 datasets for **performance optimization**
