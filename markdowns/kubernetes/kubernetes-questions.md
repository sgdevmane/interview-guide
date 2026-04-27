<div align="center">
  <a href="https://github.com/mctavish/interview-guide" target="_blank">
    <img src="https://raw.githubusercontent.com/mctavish/interview-guide/main/assets/icons/devops-icon.svg" alt="Interview Guide Logo" width="100" height="100">
  </a>
  <h1>Kubernetes Interview Questions</h1>
  <p><b>Practical, code-focused questions for developers</b></p>
</div>

---

## Table of Contents

1. [What is a Pod?](#q1-what-is-a-pod) <span class="beginner">Beginner</span>
2. [What is a Deployment?](#q2-what-is-a-deployment) <span class="beginner">Beginner</span>
3. [What is a Service?](#q3-what-is-a-service) <span class="beginner">Beginner</span>
4. [ClusterIP vs NodePort vs LoadBalancer?](#q4-clusterip-vs-nodeport-vs-loadbalancer) <span class="intermediate">Intermediate</span>
5. [What is a Namespace?](#q5-what-is-a-namespace) <span class="beginner">Beginner</span>
6. [What is Ingress?](#q6-what-is-ingress) <span class="intermediate">Intermediate</span>
7. [What is a ConfigMap?](#q7-what-is-a-configmap) <span class="beginner">Beginner</span>
8. [What is a Secret?](#q8-what-is-a-secret) <span class="beginner">Beginner</span>
9. [What is a StatefulSet?](#q9-what-is-a-statefulset) <span class="advanced">Advanced</span>
10. [What is a DaemonSet?](#q10-what-is-a-daemonset) <span class="intermediate">Intermediate</span>
11. [What is a Job vs CronJob?](#q11-what-is-a-job-vs-cronjob) <span class="intermediate">Intermediate</span>
12. [What is HPA (Horizontal Pod Autoscaler)?](#q12-what-is-hpa-horizontal-pod-autoscaler) <span class="intermediate">Intermediate</span>
13. [What is VPA (Vertical Pod Autoscaler)?](#q13-what-is-vpa-vertical-pod-autoscaler) <span class="advanced">Advanced</span>
14. [What are Liveness and Readiness Probes?](#q14-what-are-liveness-and-readiness-probes) <span class="intermediate">Intermediate</span>
15. [What is a Sidecar Pattern?](#q15-what-is-a-sidecar-pattern) <span class="intermediate">Intermediate</span>
16. [What is an Init Container?](#q16-what-is-an-init-container) <span class="intermediate">Intermediate</span>
17. [What is a Taint and Toleration?](#q17-what-is-a-taint-and-toleration) <span class="advanced">Advanced</span>
18. [What is Node Affinity?](#q18-what-is-node-affinity) <span class="advanced">Advanced</span>
19. [What is a Persistent Volume (PV)?](#q19-what-is-a-persistent-volume-pv) <span class="intermediate">Intermediate</span>
20. [What is a Persistent Volume Claim (PVC)?](#q20-what-is-a-persistent-volume-claim-pvc) <span class="intermediate">Intermediate</span>
21. [What is StorageClass?](#q21-what-is-storageclass) <span class="intermediate">Intermediate</span>
22. [How do you perform a Rolling Update?](#q22-how-do-you-perform-a-rolling-update) <span class="beginner">Beginner</span>
23. [What is a Canary Deployment?](#q23-what-is-a-canary-deployment) <span class="advanced">Advanced</span>
24. [What is a Blue/Green Deployment?](#q24-what-is-a-blue-green-deployment) <span class="advanced">Advanced</span>
25. [What is Helm?](#q25-what-is-helm) <span class="beginner">Beginner</span>
26. [What is `kubectl`?](#q26-what-is-kubectl) <span class="beginner">Beginner</span>
27. [How do you debug a CrashLoopBackOff?](#q27-how-do-you-debug-a-crashloopbackoff) <span class="beginner">Beginner</span>
28. [What is etcd?](#q28-what-is-etcd) <span class="advanced">Advanced</span>
29. [What is Kubelet?](#q29-what-is-kubelet) <span class="advanced">Advanced</span>
30. [What is Kube-Proxy?](#q30-what-is-kube-proxy) <span class="advanced">Advanced</span>
31. [What is the Control Plane?](#q31-what-is-the-control-plane) <span class="intermediate">Intermediate</span>
32. [What is RBAC?](#q32-what-is-rbac) <span class="intermediate">Intermediate</span>
33. [What is a ServiceAccount?](#q33-what-is-a-serviceaccount) <span class="intermediate">Intermediate</span>
34. [What is a NetworkPolicy?](#q34-what-is-a-networkpolicy) <span class="advanced">Advanced</span>
35. [What is a Resource Quota?](#q35-what-is-a-resource-quota) <span class="intermediate">Intermediate</span>
36. [What is a LimitRange?](#q36-what-is-a-limitrange) <span class="intermediate">Intermediate</span>
37. [What is Headless Service?](#q37-what-is-headless-service) <span class="advanced">Advanced</span>
38. [What is Pod Disruption Budget (PDB)?](#q38-what-is-pod-disruption-budget-pdb) <span class="advanced">Advanced</span>
39. [What is a Custom Resource Definition (CRD)?](#q39-what-is-a-custom-resource-definition-crd) <span class="advanced">Advanced</span>
40. [What is an Operator?](#q40-what-is-an-operator) <span class="advanced">Advanced</span>
41. [What is the difference between Request and Limit?](#q41-what-is-the-difference-between-request-and-limit) <span class="beginner">Beginner</span>
42. [How do you drain a node?](#q42-how-do-you-drain-a-node) <span class="intermediate">Intermediate</span>
43. [What is Cordoning?](#q43-what-is-cordoning) <span class="intermediate">Intermediate</span>
44. [What is a Static Pod?](#q44-what-is-a-static-pod) <span class="advanced">Advanced</span>
45. [What is Container Runtime Interface (CRI)?](#q45-what-is-container-runtime-interface-cri) <span class="advanced">Advanced</span>
46. [What is CNI (Container Network Interface)?](#q46-what-is-cni-container-network-interface) <span class="advanced">Advanced</span>
47. [What is CSI (Container Storage Interface)?](#q47-what-is-csi-container-storage-interface) <span class="advanced">Advanced</span>
48. [How do you force delete a pod?](#q48-how-do-you-force-delete-a-pod) <span class="intermediate">Intermediate</span>
49. [What is `kubectl apply` vs `create`?](#q49-what-is-kubectl-apply-vs-create) <span class="beginner">Beginner</span>
50. [How do you port forward?](#q50-how-do-you-port-forward) <span class="beginner">Beginner</span>
51. [What is a Context?](#q51-what-is-a-context) <span class="beginner">Beginner</span>
52. [How do you list all resources?](#q52-how-do-you-list-all-resources) <span class="intermediate">Intermediate</span>
53. [What is a finalizer?](#q53-what-is-a-finalizer) <span class="advanced">Advanced</span>
54. [What is Garbage Collection in K8s?](#q54-what-is-garbage-collection-in-k8s) <span class="advanced">Advanced</span>
55. [What is OOMKilled?](#q55-what-is-oomkilled) <span class="intermediate">Intermediate</span>
56. [What is ImagePullBackOff?](#q56-what-is-imagepullbackoff) <span class="beginner">Beginner</span>
57. [How do you auto-scale cluster nodes?](#q57-how-do-you-auto-scale-cluster-nodes) <span class="advanced">Advanced</span>
58. [What is Service Mesh (Istio/Linkerd)?](#q58-what-is-service-mesh-istio-linkerd) <span class="advanced">Advanced</span>
59. [How do you secure K8s dashboard?](#q59-how-do-you-secure-k8s-dashboard) <span class="intermediate">Intermediate</span>
60. [What is GitOps?](#q60-what-is-gitops) <span class="intermediate">Intermediate</span>
61. [How do you backup etcd?](#q61-how-do-you-backup-etcd) <span class="advanced">Advanced</span>
62. [What is a PriorityClass?](#q62-what-is-a-priorityclass) <span class="advanced">Advanced</span>
63. [What is Pod Security Admission?](#q63-what-is-pod-security-admission) <span class="advanced">Advanced</span>
64. [How do you mount a single file?](#q64-how-do-you-mount-a-single-file) <span class="intermediate">Intermediate</span>
65. [What is Ephemeral Storage?](#q65-what-is-ephemeral-storage) <span class="intermediate">Intermediate</span>
66. [How do you troubleshoot DNS?](#q66-how-do-you-troubleshoot-dns) <span class="intermediate">Intermediate</span>
67. [What is `kubectl top`?](#q67-what-is-kubectl-top) <span class="beginner">Beginner</span>
68. [What is Metrics Server?](#q68-what-is-metrics-server) <span class="intermediate">Intermediate</span>
69. [How do you copy files to/from pod?](#q69-how-do-you-copy-files-to-from-pod) <span class="beginner">Beginner</span>
70. [What is `kubectl exec`?](#q70-what-is-kubectl-exec) <span class="beginner">Beginner</span>
71. [What is Downward API?](#q71-what-is-downward-api) <span class="advanced">Advanced</span>
72. [What is Topology Spread Constraints?](#q72-what-is-topology-spread-constraints) <span class="advanced">Advanced</span>
73. [What is Pod Affinity?](#q73-what-is-pod-affinity) <span class="advanced">Advanced</span>
74. [What is Pod Anti-Affinity?](#q74-what-is-pod-anti-affinity) <span class="advanced">Advanced</span>
75. [How do you handle secret encryption?](#q75-how-do-you-handle-secret-encryption) <span class="advanced">Advanced</span>
76. [What is a certificate signing request (CSR)?](#q76-what-is-a-certificate-signing-request-csr) <span class="advanced">Advanced</span>
77. [How do you renew certs?](#q77-how-do-you-renew-certs) <span class="advanced">Advanced</span>
78. [What is kubeadm?](#q78-what-is-kubeadm) <span class="intermediate">Intermediate</span>
79. [What is Minikube?](#q79-what-is-minikube) <span class="beginner">Beginner</span>
80. [What is Kind?](#q80-what-is-kind) <span class="beginner">Beginner</span>
81. [What is k3s?](#q81-what-is-k3s) <span class="beginner">Beginner</span>
82. [How do you manage multiple clusters?](#q82-how-do-you-manage-multiple-clusters) <span class="intermediate">Intermediate</span>
83. [What is Federation v2 (KubeFed)?](#q83-what-is-federation-v2-kubefed) <span class="advanced">Advanced</span>
84. [How do you debug networking?](#q84-how-do-you-debug-networking) <span class="advanced">Advanced</span>
85. [What is a Lease?](#q85-what-is-a-lease) <span class="advanced">Advanced</span>
86. [How do you limit jobs history?](#q86-how-do-you-limit-jobs-history) <span class="intermediate">Intermediate</span>
87. [What is PreStop hook?](#q87-what-is-prestop-hook) <span class="intermediate">Intermediate</span>
88. [What is PostStart hook?](#q88-what-is-poststart-hook) <span class="intermediate">Intermediate</span>
89. [How do you set environment variables?](#q89-how-do-you-set-environment-variables) <span class="beginner">Beginner</span>
90. [What is `command` vs `args`?](#q90-what-is-command-vs-args) <span class="intermediate">Intermediate</span>
91. [How do you restart a deployment?](#q91-how-do-you-restart-a-deployment) <span class="beginner">Beginner</span>
92. [How do you undo a deployment?](#q92-how-do-you-undo-a-deployment) <span class="beginner">Beginner</span>
93. [What is `kubectl explain`?](#q93-what-is-kubectl-explain) <span class="beginner">Beginner</span>
94. [How do you dry-run?](#q94-how-do-you-dry-run) <span class="beginner">Beginner</span>
95. [What is a Manifest?](#q95-what-is-a-manifest) <span class="beginner">Beginner</span>
96. [How do you validate yaml?](#q96-how-do-you-validate-yaml) <span class="intermediate">Intermediate</span>
97. [What is OPA (Open Policy Agent)?](#q97-what-is-opa-open-policy-agent) <span class="advanced">Advanced</span>
98. [How do you monitor logs?](#q98-how-do-you-monitor-logs) <span class="beginner">Beginner</span>
99. [What is Prometheus?](#q99-what-is-prometheus) <span class="intermediate">Intermediate</span>
100. [What is Grafana?](#q100-what-is-grafana) <span class="intermediate">Intermediate</span>

---

<a id="q1"></a>
### Q1: What is a Pod?

**Difficulty**: Beginner

**Strategy**:
A Pod is the smallest execution unit in Kubernetes. It represents a single instance of a running process in your cluster. Pods contain one or more containers, such as Docker containers. When a Pod runs multiple containers, the containers are managed as a single entity and share the Pod's resources, such as networking and storage.

**Code Example**:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: myapp
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q2"></a>
### Q2: What is a Deployment?

**Difficulty**: Beginner

**Strategy**:
A Deployment provides declarative updates for Pods and ReplicaSets. You describe a desired state in a Deployment, and the Deployment Controller changes the actual state to the desired state at a controlled rate. It allows for rolling updates, rollbacks, and scaling.

**Code Example**:
```yaml
kind: Deployment
spec:
  replicas: 3
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q3"></a>
### Q3: What is a Service?

**Difficulty**: Beginner

**Strategy**:
A Service is an abstraction which defines a logical set of Pods and a policy by which to access them (sometimes called a micro-service). The set of Pods targeted by a Service is usually determined by a selector. This enables loose coupling between dependent Pods.

**Code Example**:
```yaml
kind: Service
spec:
  type: ClusterIP
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q4"></a>
### Q4: ClusterIP vs NodePort vs LoadBalancer?

**Difficulty**: Intermediate

**Strategy**:
These are Service types:
- **ClusterIP**: Exposes the Service on a cluster-internal IP. Choosing this value makes the Service only reachable from within the cluster. This is the default.
- **NodePort**: Exposes the Service on each Node's IP at a static port (the NodePort). A ClusterIP Service, to which the NodePort Service routes, is automatically created.
- **LoadBalancer**: Exposes the Service externally using a cloud provider's load balancer. NodePort and ClusterIP Services, to which the external load balancer routes, are automatically created.

**Code Example**:
```yaml
type: NodePort
ports:
  - nodePort: 30007
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q5"></a>
### Q5: What is a Namespace?

**Difficulty**: Beginner

**Strategy**:
Namespaces provide a mechanism for isolating groups of resources within a single cluster. Names of resources need to be unique within a namespace, but not across namespaces. Namespace-based scoping is applicable only for namespaced objects (e.g. Deployments, Services, etc) and not for cluster-wide objects (e.g. StorageClass, Nodes, PersistentVolumes).

**Code Example**:
```yaml
metadata:
  namespace: dev
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q6"></a>
### Q6: What is Ingress?

**Difficulty**: Intermediate

**Strategy**:
Ingress exposes HTTP and HTTPS routes from outside the cluster to services within the cluster. Traffic routing is controlled by rules defined on the Ingress resource. An Ingress can be configured to give Services externally-reachable URLs, load balance traffic, terminate SSL / TLS, and offer name-based virtual hosting.

**Code Example**:
```yaml
kind: Ingress
spec:
  rules:
  - host: my.app
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q7"></a>
### Q7: What is a ConfigMap?

**Difficulty**: Beginner

**Strategy**:
A ConfigMap is an API object used to store non-confidential data in key-value pairs. Pods can consume ConfigMaps as environment variables, command-line arguments, or as configuration files in a volume. This allows you to decouple environment-specific configuration from your container images.

**Code Example**:
```yaml
kind: ConfigMap
data:
  db_host: localhost
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q8"></a>
### Q8: What is a Secret?

**Difficulty**: Beginner

**Strategy**:
Kubernetes Secrets let you store and manage sensitive information, such as passwords, OAuth tokens, and ssh keys. Storing confidential information in a Secret is safer and more flexible than putting it verbatim in a Pod definition or in a container image.

**Code Example**:
```yaml
kind: Secret
type: Opaque
data:
  pass: YWRtaW4=
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q9"></a>
### Q9: What is a StatefulSet?

**Difficulty**: Advanced

**Strategy**:
StatefulSet is the workload API object used to manage stateful applications. Manages the deployment and scaling of a set of Pods, and provides guarantees about the ordering and uniqueness of these Pods. Unlike a Deployment, a StatefulSet maintains a sticky identity for each of their Pods.

**Code Example**:
```yaml
kind: StatefulSet
serviceName: mysql
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q10"></a>
### Q10: What is a DaemonSet?

**Difficulty**: Intermediate

**Strategy**:
A DaemonSet ensures that all (or some) Nodes run a copy of a Pod. As nodes are added to the cluster, Pods are added to them. As nodes are removed from the cluster, those Pods are garbage collected. Deleting a DaemonSet will clean up the Pods it created.

**Code Example**:
```yaml
kind: DaemonSet
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q11"></a>
### Q11: What is a Job vs CronJob?

**Difficulty**: Intermediate

**Strategy**:
**Job**: Creates one or more Pods and ensures that a specified number of them successfully terminate. As pods successfully complete, the Job tracks the successful completions. 
**CronJob**: Creates Jobs on a repeating schedule. One CronJob object is like one line of a crontab (cron table) file.

**Code Example**:
```yaml
kind: CronJob
schedule: "*/1 * * * *"
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q12"></a>
### Q12: What is HPA (Horizontal Pod Autoscaler)?

**Difficulty**: Intermediate

**Strategy**:
The Horizontal Pod Autoscaler automatically scales the number of Pods in a replication controller, deployment, replica set or stateful set based on observed CPU utilization (or, with custom metrics support, on some other application-provided metrics).

**Code Example**:
```yaml
kind: HorizontalPodAutoscaler
minReplicas: 1
maxReplicas: 10
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q13"></a>
### Q13: What is VPA (Vertical Pod Autoscaler)?

**Difficulty**: Advanced

**Strategy**:
VPA automatically adjusts CPU and memory requests for individual Pods based on historical usage patterns. Unlike HPA which adds or removes Pods, VPA right-sizes existing containers to avoid resource waste or starvation. Be cautious not to use VPA and HPA together on the same metric (e.g., CPU), as they can conflict and cause unstable scaling behavior.

**Code Example**:
```yaml
kind: VerticalPodAutoscaler
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q14"></a>
### Q14: What are Liveness and Readiness Probes?

**Difficulty**: Intermediate

**Strategy**:
- **Liveness Probe**: Indicates whether the container is running. If the liveness probe fails, the kubelet kills the container, and the container is subjected to its restart policy.
- **Readiness Probe**: Indicates whether the container is ready to service requests. If the readiness probe fails, the endpoints controller removes the Pod's IP address from the endpoints of all Services that match the Pod.

**Code Example**:
```yaml
livenessProbe:
  httpGet:
    path: /health
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q15"></a>
### Q15: What is a Sidecar Pattern?

**Difficulty**: Intermediate

**Strategy**:
The sidecar pattern extends a main application container by co-locating a helper container within the same Pod, sharing the same network namespace and storage volumes. Common use cases include log forwarding (Fluentd), proxying (Envoy in service meshes), and secrets injection. This pattern is frequently tested because it demonstrates understanding of Pod composition and the single-responsibility principle in container design.

**Code Example**:
```yaml
containers:
- name: main
- name: sidecar
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q16"></a>
### Q16: What is an Init Container?

**Difficulty**: Intermediate

**Strategy**:
Init Containers run to completion before the main application containers start, making them ideal for setup tasks like downloading configs, waiting for dependencies, or initializing databases. They run sequentially and must all succeed before the app container launches. A common pitfall is making init containers too complex or slow, which delays Pod startup and can block deployments.

**Code Example**:
```yaml
initContainers:
- name: setup
  command: ['sh', '-c', '...']
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q17"></a>
### Q17: What is a Taint and Toleration?

**Difficulty**: Advanced

**Strategy**:
Taints are applied to nodes to repel Pods that do not tolerate them, while tolerations are added to Pods to allow scheduling onto tainted nodes. This mechanism is essential for dedicating nodes to specific workloads (e.g., GPU nodes, control-plane nodes) and is commonly used in production clusters. A key distinction to remember in interviews: tolerations allow a Pod to be scheduled on a tainted node but do not guarantee it -- use node affinity for that guarantee.

**Code Example**:
```yaml
tolerations:
- key: "gpu"
  operator: "Exists"
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q18"></a>
### Q18: What is Node Affinity?

**Difficulty**: Advanced

**Strategy**:
Node Affinity lets you constrain which nodes a Pod can be scheduled on based on node labels, offering more expressive rules than simple nodeSelector. It supports `required` (hard constraint) and `preferred` (soft constraint) modes, giving fine-grained control over placement. This is critical for workloads with hardware requirements (e.g., SSD storage, specific CPU architectures) or compliance-driven placement policies.

**Code Example**:
```yaml
affinity:
  nodeAffinity: ...
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q19"></a>
### Q19: What is a Persistent Volume (PV)?

**Difficulty**: Intermediate

**Strategy**:
A Persistent Volume is a cluster-wide storage resource provisioned by an administrator or dynamically via StorageClasses, abstracting storage backend details (NFS, cloud disks, etc.) from Pod lifecycle. PVs exist independently of Pods, surviving Pod deletions and rescheduling. Understanding PV reclaim policies (Retain, Delete, Recycle) is critical for interviews since choosing the wrong policy can lead to data loss or orphaned storage costs.

**Code Example**:
```yaml
kind: PersistentVolume
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q20"></a>
### Q20: What is a Persistent Volume Claim (PVC)?

**Difficulty**: Intermediate

**Strategy**:
A PVC is a user's request for storage, similar to how a Pod consumes compute resources. The control plane binds the PVC to a matching PV based on size, access mode, and storage class. This abstraction decouples storage consumption from provisioning -- developers request capacity without needing to know the underlying infrastructure. A common interview trap is confusing access modes: ReadWriteOnce means one node, not one Pod.

**Code Example**:
```yaml
kind: PersistentVolumeClaim
resources:
  requests:
    storage: 1Gi
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q21"></a>
### Q21: What is StorageClass?

**Difficulty**: Intermediate

**Strategy**:
StorageClass defines categories of storage (e.g., fast SSD, standard HDD) and enables dynamic provisioning -- when a PVC is created, Kubernetes automatically provisions a PV using the StorageClass provider. This eliminates the need for admins to pre-provision storage manually. Be prepared to discuss how the `default` StorageClass annotation works and what happens when a PVC does not specify a storageClassName.

**Code Example**:
```yaml
kind: StorageClass
provisioner: aws-ebs
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q22"></a>
### Q22: How do you perform a Rolling Update?

**Difficulty**: Beginner

**Strategy**:
Rolling updates are the default deployment strategy, gradually replacing old Pods with new ones to ensure zero downtime. You control the pace with `maxSurge` (how many extra Pods can be created) and `maxUnavailable` (how many Pods can be down during the update). This is a fundamental interview topic because misconfigured values can cause service outages -- for example, setting maxUnavailable to 100% effectively becomes a recreate strategy.

**Code Example**:
```yaml
strategy:
  type: RollingUpdate
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q23"></a>
### Q23: What is a Canary Deployment?

**Difficulty**: Advanced

**Strategy**:
A canary deployment gradually routes a small percentage of traffic to the new version before a full rollout, allowing you to validate changes with real users at low risk. In Kubernetes, this is typically implemented using Ingress weight-based routing or service mesh traffic splitting. The key interview insight is that native Kubernetes lacks built-in canary support -- you need Ingress controllers (NGINX, Istio, Argo Rollouts) for percentage-based traffic shifting.

**Code Example**:
```yaml
// Use Istio or Ingress annotations
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q24"></a>
### Q24: What is a Blue/Green Deployment?

**Difficulty**: Advanced

**Strategy**:
Blue/Green deployments maintain two identical environments (blue = current, green = new) and switch all traffic at once by updating a Service's selector labels. This gives instant rollback capability -- just switch the selector back. The trade-off is that it requires double the resources during the switchover. In interviews, emphasize how this differs from canary: Blue/Green is an all-or-nothing cutover, not a gradual traffic shift.

**Code Example**:
```yaml
// Switch Service selector
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q25"></a>
### Q25: What is Helm?

**Difficulty**: Beginner

**Strategy**:
Helm is the package manager for Kubernetes, templating and managing application deployments as reusable "charts." It handles versioning, dependencies, and configuration through values files, making it easy to deploy complex applications (databases, monitoring stacks) with a single command. In interviews, be ready to discuss the difference between `helm install` (new release) and `helm upgrade` (modify existing), and how `helm rollback` leverages stored release history.

**Code Example**:
```yaml
helm install my-app ./chart
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q26"></a>
### Q26: What is `kubectl`?

**Difficulty**: Beginner

**Strategy**:
`kubectl` is the primary CLI tool for communicating with the Kubernetes API server, letting you create, read, update, and delete cluster resources. It supports both imperative commands (`kubectl run`) and declarative management (`kubectl apply -f`). Interviewers often test whether you know useful flags like `-o wide`, `-o yaml`, `-w` (watch), and `--sort-by`, as well as how to use `kubectl api-resources` to discover available resource types.

**Code Example**:
```yaml
kubectl get pods
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q27"></a>
### Q27: How do you debug a CrashLoopBackOff?

**Difficulty**: Beginner

**Strategy**:
CrashLoopBackOff means a container keeps crashing and restarting in a loop, which is one of the most common production issues. Start with `kubectl logs <pod> --previous` to see logs from the crashed container, then `kubectl describe pod` to check events and exit codes. Common causes include missing ConfigMaps/Secrets, failed health checks, incorrect command/args, or the application crashing on startup due to missing dependencies.

**Code Example**:
```yaml
kubectl logs pod-name
kubectl describe pod pod-name
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q28"></a>
### Q28: What is etcd?

**Difficulty**: Advanced

**Strategy**:
etcd is a distributed key-value store that serves as the single source of truth for all Kubernetes cluster state -- every Pod, Service, ConfigMap, and Secret is stored here. It uses the Raft consensus algorithm for consistency across the control plane. In interviews, emphasize that losing etcd without a backup means losing the entire cluster, which is why regular etcd backups and running an odd number of etcd nodes (3 or 5) for quorum are critical production practices.

**Code Example**:
```yaml
// Backing store for K8s
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q29"></a>
### Q29: What is Kubelet?

**Difficulty**: Advanced

**Strategy**:
The Kubelet is the agent that runs on every worker node, responsible for ensuring that Pods and their containers are running as declared in the PodSpec. It talks to the API server to get Pod assignments, pulls container images, and reports node and Pod status back. A key interview point is that the Kubelet is the only core component that runs on worker nodes -- understanding its role is essential for debugging node-level issues like image pull failures or volume mount errors.

**Code Example**:
```yaml
// Manages pods on node
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q30"></a>
### Q30: What is Kube-Proxy?

**Difficulty**: Advanced

**Strategy**:
Kube-Proxy runs on every node and maintains network rules that enable Service abstraction -- it routes traffic from a Service's ClusterIP to the correct backend Pod. It can operate in iptables mode (default, rule-based) or IPVS mode (for better performance at scale). Interviewers may ask why a Service is unreachable -- checking kube-proxy logs and iptables rules is a key debugging step when Service connectivity fails.

**Code Example**:
```yaml
// Handles service routing
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q31"></a>
### Q31: What is the Control Plane?

**Difficulty**: Intermediate

**Strategy**:
The control plane is the brain of the cluster, consisting of four components: the API Server (entry point for all REST commands), etcd (persistent store), the Scheduler (assigns Pods to nodes), and the Controller Manager (runs reconciliation loops for Deployments, ReplicaSets, etc.). In interviews, understanding how these components interact -- especially that all state changes go through the API Server -- demonstrates a solid grasp of Kubernetes architecture and helps with troubleshooting control plane failures.

**Code Example**:
```yaml
// Brain of the cluster
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q32"></a>
### Q32: What is RBAC?

**Difficulty**: Intermediate

**Strategy**:
Role-Based Access Control (RBAC) regulates access to Kubernetes API resources based on the roles assigned to users or ServiceAccounts. Roles define permissions within a namespace, while ClusterRoles define cluster-wide permissions -- both are bound to subjects via RoleBindings or ClusterRoleBindings. This is a high-priority interview topic because overly permissive RBAC is a common security misconfiguration; always follow the principle of least privilege.

**Code Example**:
```yaml
kind: Role
rules:
- resources: ["pods"]
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q33"></a>
### Q33: What is a ServiceAccount?

**Difficulty**: Intermediate

**Strategy**:
A ServiceAccount provides an identity for Pods to authenticate with the Kubernetes API server, controlling what actions the Pod can perform via RBAC policies. Every namespace has a default ServiceAccount, but production workloads should use dedicated ServiceAccounts with minimal permissions. A common interview pitfall is confusing ServiceAccounts (for in-cluster processes) with user accounts (for human access) -- they are separate authentication mechanisms.

**Code Example**:
```yaml
serviceAccountName: my-sa
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q34"></a>
### Q34: What is a NetworkPolicy?

**Difficulty**: Advanced

**Strategy**:
NetworkPolicy controls traffic flow at the Pod level, acting as a firewall that specifies which Pods can communicate with each other and with external endpoints. By default, all Pods can talk to all Pods -- NetworkPolicy restricts this using label selectors, namespace selectors, and IP blocks. A key caveat: NetworkPolicy is enforced by the CNI plugin, so not all network providers support it (e.g., Flannel does not natively support network policies).

**Code Example**:
```yaml
kind: NetworkPolicy
spec:
  podSelector: ...
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q35"></a>
### Q35: What is a Resource Quota?

**Difficulty**: Intermediate

**Strategy**:
ResourceQuota limits aggregate resource consumption per namespace, capping the total CPU, memory, storage, and object counts (Pods, Services, etc.) that can be used. This prevents any single team or application from monopolizing cluster resources. In multi-tenant environments, ResourceQuotas are essential -- but remember they only work when Pods have resource requests defined, since quotas are enforced against requests, not actual usage.

**Code Example**:
```yaml
kind: ResourceQuota
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q36"></a>
### Q36: What is a LimitRange?

**Difficulty**: Intermediate

**Strategy**:
LimitRange sets default, minimum, and maximum resource constraints for individual Pods or containers within a namespace. It complements ResourceQuota by providing guardrails at the container level -- for example, ensuring no container can request more than 4 CPUs. A practical interview insight: LimitRange auto-assigns default requests/limits to Pods that do not specify them, which silently affects scheduling and quota consumption.

**Code Example**:
```yaml
kind: LimitRange
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q37"></a>
### Q37: What is Headless Service?

**Difficulty**: Advanced

**Strategy**:
A Headless Service sets `clusterIP: None`, which means no load-balanced proxy is created -- DNS queries return the individual Pod IPs directly instead of a single virtual IP. This is essential for StatefulSets (e.g., databases like MySQL or Cassandra) where each replica needs a stable, discoverable network identity. In interviews, connecting Headless Services to StatefulSet DNS patterns (`pod-name.service-name.namespace.svc.cluster.local`) demonstrates deep understanding.

**Code Example**:
```yaml
clusterIP: None
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q38"></a>
### Q38: What is Pod Disruption Budget (PDB)?

**Difficulty**: Advanced

**Strategy**:
A PDB defines the minimum number of Pods that must remain available during voluntary disruptions like node drains or cluster upgrades, preventing too many replicas from being taken down simultaneously. It specifies either `minAvailable` or `maxUnavailable` but only applies to eviction-based disruptions, not Pod crashes or node failures. This is critical for production readiness -- without a PDB, a rolling node upgrade could take down all replicas of a critical service.

**Code Example**:
```yaml
kind: PodDisruptionBudget
minAvailable: 1
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q39"></a>
### Q39: What is a Custom Resource Definition (CRD)?

**Difficulty**: Advanced

**Strategy**:
A CRD extends the Kubernetes API with custom resource types beyond built-in objects like Pods and Services. Once a CRD is registered, you can create and manage custom resources using `kubectl` just like native objects. CRDs are the foundation of the Kubernetes ecosystem -- tools like Cert-Manager, Prometheus Operator, and ArgoCD all rely on them. Be prepared to explain that CRDs alone only define data schema; you need a custom controller to act on the data.

**Code Example**:
```yaml
kind: CustomResourceDefinition
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q40"></a>
### Q40: What is an Operator?

**Difficulty**: Advanced

**Strategy**:
An Operator combines a CRD (custom resource definition) with a custom controller that encodes human operational knowledge -- automating tasks like backups, scaling, failover, and upgrades for complex applications. Think of it as a Kubernetes-native way to package domain expertise (e.g., how to safely upgrade a PostgreSQL cluster). Operators are a popular interview topic because they demonstrate understanding of both the Kubernetes extension model and real-world operational challenges.

**Code Example**:
```yaml
// Automates complex apps
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q41"></a>
### Q41: What is the difference between Request and Limit?

**Difficulty**: Beginner

**Strategy**:
Requests define the minimum guaranteed resources a container gets (used for scheduling decisions), while Limits define the maximum it can consume. A container using more CPU than its limit gets throttled, and exceeding memory limits triggers an OOMKill. Setting Requests equal to Limits provides predictable performance but reduces bin-packing efficiency, while a large gap between them allows overcommit but risks resource contention under pressure.

**Code Example**:
```yaml
resources:
  requests: { cpu: 100m }
  limits: { cpu: 200m }
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q42"></a>
### Q42: How do you drain a node?

**Difficulty**: Intermediate

**Strategy**:
`kubectl drain` gracefully evicts all Pods from a node in preparation for maintenance, respecting PodDisruptionBudgets and DaemonSet exclusions. It cordons the node first (preventing new scheduling), then evicts Pods one by one. A common pitfall is draining without the `--ignore-daemonsets` flag when DaemonSets are present, which causes the command to fail. Always verify that evicted Pods reschedule successfully on other nodes before proceeding with node maintenance.

**Code Example**:
```yaml
kubectl drain node-1
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q43"></a>
### Q43: What is Cordoning?

**Difficulty**: Intermediate

**Strategy**:
Cordoning marks a node as unschedulable, preventing the Kubernetes scheduler from placing new Pods on it while leaving existing Pods untouched. This is useful during node investigation or pre-maintenance without immediately disrupting running workloads. Remember that cordoning is reversible with `kubectl uncordon`, and it does not affect DaemonSets or static Pods since they bypass the scheduler entirely.

**Code Example**:
```yaml
kubectl cordon node-1
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q44"></a>
### Q44: What is a Static Pod?

**Difficulty**: Advanced

**Strategy**:
Static Pods are managed directly by the Kubelet using manifest files from a directory on the node (typically `/etc/kubernetes/manifests`), bypassing the API server entirely. The Kubelet watches this directory and creates a mirror Pod object in the API server for visibility, but the Kubelet is the true controller. This mechanism is how Kubernetes bootstraps its own control plane components -- the API server, scheduler, and controller manager are deployed as static Pods.

**Code Example**:
```yaml
// /etc/kubernetes/manifests
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q45"></a>
### Q45: What is Container Runtime Interface (CRI)?

**Difficulty**: Advanced

**Strategy**:
The Container Runtime Interface (CRI) is a plugin interface that lets Kubernetes use different container runtimes (containerd, CRI-O, formerly Docker) without modifying the Kubelet. It standardizes the API for image management, container lifecycle, and exec operations. A common interview point is that Docker was deprecated in Kubernetes 1.20 and removed in 1.24 -- the `dockershim` was replaced by direct CRI-compatible runtimes like containerd.

**Code Example**:
```yaml
// Docker shim
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q46"></a>
### Q46: What is CNI (Container Network Interface)?

**Difficulty**: Advanced

**Strategy**:
CNI is the plugin specification that handles Pod networking -- assigning IP addresses, setting up routes, and enabling Pod-to-Pod communication across nodes. Popular CNI plugins include Calico, Cilium, Flannel, and Weave, each with different capabilities around network policy support and performance. Understanding CNI is important for troubleshooting Pod connectivity issues, since a misconfigured CNI plugin is a common cause of cross-node communication failures.

**Code Example**:
```yaml
// Pod networking
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q47"></a>
### Q47: What is CSI (Container Storage Interface)?

**Difficulty**: Advanced

**Strategy**:
CSI is a standardized interface that allows Kubernetes to use any storage vendor's driver (AWS EBS, GCE PD, NFS, Ceph, etc.) without modifying core Kubernetes code. It replaced the old in-tree volume plugins, enabling storage vendors to maintain their own drivers independently. In interviews, note that CSI drivers enable advanced features like volume snapshots, cloning, and resize -- capabilities that were difficult or impossible with the legacy plugin model.

**Code Example**:
```yaml
// EBS, NFS drivers
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q48"></a>
### Q48: How do you force delete a pod?

**Difficulty**: Intermediate

**Strategy**:
Force deletion bypasses the graceful shutdown process and immediately removes a Pod from etcd and the API server, useful when a Pod is stuck in `Terminating` state due to a dead node or unresponsive Kubelet. Use `--grace-period=0 --force` together, as setting only one flag does not work. This is a last resort -- always try normal deletion first, because force deleting a StatefulSet Pod can cause split-brain issues if the old process is still running.

**Code Example**:
```yaml
kubectl delete pod x --grace-period=0 --force
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q49"></a>
### Q49: What is `kubectl apply` vs `create`?

**Difficulty**: Beginner

**Strategy**:
`kubectl apply` is declarative -- it computes a diff against the live state and applies changes, making it safe for repeated use in CI/CD pipelines. `kubectl create` is imperative -- it creates a resource from scratch and fails if the resource already exists. The key difference is that `apply` stores a `kubectl.kubernetes.io/last-applied-configuration` annotation for three-way merge diffs, enabling smarter conflict resolution during updates.

**Code Example**:
```yaml
kubectl apply -f file.yaml
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q50"></a>
### Q50: How do you port forward?

**Difficulty**: Beginner

**Strategy**:
`kubectl port-forward` creates a secure tunnel from your local machine to a Pod, Service, or Deployment, enabling quick debugging without exposing resources externally. It proxies a local port to a remote port through the API server, making it invaluable for accessing databases, admin UIs, or REST APIs during development. Be aware that port-forwarding sessions are temporary and break on network interruption -- they are not suitable for production access.

**Code Example**:
```yaml
kubectl port-forward pod-x 8080:80
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q51"></a>
### Q51: What is a Context?

**Difficulty**: Beginner

**Strategy**:
A context in `kubectl` defines a tuple of cluster (API server URL), user (authentication credentials), and namespace, stored in the kubeconfig file. Switching contexts with `kubectl config use-context` lets you operate across multiple clusters or environments without re-entering credentials. A best practice is to name contexts clearly (e.g., `dev-cluster`, `prod-us-east`) and always verify the current context before running destructive commands.

**Code Example**:
```yaml
kubectl config use-context prod
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q52"></a>
### Q52: How do you list all resources?

**Difficulty**: Intermediate

**Strategy**:
`kubectl get all` only shows a subset of common resources (Pods, Services, Deployments, ReplicaSets), not truly "all" resources. To see everything, use `kubectl get all --all-namespaces` combined with `kubectl api-resources` to discover the full list of resource types. For a comprehensive audit, tools like `kubectl get cm,secret,ing,pvc --all-namespaces` are more reliable than relying on the shorthand `all` alias.

**Code Example**:
```yaml
kubectl get all --all-namespaces
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q53"></a>
### Q53: What is a finalizer?

**Difficulty**: Advanced

**Strategy**:
Finalizers are metadata keys that prevent Kubernetes from deleting a resource until cleanup actions (releasing external connections, removing cloud resources) are completed. When you delete a resource with finalizers, it enters a `Terminating` state and waits for the controller to remove the finalizer entries. A common debugging scenario is a resource stuck in `Terminating` because the controller that should clear the finalizer is no longer running -- manual finalizer removal may be needed.

**Code Example**:
```yaml
finalizers:
- kubernetes.io/pvc-protection
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q54"></a>
### Q54: What is Garbage Collection in K8s?

**Difficulty**: Advanced

**Strategy**:
Kubernetes garbage collection automatically cleans up dependent resources when a parent object is deleted, using `ownerReferences` metadata to track parent-child relationships. For example, deleting a Deployment automatically removes its ReplicaSets and Pods. You can control this behavior with propagation policies: `foreground` (children deleted first), `background` (parent deleted first, children cleaned up async), or `orphan` (children kept). Understanding this is essential to avoid orphaned resources that waste cluster capacity.

**Code Example**:
```yaml
// OwnerReferences
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q55"></a>
### Q55: What is OOMKilled?

**Difficulty**: Intermediate

**Strategy**:
OOMKilled (exit code 137) occurs when the Linux kernel terminates a container because it exceeded its memory limit -- this is the kernel's Out-Of-OMemory killer in action, not a Kubernetes restart. To resolve it, either increase the memory limit, optimize the application's memory usage, or investigate memory leaks. A critical distinction: OOMKilled means the limit was hit, not the request -- the node itself may still have plenty of memory available.

**Code Example**:
```yaml
// Exit Code 137
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q56"></a>
### Q56: What is ImagePullBackOff?

**Difficulty**: Beginner

**Strategy**:
ImagePullBackOff means the Kubelet could not pull the container image, and it will retry with exponential backoff. Common causes include wrong image names, missing tags, authentication failures with private registries, or network connectivity issues. Start debugging with `kubectl describe pod` to see the exact pull error, and verify that imagePullSecrets are configured if using a private container registry.

**Code Example**:
```yaml
// Check image name
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q57"></a>
### Q57: How do you auto-scale cluster nodes?

**Difficulty**: Advanced

**Strategy**:
The Cluster Autoscaler automatically adds nodes when Pods are pending due to insufficient resources and removes nodes when they are underutilized for a configurable period. It integrates with cloud provider APIs (AWS ASG, GCP MIG) to adjust the node pool size. Key interview considerations include scale-down delays (to avoid flapping), Pod Disruption Budgets preventing node removal, and that it does not scale based on CPU/memory utilization -- only on Pod scheduling pressure.

**Code Example**:
```yaml
// Adds/removes nodes
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q58"></a>
### Q58: What is Service Mesh (Istio/Linkerd)?

**Difficulty**: Advanced

**Strategy**:
A service mesh injects sidecar proxies (Envoy) alongside every Pod to handle inter-service communication, providing observability, traffic management, and security (mTLS) without changing application code. Istio and Linkerd are the two leading implementations, with Istio offering more features and Linkerd prioritizing simplicity and performance. A common pitfall is adopting a service mesh prematurely -- start with Kubernetes-native primitives (Services, NetworkPolicies) and add a mesh only when you need advanced features like canary traffic splitting or mutual TLS between services.

**Code Example**:
```yaml
// Sidecar proxies
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q59"></a>
### Q59: How do you secure K8s dashboard?

**Difficulty**: Intermediate

**Strategy**:
The Kubernetes dashboard is a frequent attack vector if exposed publicly, so it must be secured with RBAC (least-privilege ServiceAccount), network restrictions, and authentication -- never use the `--enable-skip-login` flag in production. Access it via `kubectl proxy` or an Ingress with OIDC authentication rather than exposing it as a NodePort or LoadBalancer. A best practice is to restrict dashboard access using a dedicated ServiceAccount with a RoleBinding scoped to only the namespaces the user needs, rather than granting cluster-admin privileges.

**Code Example**:
```yaml
// Never expose publicly
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q60"></a>
### Q60: What is GitOps?

**Difficulty**: Intermediate

**Strategy**:
GitOps uses Git as the single source of truth for declarative infrastructure and application definitions, with automated processes (like ArgoCD or Flux) continuously reconciling the cluster state with the Git repository. Every change goes through a Git commit and review process, providing an audit trail, easy rollback via `git revert`, and eliminating configuration drift. The key trade-off is that GitOps introduces a slight delay between committing and deploying, which can be a challenge for rapid hotfix workflows where direct `kubectl apply` may still be needed.

**Code Example**:
```yaml
// Sync git to cluster
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q61"></a>
### Q61: How do you backup etcd?

**Difficulty**: Advanced

**Strategy**:
Since etcd holds the entire cluster state, regular backups are your disaster recovery safety net -- losing etcd without a backup means rebuilding the entire cluster from scratch. Use `etcdctl snapshot save` with the correct endpoints, certificates, and keys to create a consistent snapshot, and store backups off-cluster (e.g., S3). A common pitfall is backing up only one etcd member in a HA setup -- while any member can serve a snapshot, always verify backup integrity with `etcdctl snapshot status` and test restoration periodically.

**Code Example**:
```yaml
etcdctl snapshot save backup.db
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q62"></a>
### Q62: What is a PriorityClass?

**Difficulty**: Advanced

**Strategy**:
PriorityClass maps a name to an integer priority value, controlling which Pods get scheduled first and which get evicted when the cluster is under resource pressure. Higher-value Pods preempt (evict) lower-value Pods, making this essential for ensuring critical workloads (databases, monitoring) stay running during resource contention. A best practice is to define a few well-named tiers (e.g., `system-critical`, `high`, `low`) rather than many granular classes, and always set `preemptionPolicy: PreemptLowerPriority` explicitly for clarity.

**Code Example**:
```yaml
kind: PriorityClass
value: 1000000
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q63"></a>
### Q63: What is Pod Security Admission?

**Difficulty**: Advanced

**Strategy**:
Pod Security Admission (PSA) replaced the deprecated PodSecurityPolicies, enforcing security standards at the namespace level using three privilege profiles: `privileged` (unrestricted), `baseline` (minimally restrictive), and `restricted` (heavily restricted). It operates in three modes -- `enforce` (block violations), `audit` (log violations), and `warn` (warn on violations) -- giving teams a gradual adoption path. A common pitfall is setting the `restricted` profile in enforce mode without testing, which can break existing workloads that use capabilities like `NET_BIND_SERVICE` or run as root.

**Code Example**:
```yaml
labels:
  pod-security.kubernetes.io/enforce: restricted
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q64"></a>
### Q64: How do you mount a single file?

**Difficulty**: Intermediate

**Strategy**:
Mounting a single file from a ConfigMap or Secret uses the `subPath` field in the volumeMount definition, which mounts only that specific key without overwriting the entire directory. Without `subPath`, mounting a ConfigMap volume replaces the whole target directory contents, which can unintentionally hide existing files in the container. A common pitfall is that `subPath` mounts do not receive live updates when the ConfigMap changes -- you must restart the Pod to pick up changes to that file.

**Code Example**:
```yaml
volumeMounts:
- name: config
  subPath: file.txt
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q65"></a>
### Q65: What is Ephemeral Storage?

**Difficulty**: Intermediate

**Strategy**:
Ephemeral storage tracks the local, non-persistent disk usage of a Pod -- including container writable layers, logs, and emptyDir volumes -- allowing you to set requests and limits just like CPU and memory. When a container exceeds its ephemeral-storage limit, the Pod gets evicted, making this crucial for preventing node disk exhaustion from runaway log files or large temporary data. A best practice is to set ephemeral-storage limits on log-heavy workloads and use `emptyDir.sizeLimit` to cap temporary volumes, since node disk full conditions can destabilize the entire node.

**Code Example**:
```yaml
requests:
  ephemeral-storage: "2Gi"
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q66"></a>
### Q66: How do you troubleshoot DNS?

**Difficulty**: Intermediate

**Strategy**:
Kubernetes DNS (CoreDNS) resolves Service names to ClusterIPs, and DNS failures are a common cause of inter-service communication breakdowns. Start by running `nslookup` or `dig` from a debug Pod to test resolution, check CoreDNS Pod health with `kubectl get pods -n kube-system`, and review CoreDNS logs for errors. A frequent issue is misconfigured `resolv.conf` settings (especially `ndots:5` causing excessive DNS queries) or NetworkPolicies blocking DNS traffic on port 53 -- always ensure the `kube-dns` service is allowed in any default-deny NetworkPolicy setup.

**Code Example**:
```yaml
nslookup myservice
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q67"></a>
### Q67: What is `kubectl top`?

**Difficulty**: Beginner

**Strategy**:
`kubectl top` displays real-time CPU and memory usage for Pods and nodes, making it the quickest way to identify resource bottlenecks without installing third-party monitoring tools. It requires the Metrics Server to be running in the cluster, which scrapes resource usage from Kubelet's cAdvisor endpoint. A common pitfall is getting a "Metrics API not available" error -- this means the Metrics Server is not installed or not reachable, not that the cluster is broken.

**Code Example**:
```yaml
kubectl top pods
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q68"></a>
### Q68: What is Metrics Server?

**Difficulty**: Intermediate

**Strategy**:
Metrics Server is a lightweight, cluster-wide aggregator of resource usage data that collects CPU and memory metrics from each Kubelet and exposes them via the Metrics API. It is a prerequisite for `kubectl top` commands and the Horizontal Pod Autoscaler (HPA) to function -- without it, HPA cannot make scaling decisions. Be aware that Metrics Server is designed for autoscaling, not for long-term historical monitoring -- for that, you need a full monitoring stack like Prometheus plus Grafana.

**Code Example**:
```yaml
// Required for HPA
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q69"></a>
### Q69: How do you copy files to/from pod?

**Difficulty**: Beginner

**Strategy**:
`kubectl cp` transfers files between your local machine and a running Pod, which is essential for debugging (extracting logs, config files) or injecting temporary data without rebuilding the image. It uses tar under the hood, so the container must have `tar` installed in its filesystem for the command to work. A common pitfall is trying to copy from a crashed or pending Pod -- the Pod must be in a Running state, and for multi-container Pods you must specify the container with the `-c` flag.

**Code Example**:
```yaml
kubectl cp ./file pod:/path
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q70"></a>
### Q70: What is `kubectl exec`?

**Difficulty**: Beginner

**Strategy**:
`kubectl exec` opens an interactive shell session inside a running container, allowing you to inspect the filesystem, run diagnostic commands, and troubleshoot issues in real time. Use the `-it` flags for an interactive TTY session, and specify `--` before the command to separate kubectl flags from the container command. A best practice is to avoid relying on `exec` in production for routine tasks -- if you frequently need to exec into containers, consider adding health endpoints, better logging, or a debug sidecar instead.

**Code Example**:
```yaml
kubectl exec -it pod -- bash
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q71"></a>
### Q71: What is Downward API?

**Difficulty**: Advanced

**Strategy**:
The Downward API exposes Pod and container metadata (name, namespace, labels, annotations, resource limits) as environment variables or mounted files, letting containers discover their own runtime context without querying the API server. This is useful for applications that need to know their Pod name for identity (e.g., StatefulSet members) or want to log their resource constraints. A key distinction: the Downward API does not call the Kubernetes API -- it injects values at Pod creation time, so changing a label after creation does not update an already-mounted file.

**Code Example**:
```yaml
valueFrom:
  fieldRef:
    fieldPath: metadata.name
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q72"></a>
### Q72: What is Topology Spread Constraints?

**Difficulty**: Advanced

**Strategy**:
Topology Spread Constraints distribute Pods evenly across failure domains (zones, nodes, regions) by controlling the maximum skew -- the difference in Pod count between any two topology domains. Unlike Pod Anti-Affinity (which only prevents co-location), topology spreading actively balances placement, making it the preferred mechanism for high availability. A common pitfall is using `whenUnsatisfiable: DoNotSchedule` with a tight `maxSkew` on small clusters, which can leave Pods pending -- use `ScheduleAnyway` for softer balancing that still prefers even distribution.

**Code Example**:
```yaml
topologySpreadConstraints:
- maxSkew: 1
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q73"></a>
### Q73: What is Pod Affinity?

**Difficulty**: Advanced

**Strategy**:
Pod Affinity lets you schedule Pods onto nodes where other Pods with matching labels are already running, enabling co-location of interdependent services (e.g., placing a cache Pod on the same node as the application that uses it). It supports `required` (hard constraint, Pod stays pending if no match) and `preferred` (soft constraint, best-effort) modes, with topology keys defining the failure domain scope. Be cautious with required affinity rules in small clusters, as they can create scheduling deadlocks where Pods wait for each other indefinitely.

**Code Example**:
```yaml
podAffinity:
  requiredDuringScheduling...
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q74"></a>
### Q74: What is Pod Anti-Affinity?

**Difficulty**: Advanced

**Strategy**:
Pod Anti-Affinity prevents Pods from being scheduled on the same node (or topology domain) as Pods with specific labels, which is critical for spreading replicas across failure domains for high availability. It uses the same `required`/`preferred` modes as affinity, with topology keys like `kubernetes.io/hostname` for node-level or `topology.kubernetes.io/zone` for zone-level spreading. A best practice is to use `preferred` anti-affinity for most workloads rather than `required`, since strict rules can block scheduling when cluster capacity is limited.

**Code Example**:
```yaml
podAntiAffinity:
  requiredDuringScheduling...
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q75"></a>
### Q75: How do you handle secret encryption?

**Difficulty**: Advanced

**Strategy**:
By default, Kubernetes Secrets are stored in etcd as base64-encoded (not encrypted) data, so enabling EncryptionConfiguration at the API server level is essential for protecting sensitive data at rest. Configure an encryption provider (AES-CBC, AES-GCM, or a KMS plugin like AWS KMS, Azure Key Vault) in the API server's `--encryption-provider-config` flag to encrypt secret data before writing to etcd. A common pitfall is enabling encryption but forgetting to re-encrypt existing Secrets -- new Secrets are encrypted, but old ones remain in plaintext until you rewrite them.

**Code Example**:
```yaml
// Encrypt secrets at rest
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q76"></a>
### Q76: What is a certificate signing request (CSR)?

**Difficulty**: Advanced

**Strategy**:
A CertificateSigningRequest (CSR) is a Kubernetes API object that allows nodes, users, or applications to request X.509 certificates signed by the cluster's certificate authority. This is how new worker nodes authenticate to the cluster during TLS bootstrapping and how service mesh sidecars obtain mTLS certificates. The CSR must be explicitly approved (via `kubectl certificate approve` or an auto-approving controller) before the CA signs it -- a key security control that prevents unauthorized identities from obtaining cluster certificates.

**Code Example**:
```yaml
kind: CertificateSigningRequest
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q77"></a>
### Q77: How do you renew certs?

**Difficulty**: Advanced

**Strategy**:
Kubernetes cluster certificates (API server, etcd, kubelet, etc.) expire after one year by default, and expired certs will completely lock you out of the cluster. Use `kubeadm certs check-expiration` to monitor remaining validity and `kubeadm certs renew all` to renew them before expiration. A critical best practice is to automate cert renewal (via a cron job or the `cert-manager` operator) and always restart control plane components after renewal, since the old certificates remain in memory until the processes are restarted.

**Code Example**:
```yaml
kubeadm certs renew all
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q78"></a>
### Q78: What is kubeadm?

**Difficulty**: Intermediate

**Strategy**:
kubeadm is the official tool for bootstrapping Kubernetes clusters, handling the complex setup of control plane components, TLS certificates, etcd, and kubeconfig files with simple commands like `kubeadm init` and `kubeadm join`. It follows Kubernetes best practices by default but intentionally does not provision networking, storage, or add-ons -- you must install a CNI plugin separately after initialization. Interviewers often ask about kubeadm to verify you understand the difference between bootstrapping a cluster (kubeadm) and managing workloads on an already-running cluster.

**Code Example**:
```yaml
kubeadm init
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q79"></a>
### Q79: What is Minikube?

**Difficulty**: Beginner

**Strategy**:
Minikube runs a single-node Kubernetes cluster locally on your machine using a VM or Docker container, providing a full Kubernetes environment for learning, development, and testing manifests before deploying to production. It supports features like add-ons (dashboard, ingress, metrics-server), multi-cluster management, and driver selection (Docker, VirtualBox, HyperKit). A key point for interviews: Minikube is for local development only -- it cannot replicate multi-node networking, node affinity, or real cluster autoscaling behavior.

**Code Example**:
```yaml
minikube start
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q80"></a>
### Q80: What is Kind?

**Difficulty**: Beginner

**Strategy**:
Kind (Kubernetes IN Docker) runs Kubernetes clusters inside Docker containers, making it faster and lighter than VM-based solutions like Minikube. It excels in CI/CD pipelines and automated testing because clusters can be created and torn down in seconds, and it supports multi-node topologies (multiple control plane and worker nodes). A practical distinction for interviews: unlike Minikube which focuses on developer experience with add-ons, Kind focuses on speed and testability -- it is the tool of choice for testing Kubernetes controllers and operators.

**Code Example**:
```yaml
kind create cluster
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q81"></a>
### Q81: What is k3s?

**Difficulty**: Beginner

**Strategy**:
k3s is a lightweight, CNCF-certified Kubernetes distribution by Rancher that packages the entire control plane into a single binary under 100MB, making it ideal for edge computing, IoT, and resource-constrained environments. It replaces etcd with SQLite by default (with MySQL/Postgres options for HA) and uses Traefik as the default ingress controller. An important interview distinction: k3s is production-ready and fully conformant, unlike Minikube or Kind which are development tools -- many organizations run k3s in production for lightweight workloads.

**Code Example**:
```yaml
curl ... | sh -
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q82"></a>
### Q82: How do you manage multiple clusters?

**Difficulty**: Intermediate

**Strategy**:
Multi-cluster management uses kubeconfig files that contain multiple contexts, where each context maps a cluster (API server URL + CA cert), user (credentials), and namespace into a single switchable profile. You can merge kubeconfig files with the `KUBECONFIG` environment variable or `kubectl config` commands to manage dev, staging, and production clusters from one machine. A critical best practice is to always verify the current context with `kubectl config current-context` before running any command, especially destructive operations like deletions or scale-downs.

**Code Example**:
```yaml
KUBECONFIG=c1:c2 kubectl get pods
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q83"></a>
### Q83: What is Federation v2 (KubeFed)?

**Difficulty**: Advanced

**Strategy**:
KubeFed (Kubernetes Federation v2) enables managing multiple Kubernetes clusters as a single entity, syncing resources like Deployments and Services across clusters for geographic redundancy and disaster recovery. It uses a host cluster to propagate FederatedResource templates to member clusters, with override policies for cluster-specific configurations. Be aware that KubeFed has been archived and is no longer actively maintained -- in interviews, mention modern alternatives like Karmada or cluster-management approaches using GitOps (ArgoCD with multiple clusters) instead.

**Code Example**:
```yaml
// Sync resources
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q84"></a>
### Q84: How do you debug networking?

**Difficulty**: Advanced

**Strategy**:
Networking issues in Kubernetes span multiple layers (Pod-to-Pod, Pod-to-Service, external-to-internal), so debugging requires a systematic approach starting from DNS resolution, then Service connectivity, then CNI plugin health. Deploy a debug Pod with networking tools (e.g., `nicolaka/netshoot`) to test DNS lookups, `curl` Service endpoints, and trace packet flow with `tcpdump`. A key diagnostic pattern: if DNS works but Service IP is unreachable, check kube-proxy and iptables; if cross-node Pod communication fails, investigate the CNI plugin and node network routes.

**Code Example**:
```yaml
kubectl run debug --image=nicolaka/netshoot
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q85"></a>
### Q85: What is a Lease?

**Difficulty**: Advanced

**Strategy**:
A Lease is a lightweight API object used for distributed coordination and heartbeat mechanisms, allowing controllers to signal they are alive without updating heavier resource objects. The kubelet uses Leases for node heartbeats (instead of updating NodeStatus every few seconds), and the leader-election mechanism uses them to ensure only one controller replica is active at a time. Understanding Leases is important for debugging leader election failures -- if the holder identity in the Lease is stale, a previous leader crashed without releasing it and the new leader must wait for the lease to expire.

**Code Example**:
```yaml
kind: Lease
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q86"></a>
### Q86: How do you limit jobs history?

**Difficulty**: Intermediate

**Strategy**:
Completed Jobs and CronJobs accumulate in the cluster over time, consuming etcd storage and cluttering `kubectl get jobs` output if not cleaned up automatically. Use `ttlSecondsAfterFinished` on Jobs to have Kubernetes garbage-collect them after completion, and configure `successfulJobsHistoryLimit` / `failedJobsHistoryLimit` on CronJobs to cap retained records. A common pitfall is not setting these limits on CronJobs that run every minute -- without cleanup, thousands of completed Job objects can slow down the API server and exhaust etcd space.

**Code Example**:
```yaml
ttlSecondsAfterFinished: 100
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q87"></a>
### Q87: What is PreStop hook?

**Difficulty**: Intermediate

**Strategy**:
The PreStop hook is a lifecycle handler that runs synchronously immediately before a container is terminated, giving it time to gracefully shut down (finish in-flight requests, close database connections). It runs before the SIGTERM signal and the grace period countdown, so its execution time counts against the `terminationGracePeriodSeconds`. A best practice is to combine a PreStop hook with an application SIGTERM handler, and avoid long-running operations in the hook -- if the combined shutdown exceeds the grace period, the container receives SIGKILL.

**Code Example**:
```yaml
lifecycle:
  preStop:
    exec: ...
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q88"></a>
### Q88: What is PostStart hook?

**Difficulty**: Intermediate

**Strategy**:
The PostStart hook runs immediately after a container is created, executing a command or HTTP call before the application starts serving traffic. Unlike init containers, PostStart runs concurrently with the container's main process, which means the hook can fail if the application is not yet ready to handle the request. A common pitfall is relying on PostStart for critical setup that must complete before the app starts -- use init containers for sequential pre-startup tasks instead, since PostStart provides no ordering guarantee relative to the main process.

**Code Example**:
```yaml
lifecycle:
  postStart: ...
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q89"></a>
### Q89: How do you set environment variables?

**Difficulty**: Beginner

**Strategy**:
Kubernetes supports multiple methods for injecting environment variables into containers: static `value` fields, `valueFrom` (referencing ConfigMaps, Secrets, or Downward API fields), and `envFrom` (injecting all keys from a ConfigMap or Secret at once). This is the primary mechanism for decoupling configuration from container images, enabling the same image to run in dev, staging, and production with different settings. A common pitfall is using `envFrom` with large ConfigMaps that inject unnecessary variables -- prefer explicit `env` entries referencing specific keys for clarity and security.

**Code Example**:
```yaml
env:
- name: DB_HOST
  value: localhost
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q90"></a>
### Q90: What is `command` vs `args`?

**Difficulty**: Intermediate

**Strategy**:
In Kubernetes, `command` overrides the container's Docker ENTRYPOINT and `args` overrides the CMD, following the same convention as the OCI container specification. If you specify only `args`, the original ENTRYPOINT from the image runs with your custom arguments; if you specify only `command`, it runs with no arguments. A frequent source of confusion is that omitting both fields uses the image's default ENTRYPOINT and CMD -- but specifying either field completely overrides the corresponding image field, which can silently break containers that depend on their default startup behavior.

**Code Example**:
```yaml
command: ["/bin/sh"]
args: ["-c", "echo hi"]
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q91"></a>
### Q91: How do you restart a deployment?

**Difficulty**: Beginner

**Strategy**:
`kubectl rollout restart` triggers a rolling restart of all Pods in a Deployment by updating the pod template annotation with a timestamp, causing the Deployment controller to recreate Pods one by one. This is the recommended way to restart without downtime -- it respects the Deployment's rolling update strategy (maxSurge, maxUnavailable). A common mistake is using `kubectl scale deployment --replicas=0` followed by scaling back up, which causes full downtime -- always prefer `rollout restart` for zero-downtime restarts.

**Code Example**:
```yaml
kubectl rollout restart deploy/app
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q92"></a>
### Q92: How do you undo a deployment?

**Difficulty**: Beginner

**Strategy**:
`kubectl rollout undo` rolls a Deployment back to its previous revision by default, or to a specific revision with `--to-revision=N`, leveraging the Deployment's revision history stored in ReplicaSets. This is your fastest recovery mechanism when a bad deploy causes errors -- it restores the previous pod template spec without needing to re-run CI/CD. A critical point: the revision history is limited by `revisionHistoryLimit` (default 10) -- older ReplicaSets are cleaned up, so if you need to roll back further than the retained history, you must apply the original manifest manually.

**Code Example**:
```yaml
kubectl rollout undo deploy/app
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q93"></a>
### Q93: What is `kubectl explain`?

**Difficulty**: Beginner

**Strategy**:
`kubectl explain` is a built-in reference tool that shows the API schema for any Kubernetes resource field directly from the terminal, eliminating the need to search documentation online. You can drill into nested fields with dot notation (e.g., `kubectl explain pod.spec.containers.resources`) to discover available fields, types, and descriptions. This is especially useful during interviews or exams when you cannot look things up online -- mastering `kubectl explain` lets you self-document the API without leaving the CLI.

**Code Example**:
```yaml
kubectl explain pod.spec
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q94"></a>
### Q94: How do you dry-run?

**Difficulty**: Beginner

**Strategy**:
Dry-run mode (`--dry-run=client` or `--dry-run=server`) lets you validate or generate Kubernetes manifests without actually creating resources, making it invaluable for testing and scaffolding. Client-side dry-run validates locally and is great for generating YAML templates (combine with `-o yaml`), while server-side dry-run sends the request to the API server for full validation including admission webhooks. A practical pattern is using `--dry-run=client -o yaml` to scaffold a manifest quickly, then edit it before applying -- faster than writing YAML from scratch.

**Code Example**:
```yaml
kubectl create deploy x --dry-run=client -o yaml
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q95"></a>
### Q95: What is a Manifest?

**Difficulty**: Beginner

**Strategy**:
A manifest is a YAML (or JSON) file that declaratively describes the desired state of a Kubernetes resource -- specifying the API version, kind, metadata, and spec that tell Kubernetes what to create and configure. Manifests are the foundation of GitOps and infrastructure-as-code practices because they can be version-controlled, reviewed, and applied repeatedly with `kubectl apply`. A best practice is to keep manifests in version control rather than using imperative commands, so your cluster state is always reproducible and auditable.

**Code Example**:
```yaml
// pod.yaml
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q96"></a>
### Q96: How do you validate yaml?

**Difficulty**: Intermediate

**Strategy**:
Validating Kubernetes YAML before applying catches errors early -- use `kubectl apply --dry-run=client` for basic schema validation or specialized tools like `kubeval`, `kubeconform`, or `kubectl-neat` for deeper checks. Server-side dry-run (`--dry-run=server`) goes further by running admission webhooks and RBAC checks, providing the most realistic validation without creating resources. Integrating validation into CI/CD pipelines prevents invalid manifests from reaching production -- a best practice is to validate on every pull request alongside linting tools like `yamllint`.

**Code Example**:
```yaml
kubeval pod.yaml
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q97"></a>
### Q97: What is OPA (Open Policy Agent)?

**Difficulty**: Advanced

**Strategy**:
OPA (Open Policy Agent) is a general-purpose policy engine that, when integrated with Kubernetes via Gatekeeper, enforces organizational policies on resource creation (e.g., "all Pods must have resource limits", "no containers can run as root"). It uses the Rego language to write expressive policies that go beyond what RBAC or Pod Security Admission can enforce. A common interview topic is the difference between OPA/Gatekeeper (validating/mutating admission webhooks) and native Kubernetes controls -- Gatekeeper can enforce cross-resource constraints like "no two Ingresses can share the same host".

**Code Example**:
```yaml
// Enforce rules
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q98"></a>
### Q98: How do you monitor logs?

**Difficulty**: Beginner

**Strategy**:
Kubernetes logs are written to stdout/stderr on each node and are ephemeral (lost when a Pod is deleted or a node crashes), so a centralized logging stack is essential for production. The standard approach uses Fluentd or Fluent Bit to collect container logs, sends them to Elasticsearch or Loki for storage, and uses Kibana or Grafana for visualization (the EFK/PLG stack). A best practice is to never rely on `kubectl logs` for production monitoring -- it only shows a single container's output with no aggregation, search, or alerting capabilities.

**Code Example**:
```yaml
// Fluentd collects logs
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q99"></a>
### Q99: What is Prometheus?

**Difficulty**: Intermediate

**Strategy**:
Prometheus is the de facto standard monitoring system for Kubernetes, scraping time-series metrics from instrumented applications and kubelet cAdvisor endpoints via HTTP pull at configurable intervals. It uses PromQL for powerful queries and supports alerting rules that trigger notifications via Alertmanager. A key architectural point for interviews: Prometheus uses a pull model (it scrapes targets), not push -- this means Services must expose a `/metrics` endpoint, and Prometheus uses service discovery to automatically find scrape targets in Kubernetes.

**Code Example**:
```yaml
// Scrapes /metrics
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q100"></a>
### Q100: What is Grafana?

**Difficulty**: Intermediate

**Strategy**:
Grafana is a visualization and dashboarding platform that connects to data sources like Prometheus, Loki, and Elasticsearch to create rich, interactive dashboards for Kubernetes cluster and application monitoring. It supports templating variables (e.g., switching between namespaces or clusters), alerting rules, and shared dashboards that teams can import from Grafana's public library. In interviews, emphasize that Grafana is the presentation layer -- it does not collect or store metrics itself, so it must be paired with a time-series database like Prometheus to be useful.

**Code Example**:
```yaml
// Dashboards
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---
