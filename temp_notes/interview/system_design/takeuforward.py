
# https://www.youtube.com/watch?v=43-X22tdxiI&list=PLA3GkZPtsafZdyC5iucNM_uhqGJ5yFNUM&index=1 (Beginner)


# region SYATEM DESIGN vs ARCHITECTURAL DESIGN/PATTERN
'''
architecture means internal design details
'''
# Definition
'''
System Design -	The process of planning, designing, and structuring a system to meet specific needs.
Architecture Patterns - Reusable, general-purpose solutions to common architectural problems.
'''	

# Scope
'''
System Design -	Covers both high-level and low-level design.
Architecture Patterns - Focuses primarily on high-level system structure.
'''	

# Specificity
'''
System Design -	Tailored to solve specific problems for a given system.
Architecture Patterns - General templates applicable to many systems and industries.
'''	

# Level of Detail
'''
System Design -	Contains detailed design elements such as modules, data flow, algorithms, etc.
Architecture Patterns - Offers abstract, reusable patterns that guide system structure.
'''	

# Flexibility
'''
System Design -	Highly specific to the context and requirements of the system.
Architecture Patterns - Broad, adaptable to various systems and contexts.
'''	

# Examples
'''
System Design -	E-commerce platform system design, including user management, product catalog, and payment modules.
Architecture Patterns - Microservices, Client-Server, Layered Architecture.
'''	

# Usage
'''
System Design -	Used to build and plan the complete system from top to bottom.
Architecture Patterns - Used to structure the system at a higher level.
'''	

# Complexity
'''
System Design -	Can be very complex depending on the application being designed.
Architecture Patterns - Less complex, providing overarching structure but not implementation details.
'''	

# endregion





# region MONOLITHIC vs DISTRIBUTED ARCHITECTURE

# monolithic / centralized / trivial architecture
'''
WHAT -
- a software design where all components of the application are tightly integrated and run as a single unit.

CHARACTERISTICS -
- Single codebase: The entire system is developed and deployed as one unit.
- Tightly coupled: Components are interconnected, and changes to one part may require testing and redeploying the whole system.
- Easier to start: It’s simpler and faster to develop in the initial stages, especially for small teams or small projects.
- Scalable: Typically, scaling is done at the application level, meaning you would scale the entire monolith rather than individual parts.

WHEN TO USE IT?
- Small to medium-sized applications: Monolithic architecture can be ideal for simpler applications or startups where the team is small and the scope is limited.
- Short-term projects: If the project is expected to be short-lived or doesn’t require complex scaling in the immediate future, a monolith might be more suitable.
- Tight integration of components: When the business logic is highly interdependent and modularization of components could add unnecessary complexity.

PROS
- Simplicity: It’s easier to start and develop in the initial stages.
- Easier to understand: The entire application is in one place, making it easier to understand and maintain.
- Easier to maintain: Since everything is in one place, it’s easier to maintain and debug.

CHALLENGES
- Hard to scale: While it’s easy to scale the entire application, it’s inefficient when only some parts of the application need more resources.
- Slow development: As the application grows, new features can become harder to integrate, testing becomes more complex, and the deployment cycle gets slower.
- Debugging / Tightly coupled: Changes to one part can have a ripple effect on others, making maintenance and debugging more difficult.
- single bug can bring down the entire system
- updation of single module can effect the entire system

'''


# distributed / microservices architecture
'''
WHAT -
- a design where the application is broken down into smaller, independent services that can be developed, deployed, and scaled individually.

CHARACTERISTICS -
- Decentralized: Each microservice is developed, deployed, and managed independently.
- Loose coupling: Microservices can be updated or scaled independently, which is beneficial for maintaining a high level of flexibility and modularity.
- Domain-oriented: Microservices often map to specific business domains or subdomains.
- Independent scalability: You can scale only the services that need it, rather than the entire application.

WHEN TO USE IT?
- Large and complex applications: If you're building a system that is expected to grow in complexity or scale over time (e.g., an e-commerce platform, social media site, or enterprise application).
- Distributed teams: When you have multiple teams working on different components or services of the system, microservices can help isolate work and reduce dependencies.
- Scalability: If you expect certain parts of the application to need more resources (e.g., payment processing vs. user login), microservices allow you to scale those parts independently.
- Frequent updates or independent release cycles: If different parts of the system need frequent updates and separate deployment cycles.

PROS
- Scalability: You can scale individual services independently, which is beneficial for applications that have different usage patterns.
- Flexibility: You can update or replace a service without affecting the entire system.
- Independent deployment: Each service can be deployed independently, which can speed up the development and deployment process.
- Easier maintenance: Since each service is smaller, it’s easier to understand, maintain, and debug.
- Independent scaling: You can scale only the services that need it, rather than the entire application.
- Fault isolation: If one service fails, it doesn’t bring down the entire system.

CHALLENGES
- Complexity: Managing multiple services introduces significant complexity, such as handling inter-service communication, data consistency, and ensuring that services remain independently deployable.
- Deployment overhead: More services mean more components to deploy, monitor, and maintain.
- Network latency: Since microservices communicate over a network, there’s potential for latency, especially if there are a lot of calls between services.
- Data management: Each service may have its own database, which complicates transactions and data consistency. It may cause data loss.
- Security: Managing security across multiple services can be challenging.

'''

# endregion 





# region HLD vs LLD

# High-Level Design (HLD)
'''
WHAT 
- abstract or general overview of the system architecture, providing a big-picture view of how the components and modules of the system interact with each other.

HLD INCUDES
- System architecture: Overview of the architecture, including the main components and their interactions (e.g., client-server architecture, microservices, etc.).
- Modules and Components: Description of the major components or modules of the system and their roles.
- Data Flow: Diagrams showing how data flows between different components (e.g., data input, processing, and output).
- Interfaces: The interactions between various system components and external systems or services.
- Technology stack: High-level selection of technologies and tools to be used (e.g., database systems, programming languages, frameworks).
- System boundaries: Definition of what is inside and outside the scope of the system.
- Deployment strategy: General approach to deploying the application (cloud, on-premise, hybrid, etc.).

WHEN IT IS DONE
- during early design phase.
- useful for discussions with stakeholders, such as management, clients, or non-technical teams, to give them a sense of how the system is structured.
'''


# Low-Level Design (LLD)
'''
WHAT 
- dives into the specifics of how individual modules or components of the system will be implemented.

LLD INCUDES
- Module design: Detailed design of individual modules/components, including their functionality and how they interact with other modules.
- Database design: Detailed schema design, including tables, columns, relationships, and indexes (e.g., Entity-Relationship Diagrams).
- Algorithm design: Pseudocode or flowcharts for key algorithms and business logic.
- Class and Object Design: In Object-Oriented Design, this includes class diagrams, attributes, methods, and relationships between classes (e.g., inheritance, associations).
- API Design: Specifications for the APIs between modules, including input/output parameters, request-response structures, etc.
- Error handling and exception management: Detailed plans for error handling and edge case management.
- User Interface (UI) design: Detailed wireframes or mockups of how the application’s user interface will look.
- State diagrams: For components that have different states or modes of operation.

WHEN IT IS DONE
- Once the high-level architecture is set, LLD is used to define how each part of the system will be implemented.
- Development phase

'''

