## 1. Inheritance in Different Languages (Java vs. C++)
- In **Java**:
    - A class can inherit from **only one parent class**, this is called **single inheritance**.
    - This design avoids complications like the **diamond problem**
    - However, **Java** allows a class to implement **multiple interfaces**, providing **flexibility without the complexity** of multiple class inheritance.

- In **C++**:
    - A class can inherit from **multiple base classes**, known as **multiple inheritance**, offering more power and flexibility
    - However, this can introduce **ambiguity** when multiple base classes define **the same method or member**.
    - To manage the issue, C++ provides **virtual inheritance** as a solution
 
## 2. Open-Closed Principle (OCP)
- **Open-Closed principle** says that **classes should be open for extension** but **closed for modification**
- **Inheritance** supports this be allowing us to create new classes that **extend** behavior **without changing the existing code**
  
- **Example:**
    ```c++
    class Animal {
    public:
        virtual void makeSound() {
            cout << "Some generic sound" << endl;
        }
    };

    class Cow : public Animal {
    public:
        void speak() override {
            cout << "Moo!" << endl;
        }
    };
    ```
    - In this example, `Animal` is **extended** with `Cow` class.
    - We **didn't modify** `Animal`, but gave it **new behavior** through `Cow` class
