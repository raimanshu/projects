'''
https://www.youtube.com/watch?v=N4sJj-SxX00
'''

# What is Virtualization?
'''
- virtualization is the process of creating multiple simulates environments or virtual machines from a single hardware system, enabling more efficient resource use.

- Hypervisor -  software that creates and runs virtual machines eg - oracle virtual box 

- types of hypervisor - type 1 (Bare Metal) and  type 2 (Hosted)
Bare Metal - directly setup in hardware like aws ec2, VMware Vsphere, Xen
Hosted - software in installed on an OS and gives separate space for other OS like vmware  and oracle virtual box
'''

# What is Cloud Computing?
'''
- on demand deleivery of IT resourcesover the internet with pay as you go pricing

- 3 types of cloud computing
- IaaS - Infrastructure as a service - eg - AWS EC2, AWS S3
- PaaS - Platform as a service - eg - AWS Elastic Beanstalk
- SaaS - Software as a service - eg - AWS S3

- 3 types of clod deployments
- Public 
- Private 
- Hybrid 

- types of clud services
compute services
storage services
database services
networking services
container services
serverless services
machine learning services
identity and access management services (IAM)
monitoring and logging services
content delivery network services
backup and disaster recovery services
security and compliance services
virtual private cloud services
data analytics services
api management




'''

# What is AWS? 
'''
regions
zones - available and local zones

'''

# AWS Account Setup
'''
email
identity proof
credit/debit card
'''

# AWS IAM Service
'''
- used to manage users, roles and permissions
- used to manage access to AWS services and resources
- root user - admin user
- it is a global service
- root account created by default, should't bse used or shared
- create users, assign permissions, create groups, create roles, define policies, manage federated access, 
- MFA - multifactor authentication - username + password + security code

- ways of access AWS
- aws management console - web based
- CLI - command line interface
- SDK/API - software development kit / application programming interface
'''

# AWS CLI Configuration
'''
install aws cli

aws configure

aws best practices
- avoid using root account except of account setup
- add user to a group and assign permission to group
- use password policy or MFA
- use ACCESS KEYS for CLI/SDK
- never share ACCESS KEYS or password
- audit the permission using IAM credential report
'''

# AWS EC2 Service
'''
- Elastic Compute Cloud  provides resizable virtual servers called instances which we can use to run applications 

- instance type - select the hardware capacity (eg CPU, memory)
- AMI (Amazon Machine Image) - choose the operating system and software (linux, mac, windows) 
- storage - configure the type and size of storages (eg EBS volume)
- security groups - setup firewall rules to control inbound/outbound traffic
- key pair - create and use an exixting key pair SSH access
- network settings - configure VPC, subnet and assign public or private IP address
- IAM Role - attach an IAM role for permission to access other AWS resources
- user data - add scripts to be executed when the instance starts
- elastic IP - optionally associate a static IP for consistent public access

security groups 
- network firewall rules that control inbound and outbound traffic for instances
region specific
- only allow rule (but no deny rule)
- all inbound traffic blocked and outbound allowed by default
- you define rules for specific - protocols (like HTTP, HTTPS, SSh, etc), port numbers (eg port 80 for HTTP, port 22 for SSH), IP addresses (eg allow traffic from specific IP or IPs range)
- if you allow incomming traffic on a specific port (eg port 80 for HTTP), the outgoing response traffic is automatically allowed without an explicit outbound rule
- security groups are stateful, so you don't need to explicitly allow response

- SSH allow you to control/access a remote machine

- EC2 instance types
- General Purpose - balance between compute, memory, and networking
- Compute Optimized - high performance computing (HPC) workloads
- Memory Optimized - memory-intensive workloads
- Accelerated Computing - GPU-based workloads
- Storage Optimized

- EC2 Instance Purchasing Options
- On-Demand Instances - pay for what you use
- Reserved Instances - long term, reserved capacity
- Spot Instances - short term, for unused capacity
- Dedicated Hosts - physical EC2 server dedicated for your use
- Dedicated Instances - single tenant hardware

'''
# AWS EBS Service
'''
- Elastic Block Store - block level storage volumes for EC2 instances like virtual hard drives
- EBS volumes are network attached and can be attached to multiple EC2 instances

- region and Availabilty zone  specific
- build in redundancy - EBS volumes are automatically replicated within the same availability zone to prevent data loss due to hardware failures
- different volumes types like gp2/3, io1/2.st1,sc1
- allow encryption and snapshot for backup
- scalable - no data loss will occur during resizing, no need to restart the EC2 instance during the process

- we can allow or not allow EBS deletion option with deletion of EC2 instance
- we can modify EBS size and type

EBS snapshort are incremental backups of EBS volumes
what if we want to copy our data to 
- new availability zone 
- new region
'''