# endregion






# region CONSISTANCY, AVAILABILITY and PARTITION TOLERANCE
# Throughput
'''
What is it?
- The amount of work (data or requests) processed by a system in a given time. 
- Measured in units like requests per second, bits per second, etc.

Why is it used?
- To measure the efficiency or capacity of a system in handling tasks.

What affects it?
- System capacity: The hardware and resources like CPU, memory, and storage available for the system.
- Network bandwidth: The speed and capacity of the network connection.
- Resource availability: If other resources are being overused or are under-provisioned, throughput can be negatively impacted.
- Workload: The complexity of tasks or data volume handled by the system. Complex tasks often reduce throughput.
- Latency: If the system is slow to respond, it can affect throughput.
- Protocol  overhead: The overhead of the communication protocol used can affect throughput.
- Congestion: If the network is congested, it can slow down throughput.

How to improve it?
- Parallel processing: Split tasks into smaller sub-tasks that can be processed concurrently.
- Optimized algorithms: Use efficient algorithms that process data faster.
- Increase resources: Scaling horizontally (more machines) or vertically (more powerful machines).
- Improve network efficiency: Reduce latency or use high-bandwidth networks to minimize bottlenecks. 
- Load balancing: Distribute requests across multiple servers.

'''
# Latency
'''
What is it?
- The delay before a system starts processing a request or data. 
- Measured in milliseconds (ms).
- computational delay + network delay

Why is it used?
- To measure how quickly a system responds to a request.

What affects it?
- Network delays: The time it takes for data to travel across networks (e.g., internet speed, routing).
- Processing time: How long it takes the system to process a request or operation.
- Hardware performance: Faster hardware (e.g., processors, SSDs) results in lower latency.
- Congestion: High traffic on the network or in the system itself can cause delays in processing requests.


How to improve it?
- Caching / Reduce network hops: Minimize the number of intermediary devices (like routers) that data needs to pass through.
- Use CDNs: Content Delivery Networks cache data closer to the end-users, reducing latency.
- Use faster hardware: Upgrading to faster CPUs, SSDs, or better networking equipment reduces processing delays.
- Optimize code: Efficient coding can reduce processing time by avoiding unnecessary operations.
- Edge computing: Process data closer to the user, minimizing travel time to data centers.
'''

# Consistency
'''
What is it?
- Ensuring that all copies of data are the same across distributed systems at any given time.

Why is it used?
- To ensure data correctness and prevent discrepancies across replicas.

Types of consistency:
- Strong consistency: 
Data is always up-to-date and consistent across all replicas.
when the system doesn't allow read operations until all the nodes with replicated data are updated
Eg - Bank Account System
- Eventual consistency: 
Data eventually becomes consistent after some time.
User read requests are not halted till all the replicas are updated rather the update process is eventual. Some users might recieve old data but eventually all the data is updated to the latest data.
Eg - social media feeds
- Weak consistency: 
Data may be inconsistent for a short period of time.
Eg - DNS (Domain Name System)


What affects it?
- Network partitions: When parts of a distributed system become isolated due to network issues, it may be hard to guarantee consistency.
- Concurrency: When multiple processes try to modify data at the same time, race conditions can occur, potentially causing inconsistent data.
- Replication strategy: The method by which data is copied across multiple systems impacts how quickly changes are propagated and whether data remains consistent.


How to improve it?
- Use strong consistency models: Implement strict protocols like two-phase commit or Paxos to ensure that all copies of the data are updated consistently.
- Synchronization: Ensure regular synchronization between nodes to keep data consistent.
- Locking mechanisms: Use locks to prevent multiple processes from changing the same data at once.
- Eventual consistency: In some cases, it's acceptable to let data become consistent over time, which can be easier to implement in distributed systems.

'''
# Availability
'''
What is it?
- The percentage of time a system is operational and can respond to requests.
- fault tolerance is directly proportional to availability

Why is it used?
- To ensure the system is reliable and accessible when needed.

What affects it?
- Server failures: If a server goes down, parts of the system may become unavailable.
- Network issues: Communication failures between different parts of the system can cause downtime.
- Overload: If the system is overloaded with requests or data, it may become unresponsive.
- Maintenance: Planned or unplanned maintenance can affect availability.

How to improve it?
- Redundancy: Use backup systems or failover mechanisms (e.g., multiple servers or data centers) to ensure the system remains operational even if one component fails.
- Load balancing: Distribute requests across multiple servers to avoid overloading any single server.
- Replication: Replicate data across multiple systems or regions to ensure it’s always accessible.
- Monitoring and alerting: Proactively monitor system health to detect issues before they impact availability.
'''

# Repliaction vs Redundancy 

# CAP Theorem
'''
CAP Theorem (Consistency, Availability, Partition Tolerance): In distributed systems, you can only prioritize two of the following three properties simultaneously:

- Consistency: All nodes see the same data at the same time.
- Availability: Every request receives a response, either with the data or an error.
- Partition Tolerance: The system continues to operate even if network partitions occur between nodes.

Depending on the system's requirements, you will have to make trade-offs:

- CP (Consistency and Partition Tolerance): Systems that prioritize consistency (e.g., bank transactions) may sacrifice availability during network partitions.
- AP (Availability and Partition Tolerance): Systems that need high availability (e.g., social media) may relax consistency, allowing some inconsistency during network issues.
- CA (Consistency and Availability): Rare, as network partitions often happen, but this prioritizes both availability and consistency at the cost of partition tolerance. eg monolithic systems
'''


# endregion






