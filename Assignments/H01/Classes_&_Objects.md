# Classes & Objects

## Part A: Conceptual Questions

### 1. Definition of a Class and an Object
- A **class** is a **user-defined data type** that acts as a blueprint for creating objects. A class **encapsulates** data members (variables) and member functions (methods) that define the behavior of the object.
- An **object** is an instance of a class. It represents a real-world entity with unique values for its attributes and can perform actions through methods.
- A **class** does not allocate memory but is just being defined, but an instance of a class (**an object**) does allocate memory.
  
**Relationship:**
- Objects are created from a class
- Objects inherit the attributes and methods defined in their class.
- The object is the actual component of programs, while the class specifies how instances are created and how they behave.

### 2. Constructors and Destructors
<ins>**Constructors:**
- A **constructor** is a special member function that initializes an object (by setting initial values for its attributes) when it is created.
- A **constructor** different from normal function in the following ways:
   - Constructor has the **same name** as the class itself.
   - Constructor **does not** have a return type (not even void).
   - **Default constructors** don't have input arguments, but **Copy & Parameterized Constructors** have input arguments.
   - A constructor is automatically called when an object is created.
   - Must be placed in **public** section of class.
   - If we do not specify a constructor, the C++ compiler generates a **default constructor** for the object (expects no parameters and has an empty body).
 
<ins>**Destructors**:
- A **destructor** is a special function in C++ that is automatically called when an object **goes out of scope** or explicitly **deleted**. It is used for **clean-up operations** such as **deallocating memory, closing files, or releasing resources**.
  
- **Destructors** are important for object lifecycle management because they ensure resources acquired by an object during its lifetime are released when the object is destroyed, **preventing memory leaks and resource exhaustion**.

**Key Features of a Destructor:**
  - Same name as the class but prefixed with `~`
  - No parameters and no return type
  - Automatically called when an object is destroyed
  - Only one destructor per class (cannot be overloaded)
  - Used to free resources like dynamically allocated memory (new/ delete)

### 3. Object Lifecycle
**1. Instantiation:** the object is created, memory is allocated, and its constructor initializes the current values of its attributes. 

**2. Usage:** the object is employed during program execution through method calls and property access.

**3. Destruction:** when the object is no longer needed, its destructor or cleanup method is called to release resources and free memory. 

![image](https://media.geeksforgeeks.org/wp-content/cdn-uploads/20200827160616/FlowChartObjectLifeCycle1.png)

---

### Why is it important for a class to manage its resources (e.g., memory) during its lifecycle?
- **Maintain performance**: efficient allocation and dealllocation prevent wasted memory and ensure the system runs smoothly.
- **Prevent memory leaks:** by releasing resources when they're no longer needed, the class avoids accumulating unused memory that can degrade performance over time.
- **Enhances stability:** proper cleanup avoids errors like dangling pointers or corrupted states which can lead to crashes or unpredictable behavior.
- **Optmizes resource use:** it ensures that limited resources (such as file handles) are available to other parts of the program or system when needed.
---

## Part B: Minimal Coding Example

```c++
class Unicorn
{
private:
    string name;
    float health;
public:
    Unicorn(string n, float h) : name(n), health(h) {}
    ~Unicorn()
    {
        cout << "Destructor called. The object is being destroyed." << endl;
    }

    void displayState()
    {
        cout << "Unicorn " << name << " has " << health << "%  health." << endl;
    }
};

int main()
{
    Unicorn *uni1 = new Unicorn("Stella", 100); // creates a Unicorn object on the heap
    uni1->displayState();

    delete uni1; // this calls the destructor to free memory

    return 0;
}
```
<ins>**Explanation:**
- The constructor `Unicorn(string n, float h)` initializes the object’s private members `name` and `health` when the object is created, ensuring it starts in a valid state.
- The destructor `~Unicorn()` is automatically called when the object is destroyed. In this case, because the object is created using `new`, it does not go out of scope automatically, so the destructor is only called when `delete` is used
---

## Part C: Reflection & Short-Answer

**1. Important of Constructors:**
- **Constructors** initialize objects when they are created, ensuring that all necessary attributes and resources are set up properly.
- It creates a valid and consistent state for the object, avoiding issues like uninitialized variables or incomplete setups, which could lead to errors or unpredictable behaviors.

**2. Role of Destructors:**
- **Destructors** release resources such as dynamically allocated memory or open file streams. Failing to free resources can lead to memory leaks, reduced performance, or system instability.

**3. Lifecycle Management:**
- If a class does not properly manage its resources, it can lead to problems like memory leaks, dangling pointers, and unexpected behavior. Such issues can degrade performance, cause system instability, and ultimately lead to application crashes.
- Proper lifecycle management ensures efficiency and stability in a program.
