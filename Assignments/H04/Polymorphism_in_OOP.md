# Part A: Conceptual Questions
## 1. Definition
- **Polymorphism** allows objects of different classes to be treated as objects of a common base class. This enables the same function, method, or operator to behave differently depending on which object calls it. It promotes **code reusability and flexibility**.
- **Polymorphism** is considered on the **three main pillars** of OOP, alongside **encapsulation and inheritance**. It allows **different objects to respond to the same function call in their own way**.
- It enables **flexible, reusable, and maintainable code** by letting us write programs that work with general types (like a base class or interface) while allowing **specific behavior** at runtime. 

## 2. Compile-Time vs. Runtime
- **Compile-time polymorphism (method overloading)** occurs when several methods share the same name but differ in the number or type of parameters, allowing the compiler to determine the appropriate method during compilation.
- **Runtime polymorphism (method overriding)** occurs when a derived class defines its own version of a virtual method, and the appropriate method is determined at runtime based on the object's actual type.

### Which Method Requires Inheritance?
- **Runtime polymorphism requires an inheritance relationship** as it is based on a base class declaring a `virtual` method that is **overridden** by derived classes, allowing the program to determine the correct method to call at runtime using a base class pointer or reference.

## 3. Method Overloading
- A class can **define multiple methods** with the **same name** but **different parameters** to create a more streamlined and user-friendly interface. This enables users to call the same method in various ways based on the information they possess without needing to remember several different method names.
- Example: **`Calculator` class**
    - Two numbers: `sum(int a, int b)`
    - Three numbers: `sum(int a, int b, double c)`
    - Elements in an array: `sum(int[] numbers)`
    - Instead of creating separate methods like `sum2numbers()`, `sum3numbers()`, `sumArrays()`, the class just **overloads `sum()`**, making it easier and more natural for users to interact with.

## 4. Method Overriding
- A derived class **overrides** a method from the base class by **defining a new version of that method with the same name, return type, and parameters.** This lets the derived class provide **specialized behavior** while keeping a consistent interface.
- In a language like C++, the `virtual` keyword in the base class implies that the method is **meant to be overridden**, and tells the compiler to use **runtime polymorphism (dynamic dispatch).
- The `override` keyword in the derived class:
    - Ensures the method **matches exactly** with a virtual method in the base class
    - Helps **prevent mistakes** like typos in the method name or incorrect parameter lists
    - Improves **code readability and reliability** by clearly marking the method as an override
---

# Part B: Minimal Demonstration
```c++
// BASE CLASS
class Shape {
public:
    virtual void draw() = 0;
};

// DERIVED CLASS CIRCLE
class Circle : public Shape {
public:
    void draw() override {
        cout << "Drawing a circle." << endl;
    }
};

// DERIVED CLASS RECTANGLE
class Rectangle : public Shape {
public:
    void draw() override {
        cout << "Drawing a rectangle." << endl;
    }
};

int main() {
    vector<Shape*> shape;

    shape.push_back(new Circle());
    shape.push_back(new Rectangle());

    for (Shape* sh : shape) {
        sh->draw(); // Correct draw() decides at RUNTIME
    } 

return 0;
}
```
---

# Part C: Overloading vs. Overriding Distinctions
## 1. Overloaded Methods
- In a class `Calculator` with multiple overloaded `calculate()` methods, the **compiler decides at compile time** which version to call based on the **number and types of arguments** passed to the function call.
```c++
class Calculator {
public:
    int calculate(int a, int b) {
        return a + b;
    }

    int calculate(double a, double b) {
        return a/b;
    }
};

int main() {
    Calculator cal;

    cal.calculator(2, 5);
    cal.calculator(2.5, 5.5);

    return 0;
}
```
---

# Part D: Reflection & Real-World Applications
## 1. Practical Example
**A game with a base class `Enemy` and a `virtual` method `attack()`:**
```c++
class Ememy {
public:
    virtual void attack() = 0;
};
```
- We can create derived classes like `Godzilla`, `Unicorn`, each with its own version of `attack()`
  
**Why Polymorphism Matters:**
- You can keep all types of enemies in one array of `Enemy*` and call `attack()` on each without needing to know their specific types
- The appropriate `attack()` behavior is decided at runtime, avoiding the need for lengthy if-else or switch statements to check types
- It minimizes code repetition and makes it simple to introduce new enemy types later without changing existing code

## 2. Potential Pitfalls
### Method Overloading
**Ambiguity with similar parameter types**:
- If overloaded methods have parameters that are too similar (int vs. double), the compiler might choose the wrong version or throw an error due to ambiguity. 
```c++
void calculate(int x);
void calculate(double x);

calculate(5); // Could call int or double version depending on context
```

### Runtime Polymorphism
**Performance Overhead and Debugging Complexity**:
- Because the method to call is determined at **runtime**, there is a slight **performance overhead** (due to virtual table lookup), and it can make **debugging** harder, especially when trying to track which **overridden method** is being called within a complex inheritance structure.
```c++
Base* obj = new Derived();
obj->calculate(); // Which version? Harder to trace in big system
```

## 3. Checking Understanding
- When adding a new `Triangle` class that inherits from `Shape` and overrides the `draw()` method, **polymorphism lets us use it without changing any existing code** that already works with `Shape*` or `Shape&`
- Since the existing code already use `shape->draw()` on a `Shape*`,  **runtime polymorphism** ensures that `Triangle::draw()` is called automatically if the actual object is a `Triangle`
- There's no need to alter loops, function calls, or conditionals. We simply create the new class and use it where needed.