# region CDN
'''
What is a CDN?
- a network of servers distributed across various locations worldwide that work together to deliver web content (such as images, videos, and websites) to users faster and more efficiently.

Why is it used?
- To speed up website loading times by delivering content from the server closest to the user.
- To reduce server load by offloading traffic to multiple servers.
- To improve availability and redundancy in case of server failure.

When is it used?
- When you need to improve website performance and reduce latency.
- When you have a global user base and want to deliver content efficiently across different regions.
- For media-heavy websites (images, videos, etc.) that require high-speed delivery.

Pros of CDN
- Faster content delivery by caching content closer to users.
- Scalability: Handles large amounts of traffic efficiently.
- Improved website reliability due to redundancy and failover mechanisms.
- Reduced latency for users located far from the origin server.


Cons of CDN
- Cost: CDN services can add additional expenses.
- Cache inconsistencies: Content might be stale if not updated properly.
- Complexity: Some advanced configurations can be difficult to manage.


How is it implemented in Python code?

import requests

# Fetch a static image from a CDN
cdn_url = "https://cdn.example.com/images/logo.png"
response = requests.get(cdn_url)

# Save the image locally
with open("logo.png", "wb") as file:
    file.write(response.content)

print("Image downloaded from CDN!")
In this example, you use the CDN URL to access content and retrieve it using Python. The actual CDN configuration is done through the CDN service's dashboard, not within the Python code.


Types of CDN

1. Traditional (Pull) CDN
How it works: Content is delivered from the origin server to the CDN edge servers when a user requests content for the first time. The CDN caches the content, so future requests can be served from the cache.
When to use: When you want the CDN to automatically cache your static assets without managing the content manually.

2. Push CDN
How it works: Content is proactively uploaded to the CDN's edge servers by the website owner, meaning the content is "pushed" to the CDN in advance. Users can access content directly from these cached edge servers.
When to use: When you want to have more control over what content is cached and want to manage the content yourself.

3. Peer-to-Peer (P2P) CDN
How it works: Uses a decentralized approach where users share content with each other directly. When a user downloads content, they can also upload it to other users.
When to use: For applications with high-volume content delivery, such as video streaming, where user participation can help distribute the load.

4. Dynamic CDN
How it works: Unlike traditional CDNs that mainly cache static content, dynamic CDNs can cache dynamic content (content that changes frequently based on user interactions, such as personalized data). They use advanced caching techniques to optimize dynamic content delivery.
When to use: For websites with personalized or dynamic content that needs to be delivered faster without always requesting it from the origin server.

5. Cloud CDN
How it works: Hosted by a cloud service provider (like AWS, Google Cloud, or Azure), these CDNs distribute content through a globally distributed network of servers. They typically provide both static and dynamic content caching.
When to use: When you want to leverage the scalability and infrastructure of the cloud for both static and dynamic content delivery.

6. Media Delivery CDN
How it works: Specialized CDNs focused on delivering media content such as video, audio, or live streaming. These CDNs are optimized for large file sizes and high-bandwidth usage.
When to use: For applications that heavily depend on media, like video streaming platforms (e.g., YouTube, Netflix) or online music services.

7. Multi-CDN
How it works: This involves using multiple CDN providers in parallel to increase reliability and coverage. Traffic is routed dynamically across different CDNs based on performance, location, and availability.
When to use: For applications that require high availability, resilience, or performance across diverse regions, especially when one CDN provider might have limitations.

8. Reverse Proxy CDN
How it works: A reverse proxy CDN acts as an intermediary between users and the origin server. It fetches content from the origin server and serves it to users while caching it at edge locations.
When to use: For websites where you want to manage traffic efficiently and protect your origin server from excessive load.
'''

# endregion






# region CACHING
'''
What is Caching?
- process of storing copies of data in a temporary storage (called a cache) so that future requests for that data can be served faster.

Why is it used?
- Speed: It reduces the time taken to access data by storing frequently accessed data closer to the user.
- Efficiency: Reduces load on databases or servers by serving cached data instead of fetching it repeatedly from the original source.
- Cost-saving: Reduces the need for expensive computations or repeated database queries.

When is it used?
- When you need to improve performance (faster data retrieval).
- For high-traffic systems where the same data is requested frequently.
- To reduce server load and avoid repeated processing of the same data.

Pros of Caching
- Faster data retrieval: Reduces access time.
- Reduced server load: Less frequent requests to the original data source.
- Improved scalability: Can handle more traffic with less overhead.

Cons of Caching
- Stale data: Cached data can become outdated if not refreshed properly.
- Memory consumption: Caching takes up additional memory/storage.
- Complexity: Managing cache invalidation and consistency can be tricky.

Types of Caching
- In-memory Caching: Stores data in memory (e.g., RAM) for extremely fast access (e.g., Redis, Memcached).
- Disk Caching: Stores data on disk for larger storage, though slower than in-memory.
- Distributed Caching: Caches data across multiple servers (e.g., Redis Cluster, Memcached Cluster) for scalability.
- Browser Caching: Stores static content (e.g., images, CSS) in the browser cache.
- Content Delivery Network (CDN) Caching: Caches content at geographically distributed edge servers for faster access.

How is it implemented in Python code?
To implement caching in Python, you can use libraries like functools.lru_cache (for simple in-memory caching) or redis for more advanced caching.

- Example with functools.lru_cache (In-memory caching):
import functools

@functools.lru_cache(maxsize=128)  # Cache up to 128 results
def expensive_computation(n):
    print(f"Computing {n}...")
    return n * n

# First call, computes and caches the result
print(expensive_computation(5))

# Second call, returns cached result
print(expensive_computation(5))

- Example with redis (Distributed caching):
import redis

# Connect to a Redis server
r = redis.Redis(host='localhost', port=6379, db=0)

# Set cache
r.set('key', 'value')

# Get cache
cached_value = r.get('key')
print(cached_value)  # Output: b'value' (bytes)
In these examples:

LRU Cache (Least Recently Used) stores function results in memory.
Redis allows you to store and retrieve data from an external distributed cache.
'''







# region CDN vs CACHING

# Definition
'''
Caching - storing data temporarily to reduce future retrieval time.	
CDN - a network of servers distributed globally that delivers content (such as images, videos, and websites) quickly to users.
'''

# Purpose
'''
Caching - To speed up access to frequently accessed data by reducing the need to fetch it repeatedly from the original source.
CDN - To deliver content quickly and efficiently to users by distributing it across a network of servers located closer to the end user.
'''
		

# Scope
'''
Caching - Typically focuses on storing data in memory or disk (local or centralized storage).
CDN - Focuses on distributing content globally and serving it from the nearest edge server.
'''
		

# Storage Location
'''
Caching - Can be stored locally (in RAM, disk, or even application level cache) or on a centralized server.
CDN - Content is stored across multiple geographically distributed servers (edge servers) in various locations worldwide.
'''
		

# Data Type
'''
Caching - Can store any type of data (e.g., computation results, database queries).
CDN - Primarily stores static content like images, videos, and web assets (HTML, CSS, JavaScript).
'''
		

# Use Case
'''
Caching - Improves performance of frequently accessed data within a single system or server (e.g., web server, database).
CDN - Used to improve website load times and performance for global users by reducing the distance between the user and the content.
'''
		
# Example
'''
Caching - In-memory caching with Redis or Memcached, database query caching.
CDN - Using Cloudflare or AWS CloudFront to deliver static content faster to users.
'''
		

# Caching Method
'''
Caching - Caching can be done manually within a system (e.g., code, database, etc.) using different strategies (LRU, LFU, etc.).
CDN - CDN automatically handles caching at edge servers, ensuring content is distributed and cached in multiple locations.
'''
		
