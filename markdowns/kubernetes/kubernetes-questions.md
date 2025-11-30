<div align="center">
  <a href="https://github.com/mctavish/interview-guide" target="_blank">
    <img src="https://raw.githubusercontent.com/mctavish/interview-guide/main/assets/icons/devops-icon.svg" alt="Interview Guide Logo" width="100" height="100">
  </a>
  <h1>Kubernetes Interview Questions & Answers</h1>
  <p><b>Practical, code-focused questions for DevOps engineers</b></p>
</div>

---

## Table of Contents

1. [How do you manage configuration data separately from application code?](#q1-how-do-you-manage-configuration-data-separately-from-application-code) <span class="beginner">Beginner</span>
2. [How do you ensure zero-downtime deployments?](#q2-how-do-you-ensure-zero-downtime-deployments) <span class="intermediate">Intermediate</span>
3. [How do you expose a service to the internet securely?](#q3-how-do-you-expose-a-service-to-the-internet-securely) <span class="intermediate">Intermediate</span>
4. [How do you scale pods automatically based on CPU usage?](#q4-how-do-you-scale-pods-automatically-based-on-cpu-usage) <span class="intermediate">Intermediate</span>
5. [How do you schedule a pod on a specific node (e.g., one with GPU)?](#q5-how-do-you-schedule-a-pod-on-a-specific-node-eg-one-with-gpu) <span class="intermediate">Intermediate</span>
6. [How do you restrict network traffic between pods?](#q6-how-do-you-restrict-network-traffic-between-pods) <span class="advanced">Advanced</span>
7. [How do you manage stateful applications (like Databases) in Kubernetes?](#q7-how-do-you-manage-stateful-applications-like-databases-in-kubernetes) <span class="advanced">Advanced</span>
8. [How do you ensure a pod runs on every node (e.g., log collector)?](#q8-how-do-you-ensure-a-pod-runs-on-every-node-eg-log-collector) <span class="intermediate">Intermediate</span>
9. [How do you debug a crashing pod?](#q9-how-do-you-debug-a-crashing-pod) <span class="beginner">Beginner</span>
10. [How do you limit the resources (CPU/RAM) a namespace can consume?](#q10-how-do-you-limit-the-resources-cpuram-a-namespace-can-consume) <span class="intermediate">Intermediate</span>
11. [How do you run a one-time task (e.g., DB migration)?](#q11-how-do-you-run-a-one-time-task-eg-db-migration) <span class="beginner">Beginner</span>
12. [How do you control who can access what in the cluster?](#q12-how-do-you-control-who-can-access-what-in-the-cluster) <span class="advanced">Advanced</span>
13. [How do you share storage between containers in the same pod?](#q13-how-do-you-share-storage-between-containers-in-the-same-pod) <span class="intermediate">Intermediate</span>
14. [How do you package and distribute a Kubernetes application?](#q14-how-do-you-package-and-distribute-a-kubernetes-application) <span class="intermediate">Intermediate</span>
15. [How do you ensure a pod is only scheduled on nodes with specific hardware (e.g., GPU)?](#q15-how-do-you-ensure-a-pod-is-only-scheduled-on-nodes-with-specific-hardware-eg-gpu) <span class="intermediate">Intermediate</span>
16. [How do you prevent pods from being scheduled on a node (Taints & Tolerations)?](#q16-how-do-you-prevent-pods-from-being-scheduled-on-a-node-taints-&-tolerations) <span class="intermediate">Intermediate</span>
17. [How do you configure Liveness and Readiness Probes?](#q17-how-do-you-configure-liveness-and-readiness-probes) <span class="intermediate">Intermediate</span>
18. [How do you manage sensitive configuration data (Secrets)?](#q18-how-do-you-manage-sensitive-configuration-data-secrets) <span class="beginner">Beginner</span>
19. [How do you run a pod on every node in the cluster (DaemonSet)?](#q19-how-do-you-run-a-pod-on-every-node-in-the-cluster-daemonset) <span class="intermediate">Intermediate</span>
20. [How do you perform a rolling update for a Deployment?](#q20-how-do-you-perform-a-rolling-update-for-a-deployment) <span class="beginner">Beginner</span>
21. [How do you expose a service to the outside world (Ingress)?](#q21-how-do-you-expose-a-service-to-the-outside-world-ingress) <span class="intermediate">Intermediate</span>
22. [How do you persist data for stateful applications (StatefulSet)?](#q22-how-do-you-persist-data-for-stateful-applications-statefulset) <span class="advanced">Advanced</span>
23. [How do you use ConfigMaps to decouple configuration from code?](#q23-how-do-you-use-configmaps-to-decouple-configuration-from-code) <span class="beginner">Beginner</span>
24. [How do you auto-scale pods based on CPU usage (HPA)?](#q24-how-do-you-auto-scale-pods-based-on-cpu-usage-hpa) <span class="intermediate">Intermediate</span>
25. [How do you implement a CronJob in Kubernetes?](#q25-how-do-you-implement-a-cronjob-in-kubernetes) <span class="beginner">Beginner</span>
26. [How do you grant specific permissions to a Pod (RBAC)?](#q26-how-do-you-grant-specific-permissions-to-a-pod-rbac) <span class="advanced">Advanced</span>
27. [How do you create a Service to load balance traffic to pods?](#q27-how-do-you-create-a-service-to-load-balance-traffic-to-pods) <span class="beginner">Beginner</span>
28. [How do you use a Sidecar container to handle log shipping?](#q28-how-do-you-use-a-sidecar-container-to-handle-log-shipping) <span class="intermediate">Intermediate</span>
29. [How do you perform a Canary Deployment using Istio or basic K8s?](#q29-how-do-you-perform-a-canary-deployment-using-istio-or-basic-k8s) <span class="advanced">Advanced</span>
30. [How do you secure Pod-to-Pod communication using mTLS?](#q30-how-do-you-secure-pod-to-pod-communication-using-mtls) <span class="advanced">Advanced</span>

---

### Q1: How do you manage configuration data separately from application code?

**Difficulty**: Beginner

**Strategy:**
Use **ConfigMaps** for non-sensitive data and **Secrets** for sensitive data (passwords, tokens). Mount them as environment variables or volumes in the Pod.

**Code Example:**
```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-config
data:
  DB_HOST: "db.example.com"
---
# Usage in Pod
env:
  - name: DATABASE_HOST
    valueFrom:
      configMapKeyRef:
        name: app-config
        key: DB_HOST
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q2: How do you ensure zero-downtime deployments?

**Difficulty**: Intermediate

**Strategy:**
Use a **Deployment** with `RollingUpdate` strategy. Configure `readinessProbe` to ensure new pods are ready to accept traffic before old ones are terminated.

**Code Example:**
```yaml
strategy:
  type: RollingUpdate
  rollingUpdate:
    maxUnavailable: 1
    maxSurge: 1
template:
  spec:
    containers:
      - name: app
        readinessProbe:
          httpGet:
            path: /health
            port: 8080
          initialDelaySeconds: 5
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q3: How do you expose a service to the internet securely?

**Difficulty**: Intermediate

**Strategy:**
Use an **Ingress** resource with an Ingress Controller (e.g., Nginx). Configure TLS termination using a Secret containing the SSL certificate.

**Code Example:**
```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: app-ingress
spec:
  tls:
  - hosts:
    - myapp.com
    secretName: myapp-tls
  rules:
  - host: myapp.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: my-service
            port:
              number: 80
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q4: How do you scale pods automatically based on CPU usage?

**Difficulty**: Intermediate

**Strategy:**
Use **Horizontal Pod Autoscaler (HPA)**. Ensure `metrics-server` is running and requests are defined in the Pod spec.

**Code Example:**
```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: my-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: my-app
  minReplicas: 2
  maxReplicas: 10
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 50
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q5: How do you schedule a pod on a specific node (e.g., one with GPU)?

**Difficulty**: Intermediate

**Strategy:**
Use **Node Selectors** (simple) or **Node Affinity** (flexible). Label the node first (e.g., `kubectl label nodes node1 gpu=true`).

**Code Example:**
```yaml
spec:
  affinity:
    nodeAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
        nodeSelectorTerms:
        - matchExpressions:
          - key: gpu
            operator: In
            values:
            - "true"
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q6: How do you restrict network traffic between pods?

**Difficulty**: Advanced

**Strategy:**
Use **NetworkPolicies**. By default, all traffic is allowed. Define a policy to deny ingress/egress unless explicitly allowed.

**Code Example:**
```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: deny-all
spec:
  podSelector: {}
  policyTypes:
  - Ingress
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q7: How do you manage stateful applications (like Databases) in Kubernetes?

**Difficulty**: Advanced

**Strategy:**
Use **StatefulSets** instead of Deployments. They provide stable network IDs (pod-0, pod-1), stable storage with **PersistentVolumeClaims**, and ordered deployment/scaling.

**Code Example:**
```yaml
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: db
spec:
  serviceName: "db"
  replicas: 3
  template:
    spec:
      containers:
      - name: postgres
        volumeMounts:
        - name: data
          mountPath: /var/lib/postgresql/data
  volumeClaimTemplates:
  - metadata:
      name: data
    spec:
      accessModes: [ "ReadWriteOnce" ]
      resources:
        requests:
          storage: 10Gi
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q8: How do you ensure a pod runs on every node (e.g., log collector)?

**Difficulty**: Intermediate

**Strategy:**
Use a **DaemonSet**. It ensures that a copy of the Pod runs on all (or some) Nodes.

**Code Example:**
```yaml
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: fluentd
spec:
  template:
    spec:
      containers:
      - name: fluentd
        image: fluentd:latest
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q9: How do you debug a crashing pod?

**Difficulty**: Beginner

**Strategy:**
1. Check status: `kubectl get pods`
2. View logs: `kubectl logs <pod-name> --previous`
3. Describe pod events: `kubectl describe pod <pod-name>`
4. Exec into pod (if running): `kubectl exec -it <pod-name> -- /bin/sh`

**Code Example:**
```bash
# Check why it crashed
kubectl describe pod my-pod-12345

# Check logs of the previous instance
kubectl logs my-pod-12345 --previous
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q10: How do you limit the resources (CPU/RAM) a namespace can consume?

**Difficulty**: Intermediate

**Strategy:**
Use **ResourceQuota**. It limits the aggregate resource consumption (CPU, memory, pods, etc.) in a namespace.

**Code Example:**
```yaml
apiVersion: v1
kind: ResourceQuota
metadata:
  name: compute-quota
  namespace: dev
spec:
  hard:
    pods: "10"
    requests.cpu: "4"
    requests.memory: 2Gi
    limits.cpu: "10"
    limits.memory: 4Gi
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q11: How do you run a one-time task (e.g., DB migration)?

**Difficulty**: Beginner

**Strategy:**
Use a **Job**. It creates one or more Pods and ensures they successfully terminate.

**Code Example:**
```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: db-migration
spec:
  template:
    spec:
      containers:
      - name: migration
        image: migrate:v1
        command: ["./migrate.sh"]
      restartPolicy: Never
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q12: How do you control who can access what in the cluster?

**Difficulty**: Advanced

**Strategy:**
Use **RBAC (Role-Based Access Control)**. Define `Role` (permissions) and `RoleBinding` (assign role to user/group) for namespace-level access, or `ClusterRole` and `ClusterRoleBinding` for cluster-wide access.

**Code Example:**
```yaml
# Allow reading pods in default namespace
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  namespace: default
  name: pod-reader
rules:
- apiGroups: [""]
  resources: ["pods"]
  verbs: ["get", "watch", "list"]
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q13: How do you share storage between containers in the same pod?

**Difficulty**: Intermediate

**Strategy:**
Use an `emptyDir` volume. It is created when the Pod is assigned to a node and exists as long as the Pod is running. Both containers mount the same volume.

**Code Example:**
```yaml
spec:
  volumes:
  - name: shared-data
    emptyDir: {}
  containers:
  - name: writer
    volumeMounts:
    - name: shared-data
      mountPath: /data
  - name: reader
    volumeMounts:
    - name: shared-data
      mountPath: /read
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q14: How do you package and distribute a Kubernetes application?

**Difficulty**: Intermediate

**Strategy:**
Use **Helm Charts**. Helm is a package manager for Kubernetes that allows you to define, install, and upgrade applications using templates.

**Code Example:**
```yaml
# Install a chart
helm install my-release bitnami/nginx

# Create a chart
helm create my-chart
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q15: How do you ensure a pod is only scheduled on nodes with specific hardware (e.g., GPU)?

**Difficulty**: Intermediate

**Strategy:**
Use `nodeSelector` for simple constraints or `nodeAffinity` for more expressive rules (e.g., required vs preferred).

**Code Example:**
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: gpu-pod
spec:
  containers:
  - name: cuda-container
    image: nvidia/cuda:11.0
  nodeSelector:
    disktype: ssd
    gpu: "true"
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q16: How do you prevent pods from being scheduled on a node (Taints & Tolerations)?

**Difficulty**: Intermediate

**Strategy:**
Apply a Taint to a node to repel pods. Add a Toleration to a pod to allow it to be scheduled on that tainted node.

**Code Example:**
```bash
# 1. Taint the node
# kubectl taint nodes node1 key=value:NoSchedule

# 2. Add Toleration to Pod
apiVersion: v1
kind: Pod
metadata:
  name: tolerated-pod
spec:
  containers:
  - name: nginx
    image: nginx
  tolerations:
  - key: "key"
    operator: "Equal"
    value: "value"
    effect: "NoSchedule"
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q17: How do you configure Liveness and Readiness Probes?

**Difficulty**: Intermediate

**Strategy:**
Liveness probes restart the container if it fails. Readiness probes remove the pod from service endpoints until it passes.

**Code Example:**
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: probed-pod
spec:
  containers:
  - name: nginx
    image: nginx
    livenessProbe:
      httpGet:
        path: /healthz
        port: 80
      initialDelaySeconds: 3
      periodSeconds: 3
    readinessProbe:
      httpGet:
        path: /ready
        port: 80
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q18: How do you manage sensitive configuration data (Secrets)?

**Difficulty**: Beginner

**Strategy:**
Use Kubernetes Secrets to store passwords, tokens, or keys. They can be mounted as volumes or exposed as environment variables.

**Code Example:**
```yaml
apiVersion: v1
kind: Secret
metadata:
  name: my-secret
type: Opaque
data:
  # Base64 encoded values
  username: YWRtaW4=
  password: MWYyZDFlMmU2N2Rm
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q19: How do you run a pod on every node in the cluster (DaemonSet)?

**Difficulty**: Intermediate

**Strategy:**
Use a `DaemonSet` for system daemons like log collectors (Fluentd) or monitoring agents (Node Exporter) that need to run on every node.

**Code Example:**
```yaml
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: fluentd
spec:
  selector:
    matchLabels:
      name: fluentd
  template:
    metadata:
      labels:
        name: fluentd
    spec:
      containers:
      - name: fluentd
        image: fluentd:latest
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q20: How do you perform a rolling update for a Deployment?

**Difficulty**: Beginner

**Strategy:**
Update the image in the Deployment spec. Kubernetes automatically performs a rolling update, replacing old pods with new ones gradually.

**Code Example:**
```bash
# Imperative command
kubectl set image deployment/nginx-deployment nginx=nginx:1.16.1

# Or edit the yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
spec:
  replicas: 3
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxUnavailable: 1
      maxSurge: 1
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q21: How do you expose a service to the outside world (Ingress)?

**Difficulty**: Intermediate

**Strategy:**
Use an Ingress resource to manage external access to services, typically via HTTP/HTTPS. Requires an Ingress Controller (e.g., Nginx) to be running.

**Code Example:**
```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: my-ingress
spec:
  rules:
  - host: myapp.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: my-service
            port:
              number: 80
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q22: How do you persist data for stateful applications (StatefulSet)?

**Difficulty**: Advanced

**Strategy:**
Use a `StatefulSet` with `volumeClaimTemplates`. This ensures each pod gets its own unique Persistent Volume (PV) that persists across restarts.

**Code Example:**
```yaml
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: web
spec:
  serviceName: "nginx"
  replicas: 3
  selector:
    matchLabels:
      app: nginx
  volumeClaimTemplates:
  - metadata:
      name: www
    spec:
      accessModes: [ "ReadWriteOnce" ]
      resources:
        requests:
          storage: 1Gi
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q23: How do you use ConfigMaps to decouple configuration from code?

**Difficulty**: Beginner

**Strategy:**
Store configuration in a `ConfigMap` and inject it into pods as environment variables or mounted files.

**Code Example:**
```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-config
data:
  APP_COLOR: blue
  APP_MODE: production

---
# Usage in Pod
envFrom:
- configMapRef:
    name: app-config
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q24: How do you auto-scale pods based on CPU usage (HPA)?

**Difficulty**: Intermediate

**Strategy:**
Use the Horizontal Pod Autoscaler (HPA). It automatically scales the number of pods in a replication controller, deployment, replica set or stateful set based on observed CPU utilization.

**Code Example:**
```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: php-apache
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: php-apache
  minReplicas: 1
  maxReplicas: 10
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 50
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q25: How do you implement a CronJob in Kubernetes?

**Difficulty**: Beginner

**Strategy:**
Use the `CronJob` resource to run Jobs on a time-based schedule (like Linux cron).

**Code Example:**
```yaml
apiVersion: batch/v1
kind: CronJob
metadata:
  name: hello
spec:
  schedule: "*/1 * * * *"
  jobTemplate:
    spec:
      template:
        spec:
          containers:
          - name: hello
            image: busybox
            imagePullPolicy: IfNotPresent
            command:
            - /bin/sh
            - -c
            - date; echo Hello from the Kubernetes cluster
          restartPolicy: OnFailure
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q26: How do you grant specific permissions to a Pod (RBAC)?

**Difficulty**: Advanced

**Strategy:**
Create a ServiceAccount, a Role (defining permissions), and a RoleBinding (linking the ServiceAccount to the Role). Assign the ServiceAccount to the Pod.

**Code Example:**
```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  namespace: default
  name: pod-reader
rules:
- apiGroups: [""]
  resources: ["pods"]
  verbs: ["get", "watch", "list"]

---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: read-pods
  namespace: default
subjects:
- kind: ServiceAccount
  name: my-sa
  namespace: default
roleRef:
  kind: Role
  name: pod-reader
  apiGroup: rbac.authorization.k8s.io
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q27: How do you create a Service to load balance traffic to pods?

**Difficulty**: Beginner

**Strategy:**
Create a `Service` resource. The `selector` determines which pods receive traffic. `type: ClusterIP` is default (internal only).

**Code Example:**
```yaml
apiVersion: v1
kind: Service
metadata:
  name: my-service
spec:
  selector:
    app: MyApp
  ports:
    - protocol: TCP
      port: 80
      targetPort: 9376
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q28: How do you use a Sidecar container to handle log shipping?

**Difficulty**: Intermediate

**Strategy:**
Run a secondary container (e.g., fluentd) in the same Pod to read logs from a shared volume and ship them to a central logging system.

**Code Example:**
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: sidecar-logging
spec:
  containers:
  - name: app
    image: my-app
    volumeMounts:
    - name: logs
      mountPath: /var/log/app
  - name: log-shipper
    image: fluentd
    volumeMounts:
    - name: logs
      mountPath: /var/log/app
  volumes:
  - name: logs
    emptyDir: {}
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q29: How do you perform a Canary Deployment using Istio or basic K8s?

**Difficulty**: Advanced

**Strategy:**
Create two Deployments (v1 and v2). Use a Service to split traffic between them. With plain K8s, you control the ratio by replica count. With Istio, you define `VirtualService` weights.

**Code Example:**
```yaml
# Istio VirtualService Example
apiVersion: networking.istio.io/v1alpha3
kind: VirtualService
metadata:
  name: my-app
spec:
  hosts:
  - my-app
  http:
  - route:
    - destination:
        host: my-app
        subset: v1
      weight: 90
    - destination:
        host: my-app
        subset: v2
      weight: 10
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q30: How do you secure Pod-to-Pod communication using mTLS?

**Difficulty**: Advanced

**Strategy:**
Use a Service Mesh like Istio or Linkerd. Enable 'strict' mTLS mode globally or per-namespace to ensure all traffic is encrypted and authenticated.

**Code Example:**
```yaml
# Istio PeerAuthentication
apiVersion: security.istio.io/v1beta1
kind: PeerAuthentication
metadata:
  name: default
  namespace: default
spec:
  mtls:
    mode: STRICT
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

