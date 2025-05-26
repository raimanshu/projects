# 1. API Gateway Pattern
'''
A single entry point for all clients.

Handles:

Routing

Authentication/Authorization

Rate limiting

Load balancing

Helps reduce complexity for client apps.

Tools: Kong, NGINX, AWS API Gateway, Apigee
'''
2. Backend for Frontend (BFF)
A custom API gateway tailored to each frontend (web, mobile, etc.).

Prevents frontend-specific logic from polluting backend services.

Provides optimized APIs per client.

# 3. Service Discovery/Registry
'''
Allows services to dynamically find and communicate with each other.

Avoids hardcoding service URLs.

Two types:

Client-side discovery (e.g., Netflix Eureka)

Server-side discovery (e.g., AWS Load Balancer)
'''
4. Service Mesh
A dedicated infrastructure layer for service-to-service communication.

Handles:

Routing

Observability

Security (mTLS)

Resiliency (retries, timeouts)

Tools: Istio, Linkerd, Consul Connect

# 5. Circuit Breaker
'''
Prevents cascading failures by stopping calls to failing services temporarily.

Trips when failure threshold is reached.

Automatically resumes after timeout.

Libraries: Netflix Hystrix (deprecated), Resilience4j, Istio
'''
# 6. Retry Pattern
'''
Retries failed requests with backoff strategy.

Useful for transient failures (e.g., network issues).
'''
7. Timeouts
Set time limits for external calls to prevent the calling service from hanging.

Must be combined with retries and circuit breakers.

8. Rate Limiting / Throttling
Controls the number of requests a service can handle.

Prevents abuse and ensures fair usage.

# 9. Bulkhead Pattern
'''
Isolates components/resources to limit the impact of failure.

Example: thread pools per service or per function.
'''
# 10. API Aggregator (or Composite Pattern or API Composition Pattern)
'''
One service calls multiple backend services and combines the result into a single response.

Reduces multiple round-trips from clients.
'''
11. Idempotency
Ensure that repeating the same request has the same effect as doing it once (especially POST/PUT).

Prevents accidental duplication due to retries.

# 12. Asynchronous Messaging / Event-Driven API
'''
Services emit and consume events using message brokers (e.g., Kafka, RabbitMQ).

Decouples services and improves scalability.
'''
13. Correlation ID / Distributed Tracing
Add a unique ID to each request to trace it across services.

Important for debugging and observability.

Tools: OpenTelemetry, Zipkin, Jaeger

14. Gateway Aggregation & Transformation
API Gateway not only routes but transforms or aggregates responses.

Useful when clients need combined data in specific formats.

15. Canary Releases & Feature Toggles
Gradually release new APIs to users.

Enables controlled testing and rollback.

# 16 SAGA Pattern
'''
Manage long-lived transactions acrossmultiple microservices by breaking themdown into a sequence of smaller, localtransactions.
'''

# 17 CQRS (Command Query Responsibility Segregation)
'''
CQRS PatternSeparate the read and writeresponsibilities of a system, allowing foroptimized performance and scalability.

'''

# 18 Sidecar Pattern (or Adapter Pattern)
'''
A sidecar container runs alongside the main application, providingadditional functionality.
'''

# 19 Database Per Service Pattern (or Database per Microservice Pattern)
'''
Each microservice has its own dedicateddatabase to ensure loose coupling andautonomy.
'''
# 20 Configuration Extenalization Pattern
'''
Store configuration settings outside thecodebase for easier management andupdates.
'''

# 21 Stangler Fig Pattern
'''
Gradually replace components of a legacysystem with new ones until the old systemis "strangled" and replaced entirely.

'''

# 22 Ladder Election Pattern
'''
Designate a leader among instances of amicroservice for tasks like coordinationand decision-making.
'''


| Pattern                      | Purpose                                   |
| ---------------------------- | ----------------------------------------- |
| API Gateway                  | Entry point, auth, routing, rate-limiting |
| BFF                          | Tailored APIs per client type             |
| Service Discovery            | Dynamic service endpoint resolution       |
| Service Mesh                 | Observability and communication control   |
| Circuit Breaker              | Fail fast to avoid cascading failures     |
| Retry + Timeout              | Handle transient failures gracefully      |
| Rate Limiting / Throttling   | Prevent overload                          |
| Bulkhead                     | Contain failure within isolated areas     |
| API Aggregator               | Combine data from multiple services       |
| Idempotency                  | Avoid duplicate processing                |
| Event-Driven / Async API     | Loosely coupled services                  |
| Correlation ID / Tracing     | Enable debugging and monitoring           |
| Transformation & Aggregation | Shape responses for frontend needs        |