# Content Updates
'''
Caching - Requires cache invalidation or expiration policies to ensure fresh data.
CDN - CDN caches content based on expiration rules, and it updates content when required (e.g., cache purging).
'''

		
# Implementation
'''
Caching - Implemented directly within an application (e.g., using in-memory cache or external cache like Redis).
CDN - Implemented using a CDN provider that automatically manages caching and content distribution.
'''

# endregion






# region REDUNDANCY
# Definition
'''
- refers to having additional copies of critical components (such as hardware, software, or data) to ensure that the system continues to function in case of failure.
'''

# Pros 
'''
- Increased availability: Ensures the system can continue to function even if one component fails.
- Fault tolerance: Helps to recover quickly from failures without disrupting the service.
- Load balancing: Distributes load across multiple systems, improving performance.
'''

# Cons
'''
- Costly: Requires extra hardware or resources, increasing expenses.
- Complex management: Can be harder to maintain and monitor redundant systems.
- Wasted resources: Redundant components are often idle, leading to inefficiency.
'''

# Types of Redundancy
# 1. Active Redundancy
'''
Definition: 
- all redundant components are actively working and participating in the system. 

Example:
Load Balancers
Imagine you have multiple servers in a load-balanced setup. All servers actively handle requests at the same time, sharing the traffic load equally. If one server fails, the load balancer redirects the traffic to the remaining active servers.

When it's used:
- For systems where high availability and fault tolerance are crucial.
- For systems that need to distribute load and ensure optimal performance.

Pros:
-Improved performance: All redundant components work, helping to distribute the load.
- Fault tolerance: The system can continue to function if one component fails, without impacting performance.

Cons:
- Higher resource usage: All components are active, consuming more power and resources.
- Complexity: Managing and synchronizing multiple active components can be more complex.
'''
# 2. Passive Redundancy
'''
Definition: 
- only one component is active at a time. The redundant components are on standby, and they only take over if the active component fails.

Example:
Hot Standby Systems
Imagine you have two servers, but only one is running and handling requests. The second server is kept idle and is only activated if the first server fails. This is known as "hot standby."

When it's used:
- When cost-efficiency is a priority.
- In systems where failover is more important than continuous load balancing.
- For environments where disaster recovery is needed.

Pros:
- Cost-effective: You only use resources when needed, keeping costs lower.
- Simpler setup: Easier to manage and configure because only one system is active at any time.

Cons:
- Lower performance: Only one component is active, so you don’t get the benefit of load distribution.
- Failure risk: If the active component fails, there may be a brief period before the passive system can take over.

'''

# endregion






# region REPLICATION
# Definition: 
'''
- refers to creating copies of data or databases to ensure high availability and fault tolerance. It is primarily about copying data across multiple systems or locations.
- redundancy + synchronization
'''

# Pros 
'''
- High availability: Data is always accessible from other replicas even if the primary system fails.
- Improved performance: Can distribute read requests across replicas to reduce load.
- Disaster recovery: Helps in data recovery after a failure or disaster.
'''

# Cons
'''
- Complex consistency: Ensuring data consistency across replicas can be tricky.
- Data overhead: Replicating large amounts of data consumes bandwidth and storage.
- Latency: Data synchronization between replicas can introduce delays.
'''

# Types of Replication
# 1. Active Replication
'''
Definition: 
- all replicas (copies of the data) are actively involved in processing every request. Each replica independently processes all incoming requests and updates its state accordingly. This method ensures that all replicas are consistent and have the same data at all times.

How It Works:
Every replica processes the same request and executes the same operations simultaneously (usually in parallel).
All replicas must stay synchronized, and the system must handle ensuring that all replicas receive and process every operation.
Example:
Web Servers in Load Balancing
If you have multiple servers handling web requests in an active replication setup, each server actively processes requests. For example, a user logs in, and all the servers process the login request simultaneously, ensuring they all have the same user state.

When to Use:
- When you need high availability and fault tolerance.
- For real-time systems where all replicas must have the same data at all times.

Pros:
- High availability: All replicas are actively working, so if one fails, others can continue serving requests.
- No single point of failure: Each replica processes requests independently.
- Better fault tolerance: All replicas are always up-to-date with the same data.

Cons:
- Increased overhead: Requires significant resources as every replica processes each request.
- Complex coordination: Ensuring synchronization and handling concurrency can be complex.
'''

# 2. Passive Replication
'''
Definition: 
- only one replica (often called the primary or master) is actively processing requests, while the other replicas (called secondary or backup) passively wait to receive updates from the active replica. If the active replica fails, one of the passive replicas takes over the role of the active replica.

How It Works:
Only one replica processes requests and updates the data.
The active replica sends updates to the passive replicas periodically to keep them in sync.
If the active replica fails, one of the passive replicas is promoted to be the new active replica.
Example:
Database Replication (Master-Slave)
In a typical master-slave database replication, only the master database is active, accepting read and write operations. The slave databases are passive and periodically receive updates from the master. If the master fails, one of the slaves is promoted to the master.

When to Use:
- When cost efficiency is needed and you don’t require all replicas to be active all the time.
- When system updates are infrequent and consistency is less time-sensitive.

Pros:
- Lower resource consumption: Only one replica processes requests, saving resources.
- Simpler management: The system is simpler to set up and maintain compared to active replication.
- Reduced overhead: No need for all replicas to process every request.

Cons:
- Single point of failure: If the active replica fails and there is no quick failover, there might be a period of downtime.
- Failover delay: It may take time for a passive replica to be promoted to active status if the primary fails.
- Lower fault tolerance: If the active replica fails before a passive replica can take over, the system may experience downtime.
'''

# endregion 







# region REDUNDANCY vs REPLICATION
# Definition
'''
Redundancy -  Having extra resources or components to prevent system failure.	
Replication - Creating copies of data or systems to ensure availability and reliability.
'''
# Purpose	
'''
Redundancy - Improve fault tolerance by replacing failed components.	
Replication - Ensure data availability and consistency across systems.
'''
# Focus	
'''
Redundancy - Can be applied to hardware, networks, or data.	
Replication - Primarily applies to data or databases.
'''
# Example	
'''
Redundancy - Redundant power supply, multiple servers, or load balancers.	
Replication - Database replication (master-slave setup) or file replication.
'''

# endregion





# region SCALING

# Definition 
'''
- refers to the process of increasing or decreasing the capacity of a system to handle more or fewer demands. 
'''

# Why is Scaling Used?
'''
- Handle increased load: To support more users or higher traffic without degrading performance.
- Improve performance: To ensure the system responds quickly and efficiently even under heavy use.
- Maintain availability: To prevent downtime and ensure the system remains operational as demand grows.
- Optimize resources: To adjust resources based on current demand, ensuring efficiency and cost-effectiveness.
'''

