# MLOps experiments

This project contains model-training configurations and scripts that log parameters, metrics and artifacts to MLflow, push metrics to Prometheus PushGateway, and display them in Grafana.

## Run training

Install dependencies:

```bash
pip install -r experiments/requirements.txt
```

Forward MLflow and PushGateway ports in separate terminals:

```bash
kubectl port-forward svc/mlflow -n application 5000:5000
kubectl port-forward svc/pushgateway -n monitoring 9091:9091
```

Run the training script:

```bash
python experiments/train_and_push.py
```

Experiments appear in MLflow. Prometheus exposes `mlflow_accuracy` and `mlflow_loss`, and the best model is saved in `best_model/`.

## Check service status

```bash
# MLflow
kubectl get pods -n application | grep mlflow
kubectl get svc -n application | grep mlflow

# MinIO
kubectl get pods -n application | grep minio
kubectl get svc -n application | grep minio

# PostgreSQL: MLflow backend
kubectl get pods -n application | grep postgres

# PushGateway
kubectl get pods -n monitoring | grep pushgateway
kubectl get svc -n monitoring | grep pushgateway
```

## View Grafana metrics

```bash
kubectl port-forward svc/grafana -n monitoring 3000:3000
```

Open [http://localhost:3000](http://localhost:3000), select **Explore**, choose the **Prometheus** data source, then query `mlflow_accuracy` or `mlflow_loss`.

[Argo CD application configurations](../../DevOps/goit-argo/).
