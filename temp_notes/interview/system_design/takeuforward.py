
# https://www.youtube.com/watch?v=43-X22tdxiI&list=PLA3GkZPtsafZdyC5iucNM_uhqGJ5yFNUM&index=1 (Beginner)



# region 1 BASIC
# ----------------
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



# region 8 MICROSERVICES
# region ---------------
- monolithic vs microservices
- how monoliths are migrated


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
- memory vs latency
- throughput vs latency
- consistency vs availability
- latency vs accuracy
- SQL vs NoSQL databases


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





# region 13 ADDITIONAL RESOURCES
-----------------------
interview ready course 
github page
designing data-intensive applications



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

