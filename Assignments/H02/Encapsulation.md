# Encapsulation

# Part A: Conceptual Questions

## 1. Definition
- **Encapsulation** bundles data (attributes) and methods that operate on that data in a single unit, usually a class.
- It **restricts direct access** to an object's data and only allows modifications through controlled methods.
- By **hiding the object's internal implementation**, **encapsulation** prevents unintended interference and maintains code security.

**Example**:
- **Encapsulation** works like how schools manage student grades.
- Student can view their grade but can't change it themselves.
- Only authorized people like teachers and administrators can update it, and they have specific rules to follow when making changes.

```c++
class Student
{
private:
    int grade; // Can't be changed directly

public:
    Student(int g)
    {
        setGrade(g);
    }

    void setGrade(int g)
    { // Controls how grades are set
        if (g >= 0 && g <= 100)
            grade = g;
         else 
            grade = 0; 
    }

    int getGrade() const
    { 
        return grade;
    }
};
```

- Getter `getGrade()` - allows students to view their grade
- Setter `setGrade()` - only authorized methods can modify grades
- Private data `grade` - meaning it cannot be modified directly from outside the class, prevents direct modification, so students can't just give themselves a 100
  - If `grade` is made **public**, anyone could directly modify it like
    
    ```c++
    s1.grade = 100; // unintended change, won't compile
    ```
---

## 2. Visibility Modifiers

|Modifier| Description | Benefit | Drawback|
|--------|-------------|---------|---------|
|`public`| Members are accessible from everywhere in the program| **Increases flexibility**: external code can directly use class memebers| **Reduces encapsulation**: data can be modified unexpectedly, leading to unintended behavior|
|`private`| Members are only accessible within the same class| **Ensure data security and integrity**: only controlled modifications are allowed| **Reduces flexibility**: cannot be accessed by derived classes|
|`protected`| Members are accessible within the same class and derived class| **Balances security and flexibility**: allows controlled inheritance| Can still lead to unintended modifications in derived classes, **potentially breaking encapsulation**|

**Example:**

**A game where every character has Health Points HP:**
- A player's HP can change when they take damage or heal
- An enemy can reduce the player's HP when attacking
- However, the player shouldn't be able to change their own HP (like setting it to 1000 to cheat)
  
To make this work:
- HP is **protected**: only the player or enemy classes can modify it
- HP is **not public**: prevents player from typing a command to directly change their HP

```c++
// Base class: Character
class Character
{
protected: // Accessible in derived classes but not outside
    int health;

public:
    Character(int hp) { health = hp; }

    void showHealth()
    {
        cout << "Health: " << health << endl;
    }
};

// Derived class: Player
class Player : public Character
{
public:
    Player(int hp) : Character(hp) {}

    void takeDamage(int damage)
    {
        health -= damage; // Allowed because health is `protected`
        cout << "Player took " << damage << " damage. Remaining health: " << health << endl;
    }
};

// Derived class: Enemy
class Enemy : public Character
{
public:
    Enemy(int hp) : Character(hp) {}

    void attack(Player &p)
    {
        cout << "Enemy attacks player!" << endl;
        p.takeDamage(10);
    }
};
```
---

## 3. Impact on Maintenance
- **Data hiding:** encapsulation **hides internal data** from external access, preventing unintended modifications. Using access specifiers, we control what parts of a class are exposed.
- Allows **related data and behavior** to be grouped inside a class, making the code **easier to read, maintain, and test.**
- Allows **internal changes without affecting external code** As long as the public interface stays the same, we can modify the internal logic without breaking the rest of the program.
- Ensures that **developers can work on different classes independently.** Since each class hides its details, team members don't have to worry about unintended conflicts.

### Scenario: How Code could Break if Internal Data is made Public
- A traffic light system that controls signals at an intersection. The system has an internal timer that determines when the light should turn red, yellow, or green. 
- If the timer value is made public, any part of the program or a bug could change it directly, leading to dangerous situations.
    - A faulty program sets the timer to 0, causing the light to change to red instantly without warning, which could lead to accidents as cars wouldn't have time to stop.
    - Another part of the program accidentally sets all lights to green at the same time. Multiple lanes start moving at once, leading to accidents.
    - A hacker or malfunction modifies the timers randomly, making lights change unpredictably.

