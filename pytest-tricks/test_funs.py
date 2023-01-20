from etl import get_csv_from_s3_boto3


def test_get_csv_from_s3_boto3(mocked_s3_client, s3_bucket, file_name):
    csv_data = get_csv_from_s3_boto3(mocked_s3_client, s3_bucket, file_name)
    assert csv_data.loc[0, "Location"] == "Amherst"
