import os

config_dev = {
    "username": os.getenv("proj_dev_user"),
    "password": os.getenv("proj_dev_pd"),
    "api_key": os.getenv("proj_api_dev_key"),
    "effective_date": "2023-01-01"
}


config_qa = {
    "username": os.getenv("proj_qa_user"),
    "password": os.getenv("proj_qa_pd"),
    "api_key": os.getenv("proj_api_qa_key"),
    "effective_date": "2023-01-01"
}


config_prod = {
    "username": os.getenv("proj_prod_user"),
    "password": os.getenv("proj_prod_pd"),
    "api_key": os.getenv("proj_api_prod_key"),
    "effective_date": "2023-01-01"
}