# Types of Scaling
# 1. Vertical Scaling (Scaling Up):
'''
Definition: 
Increasing the capacity of a single server or resource (e.g., adding more CPU, RAM, or storage to an existing machine).

Example: 
Upgrading a server from 8GB RAM to 32GB RAM to handle more requests.

When to Use: 
When a single machine’s resources are inadequate to handle the load, but the application doesn’t need to be distributed.

Pros: 
Simpler to implement, doesn’t require changing application architecture.

Cons:
Limited by the capacity of a single machine, and might become expensive.
'''
# 2. Horizontal Scaling (Scaling Out):
'''
Definition: 
Adding more machines or servers to the system, distributing the load across multiple nodes.

Example: 
Adding more web servers behind a load balancer to handle more traffic.

When to Use: 
When the system needs to handle large volumes of traffic and workloads, or when you need to distribute load across multiple 
machines.

Pros: 
Highly scalable and cost-effective; there’s no physical limit to the number of nodes.

Cons: 
More complex to implement and manage (e.g., managing multiple servers, database synchronization).
'''

# endregion






# region LOAD BALANCERS
# Definition 
'''
- a device or software that distributes incoming network traffic across multiple servers or resources to ensure that no single server is overwhelmed
'''

# Why is Load Balancing Used?
'''
- Improve Performance: By distributing requests across multiple servers, the system can handle more traffic and avoid overloading any single server.
- Ensure High Availability: If one server fails, the load balancer redirects traffic to other healthy servers, maintaining continuous availability.
- Increase Scalability: As traffic grows, you can add more servers, and the load balancer will automatically distribute traffic to the new servers.
- Fault Tolerance: Load balancers detect server failures and automatically reroute traffic to functioning servers, improving system reliability.
'''

# Types of Load Balancers
# 1. Hardware Load Balancers:
'''
Definition: 
Physical devices that balance traffic across multiple servers in a network.

Example: 
F5 Networks, Citrix NetScaler.

Use Case: 
Often used in enterprise-level data centers for high-performance, large-scale systems.
'''

# 2. Software Load Balancers:
'''
Definition: 
Software-based solutions that perform load balancing, typically running on general-purpose hardware or virtual machines.

Example: 
Nginx, HAProxy, Traefik.

Use Case: 
More flexible, cost-effective, and scalable for cloud environments or smaller systems.
'''

# 3. Cloud-Based Load Balancers:
'''
Definition: 
Managed load balancing services provided by cloud providers.

Example: 
AWS Elastic Load Balancer (ELB), Google Cloud Load Balancing, Azure Load Balancer.

Use Case: 
Ideal for cloud-native applications, automatically scaling with infrastructure.
'''

# Types of Load Balancing Algorithms
# 1. Round Robin:
'''
Distributes incoming requests to servers in a cyclic order.
Simple but effective for evenly distributing traffic.
Use Case: Suitable for servers with similar resources and load characteristics.
'''
# 2. Least Connections:
'''
Sends requests to the server with the least number of active connections.
Ensures that servers with fewer active sessions handle more traffic.
Use Case: Ideal when servers have varying resource capacities or traffic loads.
'''
# 3. IP Hash:
'''
Uses the client’s IP address to determine which server will handle the request, ensuring the same client is directed to the same server for consistency.
Use Case: Useful for session persistence (sticky sessions).
'''
# 4. Weighted Round Robin:
'''
Similar to round-robin, but assigns different "weights" to servers based on their capacity. Servers with higher weights get more requests.
Use Case: When some servers have more resources than others.
'''
# 5. Least Response Time:
'''
Directs traffic to the server with the fastest response time.
Use Case: Ideal when response time is a critical factor and server performance varies.
'''

# Key Features of Load Balancers
'''
Health Checks:
Load balancers continuously check the health of backend servers. If a server becomes unhealthy or fails, the load balancer stops sending traffic to it until it’s healthy again.

SSL Termination:
Load balancers can handle SSL/TLS encryption/decryption (SSL termination), offloading this heavy task from backend servers and improving performance.

Session Persistence (Sticky Sessions):
Ensures that a client’s requests are routed to the same server during the session, maintaining state across requests (useful for applications with user sessions).

Auto-scaling:
In cloud environments, load balancers automatically distribute traffic to new servers as they are added, and remove servers that are no longer needed.

Content-Based Routing:
Load balancers can route requests based on URL paths, headers, or cookies, directing traffic to different services based on the request content.
'''
# When to Use Load Balancers?
'''
- High Traffic Systems: To prevent overloading any single server and maintain smooth performance as user traffic increases.
- Distributed Systems: To ensure that multiple servers work together efficiently in handling requests.
- Cloud-Based Environments: For scalability, where servers can be dynamically added or removed based on demand.
- High Availability Requirements: To ensure continuous service even when some servers fail, by redistributing the load to healthy servers.
'''

# Advantages of Load Balancers
'''
- Improved Scalability: Distributes traffic efficiently, ensuring that new servers can be added easily as demand increases.
- Fault Tolerance: Detects server failures and reroutes traffic to healthy servers, ensuring continuous service.
- Better Resource Utilization: Prevents server overload by balancing the traffic load evenly.
- Enhanced Performance: Reduces the risk of slow response times due to overloaded servers.
'''

# Disadvantages of Load Balancers
'''
- Single Point of Failure: If the load balancer itself fails, it can disrupt the entire system unless high availability and failover mechanisms are in place.
- Increased Complexity: Introducing a load balancer can add another layer of complexity to system architecture and management.
- Cost: Depending on the setup, load balancers (especially hardware or cloud-based ones) can add to operational costs.
'''

# Popular Load Balancers
'''
Nginx:
A highly flexible and widely-used software load balancer.
Can also serve as a reverse proxy, HTTP cache, and web server.

HAProxy:
Known for high performance, reliability, and flexibility, often used in environments requiring advanced traffic management.

AWS Elastic Load Balancer (ELB):
Managed load balancing service in AWS that automatically distributes incoming traffic across EC2 instances.

Traefik:
A modern, open-source reverse proxy and load balancer designed for microservices, with native support for Kubernetes.

F5 Networks:
A hardware-based solution offering advanced load balancing, security, and traffic management for large enterprise environments.
'''




# endregion


1 system design 
2 scaling - horizontal scaling vs vertical scaling
3 capacity extimation
4 http
5 TCP/IP stack
6 what happens when you type google.com in browser?
7 relational databases
8 database indexes
9 NoSQL databases 
10 cache
11 thrashing
12 threads

# region 2 LOAD BALANCING
# -----------------------
- load balancing
- consistent hashing
- sharding


# region 3 DATA STORES
# --------------------
- bloom filters
- data replication
- how are NoSQL optimized
- location based databases
- datbase migrations

# region 4 CONSISTENCY VS AVAILABILITY
# ------------------------------------
- data consistancy
- data consistancy levels
- transaction isolation levels

# region 5 MESSAGE QUEUES
# -----------------------

- message queues
- public-subscriber model 
- event driven ststems
- database as a message queue

