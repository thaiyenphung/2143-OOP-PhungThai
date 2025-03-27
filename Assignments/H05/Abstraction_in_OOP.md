# Part A: Conceptual Questions
## 1. Definition
- **Abstraction** in OOP means focusing on **what an object does, not how does it**. It **hides complex internal details** and shows only the **essential features and functionality** that users need to interact with.
## **Real-World Analogy**
**A TV Remote**: 
- We press a button to turn it on or change between channels
- We don't need to know how the remote sends signals to the TV or how the electronics work inside

## 2. Abstraction vs. Encapsulation
### Abstraction
- Focuses on **reducing complexity** by showing only essential features or functionalities to the user and **hiding the internal details**. It's about defining **what** an object does rather than **how** it does it.
- **Example:** `drive()` method in a `Car` class gives the user the ability to "drive" the car (calls `drive()`), without needing to understand how the engine works
  
### Encapsulation
- Focuses on **bundling data and methods together**, and **restricting direct access** to the internal workings of an object. It uses **access specifiers (`private`, `protected`, `public`)** to **control how data is accessed or modified**. It's about the **implementation** or **how** the object maintain control over its data.
- **Example:** `speed` attribute of `Car` class is `private`, user must use `getSpeed()` and `setSpeed()` to interact with it. This prevents invalid or unintentional changes.

### Why People Confuse Them
- Because both involve **hiding details**, just in **different ways**:
    - **Abstraction** hides **unnecessary complexity** from the user
    - **Encapsulation** hides **data and implementation** to protect it and control access
- **Abstraction** defines **what we can do**, and **Encapsulation** ensures **how it's done safely.**

## 3. Benefits of Abstraction
**1. Simplifies Collaboration:** 
- Clear interface definitions allow **different teams** to work on separate components **independently** without needing to understand each other's implementation details

**2. Eases Maintenance and Scalability:** 
- Abstraction **conceals changes in the implementation**, allowing the system to be **updated**, **replaced**, or **extended** with minimal impact on existing code.

### How Abstraction Reduce Code Complexity
- **Abstraction** hides unnecessary details and focuses only on essential functionality, allowing developers to work with clean, high-level concepts rather than complex internal logic.
---

# Part B: Minimal Class Example 

```c++
// ABSTRACT BASE CLASS
class BankAccount {
public:
    virtual void deposit(double amount) = 0; // Pure virtual method
    virtual void withdraw(double amount) = 0;
    virtual ~BankAccount() {}
};

// DERIVED CLASS
class SavingAccount : public BankAccount {
public:
    void deposit(double amount) override {
        cout << "Deposit $" << amount << " into savings" << endl;
    }

    void withdraw(double amount) override {
        cout << "Withdraw $" << amount << " from savings." << endl;
    }
};

int main() {
    BankAccount* account = new SavingAccount();

    account->deposit(100.0);
    account->withdraw(60.0);

    delete account;

    return 0;
}
```

> - Pure `virtual` method (`virtual void deposit(double amount) = 0`) is a function in a **base class** that has **no implementation** and must be **overridden** by any **derived class**
> - It makes the base class **abstract**, meaning we **cannot create objects of that class directly** (`BankAccount account;` // ERROR: cannot directly instantiate abstract class)
>     -  Use a **pointer** or **reference** to the **abstract class** — as long as it’s pointing to a concrete **derived class**
---

# Part C: Reflection & Comparison
## 1. Distilling the Essentials
- In `SavingAccount`, we would want to **hide internal details** like:
    - `balanceUpdates`
    - `transactionLogging`
- These would be made `private` or `protected`, so the user only sees **a clean interface** with public methods like `deposit()` or `withdraw()`
- This makes the interface easier for users to use and protects the system from unintended misuse. Users don't need to know **how** the `deposit` is processed, just that it works.

## 2. Polymorphism + Abstraction Together
- When `BankAccount` is defined as an **abstract** class, calling `deposit()` on a `SavingAccount` object through a `BankAccount*` pointer or reference demonstrates **polymorphism**.
- The `deposit()` method in `BankAccount` base class serves as the **abstract interface** (it defines **what** should happen, **not how**), while `SavingAccount` provides the concrete **implementation**.
-	This use of **polymorphism** allows the caller to work with any class that inherits from BankAccount without needing to know the **exact type** of account, making the code **cleaner and more flexible for future changes**.

## 3. Real-World Example
**In healthcare software:**
- A `PatientRecord` interface offers methods like `getVital()` or `patientHistory()`
- The internal processes like data encryption and access control are **hidden** from the user through **abstraction**
- This simplifies the API for healthcare workers using the system, so they can focus on treating patients, not the technical complexities.
