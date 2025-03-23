# Part A: Conceptual Questions

## 1. Inheritance Definition
- **Inheritance** allows a **subclass** to acquire properties and behaviors (data members and member functions) from a **superclass**, promoting **code reuse** and established relationships between classes.
---

## Inheritance vs. Composition vs. Aggregation
### Composition:
- **Composition** means that one class contains another class as a **member variable** and **is responsible for creating and destroying it**, creating a "has-a" relationship rather than inheriting from a parent class.

```c++
class Engine {
public:
    void start() { cout << "Engine started." << endl; }
};

class Car {
private:
    Engine engine;  // Composition: Car owns Engine
public:
    void startCar() {
        engine.start();
        cout << "Car is moving." << endl;
    }
};

int main() {
    Car myCar;
    myCar.startCar();
    return 0;
}
```
- `Engine` is a **member variable** of `Car` class
- When `Car` is destroyed, so is its `Engine`
- `Car` manages the lifecycle of `Engine`

### Aggregation:
- **Aggregation** also a "has-a" relationship, but **no ownership**. The contained objects exist **independently** and is passed to the containing object. The container neither creates nor destroys the object it holds.
  
```c++
class Student {
public:
    string name;
    Student(string n) : name(n) {}
};

class Course {
private:
    Student* enrolledStudent;  // Aggregation: pointer, no ownership
public:
    Course(Student* student) {
        enrolledStudent = student;
    }

    void showEnrollment() {
        cout << enrolledStudent->name << " is enrolled in the course." << endl;
    }
};

int main() {
    Student s1("Alice"); // instance of Student
    Course c1(&s1);
    c1.showEnrollment();
    return 0;
}
```

- `Student` is created **outside** of `Course`
- `Course` uses a reference or pointer to `Student`
- When `Course` is destroyed, `Student` still exists
---

## 2. Types of Inheritance
### 1. Single Inheritance
- A class inherits from **only one** base class.
- Single inheritance is common when complexity is low
  
```c++
class Animal {
public:
    void breathe() { cout << "Breathing..." << endl; }
};

class Dog : public Animal {
public:
    void bark() { cout << "Barking!" << endl; }
};
```

- a `Dog` is a specific type of `Animal`

### 2. Multiple Inheritance
- A class inherits from **two or more** base classes.
- Useful in systems where a class takes on **multiple roles or capabilities**

```c++
class Printer {
public:
    void print() { cout << "Printing..." << endl; }
};

class Scanner {
public:
    void scan() { cout << "Scanning..." << endl; }
};

class MultiFunctionPrinter : public Printer, public Scanner {
    // Inherits both print() and scan()
};
```
---

### 3. Overriding Methods
- **Method overriding **is a type of **polymorphism** in which we **redefine** the member function of a class that it inherited from its base class, using the **same name, return type, and parameters**. The function signature remains the same, but the working of the function is modified to meet the needs of the derived class.

**Why Overriding a Method instead of Adding a New Method in the Derived class?**
- Because the base class already has the method we need
- To keep consistency: all classes in the family still respond to the same function name, even if they do different things
- To support polymorphism: if we use a base class pointer (or reference), it will automatically call the correct version of the method, the one that matches the actual object type

```c++
class Animal {
public:
    virtual void makeSound() {
        cout << "Animal makes a sound" << endl;
    }
};

class Dog : public Animal {
public:
    void makeSound() override {
        cout << "Dog barks" << endl;
    }
};

int main() {
  Animal* a = new Dog();
  a->makeSound(); // Output: Dog barks
```

### 4. Real-World Analogy
**Real-life Example: Family Inheritance (a parent and a child)**
- The parent has traits such as last name, eye color, hair color
- The child automatically **inherits** these trait from the parent (they are passed down)
- However, the child can also have their own traits (like their own personality or knowledge)

**How This Relates to OOP Inheritance**
|Real-life| OOP Concept|
|---------|------------|
|Parent| Base class|
|Child| Derived class|
|Inherited eye color, name, hair color| Inherited attributes and behaviors|
|Unique personality| Overidden methods|
---

# Part B: 

