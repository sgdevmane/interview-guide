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
Adjusts CPU/RAM requests of pods. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Helper container in same pod (e.g., log shipper). This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Runs before app containers. Good for setup. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Taint: Node repels pods. Toleration: Pod ignores taint.

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
Constrain pods to nodes. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Storage resource in cluster. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Request for storage. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Defines class of storage (SSD, HDD). This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Default strategy. Update pods one by one. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Route small % of traffic to new version. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Two identical envs. Switch traffic instantly. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Package manager for Kubernetes. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
CLI tool for Kubernetes. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Check logs and describe pod. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Key-value store for cluster data. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Agent running on each node. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Network proxy on each node. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Master node components (API Server, Scheduler, Controller Manager, etcd).

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
Role Based Access Control. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Identity for processes in pods. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Firewall rules for pods. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Limit total resources per namespace. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Default limits per pod/container. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Service without ClusterIP. Returns pod IPs directly.

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
Ensure min available pods during maintenance. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Extend K8s API with custom types. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Controller for CRDs. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Request: Min guaranteed. Limit: Max allowed. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Evict all pods for maintenance. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Mark node as unschedulable. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Managed directly by Kubelet, not API server. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Plugin interface for runtimes (containerd, CRI-O).

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
Plugin for networking (Calico, Flannel). This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Plugin for storage. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Grace period 0. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Apply is declarative (upsert). Create is imperative.

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
Access pod port locally. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Cluster + User + Namespace config. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Get all. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Blocks deletion until logic runs. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Deleting orphaned resources. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Container used more RAM than limit. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Cannot pull image (auth, typo). This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Cluster Autoscaler. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Traffic management, security, observability. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
RBAC + Auth Proxy. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Git as source of truth (ArgoCD, Flux). This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
etcdctl snapshot save. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Scheduling priority. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Replace PSP. Enforce security standards. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
subPath in volumeMounts. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Local disk used by logs/emptyDir. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Check CoreDNS pods. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Show metrics (CPU/RAM). This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Aggregates resource usage. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
kubectl cp. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Run command in container. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Expose pod info to container. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Spread pods across zones. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Co-locate pods. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Separate pods. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
EncryptionConfiguration for etcd. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Request cert from K8s CA. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
kubeadm certs renew. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Tool to bootstrap cluster. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Local single-node cluster. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Kubernetes in Docker. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Lightweight K8s. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Kubeconfig contexts. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Coordinate multiple clusters. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
tcpdump, netshoot container. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Distributed lock (e.g., leader election). This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
ttlSecondsAfterFinished. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Run before termination. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Run after start. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
env or envFrom. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Command = Entrypoint, Args = Cmd. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Rollout restart. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Rollout undo. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Documentation in CLI. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Print yaml without applying. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
YAML file defining resources. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
kubeval or kubectl --dry-run. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Policy engine (Gatekeeper). This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
EFK/ELK stack or Loki. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Metrics collection. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

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
Visualization. This concept is fundamental in this domain and understanding it allows developers to write more efficient and maintainable code. It is commonly asked in interviews to test foundational knowledge.

**Code Example**:
```yaml
// Dashboards
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---