# AWS AMI
'''
- Amazon Machine Image - pre-configured template that provides the necessary information to launch an EC2 instance in AWS
- It includes - operating system (eg linux, windows, etc), application server (apache, nginx, etc), pre-installed software and configurations
- with an AMI, you can launch new EC2 instances with a consistent, predefined configurations
- you can also create custom AMIs to include specific software or settings, allowing for quick replication of environments

types of AMIs
- public AMIs - available to all AWS users. useful for basic use cases like popular operating systems eg Windows, Linux, etc
- private AMIs - created by a user account and only available within that account or shared with specific  accounts
- Paid AMIs / Marketplace AMIs - AMIs that are available for purchase from third parties through AWS Marketplace, offering softwares like databases, web servers or pre-defined environments.

use case of paid AMIs
- rapid deployment - the LAMP stack is pre-configured, eleminating the need to manually install and configure Apache, mysql and php
- scalability and load balancing - running on AWS enables quick scaling to match website traffic, while elastic load balancers helps in distributing requests
- cost efficiency - you only pay for the infrastructure and the software according to usuage

run cleanup script

create launch template ??
- create a reusuable blueprint for launching instances
- contains configurations settings (eg AMI, instance type, security groups, etc)
- used repeatedly to launch new instances in a consistent way
- auto scaling, spot instances, standardizing instance settings
- can have multiple versions for different configurations

create image ??
- create a custom AMI snapshot of an EC2 instance
- captures OS, applications, configurations, and data
- used to create new instances that replicate the captured image
- backup, replication, migrating instances to another region
- typically, an AMI is a point-in-time capture of an instance

summary
- yes, all installed applications, configuration settings, environment variables, network configurations, DNS settings, users and firewall settings in the AMI
- an AMI is essentially a complete snapshot of the instance at the point in time you created the image, allowing you to replicate the exact state of that server, including all software, configuration and operating system level changes
- when you create an EC2 instance from this AMI, it will boot up as if it were an exact clone of the original with all installed software and settings intact

'''

# EC2 Image Builder
'''
- automate CM or image creation - creating, testing and deployment of AMIs
- can be configured to run at regular intervals (eg dail, weekly or monthly)
- free

'''

# AWS ELB
'''
AWS Elastic Load Balancing (ELB) is a service that distributes incoming application traffic across multiple EC2 instances in a load balancer

- scalability means the ability to grow your system's resource when your application or website gets more traffic or more users
- types of scaling - vertical scaling (scale up or down) and horizontal scaling (scale out or in)
- vertical scaling means adding more power (CPU, RAM) to your existing server like t2.micro to m5.large
- borizontal scaling means adding more instances (servers) to distribute the load. you can add more EC2 instances behind a load balancers

- high availability (HA) means keeing your service up and running with minimal downtime, so it's always accessible to users. Running resources in multiple avaiability zoness

- elasticity menas ability to automatically adjust resources as the demand changes - adding more when needed and removing when it's no longer necessary eg ASG

types of load balancers
- application load balancers (ALB) - designed for HTTP and HTTPS traffic, routing based on URL or host header eg web applications (layer 7)
- network load balancers (NLB) - designed for high-performance and low latency for TCP/UDP traffic, routing based on IP protocol and port eg gaming, financial apps etc.(layer 4
- gateway load balancers (GWLB) - helps deploy, scale and manage third party virtual appliances such as firewalls and monitoring solutions

summary
- distributes traffic -  splits incomming traffic accross multiple servers so no single server gets overloaded.
- improves availability -  if one server goes down, the load balancer automatically sends traffic to the working servers, ensuring your application stays available
- scales resources -  it helps manage high demend by adding more servers during peak times and distributing load
- single point of access need to be expose
- high availability accross available zones
'''