# region 6 DEVOPS CONCEPT
# ---------------------
- single point of failure
- containers
- service discovery and heartbeats
- how to avoid cascading failures
- anomaly detection in distribute systems
- distribute rate limiting

# region 7 CACHING
# -----------------
- distribute caching
- content delivery networks
- policies
- replacement policies






# region 9 API GATEWAYS
# region --------------
- how api are designed
- asynchronous APIs




# region AUTHENTICATION
# ------------------------

# authentication va authorization
# https://www.youtube.com/watch?v=B76BhEq1FN8&list=PLA3GkZPtsafZdyC5iucNM_uhqGJ5yFNUM&index=27    
'''
- authentication - who are you? / how to prove your identity?
- authorization - what can you do?

- types of authentication - password based authentication, token based authentication, OAuth,
- other types of authentication - digest authentication, OpenID

- types of authorization - role based access control (RBAC), access control lists (ACLs), rule engines
- other types if authorization - attribute based access control (ABAC), discretionary access control (DAC), mandatory access control (MAC), rule-based access control (RBAC), OAuth (Authorization Framework), API Key-based Authorization, Attribute-Based Access Control (ABAC) with Role Hierarchy, Time-based Access Control, Contextual Access Control (Context-Aware)
'''





# Password-based Authentication
'''
- User provides a username and password
- How it works:
    The user enters a password.
    The system checks if the password matches the stored hash in the database.
    If they match, access is granted.
- Drawbacks:
    Vulnerable to brute force attacks, phishing, and weak password usage.
    Requires strong password management.
Enhancements:
Password Hashing: Hashing passwords (e.g., bcrypt, Argon2) to ensure they aren't stored in plaintext.
Salting: Adding random data to passwords before hashing to prevent rainbow table attacks.
'''

# Two-Factor Authentication (2FA)
'''
- Requires both password and an additional factor (e.g., OTP)
- How it works:
    First factor: Something the user knows (e.g., password).
    Second factor: Something the user has (e.g., a one-time password (OTP) sent to a mobile device or email, or an authentication app).
- Drawbacks:
    May be inconvenient for users.
    Relies on the security of the second factor (e.g., SMS could be intercepted).
- Enhancements:
    Using time-based OTPs (TOTP) with apps like Google Authenticator or Authy.
    Push notifications to an app like Duo Security.
'''

# Multi-Factor Authentication (MFA)
'''
- Requires multiple forms of authentication
- How it works:
    First factor: Something the user knows (e.g., password).
    Second factor: Something the user has (e.g., OTP or smartcard).
    Third factor: Something the user is (e.g., biometrics).
- Drawbacks:
    Can be more complex and less user-friendly.
    May require additional infrastructure or hardware.

'''

# Biometric Authentication
'''
- uses unique physical or behavioral characteristics of the user, such as fingerprints, face recognition, or voice recognition, to authenticate.
- How it works:
    The user provides a biometric input (e.g., scanning a fingerprint).
    The system compares the input against stored biometric data to verify identity.
- Drawbacks:
    Privacy concerns related to storing biometric data.
    Accuracy can be impacted by environmental factors (e.g., dirty fingerprints, poor lighting).
- Examples: Fingerprint scanners, facial recognition, retina scans, voice recognition.
'''

# Token-based Authentication
'''
- Uses tokens (e.g., JWT) for stateless authentication
- How it works:
    The user logs in with a username and password (or via 2FA).
    The server generates a token (JWT) that includes the user's credentials and expiry time.
    The token is sent to the client, and the client includes it in the header of subsequent requests to authenticate.
- Drawbacks:
    Tokens can be intercepted if not transmitted securely.
    Tokens must be properly validated on the server to avoid impersonation.
- Example: JWT used in RESTful APIs for stateless authentication.
'''

# OAuth Authentication
'''
- an authorization framework that allows third-party services to exchange user information without sharing credentials.
- How it works:
    The user authenticates with a third-party identity provider (e.g., Google, Facebook, GitHub).
    The identity provider sends an authorization code or access token to the requesting service.
    The service uses the token to access the user's information.
- Drawbacks:
    It requires external identity providers, and user trust is necessary.
    Misconfiguration or poor token management can lead to security issues.
- Examples: Logging into websites with Google/Facebook accounts.
'''

# OpenID Connect (OIDC)
'''
- Layer on top of OAuth for identity verification
- How it works:
    It involves authentication with an identity provider (IDP) and issuing an ID token (often JWT).
    The system verifies the ID token to authenticate the user.
- Drawbacks:
    Like OAuth, it requires trust in the identity provider.
    Mismanagement of tokens can lead to security risks.
- Example: Google authentication via OpenID Connect.
'''

# Certificate-based Authentication
'''
- uses public key infrastructure (PKI) and digital certificates to authenticate users or systems.
- How it works:
    The user or system presents a certificate (typically an X.509 certificate) that proves their identity.
    The server verifies the certificate against a trusted certificate authority (CA).
- Drawbacks:
    Requires infrastructure to manage certificates.
    Certificates need to be securely stored and regularly updated.
'''
 
# Kerberos Authentication
'''
- Kerberos is a network authentication protocol that uses secret-key cryptography to authenticate clients and services in a secure manner.
- How it works:
    The client requests authentication from a central Key Distribution Center (KDC).
    The KDC provides a Ticket Granting Ticket (TGT) that can be used to request service tickets for specific services.
    The client uses the service ticket to authenticate with the target service.
- Drawbacks:
    Requires a centralized authority and infrastructure.
    Can be complex to configure and maintain.
'''

# SSO (Single Sign-On)
'''
- SSO allows users to authenticate once and gain access to multiple systems or applications without re-authenticating.
- How it works:
    The user logs in once to an identity provider.
    The identity provider issues a token or session to access various applications without requiring login again.
- Drawbacks:
    If the SSO system is compromised, it can expose access to multiple systems.
    If the user forgets their login credentials, access to all systems may be blocked.
'''

# endregion





# region AUTHORIZATION
# ----------------------
# Role-Based Access Control (RBAC)
'''
- RBAC assigns permissions based on the roles assigned to users. A role is typically associated with a set of permissions that define what actions a user can perform within a system.
- How it works:
    Users are assigned roles (e.g., Admin, User, Manager).
    Each role has a specific set of permissions (e.g., "read," "write," "delete").
    Users inherit the permissions associated with their roles.
- Use case:
    Enterprise systems, where different users have different job roles (e.g., an Admin vs. a User).
- Advantages:
    Simplifies management of access control.
    Easier to implement and maintain.
- Drawbacks:
    Can be too rigid for systems with complex or dynamic permissions.
    May require large numbers of roles for more granular access control.
'''


