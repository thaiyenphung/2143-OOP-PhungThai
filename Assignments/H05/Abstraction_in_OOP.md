# Part A: Conceptual Questions
## 1. Definition
- **Abstraction** in OOP means focusing on **what an object does, not how does it**. It hides complex internal details and shows only the **essential features and functionality** that users need to interact with.
## **Real-World Analogy**
**A TV Remote**: 
- We press a button to turn it on or change between channels
- We don't need to know how the remote sends signals to the TV or how the electronics work inside

## 2. Abstraction vs. Encapsulation
### Abstraction
- Focuses on **reducing complexity** by showing only essential features or functionalities to the user and **hiding the internal details**. It's about defining **what** an object does rather than **how** it does it.
- **Example:** `drive()` method in a `Car` class gives the user the ability to "drive" the car (call `drive()`, without needing to understand how the engine works
  
### Encapsulation
- Focuses on **bundling data and methods together**, and **restricting direct access** to the internal workings of an object. It uses **access specifiers (`private`, `protected`, `public`)** to **control how data is accessed or modified**. It's about the **implementation** or **how** the object maintain control over its data.
- **Example:** `speed` attribute of `Car` class is `private`, user must use `getSpeed()` and `setSpeed()` to interact with it. This prevents invalid or unintentional changes.

### Why People Confuse Them? 
- Because both involve **hiding details**, just in **different ways**:
    - **Abstraction** hides **unnecessary complexity** from the user
    - **Encapsulation** hides **data and implementation** to protect it and control access
- **Abstraction** defines **what we can do**, and **Encapsulation** ensures **how it's done safely.**
