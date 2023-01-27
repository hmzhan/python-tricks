import os


class Common:
    def __init__(self):
        self.effective_date = "2023-01-01"
        self.role = "data-scientist"
        self.s3_object_key = "path/to/proj_data"


class ConfigQa(Common):
    def __init__(self):
        super().__init__()
        self.username = os.getenv("proj_qa_user")
        self.password = os.getenv("proj_qa_pd")
        self.api_key = os.getenv("proj_api_qa_key")


class ConfigProd(Common):
    def __init__(self):
        super().__init__()
        self.username = os.getenv("proj_prod_user")
        self.password = os.getenv("proj_prod_pd")
        self.api_key = os.getenv("proj_api_prod_key")
