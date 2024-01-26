# RailwayTrackFaultDetection

## work flows
1. Update config.yaml
2. Update Params.yaml
3. Updae the entity
4. Update the configuration manager in src config
5. Update the components
6. Update the pipline
7. Update the main.py
8. Update the dvc.yaml
9. app.py

# How to run 
## STEPS:
Clone the repository
```bash
https://github.com/srinivas-dheekonda/RailwayTrackFaultDetection.git
```
## STEP 01- Create a conda environment after opening the repository

```bash
conda create -n cnncls python=3.8 -y
```
```bash
conda activate cnncls

```

## STEP 02- install the requirements

```bash
pip install -r requirements.txt

```
```bash
# Finally run the following command
python app.py

```

```bash
# Finally run the following command
open up you local host and port

```



## MLflow

- [Documentation](https://mlflow.org/docs/latest/index.html)

- [MLflow tutorial](https://youtu.be/qdcHHrsXA48?si=bD5vDS60akNphkem)

##### cmd
- mlflow ui

### dagshub
[dagshub](https://dagshub.com/)

MLFLOW_TRACKING_URI=https://dagshub.com/srinivas-dheekonda/RailwayTrackFaultDetection.mlflow
MLFLOW_TRACKING_USERNA="srinivas-dheekonda"
MLFLOW_TRACKING_PASSWORD=225798ebbba2380a98b1556a67323dfe28b44640
python script.py

Run this to export as env variables:

```bash

get MLFLOW_TRACKING_URI=https://dagshub.com/srinivas-dheekonda/RailwayTrackFaultDetection.mlflow

get MLFLOW_TRACKING_USERNAME="srinivas-dheekonda" 

get MLFLOW_TRACKING_PASSWORD=225798ebbba2380a98b1556a67323dfe28b44640

```


### DVC cmd

1. dvc init
2. dvc repro
3. dvc dag

