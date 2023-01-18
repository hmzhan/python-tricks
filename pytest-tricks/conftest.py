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



