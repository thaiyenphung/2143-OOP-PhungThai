# Part A: Conceptual Questions
## 1. Composition vs. Aggregation
### Definition:
- **Composition** is a **"has-a" relationship** where one class **completely owns** another class. If the owner is destroyed, the contained object is also destroyed. This implies **strong ownership**.
  - **Example:** A `Car` **has an** `Engine`. If `Car` is destroyed, the `Engine` is also destroyed
    
  ```c++
  class Engine {
  public:
      void start() { cout << "Engine started."; }
  };

  class Car {
  private:
      Engine engine; // Strong ownership: Car contains Engine directly

  public:
      void startCar() { engine.start(); }
  };
  ```
  ---

- **Aggregation** is also a **"has-a" relationship" but it's **weaker**. This container **uses** the object, but **does not own it**. The contained object exists **independently** of the container.
    - **Example:** A `Library` contains many `Books`, but the books can exist independently of the library as they might belong to another library, get transferred, or be stored in the storage. If the `Library` is destroyed, `Book` objects still exist elsewhere.
      
    ```c++
    class Book {
    public:
        string title;
        Book(string t) : title(t) {}
    };

    class Library {
    private:
        Book* books[10];  // Aggregation: array of pointers (not owned)
        int count = 0;

    public:
        void addBook(Book* book) {
            if (count < 10)
            books[count++] = book;
        }

        void showBooks() {
            for (int i = 0; i < count; ++i)
                cout << books[i]->title << endl;
        }
    };
    ```
    ---

## 2. When to Use
### Composition
**In a game**, a `Player` that has **attributes** (not base or derived classes because they represent components of a character) like `Health`, `Weapon`
- A `Player` **has a** `Health` object to manage health points
- A `Player` **has a** `Weapon` object to attack
  
**Composition** offers a **modular and flexible system**. For example, if a player needs to change their weapon from gun to knife, we can just replace the `Weapon` object without needing to modify the class hierarchy. **Compostion** helps avoid the rigid structure and tight coupling that comes with **inheritance.**

---

### Aggregation
**In a hospital:**
- A `Doctor` has multiple `Patients`
- A `Patient` may see multiple doctors (a family doctor and a specialist)
- If a `Doctor` retires or leaves the hospital, the `Patient` still exists and continues to see other doctors.

A `Doctor` **has a relationship** with `Patients` but **does not own** them.\
`Patients` exist **independently**, they are not deleted or destroyed when the doctor is
  
## 3. Differences from Inheritance
**Inheritance ("Is-a")**
- **Inheritance** creates a hierarchical relationship between classes, where a subclass derives (extends) from a base class, meaning the subclass is a **specific type** of the base class
- **Example**: A `Cow` "is-a" `Animal`, it inherits behaviors like makeSound() from the `Animal` class

**Composition/ Aggregation ("Has-a")**
- **Composition and Aggregation** create an ownership relationship where one class contains or is associated with another class.
    - **Composition** implies strong ownership: if the container is destroyed, so is the contained object
    - **Aggregation** implies weaker coupling: the associated object can exist independently

### Why Favor Composition Over Inheritance
**1. More flexible**
- **Composition** allows us to **replace or modify components** independently of the main class. This promotes **modularity** and makes systems easier to develop.

**2. Avoiding Inheritance Pitfalls**
- **Inheritance** can lead to **tight coupling** between base and derived classes
- Changes in the base class may unintentionally affect all subclasses, leading to fragile designs and harder maintenance.

**3. Reusability**
- Components like `Weapon` or `Health` can be reused across multiple classes, promoting **code reuse**

**4. Follows the Open-Closed Principle**
- **Composition** supports the Open-Closed Principle: a class should be **open for extension** (we can add new features by plugging in new components), but **closed for modification** (we don't have to change the existing code to do it)
  
---

## 4. Real-World Analogy 
**A School**
- **Composition: School has Classrooms**
  - `School` **has-a** number of `Classroom` objects
  - If the school is torn down, so is the classroom (they don't exist on their own)
  - This is a **strong ownership relationship**
    
- **Aggregation: School has Students
  - `School` **has-a** group of `Students`
  - But a student can transfer to another school or attend a different school to earn extra credits
  - A student can still exist **independently** if the school is closed (**loose relationship**)

### Why These Distinctions Matter in Code
- Understanding ownership is important for managing object lifecycles:
    - With **composition**, the parent object handles both the creation and destruction of its parts
    - With **aggregation**, the associated objects are independently managed, as they are not owned.
- Makes code clearer, safer, and maintainable:
    - Won't accidentally delete a shared object
    - Easier to determine which class is responsible for specific functionality and resource management

---

# Part B: Minimal Class Design
**1. Composition (Strong "has-a": Address belongs to Person)**
```c++
class Address {
private:
    string street, city;

public:
    Address(string s, string c) : street(s), city(c) {}
    void show() { cout << street << ", " << city << endl; }
};

class Person {
private:
    string name;
    Address address;  // Composition: Address is part of Person

public:
    Person(string n, string s, string c) : name(n), address(s, c) {}

    void showInfo() {
        cout << "Name: " << name << " , Address: ";
        address.show();
    }
};
```
- `Address` is created **inside** `Person` constructor
- When `Person` is destroyed, so is `Address`
---

**2. Aggregation (Weak "has-a": Address can exist independently without Person)**
```c++
class Address {
public:
    string street, city;
    Address(string s, string c) : street(s), city(c) {}
    void show() { cout << street << ", " << city << endl; }
};

class Person {
private:
    string name;
    Address* address;  // Aggregation: just a reference
public:
    Person(string n, Address* a) : name(n), address(a) {}

    void showInfo() {
        cout << "Name: " << name << "\nAddress: ";
        address->show();
    }
};
```
- `Address` is created externally, `Person` holds a **reference** to it
- When `Person` is deleted, `Address` still exists
---

# Part C: Reflection & Short Discussion
## Ownership & Lifecycle
### 1. Composition
- The **child object is fully owned** by the parent
- If the parent is destroyed or deallocated, the child is also destroyed automatically because their lifecycle is tight strongly together

### 2. Aggregation
- The child object **exists independently** of the parent
- Even if the parent is destroyed, the child can continue to exist since it's **not owned or managed** by the parent
---

## Advantages & Pitfalls
### Advantages
- **Composition** offers full control over object lifecycles.
- It ensures that child objects are cleaned up automatically when the parent is destroyed, reducing the risk of **memory leaks** in strong relationships

### Pitfalls
- Using composition instead of **aggregation** can lead to **unintended deletion or recreation** of shared objects that should remain independent.
---

## Constrast with Inheritance
**1. "Has-a" Relationship (Composition/ Aggregation)**
- Focuses on building systems by combining objects with specific roles (ex: a `Car` has an `Engine`)
- Promotes modularity, flexibility and code reuse

**2. "Is-a" Relationship (Inheritance)**
- Defines a hierarchical relationship where one class is a **specialized type** of another (ex: `Cow` is an `Animal`, inherits traits like `makeSound()` or `eat()`)
---

### Why Avoid Inheritance When Possible
- **Inheritance** creates **tight coupling** between the **subclass** and **base class**, which can make code more difficult to extend, easier to break with changes, and less reusable across different use cases.
- By favoring **composition** or **aggregation**, behaviors can be added or modified without changing the inheritance hierarchy, offering designs that are easier to maintain.