# AWS ASG
'''
- AWS Auto Scaling Groups (ASG) is a service that automatically adjusts the number of EC2 instances in a group based on predefined scaling policies and rules

functions
- automatic scaling - scale the number of EC2instances up or down based on demand
- maintain instance health - replace unhealty instances auto matically to ensure reliability
- use scaling policies -  set rules for scaling based on metrices like CPU usuage or request count
- ensure availability -  always keep a defined number of instances running to meet applications needs
- scheduling scaling - pre-configure scaling activities for specific times eg traffic peaks
- distribute instances - deploy instances accross multiple availability zones for high availability
- integrate with ELB - attch instances to an elastic load balancers to auto matically balance traffic
- optimize costs - scale down during low demand to save on infrastructure costs

'''

# AWS S3 Service
'''
AWS Simple Storage Service (S3) is a cloud based storage service that allows you to store, manage, and retrieve large amounts of data like files, images, videos and backups securely and at scale
- it provides highly reliable, scalable object dtorage making your data accessible from anywhere anytime via internet
- store data as objects
- globally unique name
- region specific service
- each object within a bucket is stored as a key-value pair where key is the object's name (which can contain slashes/, mimicking directory structure) and value is the content of the object (the file/data itself)
- maximum object size - 5TB (Terabytes) is the maximum size for a single object in amazon S3
- multipart upload is recommended for objects larger than 5 GB (split the file into smaller parts and upload them separately)

- host static website

s3 bucket policies
- JSON based access control policies that you attch directly to an S3 bucket to manage permissions for accessing the bucket and it's objects
- they allow you to define who can access the data and what actions can perform such as read, write or delete enabling fine-grained control over the security of your data stored in S3
- write or paste JSON policy in the bucket policy editor
- you can use AWS's Policy Generator to create a custom policy, or you can manually write the policy in JSON format
GetObject - used to retrieve or download files from an S# bucket
PUTObject - used to upload or add files into an S3 bucket

s3 versioning
- it allows you to keep multiple versions of an object in the same bucket, providing protction against accidental deletions or overwrites
- when versioning is enabled, s3 stores every version of an object allowing you to recover older versions if needed making it ideal for data safety and backup

s3 replication
- it allows you to automatically copy objects from one s3 bucket to another, which can be :
within the same region (Same-Region Replication -SRR)
in defferent regions (Cross-Region Replication - CRR)
- it's commonly used for compliance, redundancy and to improve data access performance by maintaining copies closer to your users.

s3 storage classes
- s3 provides different storage classes to suit different use cases and cost requirements
- s3 standard - designed for frequently accessed data, offering high durability, availability, and low latency
- s3 inteligent-tiering - data with unknown or unpredictable access patterns, moves data automatically between frequent and infrequent tiers
- s3 standard-infrequent access (S3 Standard-IA) - designed for data accessed less frequently but quickly retrievable
- s3 one zone-infrequent access (S3 One Zone-IA) - designed for non-critical data, infrequently accessed data, offering lower cost than S3 Standard
- s3 glacier - designed for long-term data archiving, offering low cost and high durability
- s3 glacier deep archive - designed for long-term data archiving, offering lowest cost and high durability
- s3 outposts - designed for on-premises data storage, offering low latency and high throughput

s3 bucket lifecycle 
- you can use lifecycle policies to control the movement of objects between different storage class or delete them entirely based on specific conditions like age or inactivity

s3 snow family
- the s3 snow family is a group of physical devices offered by AWS to help move large amounts of data to the cloud when using the internet isn't practical
- these devices are used when there's too much data to upload over a regular connection or when dealing with remote areas without good internet
- types in snow family - snowcone, snowball and snowmobile
- AWS snowcone - small, portable device for a few terabytes of data
- AWS snowball - larger device for moving petabytes of data and can also be used for edge computing
- AWS snowmobile - massive truck sized container used for exabyte-scale data transfers typically used by big companies moving entire data centers

s3 storage gateway
- it is a hybrid cloud storage service that connects on-premises environments to cloud storage in Amazon S3. It helps extend your local storage to the cloud by acting as a bridge
'''