# Attribute-Based Access Control (ABAC)
'''
- ABAC grants access based on attributes (or characteristics) of users, resources, and the environment (e.g., time, location).
- How it work,
    Access is determined by evaluating user attributes (such as department, job title), resource attributes (e.g., document type, classification),and environmental factors (e.g., IP address, time of day,
    Policies are defined to specify what attributes are needed to access a resource.
- Use case:
    Complex systems where access is based on dynamic and fine-grained attributes (e.g., healthcare systems, financial institutions).
- Advantages:
    Highly flexible and scalable for complex systems.
    Can handle more detailed and context-sensitive access controls.
- Drawbacks:
    More complex to implement and manage.
    Requires sophisticated policy definition and management.
'''


# Discretionary Access Control (DAC)
'''
- DAC is a flexible access control model where the owner of a resource determines who can access it.
- How it works:
    Users (resource owners) can grant or revoke access to other users for the resources they own.
    Permissions can be assigned to individual users or groups.
- Use case:
    Common in operating systems (e.g., file system access), where file owners can specify who can read or write to their files.
- Advantages:
    Simple and flexible for individual resource owners to control access.
- Drawbacks:
    Less secure because it allows resource owners to grant permissions that might violate security policies.
    Harder to enforce strict access policies in large systems.
'''


# Mandatory Access Control (MAC)
'''
- In MAC, access to resources is controlled by a central authority, and users cannot alter permissions on resources. Access is granted based on fixed security policies.
- How it works:
    Users are granted access based on system-defined policies (e.g., clearance level, sensitivity of information).
    Resources have labels or classifications (e.g., "Top Secret," "Confidential").
    Users have clearance levels (e.g., "Classified," "Unclassified").
- Use case:
    Highly secure systems, such as government or military systems, where strict access control is required based on sensitivity levels.
- Advantages:
    Strong security, since policies cannot be modified by individual users.
- Drawbacks:
    Less flexibility and user control over resources.
    Complex to manage in dynamic environments.
'''

# Access Control Lists (ACLs)
'''
- An ACL is a list attached to a resource that defines which users or groups are allowed or denied access to that resource.
- How it works:
    Each resource (e.g., file, database table) has an associated ACL, specifying which users or groups can perform what actions (e.g., read, write, execute).
- Use case:
    Common in file systems and network devices.
- Advantages:
    Provides fine-grained control over who can access a resource and what actions they can perform.
- Drawbacks:
    Managing large ACLs can become cumbersome.
    Not as scalable as other systems like RBAC.
'''


# 6. OAuth (Authorization Framework)
'''
- OAuth is an open standard for token-based authorization, allowing third-party services to access user data without sharing credentials.
- How it works:
    The user grants permission to a third-party application (e.g., Google or Facebook) to access specific resources.
    The third-party service receives an access token, which it uses to authenticate and authorize API calls on behalf of the user.
- Use case:
    Used for delegating access, such as signing into an application with Google or Facebook.
- Advantages:
    Secure way to authorize third-party applications without sharing passwords.
- Drawbacks:
    Token management can be complex.
    Potential risks if the authorization server is compromised.
'''

# API Key-based Authorization
'''
- API key-based authorization is used to authenticate API requests by sending a unique API key with each request.
- How it works:
    The client generates an API key (usually after registration).
    The client includes the API key in the headers of requests sent to the server.
    The server checks the key and grants or denies access based on its validity.
- Use case:
    Common in web services and APIs, especially when you need to track or limit access.
- Advantages:
    Simple to implement for accessing APIs.
    Easily managed via environment variables or configuration files.
- Drawbacks:
    API keys are vulnerable if exposed.
    Requires secure storage and transmission methods (e.g., using HTTPS).
'''


# Attribute-Based Access Control (ABAC) with Role Hierarchy
'''
- ABAC with role hierarchy is an extension of ABAC where roles are organized hierarchically. A higher-level role inherits the permissions of lower-level roles.
- How it works:
    Permissions are granted based on attributes, but roles within the system have hierarchical structures (e.g., "Admin" > "Manager" > "Employee").
    A user in a higher-level role automatically inherits the permissions of the lower roles.
- Use case:
    Systems that require dynamic permissions based on roles and attributes.
- Advantages:
    More flexible and dynamic than standard RBAC.
    Easier to manage hierarchical structures in organizations.
- Drawbacks:
    More complex to implement than basic ABAC or RBAC.
'''


# Time-based Access Control
'''
- Time-based access control limits access to resources based on time, such as restricting access to a system during specific hours or days.
- How it works:
    Permissions are granted or denied based on the time of day or the day of the week.
    This can be enforced using policies tied to specific time frames.
- Use case:
    Sensitive environments where access should be restricted outside working hours, such as databases or office systems.
- Advantages:
    Helps restrict access during non-working hours or maintenance windows.
- Drawbacks:
    Can become cumbersome to manage for complex systems.
'''

# Contextual Access Control (Context-Aware)
'''
- Contextual access control grants or denies access based on real-time conditions, such as user behavior, device location, or network context.
- How it works:
    Policies are enforced dynamically based on attributes such as time, location, IP address, device type, or user activity.
- Use case:
    Adaptive security systems where access is granted based on the current context or risk level.
- Advantages:
    Increases security by adapting to changing contexts and conditions.
- Drawbacks:
    Complex to implement and manage.
    Requires real-time context awareness and monitoring.    
'''

# Rule-Based Access Control (RBAC)
'''
- Permissions are granted based on predefined rules and conditions.
- How it works:
    Rules: A rule is defined with conditions (e.g., a user is allowed to access a resource if the current time is between 9 AM and 5 PM).
    Conditions: Rules can depend on various attributes such as user attributes (e.g., role, department), environment (e.g., time, location), or resource attributes (e.g., document type).
    Dynamic Decisions: Access decisions are often made based on real-time evaluation of these rules rather than predefined roles.
- Use case:
    Suitable for systems requiring fine-grained, dynamic access control (e.g., financial systems, dynamic workflows).
- Advantages:
    Flexibility: Rule-based access can accommodate more granular and dynamic conditions for access control.
    Fine-Grained Access: Allows defining complex and specific conditions that can be more flexible than RBAC.
    Adaptability: Changes to access control policies can be made by modifying rules rather than redefining roles.
- Drawbacks:
    Complexity: Rules can become complex and harder to manage if there are many conditions and combinations of rules.
    Performance Overhead: Evaluating multiple conditions or rules for each access request can introduce performance overhead, especially in real-time systems.
    Maintenance: Managing and maintaining a large number of rules can become cumbersome, especially as rules change over time.
'''

# endregion







# region 11 SYSTEM DESIGN TRADEOFFS
# region --------------------------
- pull vs push
# memory vs latency
'''
- More memory (caching) reduces latency (faster response).
- Less memory = more computation/disk access = higher latency.
Trade-off: Store precomputed results (increase storage) vs. Compute on-demand (reduce storage but increase CPU usage).

| More Memory                   | Less Memory                  |
|--------------------------     |------------------------------|
| Faster response (low latency) | Saves cost/resources         |
| Higher infra cost             | Slower system                |
'''