## 4. Real-World Analogy
**A vending machine:**
- **Public Interface:**
    - The buttons to select the product
    - The coin slot and card reader
    - The display screen showing the price and product availability
    - The dispensing area where you receive the item
- **Private Implementation:**
    - The internal wiring and software that process the payment
    - The motor storage mechanism that keeps and releases the products
    - The security system that prevents people from tampering with the machine

### Why are they Hidden?
- Prevents manipulations: if anyone could access the machine's internals, they could take products without paying
- Protects functionality: users don't need to know how the motors work. They just press a button and it functions as expected
- Simplifies interaction: if customers have to manually enter commands to dispense a snack, it is confusing and inefficient
---

# Part B: Small-Class Design
## 1. Class Skeleton

```c++
class BankAccount
{
private:
    double balance;
    string accountNumber;
public:
    // Constructor
    BankAccount(string accNum, double initialBalance)
    {
        accountNumber = accNum;
        if (initialBalance >= 0)
            balance = initialBalance;
        else
            balance = 0;
    }

    // Public method to deposit money
    void deposit(double amount)
    {
        balance += amount;
        cout << "New balance is $" << balance << endl;
    }

    // Private method to withdraw money
    void withdraw(double amount)
    {
        if(amount <= balance)
        {
            balance -= amount;
            cout << "New balance is $" << balance << endl;
        }
        else
            cout << "No funds to withdraw." << endl;
    }

    // Public method to check balance
    double getBalance()
    {
        return balance;
    }
};
```
---

## 2. Encapsulation Justification
**`private` Data Members:**
- `balance`: prevent direct modification of the account balance. This ensures that deposits and withdrawals only happen through controlled methods, prevents behaviors like setting a negative balance.
- `accountNumber`: protect sensible account information. If it is public, external code can change the account number, leading to mix-ups and unauthorized modifications.

**`public` methods:**
- `deposit(double amount)`:
    - Acts as a controlled method, ensures that only valid deposits affect the balance.
    - Prevents incorrect transactions (`myAccount.balance += 100;` is invalid)
- `withdraw(double amount)`:
    - Ensures that the withdrawal amount is not greater than the current balance to prevent overdrafts.
    - Ensures that only valid withdrawals are processed, preventing tempering with account balance.
- `getBalance()`:
    - Users can only view the balance, external code cannot modify `balance` directly.
    - Allows secure access to the balance without exposing it for unintended changes.
  
## 3. Documentation
**Why other developers must not directly manipulate the `balance`:**
- `balance` is made private so that it can only be accessed using methods within the class.
- The only way to increase the balance is through the `deposit(double amount)` method, directly modifying the balance is not allowed
- Balance decreases only when users withdraw the money using the `withdrawal(double amount)` and the amount of withdrawal cannot be greater than the current balance.
---

# Part C: Reflection & Short-Answer
## 1. Pros and Cons
**Pros:**
- **Data integrity and security:** prevents accidental or unauthorized modifications by ensuring all data changes go through controlled methods.
- **Easier maintenance & debugging:** since data can only be modified through methods within the class, bugs and errors are easier to track and fix, which is good for code maintainability.

**Cons:**
- **Increase code complexity**: adding getter and setter methods makes the code larger and more complex compared to directly accessing variables.

## 2. Encapsulation vs. Abstraction:
- **Encapsulation** focuses on restricting access to data by bundling it with controlled methods within a class. It protects the internal data from outside use, preventing unauthorized modifications.
- **Abstraction** hides unnecessary implementation details of a complex object from users, allowing a simpler interface for users to interact with an object without knowing its internal workings.

### Why Encapsulation and Abstraction are forms of Information Hiding:
- **Encapsulation** hides implementation details at the data levels (private variables, controlled access via methods).
- **Abstraction** hides complex implementation details while exposing only the functionality, allowing users to interact with an object without needing to understand its internal workings.

## 3. Testing Encapsulation Classes
**Test Through Public Method:**
- Example: test if `deposit(100)` correctly increases the balance by calling `getBalance()`
  
**Check Expected Outcome:**
- Example: ensure public methods like `deposit` increase balance, `withdraw` deduct balance correctly, and withdrawing more than the balance fails
    