# AWS RDS Service
'''
AWS Relational Database Service (RDS) is a managed database service that simplifies database setup, operation and scaling
- Purpose - handling administrative tasks like backups, patching, monitoring and scaling

RDS snapshots

AWS offered database - Aurora offers
- up to 5x the throughput of mysql community edition & 3x of postgres
- upto 128 TB autoscaling SSD storage
- six-way replication accross three availability zone
upto 15 read replicas with replica lag under 10-ms
- automatic monitoring with failover

benifits of using RDS
- high avaiability and fault tolerance
- vertical and horizontal scaling
- automated backups and recovery
- read replicas for improved read performance
- multi availability zone setup for disaster recovery
- cost effectiveness

RDS architecture
- RDS read replica - multi region
- RDS multi - availability zone

common use cases of RDS
- web applications - relational databases are ideal for web apps requiring structured data
- e-commerce platforms - for handling inventory, customer data and order transactions
- business applications - ERP, CRM and financial applications with strong data integrity needs
'''

# AWS DynamoDB Service
'''
AWS DynamoDB is a fully managed NoSQL database service that provides fast and predictable performance with seamless scalability
- NoSQL is a type of database designed to store and manage data in flexible, non-tabular formats making it ideal for handling large volumnes of unstructured data
- dynamoDB stores data as items in tables with each item represented as a JSON-like document consisting of key-value pairs
- dynamoDB also offers a free tier that provides 25 GB of storage 
- the free tier also includes 25 provisioned write/read capacity units (WCU, RCU) which is enough to handle 200 million requests per month

features
- serverless - no need for server provisioning, software installation, maintainance or patching
- automatic scaling - instantly scales up or down based on demand with no manua adjustments needed
- zero downtime - provides continuous availability without maintanence windows
- on-demand pricing - pay only for the read/write requests used, ideal for fluctuating workloads
- idle cost savings - scales down to zero during inactivity, so there's no cost when tables have no traffic

- its flexible data model and reliable performance make dynamoDB a greatfit for mobile, web, gaming, advertising technology, internet of things and other applications

DynamoDB Accelerator - DAX
- fully managed in-memory cache for dynamoDB
- DAX offers microsecond latency achieving upto 10x performance over standard dynamoDB quries
- high availability and scalability - can be deployed in multiple availability zones
- DAX is only used for and is integrated with dynamoDB, while ElasticCache can be used for other databases

dynamoDB global table

'''