```c++
// BASE CLASS
class Vehicle {
protected:
    string brand;

public:
    Vehicle(string b) {
      brand = b;
    }

     virtual void drive() {
        cout << brand << " vehicle is driving." << endl;
      }
};

// DERIVED CLASS
class Car : public Vehicle {
private:
    int numDoors;

public:
    Car(string b, int d) : Vehicle(b) {
        numDoors = d
    }

    void drive() override {
        cout << brand << " car with " << numDoors << " doors is driving." << endl;
    }
};

// DRIVER CODE
int main()
{
    Vehicle vhc("Japanese brand");
    Car c("Toyota", 4);

    vhc.drive(); // Output: Japanese brand vehicle is driving.
    c.drivve(); // Output: Toyota with 4 doors is driving.

    return 0;
}
```
---

# Part C: Short Reflection & Discussion

## 1. When to Use Inheritance
**Beneficial Scenario:**
- **Base class:** `Vehicle` has common features (attributes and methods like `speed`, `brand`, `start()`, `stop()`)
- **Derived class:** `Car`, `Bicyle`, `Motocycle`, `SchoolBus` inherit from `Vehicle`, extending or overriding its methods. Each derived class can have a unique functionality like `openTrunk` for `Car` or `openStopSign` for `SchoolBus`

**Overkill Scenario:**
**Making a `Student` Inherit from a `Classroom`
- `Student` has `name`, `grade`, `study()`, `takeTests()`
- `Classroom` has `roomNumber`, `whiteboard`, `numDesks`, or `listOfStudents`
- `Student` cannot inherit from `Classroom` because a student is not a type of classroom. A student belongs in a classroom, but they shouldn't inherit things like whiteboard, roomNumber or desks. That would be like saying "I'm a classroom because I'm sitting in one."

**To make this works, we can use *composition***
- `Classroom` has many students (has-a relationship)
- `Student` stays focused on being... a student and can be placed in a classroom

## 2. Method Overriding vs. Method Overloading
|            |Method Overriding| Method Overloading|
|------------|-----------------|-------------------|
|**Definition**|Redefining a method from the base class in a derived class|Defining multiple methods with the same name but different parameters|
|**Where it happens**|Between **base** and **derived classes**| Inside the **same class**|
|**When it's decided**| **Runtime** (dynamic polymorphism)|**Compile-time** (static polymorphism)|
|**Purpose**| Change or extend inherited behavior|Provide multiple ways to call a function|
|**Keywords**|`virtual`, `override`|None|

### Why Inheritance Relies on Overriding
- Inheritance becomes truly **flexible and powerful** becauseo of **method overriding**. It allows derived classes to **redefine** or **customize** methods they inherit from a base class without changing the class itself.
  
**1. Custom Behavior for each Derived class**
  - When a derived class overrides a method, it can do **the same thing differently**.
  - Example: base class `Shape` with a method `draw()`, derived class `Circle` and `Square` can override `draw()` to display their own shape.
    
**2. Enables Polymorphism**
  - Overriding is what makes polymorphism possible. We can write code that works with a base class reference or pointer, but it will automatically call the **correct version** of the method based on the actual object type at runtime.
    
**3. Reuse Without Changing Existing Code**
  - With overriding, we can **reuse the base class structure** and just change what we need. The base class stays unchanged, while each derived class adjusts behavior to fit its needs.
    
**4. Easier Maintenance**
  - As the program grows, overriding helps us **add new types or feautures** easily. We can create a new derived class, override only the methods we need to change and still keep the rest of the inherited functionality.
 
## 3. Inheritance vs. Interfaces/Abstract Classes
## Inheritance
- **Purpose**: to create a parent-child relationship between classes, where the child (derived) class can reuse and customize the behavior and attributes of the parent (base) class.
- **Behavior Sharing**: the derived class inherits concrete methods and properties from the base class. It can also override those methods to provide specialized behavior.
- **Single vs. Multiple Inheritance:**
    - Languages like Java support single inheritance (one parent).
    - C++ supports multiple inheritance, which adds flexibility but can also introduce complexity
- Inheritance creates a **strong link** between the child and parent classess. If the base class changes, it can unintentionally affect all derived classes.

## Interfaces and Abstract Classes
- **Purpose:** allows classes to define a set of methods that must be implemented, without dictating how those methods shoule be carried out.
  ### Interfaces:
    - Contain **only method declarations** (no actual code)
	  - Focus **what** a class should do, not **how** it does it
	  - A class can implement multiple interfaces, allowing for more flexible design
	### Abstract Classes:
    - Can have both declared (pure virtual) and implemented methods
	  - Cannot be instantiated, they act as a template for derived classes
	  - Useful when we want to enforce specific behaviro while also sharing common logic
