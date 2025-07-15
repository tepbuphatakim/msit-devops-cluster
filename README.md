# DevOps Microservices Cluster

A containerized microservices application with API Gateway pattern using Docker Swarm and HAProxy.

## Project Overview

This project demonstrates a microservices architecture with three services:
- **Auth Service**: Python/Flask service for authentication (port 5000)
- **Shop Service**: Go/Gin service for shop functionality (port 4000)
- **Product Service**: Node.js/Express service for product management (port 3000)

All services are accessible through a single entry point using HAProxy as an API Gateway.

## Service Discovery

The project uses Docker Swarm's built-in DNS-based service discovery. HAProxy routes requests to the appropriate service based on the URL path.

## CI/CD Pipeline

GitHub Actions workflow automatically builds and pushes Docker images to Docker Hub when version tags are pushed.
