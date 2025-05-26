

# 1. SOLID Principles (for OOP)
'''
S – Single Responsibility Principle (SRP)
A class should have only one reason to change.

O – Open/Closed Principle
Software entities should be open for extension, closed for modification.

L – Liskov Substitution Principle
Subtypes must be substitutable for their base types.

I – Interface Segregation Principle
Clients should not be forced to depend on interfaces they do not use.

D – Dependency Inversion Principle
Depend on abstractions, not concrete implementations.
'''
# 2. DRY (Don't Repeat Yourself)
'''
Avoid code duplication by abstracting reusable logic.
'''

# 3. KISS (Keep It Simple, Stupid)
'''
Keep the design as simple as possible. Simpler systems are easier to understand and maintain.
'''

# 4. YAGNI (You Aren't Gonna Need It)
'''
Don't add functionality until it's necessary.
'''

# 5. Separation of Concerns (SoC)
'''
Break the system into distinct features that overlap as little as possible.
'''

# 6. High Cohesion, Low Coupling
'''
Cohesion: Keep related code together.
Coupling: Reduce dependencies between modules.
'''

# 7. Law of Demeter (LoD) – “Don’t talk to strangers”
'''
A method should only call methods of:
Itself
Its parameters
Any objects it creates
Its own fields
'''

# 8. Composition over Inheritance
'''
Favor using objects with desired behavior over inheriting from a base class.
'''

# 9. Encapsulate What Varies
'''
Hide the parts of the code that tend to change behind stable interfaces.
'''

# 10. Program to an Interface, Not an Implementation
'''
Rely on abstractions rather than concrete implementations.
'''

# 11. Inversion of Control (IoC)
'''
Move control of dependencies outside the class (e.g., via DI frameworks).
'''

# 12. Dependency Injection (DI)
'''
Provide dependencies from outside rather than hardcoding them inside.
'''

# 13. Principle of Least Astonishment
'''
The code should behave in a way that least surprises the developer/user.
'''

# 14. Information Hiding
'''
Hide internal details and expose only what’s necessary through public interfaces.
'''

# 15. Design by Contract (DbC)
'''
Define clear preconditions, postconditions, and invariants for software modules.
'''

# 16. Tell, Don't Ask
'''
Tell objects what to do, instead of asking for their data and acting on it yourself.
'''

