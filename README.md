# E-commerce App for GitHub actions practice
[![Day 45 - Docker Build and Publish](https://github.com/rashid-khan681/e-commerce-github-actions/actions/workflows/docker-publish.yml/badge.svg)](https://github.com/rashid-khan681/e-commerce-github-actions/actions/workflows/docker-publish.yml)
## GitHub Actions Fundamentals:
- What is CI/CD
- Workflows, Jobs, Steps, Actions
- Creating workflows
- Secrets & Variables
- GitHub Pages
- Workflow Dispatch vs push


## Deploy on Elastic Beanstalk (Standard Mode)

Elastic Beanstalk is a powerful PaaS that runs your application and manages the servers, load balancer and health checks for you. This app ships as a Docker image on Docker Hub, so the only file you upload is `beanstalk/docker-compose.yml`. There is no ZIP and no Dockerfile to upload.

The image is `trainwithshubham/e-commerce-python:1.1.0`. It is built for both linux/amd64 and linux/arm64, runs as a non-root user and listens on port 8080 inside the container. The compose file publishes it on port 80 of the instance. The app also has a `/health` route that returns `{"status":"ok"}`.

### Steps

1. Sign in to the AWS console, pick a region and open the Elastic Beanstalk service.
2. Click Create environment.
3. Choose the Web server environment and keep Standard as the configuration mode.
4. Enter an application name such as `ecommerce-app`. The environment name and domain are filled in for you.
5. Under Platform, choose Docker, with the platform branch Docker running on 64bit Amazon Linux 2023. Keep the recommended platform version.
6. Under Application code, choose Upload your code and select Local file.
7. Choose the file `beanstalk/docker-compose.yml` from this repo. Give it a version label like `v1`.
8. On the service access step, pick Create and use new service role, and pick an EC2 instance profile. If you do not have one, create it from the IAM link on that page, using the AWSElasticBeanstalkWebTier managed policy. Skip the key pair.
9. Leave the remaining steps on their defaults and click Submit on the review page.

### Check that it works

1. Open the Events tab and wait for the message that the environment launched successfully. This takes a few minutes.
2. The environment health should turn green and show Ok.
3. Click the environment URL at the top of the page. You should see the e-commerce home page.
4. Add `/health` to the end of the URL. You should get `{"status":"ok"}`.

### Clean up

Terminate the environment when you are done so you are not charged for the instance. From the environment page choose Actions, then Terminate environment, and type the environment name to confirm. You can delete the application as well from the Applications page.

### Run it locally

```
docker compose up -d
```

Then open http://localhost. The root `docker-compose.yml` uses the `latest` tag, and the Beanstalk one pins `1.1.0`.
