# Part A: Conceptual Questions
## 1. Definition
- **Polymorphism** allows objects of different classes to be treated as objects of a common base class. This enables the same function, method, or operator to behave differently depending on which object calls it. It promotes **code reusability and flexibility**.
- **Polymorphism** is considered on the **three main pillars** of OOP, alongside **encapsulation and inheritance**. It allows **different objects to respond to the same function call in their own way**. - It enables **flexible, reusable, and maintainable code** by letting us write programs that work with general types (like a base class or interface) while allowing **specific behavior** at runtime. 

## 2. Compile-Time vs. Runtime
- **Compile-time polymorphism (method overloading)** occurs when several methods share the same name but differ in the number or type of parameters, allowing the compiler to determine the appropriate method during compilation.
- **Runtime polymorphism (method overriding)** occurs when a derived class defines its own version of a virtual method, and the appropriate method is determined at runtime based on the object's actual type.

## Which Method Requires Inheritance?
- **Runtime polymorphism requires an inheritance relationship** as it is based on a base class declaring a `virtual` method that is **overridden** by derived classes, allowing the program to determine the correct method to call at runtime using a base class pointer or reference.

## 3. Method Overloading
- A class can define multiple methods with the same name but different parameters to create a more streamlined and user-friendly interface. This enables users to call the same method in various ways based on the information they possess without needing to remember several different method names.
- Example: **`Calculator` class
    - Two numbers: `sum(int a, int b)`
    - Three numbers: `sum(int a, int b, double c)`
    - Elements in an array: `sum(int[] numbers)`
    - Instead of creating separate methods like `sum2numbers()`, `sum3numbers()`, `sumArrays`, the class just **overloads `sum()`, making it easier and more natural for users to interact with. 