# AWS Lambda Function
'''
AWS Lambda is a serverless compute service that lets you run code without provisioning or managing servers
-  it is a serverless computing service that lets you run code in response to events without managing servers
- you just upload your code and AWS automatically handles the rest, scaling as needed and only charging for the time your code runs

Event-Driven Execution
- lambda is an event-driven service meaning that it runs your code in response to certain triggers or events
- these events can come from many different AWS services like S#(file uploads), dynamoDB(dtabase changes), API Gateway (HTTP requests), cloudwatch (scheduled events), etc

AWS lambda limitations
- execution time limit - limit functions can only run for a maximum of 15 minutes. If you need longer running tasks, lambda might be the best choice
- stateless - lambda functions don't keep state between invocations, so they are for tasks that don't require long-term memory 
- cold start delays - if a lambds function has't run in a while, there's sometimes a slight delay called a "cold start" when it starts up. This can add little latency, but AWS provides ways to mitigate it for critical functions

where to use lambda
- image processing - lets say users upload images to your app. You can set up lambda to automatically resize, compress or even apply filters to each image as it's uploaded
- data transformation -  if you need to clean up or process data before storing it in a database a lambda function can handle that transformation automatically
- real time notification - if an event happens - like a new user signing up you can use lambda to trigger an email, SMS or other notifications instantly

Automatic scaling
- AWS lambda automatically scales the execution of functions in response to the number of incomming requests
- if a thousand requests come in at the same time, AWS lambda will handle in parallel making it highly scalable without any configuration

pay as you go
- lambda uses a pau-as-you-go pricing model. You are billed based on the umber of function executions and the duration of each function's runtime (measured in milliseconda)
- this is cost-effective as you only pay for the compute time that you use and there's no charge for idle time

'''

# AWS CloudFormation IAC
'''
AWS CloudFormation is a service that helps you model and set up your AWS resources so that you can spend less time managing those resources and more time focusing on your applications that run in AWS
- it is an infrastructure as code (IaC) service that lets you define, provision and manage AWS resources in a declarative template based format

stack - collection of AWS resources that are defined in a CloudFormation template

why use it?
- consistency - define infrastructure in code
- automation - reduce manual work
- repeatable - replicate environments easily

summary
- Infrastructure as Code (IaC) Tool - automates the creating, management and updating of AWS infrastructure
- declarative language - users define desired end states for resources and cloudFormation handles provisioning
- template-based - uses yaml or json templates to specify AWS resources and configurations
- AWS native - exclusively supports AWS resources fully integrated with AWS services
- state management - manages state internally, eliminating the need for separate state files
- stacks and stack sets - organizes resources in stacks for easier management and allows for multi-account and region deployments with stack sets
- cost free tool - cloud formation itself is free, you only pay for the AWS resources created
- drift detction - identifies and reports on resources changes made outside of cloudformation to ensure resources stay alligned with the template

'''

# AWS Route53 Service
'''
AWS Route 53 is a highly available and scalable cloud DNS web service
- it is a scalable DNS service for domain registration, traffic routing and health checking capabilities

Domain Name System (DNS)
- it is the internet service that translates human-friendly domain names like www.example.com into machine readable IP addresses
- default port for DNS service is :53

summary
- Domain Name Registration - register a domain and point it to AWS route 53
- hosted zone creation - create a hosted zone to manage DNS records for your domain
- DNS records - add records (eg A, CNAME, MX) to route traffic to various endpoints
- routing policies - setup routing policies based on your needs, such as latency-based or failover routing
- health checks - configure health checks to monitor endpoints and trigger failover when needed.

types of records
- A record (IPv4) - maps a domain name to an IPv4 address
eg www.google.com  --> 12.34.56.78
- AAAA record (IPv6) - maps a domain name to an IPv6 address
eg www.google.com --> 2001:0db8:85a3:0000:0000:8a2e:0370:7334
- CNAME record - maps a domain name to another domain name (alias)
eg www.example.com --> www.google.com
- MX record - maps a domain name to an email server
eg example.com --> mail.example.com (priority 10)

use cases
- hosting websites - manage domain names and route traffic to web applications
- load balancing - ditribute traffic accross multiple endpoints using weighted or latency-based routing
- disaster recovery - use health checks and failover routing for high availability
- multi-region deployments - route traffic to the closest region for low latency

summary of billing
- billing components include hosted zone, DNS quries, health checks, domain registration and traffic policies
- costs vary based on usuage and the type of configuration (eg standard vs advanced routing policies)
- free tier - route 53 doesnot include a free tier so charges start as soon as you use it's services

'''

