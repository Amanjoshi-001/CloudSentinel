import boto3
from datetime import datetime, timedelta, timezone

INSTANCE_ID = "i-045452cdc51cb0be1"
REGION = "ap-south-1"


def get_cpu_metrics():
    cloudwatch = boto3.client(
        "cloudwatch",
        region_name=REGION
    )

    end_time = datetime.now(timezone.utc)
    start_time = end_time - timedelta(hours=1)

    response = cloudwatch.get_metric_statistics(
        Namespace="AWS/EC2",
        MetricName="CPUUtilization",
        Dimensions=[
            {"Name": "InstanceId", "Value": INSTANCE_ID}
        ],
        StartTime=start_time,
        EndTime=end_time,
        Period=300,
        Statistics=["Average"]
    )

    datapoints = sorted(
        response["Datapoints"],
        key=lambda point: point["Timestamp"]
    )

    print("\nCloudSentinel - AWS CloudWatch Monitoring")
    print("-----------------------------------------")

    if not datapoints:
        print("No CPU metrics available yet.")
        return

    for point in datapoints:
        print(
            point["Timestamp"].strftime("%Y-%m-%d %H:%M:%S"),
            "- CPU Usage:",
            round(point["Average"], 2),
            "%"
        )


if __name__ == "__main__":
    get_cpu_metrics()
