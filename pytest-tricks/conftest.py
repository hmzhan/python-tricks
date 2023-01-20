import os
import pytest
import pandas as pd
from boto3.session import Session
from moto import mock_s3


@pytest.fixture(scope="session")
def s3_bucket() -> str:
    return "BUCKET_FOR_TEST"


@pytest.fixture(scope="session")
def file_name() -> str:
    return "FILE_FOR_TEST.csv"


@pytest.fixture(scope="session")
def input_file_content() -> str:
    input_data = """Name, DOB, Location
        John Smith, 19900101, Boston
        James Harold, 19800101, New York
        Aura Anderson, 20000117, Amherst
    """
    return input_data


@pytest.fixture(scope="session")
def input_file_path(tmp_path_factory, input_file_content, file_name) -> str:
    fn = tmp_path_factory.mktemp("data") / file_name
    fn.write_text(input_file_content)
    return fn


@pytest.fixture(scope="session")
def aws_credentials() -> None:
    os.environ["AWS_ACCESS_KEY_ID"] = "TEST"
    os.environ["AWS_SECRET_ACCESS_KEY"] = "TEST"
    os.environ["AWS_SECURITY_TOKEN"] = "TEST"
    os.environ["AWS_SESSION_TOKEN"] = "TEST"


@pytest.fixture(scope="session")
def moto_s3_session(aws_credentials, s3_bucket, file_name, input_file_path):
    with mock_s3():
        session = Session()
        s3 = session.client("s3", region_name="us-east-1")
        s3.create_bucket(Bucket=s3_bucket)
        s3.upload_file(input_file_path, s3_bucket, file_name)
        buckets = s3.list_buckets()["Buckets"]
        assert len(buckets) == 1
        assert buckets[0]["Name"] == s3_bucket
        yield session


@pytest.fixture(scope="session")
def mocked_s3_client(moto_s3_session):
    yield moto_s3_session.client("s3")


@pytest.fixture(scope="session")
def example_data():
    input_data = pd.DataFrame({
        "Name": ["John Smith", "James Harold", "Aura Anderson"],
        "DOB": ["19900101" "19800101", "20000117"],
        "Location": ["Boston", "New York", "Amherst"]
    })
    return input_data


@pytest.fixture(scope="session")
def example_data2():
    input_data = pd.DataFrame({
        "Name": ["John Smith", "James Harold", "Aura Anderson"],
        "Score": [10, 20, 30]
    })
    return input_data
