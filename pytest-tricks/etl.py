import boto3
import pandas as pd


def change_location(df: pd.DataFrame) -> pd.DataFrame:
    df.loc[0, "Location"] = "Amherst"
    return df


def get_csv_from_s3_boto3(client: boto3.client, bucket_name: str, file_path: str) -> pd.DataFrame:
    s3_object = client.get_object(Bucket=bucket_name, Key=file_path)
    df = pd.read_csv(s3_object["Body"])
    return change_location(df)

