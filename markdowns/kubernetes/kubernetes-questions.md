<div align="center">
  <a href="https://github.com/mctavish/interview-guide" target="_blank">
    <img src="https://raw.githubusercontent.com/mctavish/interview-guide/main/assets/icons/devops-icon.svg" alt="Interview Guide Logo" width="100" height="100">
  </a>
  <h1>Kubernetes Interview Questions & Answers</h1>
  <p><b>Practical, code-focused questions for DevOps engineers</b></p>
</div>

---

## Table of Contents

1. [How do you decouple configuration from application code using ConfigMaps?](#q1-how-do-you-decouple-configuration-from-application-code-using-configmaps) <span class="beginner">Beginner</span>
2. [How do you securely manage sensitive data like passwords?](#q2-how-do-you-securely-manage-sensitive-data-like-passwords) <span class="beginner">Beginner</span>
3. [How do you ensure zero-downtime deployments?](#q3-how-do-you-ensure-zero-downtime-deployments) <span class="intermediate">Intermediate</span>
4. [How do you expose HTTP/HTTPS services to the internet?](#q4-how-do-you-expose-httphttps-services-to-the-internet) <span class="intermediate">Intermediate</span>
5. [How do you auto-scale pods based on CPU or Memory usage?](#q5-how-do-you-auto-scale-pods-based-on-cpu-or-memory-usage) <span class="intermediate">Intermediate</span>
6. [How do you ensure a pod runs on a specific node (e.g., with GPU)?](#q6-how-do-you-ensure-a-pod-runs-on-a-specific-node-eg-with-gpu) <span class="intermediate">Intermediate</span>
7. [How do you restrict network traffic between pods?](#q7-how-do-you-restrict-network-traffic-between-pods) <span class="advanced">Advanced</span>
8. [How do you manage stateful applications (Databases) with stable identities?](#q8-how-do-you-manage-stateful-applications-databases-with-stable-identities) <span class="advanced">Advanced</span>
9. [How do you run a system daemon (like logs/monitoring) on every node?](#q9-how-do-you-run-a-system-daemon-like-logsmonitoring-on-every-node) <span class="intermediate">Intermediate</span>
10. [How do you debug a crashing Pod?](#q10-how-do-you-debug-a-crashing-pod) <span class="beginner">Beginner</span>
11. [How do you limit the total resources (CPU/RAM) a namespace can use?](#q11-how-do-you-limit-the-total-resources-cpuram-a-namespace-can-use) <span class="intermediate">Intermediate</span>
12. [How do you run a one-off task (like a DB migration)?](#q12-how-do-you-run-a-one-off-task-like-a-db-migration) <span class="beginner">Beginner</span>
13. [How do you control user permissions in the cluster?](#q13-how-do-you-control-user-permissions-in-the-cluster) <span class="advanced">Advanced</span>
14. [How do you share temporary storage between containers in the same Pod?](#q14-how-do-you-share-temporary-storage-between-containers-in-the-same-pod) <span class="intermediate">Intermediate</span>
15. [How do you package Kubernetes applications for easy distribution?](#q15-how-do-you-package-kubernetes-applications-for-easy-distribution) <span class="intermediate">Intermediate</span>
16. [How do you prevent pods from being scheduled on a specific node (Taints)?](#q16-how-do-you-prevent-pods-from-being-scheduled-on-a-specific-node-taints) <span class="intermediate">Intermediate</span>
17. [How do you detect if a container is alive vs. ready to serve traffic?](#q17-how-do-you-detect-if-a-container-is-alive-vs-ready-to-serve-traffic) <span class="intermediate">Intermediate</span>
18. [How do you load balance traffic to a set of Pods?](#q18-how-do-you-load-balance-traffic-to-a-set-of-pods) <span class="beginner">Beginner</span>
19. [How do you use a Sidecar container?](#q19-how-do-you-use-a-sidecar-container) <span class="intermediate">Intermediate</span>
20. [How do you run tasks on a schedule (Cron)?](#q20-how-do-you-run-tasks-on-a-schedule-cron) <span class="beginner">Beginner</span>
21. [How do you perform a Canary Deployment?](#q21-how-do-you-perform-a-canary-deployment) <span class="advanced">Advanced</span>
22. [How do you secure Pod-to-Pod communication with mTLS?](#q22-how-do-you-secure-pod-to-pod-communication-with-mtls) <span class="advanced">Advanced</span>
23. [How do you ensure high availability during voluntary disruptions (e.g., node draining)?](#q23-how-do-you-ensure-high-availability-during-voluntary-disruptions-eg-node-draining) <span class="advanced">Advanced</span>
24. [How do you manage persistent storage requests?](#q24-how-do-you-manage-persistent-storage-requests) <span class="intermediate">Intermediate</span>
25. [How do you initialize a Pod before the main container starts?](#q25-how-do-you-initialize-a-pod-before-the-main-container-starts) <span class="intermediate">Intermediate</span>
26. [How do you extend Kubernetes capabilities?](#q26-how-do-you-extend-kubernetes-capabilities) <span class="advanced">Advanced</span>
27. [How do you troubleshoot DNS issues in the cluster?](#q27-how-do-you-troubleshoot-dns-issues-in-the-cluster) <span class="intermediate">Intermediate</span>
28. [How do you assign an identity to a Pod for AWS/GCP access?](#q28-how-do-you-assign-an-identity-to-a-pod-for-awsgcp-access) <span class="advanced">Advanced</span>
29. [How do you vertically scale a pod (VPA)?](#q29-how-do-you-vertically-scale-a-pod-vpa) <span class="advanced">Advanced</span>
30. [How do you define a custom metric for HPA?](#q30-how-do-you-define-a-custom-metric-for-hpa) <span class="advanced">Advanced</span>
31. [How do you perform a blue-green deployment?](#q31-how-do-you-perform-a-blue-green-deployment) <span class="advanced">Advanced</span>
32. [How do you manage multi-tenancy in a cluster?](#q32-how-do-you-manage-multi-tenancy-in-a-cluster) <span class="advanced">Advanced</span>
33. [How do you inject a sidecar proxy automatically (e.g., Istio)?](#q33-how-do-you-inject-a-sidecar-proxy-automatically-eg-istio) <span class="advanced">Advanced</span>
34. [How do you handle container termination gracefully?](#q34-how-do-you-handle-container-termination-gracefully) <span class="intermediate">Intermediate</span>
35. [How do you secure the Kubernetes API server?](#q35-how-do-you-secure-the-kubernetes-api-server) <span class="advanced">Advanced</span>
36. [How do you use a headless service?](#q36-how-do-you-use-a-headless-service) <span class="intermediate">Intermediate</span>
37. [How do you implement gitops for Kubernetes?](#q37-how-do-you-implement-gitops-for-kubernetes) <span class="advanced">Advanced</span>
38. [How do you drain a node for maintenance?](#q38-how-do-you-drain-a-node-for-maintenance) <span class="intermediate">Intermediate</span>
39. [How do you verify that a Helm chart is valid?](#q39-how-do-you-verify-that-a-helm-chart-is-valid) <span class="intermediate">Intermediate</span>
40. [How do you use ephemeral containers for debugging?](#q40-how-do-you-use-ephemeral-containers-for-debugging) <span class="advanced">Advanced</span>
41. [How do you mount a single file from a ConfigMap without overwriting the directory?](#q41-how-do-you-mount-a-single-file-from-a-configmap-without-overwriting-the-directory) <span class="intermediate">Intermediate</span>
42. [How do you set a default StorageClass?](#q42-how-do-you-set-a-default-storageclass) <span class="intermediate">Intermediate</span>
43. [How do you backup a Kubernetes cluster (etcd)?](#q43-how-do-you-backup-a-kubernetes-cluster-etcd) <span class="advanced">Advanced</span>
44. [How do you force delete a Pod stuck in 'Terminating'?](#q44-how-do-you-force-delete-a-pod-stuck-in-terminating) <span class="intermediate">Intermediate</span>
45. [How do you monitor Kubernetes components?](#q45-how-do-you-monitor-kubernetes-components) <span class="intermediate">Intermediate</span>
46. [How do you limit the number of Jobs history kept?](#q46-how-do-you-limit-the-number-of-jobs-history-kept) <span class="intermediate">Intermediate</span>
47. [How do you run a Windows container in Kubernetes?](#q47-how-do-you-run-a-windows-container-in-kubernetes) <span class="advanced">Advanced</span>
48. [How do you use a priority class to ensure critical pods are scheduled?](#q48-how-do-you-use-a-priority-class-to-ensure-critical-pods-are-scheduled) <span class="advanced">Advanced</span>
49. [How do you automatically rotate TLS certificates?](#q49-how-do-you-automatically-rotate-tls-certificates) <span class="advanced">Advanced</span>
50. [How do you secure your supply chain with Image Signing (Kyverno/Gatekeeper)?](#q50-how-do-you-secure-your-supply-chain-with-image-signing-kyvernogatekeeper) <span class="advanced">Advanced</span>

---

### Q1: How do you decouple configuration from application code using ConfigMaps?

**Difficulty**: Beginner

**Strategy:**
Use **ConfigMaps** to store non-sensitive configuration. Inject them into Pods as environment variables or mounted files.

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

### Q2: How do you securely manage sensitive data like passwords?

**Difficulty**: Beginner

**Strategy:**
Use **Secrets**. They are base64 encoded (not encrypted by default, use encryption-at-rest) and mounted as volumes or env vars, kept in tmpfs on the node.

**Code Example:**

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: db-secret
type: Opaque
data:
  # echo -n 'password' | base64
  password: cGFzc3dvcmQ=
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q3: How do you ensure zero-downtime deployments?

**Difficulty**: Intermediate

**Strategy:**
Use a **Deployment** with `RollingUpdate` strategy and configure **Readiness Probes** to prevent traffic to unready pods.

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
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q4: How do you expose HTTP/HTTPS services to the internet?

**Difficulty**: Intermediate

**Strategy:**
Use an **Ingress** resource backed by an Ingress Controller (e.g., Nginx). It provides load balancing, SSL termination, and name-based virtual hosting.

**Code Example:**

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: app-ingress
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

### Q5: How do you auto-scale pods based on CPU or Memory usage?

**Difficulty**: Intermediate

**Strategy:**
Use the **Horizontal Pod Autoscaler (HPA)**. It scales the number of replicas based on observed metrics like CPU utilization.

**Code Example:**

```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: my-app-hpa
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

### Q6: How do you ensure a pod runs on a specific node (e.g., with GPU)?

**Difficulty**: Intermediate

**Strategy:**
Use **Node Affinity** for flexible rules or `nodeSelector` for simple equality checks against node labels.

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

### Q7: How do you restrict network traffic between pods?

**Difficulty**: Advanced

**Strategy:**
Use **NetworkPolicies**. By default, all traffic is allowed. Create a policy to deny all ingress/egress and then whitelist specific traffic.

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

### Q8: How do you manage stateful applications (Databases) with stable identities?

**Difficulty**: Advanced

**Strategy:**
Use **StatefulSet**. It provides stable network IDs (web-0, web-1), stable persistent storage, and ordered deployment.

**Code Example:**

```yaml
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: web
spec:
  serviceName: "nginx"
  replicas: 3
  template:
    spec:
      containers:
      - name: nginx
        volumeMounts:
        - name: www
          mountPath: /usr/share/nginx/html
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

### Q9: How do you run a system daemon (like logs/monitoring) on every node?

**Difficulty**: Intermediate

**Strategy:**
Use a **DaemonSet**. It ensures that a copy of the Pod runs on all (or a subset of) nodes.

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

### Q10: How do you debug a crashing Pod?

**Difficulty**: Beginner

**Strategy:**
Check logs (`kubectl logs`), previous logs (`--previous`), and events (`kubectl describe pod`).

**Code Example:**

```yaml
# Check current logs
kubectl logs my-pod

# Check logs of the previous crashed instance
kubectl logs my-pod --previous

# Check events (OOMKilled, Scheduling failures)
kubectl describe pod my-pod
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q11: How do you limit the total resources (CPU/RAM) a namespace can use?

**Difficulty**: Intermediate

**Strategy:**
Use **ResourceQuota** to set hard limits on aggregate resource usage per namespace.

**Code Example:**

```yaml
apiVersion: v1
kind: ResourceQuota
metadata:
  name: quota
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

### Q12: How do you run a one-off task (like a DB migration)?

**Difficulty**: Beginner

**Strategy:**
Use a **Job**. It creates pods that run to completion and then terminate.

**Code Example:**

```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: db-migrate
spec:
  template:
    spec:
      containers:
      - name: migrate
        image: my-app:latest
        command: ["./migrate.sh"]
      restartPolicy: Never
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q13: How do you control user permissions in the cluster?

**Difficulty**: Advanced

**Strategy:**
Use **RBAC (Role-Based Access Control)**. Create `Role` (permissions) and `RoleBinding` (assignment) for namespaced access.

**Code Example:**

```yaml
kind: Role
apiVersion: rbac.authorization.k8s.io/v1
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

### Q14: How do you share temporary storage between containers in the same Pod?

**Difficulty**: Intermediate

**Strategy:**
Use an `emptyDir` volume. It's created with the pod and deleted when the pod is removed.

**Code Example:**

```yaml
spec:
  volumes:
  - name: shared-data
    emptyDir: {}
  containers:
  - name: writer
    image: alpine
    command: ["/bin/sh", "-c", "echo hello > /data/hello"]
    volumeMounts:
    - name: shared-data
      mountPath: /data
  - name: reader
    image: alpine
    command: ["cat", "/data/hello"]
    volumeMounts:
    - name: shared-data
      mountPath: /data
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q15: How do you package Kubernetes applications for easy distribution?

**Difficulty**: Intermediate

**Strategy:**
Use **Helm**. It allows you to define, install, and upgrade complex Kubernetes applications using 'Charts'.

**Code Example:**

```yaml
# Install a chart
helm install my-release bitnami/nginx

# Upgrade a release
helm upgrade my-release bitnami/nginx
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q16: How do you prevent pods from being scheduled on a specific node (Taints)?

**Difficulty**: Intermediate

**Strategy:**
Apply a **Taint** to the node. Only pods with a matching **Toleration** can be scheduled there.

**Code Example:**

```yaml
# Taint node
kubectl taint nodes node1 key=value:NoSchedule

# Pod Toleration
tolerations:
- key: "key"
  operator: "Equal"
  value: "value"
  effect: "NoSchedule"
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q17: How do you detect if a container is alive vs. ready to serve traffic?

**Difficulty**: Intermediate

**Strategy:**
Use **Liveness Probes** (restart if dead) and **Readiness Probes** (remove from endpoints if busy/starting).

**Code Example:**

```yaml
livenessProbe:
  httpGet:
    path: /healthz
    port: 8080
  initialDelaySeconds: 3
readinessProbe:
  httpGet:
    path: /ready
    port: 8080
  initialDelaySeconds: 5
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q18: How do you load balance traffic to a set of Pods?

**Difficulty**: Beginner

**Strategy:**
Use a **Service**. It provides a stable IP and DNS name, and load balances traffic across pods matching the selector.

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

### Q19: How do you use a Sidecar container?

**Difficulty**: Intermediate

**Strategy:**
Run a second container in the same Pod to assist the main container (e.g., log shipping, proxying). They share the same network and volumes.

**Code Example:**

```yaml
spec:
  containers:
  - name: app
    image: my-app
  - name: log-shipper
    image: fluentd
    volumeMounts:
    - name: logs
      mountPath: /var/log/app
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q20: How do you run tasks on a schedule (Cron)?

**Difficulty**: Beginner

**Strategy:**
Use a **CronJob**. It creates Jobs based on a cron schedule string.

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
            args:
            - /bin/sh
            - -c
            - date; echo Hello from the Kubernetes cluster
          restartPolicy: OnFailure
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q21: How do you perform a Canary Deployment?

**Difficulty**: Advanced

**Strategy:**
Create a new Deployment with the new version and a small replica count. Both deployments share the same Service selector. For advanced traffic splitting (percentage-based), use **Istio** or **Argo Rollouts**.

**Code Example:**

```yaml
# Deployment V1 (9 replicas)
labels:
  app: my-app
  version: v1

# Deployment V2 (1 replica)
labels:
  app: my-app
  version: v2

# Service targets 'app: my-app', balancing traffic 90/10 naturally
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q22: How do you secure Pod-to-Pod communication with mTLS?

**Difficulty**: Advanced

**Strategy:**
Use a Service Mesh like **Istio** or **Linkerd**. They automatically inject sidecar proxies that handle mutual TLS encryption between services.

**Code Example:**

```yaml
# Istio PeerAuthentication policy
apiVersion: security.istio.io/v1beta1
kind: PeerAuthentication
metadata:
  name: default
  namespace: foo
spec:
  mtls:
    mode: STRICT
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q23: How do you ensure high availability during voluntary disruptions (e.g., node draining)?

**Difficulty**: Advanced

**Strategy:**
Use a **PodDisruptionBudget (PDB)** to ensure a minimum number of replicas are always available.

**Code Example:**

```yaml
apiVersion: policy/v1
kind: PodDisruptionBudget
metadata:
  name: zk-pdb
spec:
  minAvailable: 2
  selector:
    matchLabels:
      app: zookeeper
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q24: How do you manage persistent storage requests?

**Difficulty**: Intermediate

**Strategy:**
Use **PersistentVolumeClaim (PVC)**. The pod requests storage via PVC, and the cluster binds it to a matching **PersistentVolume (PV)** (often dynamically provisioned via StorageClass).

**Code Example:**

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: my-pvc
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 10Gi
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q25: How do you initialize a Pod before the main container starts?

**Difficulty**: Intermediate

**Strategy:**
Use **Init Containers**. They run to completion before app containers start. Useful for waiting for DBs or setting permissions.

**Code Example:**

```yaml
spec:
  initContainers:
  - name: init-myservice
    image: busybox:1.28
    command: ['sh', '-c', 'until nslookup myservice; do echo waiting for myservice; sleep 2; done;']
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q26: How do you extend Kubernetes capabilities?

**Difficulty**: Advanced

**Strategy:**
Use **Operators** and **Custom Resource Definitions (CRDs)**. Operators use custom controllers to automate complex application logic.

**Code Example:**

```yaml
# Example CRD usage (Prometheus Operator)
apiVersion: monitoring.coreos.com/v1
kind: Prometheus
metadata:
  name: prometheus
spec:
  serviceAccountName: prometheus
  replicas: 2
  version: v2.26.0
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q27: How do you troubleshoot DNS issues in the cluster?

**Difficulty**: Intermediate

**Strategy:**
Run a temporary pod with DNS tools (`busybox` or `dnsutils`) and use `nslookup` or `dig` to query the CoreDNS service.

**Code Example:**

```bash
kubectl run -it --rm --restart=Never busybox --image=busybox:1.28 -- nslookup kubernetes.default
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q28: How do you assign an identity to a Pod for AWS/GCP access?

**Difficulty**: Advanced

**Strategy:**
Use **Service Accounts** mapped to IAM roles (IRSA in AWS, Workload Identity in GKE).

**Code Example:**

```yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: my-sa
  annotations:
    eks.amazonaws.com/role-arn: arn:aws:iam::123456789012:role/my-role
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q29: How do you vertically scale a pod (VPA)?

**Difficulty**: Advanced

**Strategy:**
Use **Vertical Pod Autoscaler (VPA)**. It recommends or automatically updates CPU/Memory requests based on usage.

**Code Example:**

```yaml
apiVersion: autoscaling.k8s.io/v1
kind: VerticalPodAutoscaler
metadata:
  name: my-app-vpa
spec:
  targetRef:
    apiVersion: "apps/v1"
    kind: Deployment
    name: my-app
  updatePolicy:
    updateMode: "Auto"
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q30: How do you define a custom metric for HPA?

**Difficulty**: Advanced

**Strategy:**
Use the **Prometheus Adapter**. It exposes Prometheus metrics to the Kubernetes Custom Metrics API, allowing HPA to scale on application-level metrics (e.g., http_requests).

**Code Example:**

```yaml
# HPA using custom metric
spec:
  metrics:
  - type: Pods
    pods:
      metric:
        name: http_requests_per_second
      target:
        type: AverageValue
        averageValue: 500m
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q31: How do you perform a blue-green deployment?

**Difficulty**: Advanced

**Strategy:**
Maintain two separate environments (Blue and Green). Deploy the new version to Green, run tests, and then switch the Service selector to point to Green.

**Code Example:**

```yaml
# Service pointing to Blue (v1)
selector:
  app: my-app
  version: v1

# Update to point to Green (v2)
kubectl patch service my-service -p '{"spec":{"selector":{"version":"v2"}}}'
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q32: How do you manage multi-tenancy in a cluster?

**Difficulty**: Advanced

**Strategy:**
Use **Namespaces** for isolation, **ResourceQuotas** for fairness, **NetworkPolicies** for traffic isolation, and **RBAC** for access control.

**Code Example:**

```yaml
# Namespace isolation
kubectl create namespace tenant-a
kubectl create rolebinding ... -n tenant-a
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q33: How do you inject a sidecar proxy automatically (e.g., Istio)?

**Difficulty**: Advanced

**Strategy:**
Enable the **MutatingAdmissionWebhook**. Label the namespace (e.g., `istio-injection=enabled`), and the admission controller will inject the sidecar container into new pods.

**Code Example:**

```bash
kubectl label namespace default istio-injection=enabled
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q34: How do you handle container termination gracefully?

**Difficulty**: Intermediate

**Strategy:**
Handle the **SIGTERM** signal in your application to finish in-flight requests. Kubernetes waits for `terminationGracePeriodSeconds` (default 30s) before sending SIGKILL.

**Code Example:**

```javascript
// Node.js example
process.on('SIGTERM', () => {
  server.close(() => {
    console.log('Process terminated');
  });
});
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q35: How do you secure the Kubernetes API server?

**Difficulty**: Advanced

**Strategy:**
Disable anonymous access, use RBAC, enable audit logging, and restrict access to the API server endpoint (e.g., private VPC endpoint).

**Code Example:**

```yaml
# kube-apiserver flags
--anonymous-auth=false
--authorization-mode=Node,RBAC
--audit-log-path=/var/log/audit.log
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q36: How do you use a headless service?

**Difficulty**: Intermediate

**Strategy:**
Set `clusterIP: None`. This returns the IPs of all backing pods directly via DNS, rather than a single VIP. Useful for stateful sets and service discovery.

**Code Example:**

```yaml
apiVersion: v1
kind: Service
metadata:
  name: my-headless
spec:
  clusterIP: None
  selector:
    app: my-app
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q37: How do you implement gitops for Kubernetes?

**Difficulty**: Advanced

**Strategy:**
Use tools like **ArgoCD** or **Flux**. They synchronize the cluster state with a Git repository.

**Code Example:**

```yaml
# ArgoCD Application
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: guestbook
spec:
  source:
    repoURL: https://github.com/argoproj/argocd-example-apps.git
    path: guestbook
    targetRevision: HEAD
  destination:
    server: https://kubernetes.default.svc
    namespace: guestbook
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q38: How do you drain a node for maintenance?

**Difficulty**: Intermediate

**Strategy:**
Use `kubectl drain`. It cordons the node (unschedulable) and evicts all pods to other nodes (respecting PDBs).

**Code Example:**

```bash
kubectl drain node-1 --ignore-daemonsets --delete-emptydir-data
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q39: How do you verify that a Helm chart is valid?

**Difficulty**: Intermediate

**Strategy:**
Use `helm lint` to check for syntax errors and best practices, and `helm template` to render the YAML locally for inspection.

**Code Example:**

```bash
helm lint ./my-chart
helm template ./my-chart --debug
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q40: How do you use ephemeral containers for debugging?

**Difficulty**: Advanced

**Strategy:**
Use `kubectl debug`. It attaches a new container (with tools) to a running pod without restarting it (K8s v1.23+).

**Code Example:**

```bash
kubectl debug -it my-pod --image=busybox --target=my-container
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q41: How do you mount a single file from a ConfigMap without overwriting the directory?

**Difficulty**: Intermediate

**Strategy:**
Use `subPath` in the `volumeMounts` section.

**Code Example:**

```yaml
volumeMounts:
- name: config-vol
  mountPath: /etc/app/config.json
  subPath: config.json
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q42: How do you set a default StorageClass?

**Difficulty**: Intermediate

**Strategy:**
Annotate the StorageClass with `storageclass.kubernetes.io/is-default-class=true`.

**Code Example:**

```bash
kubectl patch storageclass gp2 -p '{"metadata": {"annotations":{"storageclass.kubernetes.io/is-default-class":"true"}}}'
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q43: How do you backup a Kubernetes cluster (etcd)?

**Difficulty**: Advanced

**Strategy:**
Use `etcdctl` to take a snapshot of the etcd database. This saves the entire cluster state.

**Code Example:**

```bash
ETCDCTL_API=3 etcdctl snapshot save snapshot.db   --endpoints=https://127.0.0.1:2379   --cacert=/etc/kubernetes/pki/etcd/ca.crt   --cert=/etc/kubernetes/pki/etcd/server.crt   --key=/etc/kubernetes/pki/etcd/server.key
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q44: How do you force delete a Pod stuck in 'Terminating'?

**Difficulty**: Intermediate

**Strategy:**
Use `--force --grace-period=0`. This removes the API object immediately (use with caution).

**Code Example:**

```bash
kubectl delete pod my-pod --grace-period=0 --force
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q45: How do you monitor Kubernetes components?

**Difficulty**: Intermediate

**Strategy:**
Use **Prometheus** with **Grafana**. Deploy `kube-prometheus-stack` which includes exporters for kubelet, etcd, scheduler, and controller-manager.

**Code Example:**

```bash
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm install monitoring prometheus-community/kube-prometheus-stack
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q46: How do you limit the number of Jobs history kept?

**Difficulty**: Intermediate

**Strategy:**
Set `.spec.successfulJobsHistoryLimit` and `.spec.failedJobsHistoryLimit` in the CronJob definition.

**Code Example:**

```yaml
spec:
  successfulJobsHistoryLimit: 3
  failedJobsHistoryLimit: 1
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q47: How do you run a Windows container in Kubernetes?

**Difficulty**: Advanced

**Strategy:**
You need a cluster with Windows nodes. Use `nodeSelector` or `tolerations` to schedule the pod on a Windows node.

**Code Example:**

```yaml
nodeSelector:
  kubernetes.io/os: windows
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q48: How do you use a priority class to ensure critical pods are scheduled?

**Difficulty**: Advanced

**Strategy:**
Create a **PriorityClass** and assign it to the Pod. Higher priority pods can preempt (evict) lower priority pods if resources are scarce.

**Code Example:**

```yaml
apiVersion: scheduling.k8s.io/v1
kind: PriorityClass
metadata:
  name: high-priority
value: 1000000
---
spec:
  priorityClassName: high-priority
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q49: How do you automatically rotate TLS certificates?

**Difficulty**: Advanced

**Strategy:**
Use **cert-manager**. It automates the issuance and renewal of certificates from issuers like Let's Encrypt or HashiCorp Vault.

**Code Example:**

```yaml
apiVersion: cert-manager.io/v1
kind: Certificate
metadata:
  name: my-cert
spec:
  secretName: my-cert-tls
  issuerRef:
    name: letsencrypt-prod
  dnsNames:
  - example.com
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q50: How do you secure your supply chain with Image Signing (Kyverno/Gatekeeper)?

**Difficulty**: Advanced

**Strategy:**
Use an admission controller (Kyverno or Gatekeeper) to verify Cosign signatures before allowing image deployment.

**Code Example:**

```yaml
# Kyverno Policy
apiVersion: kyverno.io/v1
kind: ClusterPolicy
metadata:
  name: check-image
spec:
  rules:
  - name: verify-signature
    match:
      resources:
        kinds:
        - Pod
    validate:
      message: "Image must be signed."
      imageVerification:
        # ... verification config
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

