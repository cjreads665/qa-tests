# qa-test

**Kubernetes Deployment:**

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

6. Copy the URL for the frontend-service tunnel

7. Navigate to cypress/e2e/helloWorld.js

8. Paste the copied URL in 

**Verification:**

- Ensure the frontend service can successfully communicate with the backend service.
- Verify that accessing the frontend URL displays the greeting message fetched from the backend.

**Automated Testing:**

- Write a simple test script (using a tool of your choice) to verify the integration between the frontend and backend services.
- The test should check that the frontend correctly displays the message returned by the backend.

**Documentation:**

- Provide a README file with instructions on how to set up and run the automated tests script.

**Deliverables:**
- Test script for automated testing.
- README file with setup and execution instructions.

**Github repo should be Public**
