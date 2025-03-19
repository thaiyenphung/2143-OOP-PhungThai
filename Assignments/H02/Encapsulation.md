# Encapsulation

## Part A: Conceptual Questions

**1. Definition**
- **Encapsulation** bundles data (attributes) and methods that operate on that data in a single unit, usually a class.
- It **restricts direct access** to an object's data and only allows modifications through controlled methods.
- By **hiding the object's internal implementation**, **encapsulation** prevents unintended interference and maintains code security.

**Example**:
- Encapsulation works like how schools manage student grades. Student can view their grade but can't change it themselves. Only authorized people like teachers and administrators can update it, and they have specific rules to follow when making changes.

```c++
class Student {
private:
    int grade; // Private: Can't be changed directly

public:
    Student(int g) {
        setGrade(g);
    }

    void setGrade(int g) { // Controls how grades are set
        if (g >= 0 && g <= 100) {
            grade = g;
        } else {
            grade = 0; // Default value if invalid
        }
    }

    int getGrade() const { // Read-only access
        return grade;
    }
};

int main() {
    Student s1(85);

    cout << "Your grade: " << s1.getGrade() << endl; // Can view grade

    // Can't cheat by setting an invalid value:
    s1.setGrade(150);
    cout << "Updated grade: " << s1.getGrade() << endl; // Still valid (0-100)

    return 0;
}
```

- Getter `getGrade()` - allows students to view their grade
- Setter `setGrade()` - only authorized methods can modify grades
- Private data `grade` - meaning it cannot be modified directly from outside the class, prevents direct modification, so students can't just give themselves a 100
  - If `grade` is made **public**, anyone could directly modify it like
    
    ```c++
    s1.grade = 100; // unintended change, won't compile
    ```
    
**2. Visibility Modifiers**

|Modifier| Description | Benefit | Drawback|
|--------|-------------|---------|---------|
|`public`| Members are accessible from everywhere in the program| **Increases flexibility**: external code can directly use class memebers| **Reduces encapsulation**: data can be modified unexpectedly, leading to unintended behavior|
|`private`| Members are only accessible within the same class| **Ensure data security and integrity**: only controlled modifications are allowed| **Reduces flexibility**: cannot be accessed by derived classes|
|`protected`| Members are accessible within the same class and derived class| **Balances security and flexibility**: allows controlled inheritance| Can still lead to unintended modifications in derived classes, **potentially breaking encapsulation**|

**Example:**

A game where every character has Health Points HP:
- A player's HP can change when they take damage or heal
- An enemy can reduce the player's HP when attacking
- However, the player shouldn't be able to change their own HP (like setting it to 1000 to cheat)
  
To make this work in programming:
- HP is **protected**: only the player or enemy classes can modify it
- HP is **not public**: prevents player to type a command to directly change their HP