# AWS CloudFront CDN
'''
AWS cloudfront is a content delivery network (CDN) service provided by AWS that speeds up the delivery of web content to users by caching it at servers (edge locations) close to them, improving load times and performance globally
- it primarily caches static content like images, css, javascript and videos. it can also cache dynamic content (eg HTML or API responses) if configured with caching policies and headers
- by default sensitive or user specific data and backend logic are not cached. Cache behaviour is controlled via TTLs, cache behaviours and origin headers

- Edge cache points

- browsers act like mini-CDN by caching websites files locallt on a user's device which speeds up loading for repeat visits. Only help individual users 

cloudfront vs multi-location hosting ??
'''

# AWS VPC
'''
AWS Virtual Private Cloud (VPC) is a service that lets you provision a logically isolated virtual network within AWS. It allows you to define your own private network within AWS, complete with subnets, routing tables, network gateways, and security groups.
- a private isolated network within the AWS cloud where you can alunch and manage your resources securely
- to securely isolate and control network environments

VPC CIDR Block ??
- when you create a VPC, you specify a CIDR block that defines the IP address range for the entire VPC eg 10.0.0.0/16
- this block allows for 65,536 IP addressess (but in reality 65,531 usuable addressess)
- CIDR (Classless Inter-Domain Routing) is a method for allocating IP addressess and routing internet protocol (IP) packets
- https://cidr.xyz/

Submets
- it is a smaller, segmented part of a larger network that isolates and organizes within a specific IP address range
- public subnet vs private subnet ??

what happens when crreating sunet?
- CIDR block allocation - you specify a range addresses (CIDR block) within the VPC's IP address range for the subnet
- this determines the pool of IP addresses available for instances in the subnet

Route Table
- it is a set of rules, called routes that are used to dtermine where network traffic from your subnets or gateway is directed. Each subnet in your VPC must be associated with a route table which controls the routing for that subnet

Internet gateway
- it is a component that allows communication between instances in your VPC and the internet

Security Groups
Network firewall rules that control inbound and outbound traffic for instances

Network ACLs (Access Control Lists)
- optional layer of security for your VPC that acts as a firewall for controlling traffic in and out of one or more subnets
- allow or deny rule

NAT (Network Address Translation) Gateway
- it enables instances in a private subnet to connect to the internet or other AWS services but prevents the internet from initiating connections to those instances

VPC Peering
- networking connection between two VPCs that enables you to route traffic between them privately

VPC Endpoints
- allows you to privately connect your VPC to support AWS services and VPC endpoint services powered by AWS private link

Bastion Host
- special purpose instance that provides secure access to your instances in private subnets

Elatic IP Address
- static IP address designed for dynamic cloud computing

VPC flow logs
- caputing information about the IP traffic going to and from network interfaces in your VPC

Direct Connect
- establishes a dedicated network connection from your premises to AWS

AWS Client VPN
- managed VPN services that enables secure remote access to AWS resources and on-premises networks using OpenVPN-based clients







'''

# AWS VPC Creation 

# AWS Billing and Organization
'''
- cost free service

AWS pricing calculator





'''

# AWS Amplify - Full Stack Web Demo
'''
AWS Amplify is a set of tools and services that help developers build and deploy full-stack web and mobile applications on AWS. It provides a set of tools and services that help developers build and deploy full-stack web and mobile applications on AWS.
- platform that simplifies building, deploying and hosting full stack web and mobile apps
- connects to backend services like user login, data storage andAPIs
- offers hosting and automatic updates for web apps

- deploying
- ci/cd pipelines
- configure cusyom domain
- domain from hostinger
- local AWS credentials
- backend endpoints
- cloud sandbox

benifits
- speeds up app development with built-in tools
- provides scalable backend services that can grow with your apps
- simplifies cloud integration making it easier for beginners and experienced developers

'''

