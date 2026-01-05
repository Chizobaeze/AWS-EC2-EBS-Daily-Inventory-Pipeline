import boto3
import pandas as pd
import awswrangler as wr
from airflow.models import Variable
from datetime import datetime
import os

# Load AWS credentials from Airflow Variables
AWS_ACCESS_KEY = Variable.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_KEY = Variable.get("AWS_SECRET_ACCESS_KEY")
AWS_DEFAULT_REGION = Variable.get("AWS_DEFAULT_REGION", default_var="us-east-1")

# Set environment variables so awswrangler picks them up automatically
os.environ["AWS_ACCESS_KEY_ID"] = AWS_ACCESS_KEY
os.environ["AWS_SECRET_ACCESS_KEY"] = AWS_SECRET_KEY
os.environ["AWS_DEFAULT_REGION"] = AWS_DEFAULT_REGION

# Create a default EC2 client to fetch all regions
client = boto3.client("ec2", region_name=AWS_DEFAULT_REGION)
regions = [r["RegionName"] for r in client.describe_regions()["Regions"]]

def ec2_data():
    instance_records = []
    volume_records = []

    for region_name in regions:
        print(f"Processing region: {region_name}")

        ec2 = boto3.client(
            "ec2",
            region_name=region_name
        )

        # Fetch EC2 instances
        reservations = ec2.describe_instances().get("Reservations", [])
        if not reservations:
            print(f"  No instances in {region_name}")
        else:
            for reservation in reservations:
                for instance in reservation.get("Instances", []):
                    instance_records.append({
                        "Region": region_name,
                        "InstanceId": instance["InstanceId"],
                        "State": instance["State"]["Name"]
                    })

        # Fetch EBS volumes
        volumes = ec2.describe_volumes().get("Volumes", [])
        if not volumes:
            print(f"  No volumes in {region_name}")
        else:
            for volume in volumes:
                volume_records.append({
                    "Region": region_name,
                    "VolumeId": volume["VolumeId"],
                    "Size(GB)": volume["Size"],
                    "State": volume["State"]
                })

    # Convert to DataFrames
    df_instances = pd.DataFrame(instance_records)
    df_volumes = pd.DataFrame(volume_records)

    # Save to S3 using awswrangler (no boto3 session passed!)
    date_str = datetime.today().strftime("%Y-%m-%d")

    if not df_instances.empty:
        wr.s3.to_parquet(
            df=df_instances,
            path=f"s3://ec2-ebsinstances/zobs_instance/{date_str}.parquet",
            dataset=False
        )

    if not df_volumes.empty:
        wr.s3.to_parquet(
            df=df_volumes,
            path=f"s3://ec2-ebsinstances/zobs_volumes/{date_str}.parquet",
            dataset=False
        )

    print("EC2 and volume data uploaded to S3 successfully.")
