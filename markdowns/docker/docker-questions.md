<div align="center">
  <a href="https://github.com/mctavish/interview-guide" target="_blank">
    <img src="https://raw.githubusercontent.com/mctavish/interview-guide/main/assets/icons/devops-icon.svg" alt="Interview Guide Logo" width="100" height="100">
  </a>
  <h1>Docker Interview Questions & Answers</h1>
  <p><b>Practical, code-focused questions for DevOps engineers</b></p>
</div>

---

## Table of Contents

1. [How do you optimize a Docker image size using multi-stage builds?](#q1-how-do-you-optimize-a-docker-image-size-using-multi-stage-builds) <span class="intermediate">Intermediate</span>
2. [How do you secure a Docker container by running it as a non-root user?](#q2-how-do-you-secure-a-docker-container-by-running-it-as-a-non-root-user) <span class="intermediate">Intermediate</span>
3. [How do you implement health checks in Docker Compose to ensure dependent services start in order?](#q3-how-do-you-implement-health-checks-in-docker-compose-to-ensure-dependent-services-start-in-order) <span class="intermediate">Intermediate</span>
4. [How do you persist database data using Docker Volumes?](#q4-how-do-you-persist-database-data-using-docker-volumes) <span class="beginner">Beginner</span>
5. [How do you debug a crashing container that exits immediately upon starting?](#q5-how-do-you-debug-a-crashing-container-that-exits-immediately-upon-starting) <span class="intermediate">Intermediate</span>
6. [How do you connect two containers on the same host so they can communicate by name?](#q6-how-do-you-connect-two-containers-on-the-same-host-so-they-can-communicate-by-name) <span class="beginner">Beginner</span>
7. [How do you pass sensitive configuration (secrets) to a Docker container securely?](#q7-how-do-you-pass-sensitive-configuration-secrets-to-a-docker-container-securely) <span class="advanced">Advanced</span>
8. [How do you speed up Docker builds by leveraging the build cache effectively?](#q8-how-do-you-speed-up-docker-builds-by-leveraging-the-build-cache-effectively) <span class="intermediate">Intermediate</span>
9. [How do you limit the memory and CPU usage of a Docker container?](#q9-how-do-you-limit-the-memory-and-cpu-usage-of-a-docker-container) <span class="intermediate">Intermediate</span>
10. [How do you export and import a Docker image to transfer it between air-gapped systems?](#q10-how-do-you-export-and-import-a-docker-image-to-transfer-it-between-air-gapped-systems) <span class="intermediate">Intermediate</span>
11. [How do you mount a local configuration file into a container to override defaults?](#q11-how-do-you-mount-a-local-configuration-file-into-a-container-to-override-defaults) <span class="beginner">Beginner</span>
12. [How do you prevent a Docker container from accumulating large log files?](#q12-how-do-you-prevent-a-docker-container-from-accumulating-large-log-files) <span class="advanced">Advanced</span>
13. [How do you execute a command inside a running container?](#q13-how-do-you-execute-a-command-inside-a-running-container) <span class="beginner">Beginner</span>
14. [How do you clean up unused Docker resources (images, containers, networks, volumes)?](#q14-how-do-you-clean-up-unused-docker-resources-images-containers-networks-volumes) <span class="beginner">Beginner</span>
15. [How do you run a container that automatically restarts on failure?](#q15-how-do-you-run-a-container-that-automatically-restarts-on-failure) <span class="beginner">Beginner</span>
16. [How do you use `docker buildx` for multi-architecture builds?](#q16-how-do-you-use-docker-buildx-for-multi-architecture-builds) <span class="advanced">Advanced</span>
17. [How do you speed up builds using BuildKit cache mounts?](#q17-how-do-you-speed-up-builds-using-buildkit-cache-mounts) <span class="advanced">Advanced</span>
18. [How do you implement a healthcheck in Docker Compose?](#q18-how-do-you-implement-a-healthcheck-in-docker-compose) <span class="intermediate">Intermediate</span>
19. [How do you secure a container using read-only filesystems?](#q19-how-do-you-secure-a-container-using-read-only-filesystems) <span class="intermediate">Intermediate</span>
20. [How do you copy files between a container and the host?](#q20-how-do-you-copy-files-between-a-container-and-the-host) <span class="beginner">Beginner</span>
21. [How do you analyze the contents and layers of an image?](#q21-how-do-you-analyze-the-contents-and-layers-of-an-image) <span class="intermediate">Intermediate</span>
22. [How do you change the default ENTRYPOINT of an image at runtime?](#q22-how-do-you-change-the-default-entrypoint-of-an-image-at-runtime) <span class="intermediate">Intermediate</span>
23. [How do you create a Docker network for container communication?](#q23-how-do-you-create-a-docker-network-for-container-communication) <span class="intermediate">Intermediate</span>
24. [How do you use `.dockerignore` to optimize build context?](#q24-how-do-you-use-dockerignore-to-optimize-build-context) <span class="beginner">Beginner</span>
25. [How do you mount a specific file as a volume (Bind Mount)?](#q25-how-do-you-mount-a-specific-file-as-a-volume-bind-mount) <span class="beginner">Beginner</span>
26. [How do you view the logs of a running container in real-time?](#q26-how-do-you-view-the-logs-of-a-running-container-in-real-time) <span class="beginner">Beginner</span>
27. [How do you inspect a container's IP address and configuration?](#q27-how-do-you-inspect-a-containers-ip-address-and-configuration) <span class="intermediate">Intermediate</span>
28. [How do you perform a multi-architecture build using Docker Buildx?](#q28-how-do-you-perform-a-multi-architecture-build-using-docker-buildx) <span class="advanced">Advanced</span>
29. [How do you implement caching for `pip install` or `npm install` in Docker builds?](#q29-how-do-you-implement-caching-for-pip-install-or-npm-install-in-docker-builds) <span class="advanced">Advanced</span>

---

### Q1: How do you optimize a Docker image size using multi-stage builds?

**Difficulty**: Intermediate

**Strategy:**
Use a builder stage to compile dependencies/code and copy only the necessary artifacts to a slim runtime stage.

**Code Example:**
```dockerfile
# Build Stage
FROM node:18 AS builder
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

# Runtime Stage
FROM node:18-alpine
WORKDIR /app
COPY --from=builder /app/dist ./dist
COPY package*.json ./
RUN npm install --production
CMD ["node", "dist/main.js"]
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q2: How do you secure a Docker container by running it as a non-root user?

**Difficulty**: Intermediate

**Strategy:**
Create a user/group in the Dockerfile and switch to it using the `USER` instruction.

**Code Example:**
```dockerfile
FROM python:3.9-slim

# Create a group and user
RUN groupadd -r appuser && useradd -r -g appuser appuser

WORKDIR /app
COPY . .

# Change ownership
RUN chown -R appuser:appuser /app

# Switch to user
USER appuser

CMD ["python", "app.py"]
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q3: How do you implement health checks in Docker Compose to ensure dependent services start in order?

**Difficulty**: Intermediate

**Strategy:**
Define a `healthcheck` in the dependency service and use `depends_on` with `condition: service_healthy` in the consumer service.

**Code Example:**
```yaml
version: "3.8"
services:
  db:
    image: postgres
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 5s
      timeout: 5s
      retries: 5
  
  web:
    build: .
    depends_on:
      db:
        condition: service_healthy
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q4: How do you persist database data using Docker Volumes?

**Difficulty**: Beginner

**Strategy:**
Use named volumes or bind mounts. Named volumes are managed by Docker and are preferred for databases.

**Code Example:**
```yaml
version: "3.8"
services:
  db:
    image: postgres
    volumes:
      - db_data:/var/lib/postgresql/data

volumes:
  db_data:
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q5: How do you debug a crashing container that exits immediately upon starting?

**Difficulty**: Intermediate

**Strategy:**
1.  **Logs:** Check `docker logs <container_id>`.
2.  **Inspect:** Check exit code with `docker inspect <container_id>`.
3.  **Override Entrypoint:** Run with a shell to explore the environment.

**Command:**

**Code Example:**
```bash
docker run --rm -it --entrypoint sh my-image
# Once inside, try running the startup command manually
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q6: How do you connect two containers on the same host so they can communicate by name?

**Difficulty**: Beginner

**Strategy:**
Create a user-defined bridge network. Containers on the same user-defined network can resolve each other by container name (DNS).

**Code Example:**
```bash
docker network create my-net

docker run -d --name db --network my-net postgres
docker run -d --name web --network my-net my-web-app
# 'web' can now ping 'db'
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q7: How do you pass sensitive configuration (secrets) to a Docker container securely?

**Difficulty**: Advanced

**Strategy:**
Use Docker Secrets (Swarm) or environment variables via an env file (Compose). For high security in production, use a secrets manager (Vault, AWS Secrets Manager) injected at runtime.

**Code Example:**
```bash
services:
  web:
    image: my-app
    secrets:
      - db_password

secrets:
  db_password:
    file: ./secrets/db_password.txt
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q8: How do you speed up Docker builds by leveraging the build cache effectively?

**Difficulty**: Intermediate

**Strategy:**
Order instructions from least to most frequently changing. Copy dependency definitions (`package.json`, `requirements.txt`) first, install dependencies, *then* copy source code.

**Code Example:**
```dockerfile
# Good Caching Strategy
COPY package.json .
RUN npm install       # Cached unless package.json changes
COPY . .              # Re-runs only if source changes
CMD ["npm", "start"]
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q9: How do you limit the memory and CPU usage of a Docker container?

**Difficulty**: Intermediate

**Strategy:**
Use runtime flags `--memory` and `--cpus` (or equivalent in Compose).




**Compose:**

**Code Example:**
```bash
services:
  web:
    image: nginx
    deploy:
      resources:
        limits:
          cpus: '0.50'
          memory: 512M
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q10: How do you export and import a Docker image to transfer it between air-gapped systems?

**Difficulty**: Intermediate

**Strategy:**
Use `docker save` to create a tarball and `docker load` to restore it.

**Commands:**

**Code Example:**
```bash
# Export
docker save -o my-image.tar my-image:latest

# Transfer file...

# Import
docker load -i my-image.tar
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q11: How do you mount a local configuration file into a container to override defaults?

**Difficulty**: Beginner

**Strategy:**
Use a bind mount to map a host file to the container path.

**Code Example:**
```bash
docker run -d   -v $(pwd)/nginx.conf:/etc/nginx/nginx.conf:ro   nginx
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q12: How do you prevent a Docker container from accumulating large log files?

**Difficulty**: Advanced

**Strategy:**
Configure the logging driver with `max-size` and `max-file` options.

**Code Example:**
```bash
services:
  web:
    image: nginx
    logging:
      driver: "json-file"
      options:
        max-size: "10m"
        max-file: "3"
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q13: How do you execute a command inside a running container?

**Difficulty**: Beginner

**Strategy:**
Use `docker exec`. Adding `-it` allows interactive shell access.

**Command:**

**Code Example:**
```bash
# Run a database migration
docker exec my-container python manage.py migrate

# Open a shell
docker exec -it my-container /bin/bash
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q14: How do you clean up unused Docker resources (images, containers, networks, volumes)?

**Difficulty**: Beginner

**Strategy:**
Use the `docker system prune` command.

**Commands:**

**Code Example:**
```bash
# Basic cleanup (stopped containers, unused networks, dangling images)
docker system prune

# Deep cleanup (includes volumes and all unused images)
docker system prune -a --volumes
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q15: How do you run a container that automatically restarts on failure?

**Difficulty**: Beginner

**Strategy:**
Use the `--restart` policy.

**Command:**


**Compose:**

**Code Example:**
```bash
services:
  app:
    restart: always
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q16: How do you use `docker buildx` for multi-architecture builds?

**Difficulty**: Advanced

**Strategy:**
Use `docker buildx` to build images for multiple platforms (e.g., linux/amd64, linux/arm64) simultaneously and push them to a registry.

**Code Example:**
```bash
# Create a builder instance
docker buildx create --use

# Build and push for multiple platforms
docker buildx build \
  --platform linux/amd64,linux/arm64 \
  -t myuser/myimage:latest \
  --push .
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q17: How do you speed up builds using BuildKit cache mounts?

**Difficulty**: Advanced

**Strategy:**
Use `--mount=type=cache` in your Dockerfile to cache directories (like package manager caches) between builds, speeding up dependency installation.

**Code Example:**
```dockerfile
# Syntax required for BuildKit
# syntax=docker/dockerfile:1

FROM golang:1.21
WORKDIR /app
COPY go.mod go.sum ./

# Cache Go modules
RUN --mount=type=cache,target=/go/pkg/mod \
    go mod download

COPY . .
RUN go build -o main .
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q18: How do you implement a healthcheck in Docker Compose?

**Difficulty**: Intermediate

**Strategy:**
Define a `healthcheck` block in your service. Dependent services can use `condition: service_healthy` in `depends_on` to wait for it.

**Code Example:**
```bash
services:
  db:
    image: postgres
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 10s
      timeout: 5s
      retries: 5
      
  app:
    build: .
    depends_on:
      db:
        condition: service_healthy
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q19: How do you secure a container using read-only filesystems?

**Difficulty**: Intermediate

**Strategy:**
Run the container with `--read-only` to prevent modifications to the container's filesystem. Use volumes for paths that need to be writable.

**Code Example:**
```bash
docker run -d \
  --read-only \
  --tmpfs /tmp \
  --tmpfs /run \
  -v my-data:/var/lib/app/data \
  my-app:latest
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q20: How do you copy files between a container and the host?

**Difficulty**: Beginner

**Strategy:**
Use `docker cp` to copy files/directories from container to host or vice versa. Useful for debugging or extracting logs/artifacts.

**Code Example:**
```bash
# Copy file from container to host
docker cp my-container:/app/logs.txt ./local-logs.txt

# Copy file from host to container
docker cp ./config.json my-container:/app/config.json
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q21: How do you analyze the contents and layers of an image?

**Difficulty**: Intermediate

**Strategy:**
Use `docker history` to see the layers and size. For deep analysis, tools like `dive` are excellent.

**Code Example:**
```bash
# Built-in command
docker history my-image:latest

# Using dive (if installed)
dive my-image:latest
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q22: How do you change the default ENTRYPOINT of an image at runtime?

**Difficulty**: Intermediate

**Strategy:**
Use the `--entrypoint` flag to override the image's defined entrypoint. Useful for debugging (e.g., starting a shell instead of the app).

**Code Example:**
```bash
# Override entrypoint to run bash
docker run -it --entrypoint /bin/bash my-app:latest

# If the image has no bash, try sh
docker run -it --entrypoint /bin/sh my-app:latest
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q23: How do you create a Docker network for container communication?

**Difficulty**: Intermediate

**Strategy:**
Create a user-defined bridge network. Containers on the same user-defined network can communicate by container name (DNS resolution).

**Code Example:**
```bash
# Create network
docker network create my-net

# Connect containers
docker run -d --name db --network my-net postgres
docker run -d --name app --network my-net my-app-image

# App can now connect to 'db:5432'
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q24: How do you use `.dockerignore` to optimize build context?

**Difficulty**: Beginner

**Strategy:**
Create a `.dockerignore` file to exclude files (node_modules, git, logs) from being sent to the Docker daemon. This speeds up builds and reduces image size.

**Code Example:**
```bash
# .dockerignore
node_modules
.git
.env
*.log
dist
tmp
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q25: How do you mount a specific file as a volume (Bind Mount)?

**Difficulty**: Beginner

**Strategy:**
Use `-v /host/path:/container/path` to mount a specific file. This is often used for injecting configuration files.

**Code Example:**
```bash
docker run -d \
  -v $(pwd)/nginx.conf:/etc/nginx/nginx.conf:ro \
  nginx:latest
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q26: How do you view the logs of a running container in real-time?

**Difficulty**: Beginner

**Strategy:**
Use `docker logs -f <container_id>` to follow the log output (stdout/stderr).

**Code Example:**
```bash
# Follow logs
docker logs -f my-container

# Show last 100 lines and follow
docker logs --tail 100 -f my-container
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q27: How do you inspect a container's IP address and configuration?

**Difficulty**: Intermediate

**Strategy:**
Use `docker inspect` to get detailed JSON output. You can use `-f` (format) to extract specific fields.

**Code Example:**
```bash
# Get full JSON
docker inspect my-container

# Get just the IP address
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' my-container
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q28: How do you perform a multi-architecture build using Docker Buildx?

**Difficulty**: Advanced

**Strategy:**
Use `docker buildx create` to setup a builder, then use `docker buildx build --platform linux/amd64,linux/arm64` to build for multiple architectures and push to a registry.

**Code Example:**
```bash
# Create and use a new builder instance
docker buildx create --name mybuilder --use

# Build and push for multiple platforms
docker buildx build \
  --platform linux/amd64,linux/arm64 \
  -t user/app:latest \
  --push .
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q29: How do you implement caching for `pip install` or `npm install` in Docker builds?

**Difficulty**: Advanced

**Strategy:**
Use BuildKit's cache mounts (`--mount=type=cache`) to persist package directories between builds, speeding up dependency installation.

**Code Example:**
```dockerfile
# Python example
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install -r requirements.txt

# Node example
RUN --mount=type=cache,target=/root/.npm \
    npm ci
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

