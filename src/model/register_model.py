import mlflow
import dagshub
import json
from pathlib import Path
from mlflow import MlflowClient
import logging


# # create logger
# logger = logging.getLogger("register_model")
# logger.setLevel(logging.INFO)

# # console handler
# handler = logging.StreamHandler()
# handler.setLevel(logging.INFO)

# # add handler to logger
# logger.addHandler(handler)

# # create a fomratter
# formatter = logging.Formatter(fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# # add formatter to handler
# handler.setFormatter(formatter)

# initialize dagshub
import dagshub
import mlflow.client
dagshub.init(repo_owner='himanshu1703', 
             repo_name='swiggy-delivery-time-prediction', 
             mlflow=True)

# set the mlflow tracking server
mlflow.set_tracking_uri("https://dagshub.com/dhirajkc15101991/food_delivery_predictions.mlflow")


def load_model_information(file_path):
    with open(file_path) as f:
        run_info = json.load(f)
        
    return run_info


if __name__ == "__main__":
    # root path
    root_path = Path(__file__).parent.parent.parent

     ################Logger Start#########################
    # create logger
    logger = logging.getLogger("model_register")
    logger.setLevel(logging.INFO)
    # console handler
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)
    # Create logs directory if not exists and make the file path
    log_dir = root_path/"logs"
    log_dir.mkdir(exist_ok=True,parents=True)
    log_data_cleaning_file_path=log_dir/"model_register.log"
    #file handler
    file_handler=logging.FileHandler(log_data_cleaning_file_path)
    file_handler.setLevel(logging.INFO)
    # add handler to logger
    logger.addHandler(stream_handler)
    logger.addHandler(file_handler)
    # create a fomratter
    formatter = logging.Formatter(fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    # add formatter to handler
    stream_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)
    ################Logger End#########################
    
    # run information file path
    run_info_path = root_path / "run_information.json"
    
    # register the model
    run_info = load_model_information(run_info_path)
    
    # get the run id
    run_id = run_info["run_id"]
    model_name = run_info["model_name"]
    
    # model to register path
    model_registry_path = f"runs:/{run_id}/{model_name}"
    
    
    # register the model
    model_version = mlflow.register_model(model_uri=model_registry_path,
                                          name=model_name)
    
    
    # get the model version
    registered_model_version = model_version.version
    registered_model_name = model_version.name
    logger.info(f"The latest model version in model registry is {registered_model_version}")
    
    # update the stage of the model to staging
    client = MlflowClient()
    client.transition_model_version_stage(
        name=registered_model_name,
        version=registered_model_version,
        stage="Staging"
    )
    
    logger.info("Model pushed to Staging stage")
    