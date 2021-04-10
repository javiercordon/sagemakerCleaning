import boto3

def remove_endpoints(region_name):
    client = boto3.client("sagemaker", region_name=region_name)
    endpoint_list = client.list_endpoints()
    for endpoint in endpoint_list["Endpoints"]:
        endpoint_name = endpoint["EndpointName"]
        endpoint_status = client.describe_endpoint(EndpointName=endpoint_name)["EndpointStatus"]
        if endpoint_status == "InService":
            client.delete_endpoint(EndpointName=endpoint_name)
            print(f"Deleted endpoint: {endpoint_name}")

def remove_notebooks(region_name):
    client = boto3.client("sagemaker", region_name=region_name)
    notebook_list = client.list_notebook_instances()
    for notebook in notebook_list["NotebookInstances"]:
        notebook_name = notebook["NotebookInstanceName"]
        notebook_status = notebook["NotebookInstanceStatus"]
        if notebook_status == "InService":
            client.stop_notebook_instance(NotebookInstanceName=notebook_name)
            print(f"Stop Notebook: {notebook_name}")
        if notebook_status == "Stopped":
            client.delete_notebook_instance(NotebookInstanceName=notebook_name)
            print(f"Deleted Notebook: {notebook_name}")

def remove_models(region_name):
    client = boto3.client("sagemaker", region_name=region_name)
    models_list = client.list_models()
    for model in models_list['Models']:
        model_name = model['ModelName']
        client.delete_model(ModelName=model_name)
        print(f"Deleted model: {model_name}")

def remove_endpoints_configuration(region_name):
    client = boto3.client("sagemaker", region_name=region_name)
    endpoint_configs_list = client.list_endpoint_configs()['EndpointConfigs']
    for endcpoint_config in endpoint_configs_list:
        endcpoint_config_name = endcpoint_config['EndpointConfigName']
        client.delete_endpoint_config(EndpointConfigName=endcpoint_config_name)
        print(f"Deleted Endpoint Config: {endcpoint_config_name}")
