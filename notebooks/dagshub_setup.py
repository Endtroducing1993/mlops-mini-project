import mlflow
import dagshub


mlflow.set_tracking_uri(dagshub.get_mlflow_tracking_uri("https://dagshub.com/Endtroducing1993/mlops-mini-project.mlflow"))
dagshub.init(repo_owner='Endtroducing1993', repo_name='mlops-mini-project', mlflow=True)


with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)