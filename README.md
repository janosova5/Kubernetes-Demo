# Kubernetes Demo Project

This project demonstrates a microservices application deployed on Azure Kubernetes Service (AKS) using two FastAPI applications: Service A and Service B.

## Overview

**Service A**: A basic FastAPI application that responds with "Hello World".

**Service B**: A FastAPI application that responds to a request from Service A with "Hello from Service B".

## Architecture

Service A makes a FastAPI call to Service B.

Each service has: main.py file containing the FastAPI code and deployment.yaml and service.yaml files for Kubernetes configurations.

## Deployment

Setup AKS: Ensure you have an AKS cluster and have configured kubectl to connect to it.
Deploy Services:
Run:

```kubectl apply -f serviceA/deployment.yaml```


```kubectl apply -f serviceA/service.yaml```

Then:

```kubectl apply -f serviceB/deployment.yaml```

```kubectl apply -f serviceB/service.yaml```

## Access the Application:
Use the external IP address (http://74.248.137.135/) configured for Service A to access the app in a browser.

##  Additional Files

**AKS Template**: A template file from AKS Azure is included in the repository to assist with Azure resource deployment and configuration.
