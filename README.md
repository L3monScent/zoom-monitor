# Zoom Status Monitor
Checks the Public Zoom Service Status API and returns the status of each component. Runnable localy, as as Docker container, or as a Kubernetes job

## Run Locally
'''bash
python zoom_monitor.py

### Docker
'''bash
docker built -t zoom-monitor .
docker run zoom-monitor

#### Kubernetes
'''bash
kubectl apply -f zoom-job.yml
kubectl logs jobs/zoom-status-check

##### CI/CD
Automated GitHub Actions workflow runs every 30 minutes can can be triggered manually from the Actions tab.