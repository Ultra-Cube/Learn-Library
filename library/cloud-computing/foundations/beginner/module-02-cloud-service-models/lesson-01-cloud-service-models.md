
# Lesson 01: Understanding Cloud Service Models

## Overview

Cloud service models define how cloud services are delivered and consumed. The three primary models are:

* **Infrastructure as a Service (IaaS)**
* **Platform as a Service (PaaS)**
* **Software as a Service (SaaS)**

Each model offers different levels of control, flexibility, and management.

## Learning Objectives

* Distinguish between IaaS, PaaS, and SaaS
* Identify real-world examples of each model
* Understand the responsibilities of users and providers in each model

## Visual: Cloud Service Models

```mermaid
graph TD
    IaaS[Infrastructure as a Service (IaaS)] -->|Provides| VM[Virtual Machines, Storage, Networking]
    PaaS[Platform as a Service (PaaS)] -->|Provides| Platform[App Hosting, Databases, Dev Tools]
    SaaS[Software as a Service (SaaS)] -->|Provides| Apps[End-User Applications]
    IaaS --> User1[User Manages: OS, Apps, Data]
    PaaS --> User2[User Manages: Apps, Data]
    SaaS --> User3[User Manages: Data Only]
```

## Detailed Explanation

### Infrastructure as a Service (IaaS)

IaaS provides fundamental computing resources such as virtual machines, storage, and networking. Users are responsible for managing the operating system, applications, and data. This model offers maximum flexibility and control over the environment.

**Examples:**

* Amazon EC2
* Microsoft Azure Virtual Machines

### Platform as a Service (PaaS)

PaaS delivers a platform that allows customers to develop, run, and manage applications without the complexity of building and maintaining infrastructure. The provider manages the OS, middleware, and runtime.

**Examples:**

* Google App Engine
* Azure App Service

### Software as a Service (SaaS)

SaaS provides ready-to-use software applications over the internet. The provider manages everything except user data. Users simply access the application via a web browser or client.

**Examples:**

* Google Workspace
* Microsoft 365

## References

* [NIST Cloud Computing Definition](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-145.pdf)
* [Microsoft Azure Cloud Service Models](https://learn.microsoft.com/en-us/azure/architecture/cloud-adoption/overview/cloud-service-models)
* [AWS Cloud Service Models](https://aws.amazon.com/types-of-cloud-computing/)