# - throughput vs latency
'''
Throughput: How much you can process in unit time (per second).

Latency: How fast a single request completes.

Trade-off: Optimizing for one can reduce the other.

| High Throughput          | Low Latency                  |
|--------------------------|------------------------------|
| Handles many users       | Fast for individual users    |
| May queue/delay requests | May limit total volume       |
'''
# - consistency vs availability
'''
Consistency: All nodes have same data.

Availability: System is always responsive.

| Consistency             | Availability                 |
|--------------------------|------------------------------|
| Accurate data            | Always accessible            |
| Possible downtime        | May return stale data        |
'''
# latency vs accuracy
'''
Real-time = low latency but possibly approximate/incomplete results.

Accurate results = higher latency (more processing time).

| Low Latency             | High Accuracy                |
|--------------------------|------------------------------|
| Fast but rough results   | Slower but precise           |
| Used in predictions, ML  | Used in financial reports    |
'''

# SQL vs NoSQL databases
'''
| SQL (Relational)        | NoSQL (Non-relational)       |
|--------------------------|------------------------------|
| Structured schema        | Flexible, schema-less        |
| Strong consistency       | Scales easily (horizontally) |
| Used for banking, ERP    | Used for big data, real-time apps |

'''


# rest vs rpc
'''
| REST                    | RPC                          |
|--------------------------|------------------------------|
| Standard HTTP, human-readable | Compact, fast, binary (like gRPC) |
| Language-agnostic       | Language-specific sometimes  |
| Good for public APIs     | Good for internal services   |

'''
# strong vs eventful consistency
'''
Trade off:
Strong consistency often requires tight coordination across nodes, limiting scalability.
Relaxing consistency (eventual consistency) can allow for greater scalability.

| Strong Consistency       | Eventual Consistency         |
|--------------------------|------------------------------|
| All users see same data  | May take time to sync        |
| Slower writes            | Fast, scalable               |
| Banking systems          | Social feeds, DNS            |
'''
# vertical vs horizontal scaling
'''
| Vertical Scaling         | Horizontal Scaling           |
|--------------------------|------------------------------|
| Add power to one machine | Add more machines            |
| Simple but limited       | Scalable but complex         |
'''
# stateful vs stateless design
'''
| Stateful                 | Stateless                   |
|--------------------------|------------------------------|
| Server remembers client state | Server doesn’t remember anything |
| Harder to scale          | Easier to scale (like REST) |
| Used in games, sessions  | Used in APIs, microservices |
'''
# read vs write through cache 
'''
| Read-through            | Write-through               |
|--------------------------|------------------------------|
| Lazy loading             | Consistent cache             |
| Cache may miss initially| Higher write latency         |

'''
# synchronous vs asynchronous 
'''
| Synchronous              | Asynchronous                 |
|--------------------------|------------------------------|
| Waits for response       | Doesn’t wait                 |
| Simple to debug          | Better performance/scaling  |
| Used in simple apps      | Used in queues, emails       |
'''
# batch vs stream processing
'''
| Batch Processing         | Stream Processing            |
|--------------------------|------------------------------|
| Process large data chunks | Process data in real-time    |
| Slower, but efficient    | Fast, but complex            |
| Used in reports          | Used in fraud detection, live analytics |
'''
# long polling vs websockets
'''
| Long Polling             | WebSockets                   |
|--------------------------|------------------------------|
| Client asks repeatedly   | Full-duplex connection       |
| Higher overhead           | Real-time communication      |
| Used where WebSocket not available | Used in chat, games   |
'''
# normalization vs denormalization
'''
Trade-offs:
Optimizing for read (e.g., denormalization) may make writes slower or more complex.
Optimizing for write (e.g., normalization) can make reads slower.

| Normalization            | Denormalization             |
|--------------------------|------------------------------|
| Removes redundancy        | Duplicates data for speed   |
| Saves space, avoids errors| Faster reads, slower writes |
| Used in OLTP (writes)     | Used in OLAP (reads, reports)|
'''
# security vs usability
'''
Trade off:
Stronger security often makes systems harder to use.
Easier user experience may expose more attack vectors.
'''
# simplicity vs flexibility
'''
Simple systems are easier to understand and maintain but might not cover all use cases.

Flexible systems can adapt to more scenarios but are harder to build and maintain.
'''
# modularity vs performance
'''
Modular (decoupled) design helps maintenance and scalability.
But it can introduce performance overhead due to abstractions or service boundaries.
'''
# endregion

# region 12 PRACTICE PROBLEMS
# region --------------------
live straming app
instagram
tinder
whatsapp
tiktok
system design of an online coding judge - part 1
system design of an online coding judge - part 2
UPI payments
IRCTC
netflix video onboarding pipelines
doordash
amazon online shops
google maps
gmail
chess website
UnboundLocalErrorgoogle docs
stock exchange

whatsapp
https://www.youtube.com/watch?v=QhFvII571Lc




# region 13 ADDITIONAL RESOURCES
# --------------------------------
interview ready course 

github page
https://github.com/InterviewReady/system-design-resources
https://github.com/InterviewReady/Low-Level-Design

designing data-intensive applications

# endregion

# region DOUBTS 
# ---------------
'''- sytem desin types vs architectural patterns
- HLD vs  LLD ?? 
- monolithic/centralized/trivial architecture vs distribute/microservices architecture

- Latency  (complexity delay + netword delay)- caching, CDN, upgrading systems
- throughput - volume of work/information flowing through a system
- availabilty - how long a system is operational, replication(redundancy + synchronous), redundancy 
- consistancy - data integrity, consistency, consistency model, dirty read, types (strong, eventual consistency, weak consistancy)
- CAP theorem - consistency, availability, partition tolerance






- Lamport logical clock - 
- scaling - vertical scaling vs horizontal scaling 
- redundancy (active vs passive) vs replication (redundancy + synchronization, active & passive)
- load balancers - load balancers algo
- cacheing - in-memory/local cache (memory cache) , distribute/external cache (redis)
- cache vs cdn, cache miss
- cache eviction techniques - LRU, LFU, MRU, LIFO, FIFO, RR
- File based storage system 
- can rdbms scale horizontaly 
- types of NoSQL databases - key value database, document database, columnar database, graph database
- polyglot persistence
- denormalization in rdms
- how does indexing work in rdbms
- synchronous communication
- asynchronous communication
- message based commiunication - produce, consumer,agent, types - P2P model, public subscriber model, 
- web server - push, pull/polling, long polling, socket, server sent event
- communication protocols
- REST API, SOA, microservices architecture, tier architecture - web application, REST api, SOA, 
- authentication vs authorization - who are you, what can you do
- basic authentication - 
- token based authentication
- OAuth authentication
- Forward proxy and reverse proxy
- URL shortner
- dropbox 



'''

