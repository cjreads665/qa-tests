# qa-test

**Frontend Tests**

Deploy the services to a local Kubernetes cluster (e.g., Minikube or Kind).
1. Open CLI in the cloned repository. Also make sure docker is running.

2. Run minikube 
```bash
minikube start --driver=docker
```
3. Navigate to Deployment directory and run the deployment yaml files

```bash
cd ./Deployment
kubectl apply -f backend-deployment.yaml
kubectl apply -f frontend-deployment.yaml
```
4. Check for status of the deployed services
```bash
kubectl get service
```

5. Once the services are listed, expose the frontend and backend to your machine
```bash
minikube service frontend-service
```

6. Run the following in the CLI and create a .env file or use the existing one.

```bash
npm i
```

7. add the frontend url as CYPRESS_BASE_URL in the .env file

8. run the following in the roor directory to run the test.
 ```bash
npx cypress run
```

**Scripts in Python**

1. Install the packages in requirements.txt
```bash
pip install -r requirements.txt
```

2. Run the programs using :
```bash
python3 py-health-linux.py
```

```bash
python3 py-health-request.py
```