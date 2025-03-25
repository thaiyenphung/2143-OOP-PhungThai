## 1. Encapsulation in Java vs. C++
- Both Java and C++ use visibility modifiers to carry out encapsulation, but they differ slightly in their **implementation** and **scope**
### Java:
- `public`: accessible from any other class
- `protected`: accessible from within the same package and by subclasses
- default (no modifiers): accessible only within the same package (package-private)
- `private`: accessible only within the same class

### C++
- `public`: accessible from anywhere
- `protected`: accessible within the class and its derived class
- `private`: accessible only within the class itself
    - the default access level for class members is `private`
- C++ offers **`friend` functions and classes**, which can access `private` and `protected` members, **a feature not available in Java**

## 2. Encapsulation in Large-Scale System
**Article**: [Source Code Security Best Practices to Protect Against Theft](https://www.digitalguardian.com/blog/source-code-security-best-practices-protect-against-theft)

**Key Points:**
- **Limit access to source code**:
  - only give access to people who actually need it, just like using private in a class.
- **Use secure version control (like Git)**:
  - helps control who can see or change parts of the code, similar to keeping class internals protected.
- **Follow the “least privilege” rule**:
  - don’t give full access to everyone, only what’s necessary, like exposing only public methods in a class.
- **Code reviews and audits**:
  - make sure sensitive parts of the code aren’t exposed, just like keeping internal logic hidden from other parts of a program.
- **Clear boundaries between systems**:
  - like separating class responsibilities, this helps protect each system’s inner workings from being misused or accessed directly.