# AWS ECS (Elastic Container Service)
'''
AWS ECS is a container orchestration service that allows you to run, stop and manage containers on AWS. It provides a scalable and reliable way to run containerized applications on AWS.
- it is a cloud-based container management service that allows you to run and manage Docker on a cluster of virtual servers

why ECS??
- it automatically handles - creation, management and updating

cluster
- group of tasks and services, hosts all the resources and infrastructure

service
- handles scalability, load balancing and health checks

task
- represents the running containers of your AWS


cluster vs service vs task ??

'''

# AWS EKS (Elastic Kubernetes Servie)
'''
AWS Elastic Kubernetes Service (EKS) is a managed Kubernetes service provided by Amazon Web Services (AWS). It allows you to run and manage Kubernetes clusters on AWS infrastructure.

Kubernetes
- open source platform for automating the deployment, scaling and management of containerized applications
- when you deploy kubernetes, you get cluster
- master (control pane) and worker nodes






'''

# Bonus Must learn Session

# What is Terraform?
'''
- Terraform is an open source infrastucture as code (IaC) tool
- IaC enables you to define, provision and manage infrastucture accross multiple cloud providers using a declarative configuration language
- supports multi-cloud environments allowing consistent and efficient infrastucture management

terraform config
- it uses .tf extension
- format is HCL (HashiCorp Configuration Language)
- declarative language

basic commands
- terraform init - initialize a working directory containing Terraform configuration files
- terraform plan - generates an execution plan
- terraform apply - apply changes to the infrastructure
- terraform destroy - destroy the infrastructure

benefits
- consistency - define infrastructure in code
- automation - reduce manual work
- repeatable - replicate environments easily

state management
- the state file (terraform.tfstate) mantains a detailed record of the current state of managed resources
- the state file can be stored locally or remotely with remote storage options enabling collaboration by sharing the state across teams and environments

multiple resource using - count and for_each

terraform modules
- modules are containers for multiple resorces that are used together
- a module consists of a collection of .tf and/or .tf.json files kept together in a directory
- modules are the main way to package and reuse resources configurations with terraform

terraform cloud
- it is a managed service provided by HashiCorp that facilitates collaboration on terraform configurations
- it provides - remote state management, version control system (VCS) integration, automated runs and secure variable management

'''

# Understand DNS working with Practical
'''
DNS translate
- A record that maps a domain name to an IP address
- PTR record that maps an IP address to a domain name
- CNAME record that maps a domain name to another domain name

xone files
forward zone - maps domain names to IP addresses
backward zone - maps IP addresses to domain names


'''

# Understand SSL/TLS Certificates and Encryptions
'''
SSL/TLS (Secured Sockets Layer/Transport Layer Security)
- cryptographic protocols designed to provide secure communication over a computer network
- TLS is the successor to SSL

How SSl/TLS secure data?
encrypt data and ensure its
confidentility - papers is only accessed by exam center - encryption
integrity - paper is not modified in between - hashing 
authenticity - verifying the identity of the parties who they are supposed to be - certificates
between client and server

encryption
- converting plain text information into a coded form (cipher text)
- types - symmetric and asymmetric
- symmetric uses the same key to encrypt and decrypt, faster and more efficient, suitable for large data, challenging key distribution, single key must be kept secret
- asymmetric uses a public key to encrypt data and a private key to decrypt data, slower, suitable for small data, simplified key distribution, secure even if the public key is shared

hybrid encryption
- combines the strengths of both symmetric and asymmetric encryption to achieve efficient and secure communication
- asymmetric encryption is used to securely exchange a symmetric key between parties
- once the symmetric key is securely exchanged, it is used to encrypt and decrypt the actual data, symmetric encryption is faster and more efficient, making it ideal for encrypting large amounts of data

some algo examples
- asymmetric - DSA, RSA, ECC, ECDH
- symmetric - AES, DES, 3DES, RC4, RC5, Blowfish, ChaCha20

hashing
- process of converting data into a fixed size string of characters, as sequence of numbers and letters

'''
