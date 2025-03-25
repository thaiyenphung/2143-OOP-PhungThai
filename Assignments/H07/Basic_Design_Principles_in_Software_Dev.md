# Part A: Conceptual Questions
## 1. DRY (DON'T REPEAT YOURSELF)
- **DRY** is a programming principle to avoid duplicating code or logic. The idea is to write code once and reuse it, rather than copying and pasting the same code in multiple places.
- **Example: Code that violates DRY**

```c++
int main() {
    int x = 1, y = 2;
    int sum = x + y;
    cout << "Sum of 2 integers: " << sum << endl;

    int x2 = 10, y2 = 6;
    int sum2 = x2 + y2; // x + y is 
    cout << "Sum of 2 new integers: " << sum << endl;

    return 0;
}
```

- **Refractor Code (Adhering to DRY):**
```c++
// Function for adding 2 integers
int sumNums(int num1, int num2) {
    return x + y;
}

int main() {
    int x = 1, y = 2;
    cout << "Sum of 2 integers: " << sumNums(x, y) << endl;

    int x2 = 10, y2 = 6;
    cout << "Sum of 2 new integers:  " << sumNums(x2, y2) << endl;

  return 0;
}
```
- Now `sumNums()` function handles the calculation. If the calculation logic changes, we only need to update the function
- This offers consistency and makes code **easier to read and maintain

## 2. KISS (KEEP IT SIMPLE, STUPID)
- **KISS** is a design principle that encourages developers to **keep their code as simple as possible** (but not simpler than necessary).
- Simpler code is **easier to read, understand, and maintain** which reduces bugs and increases clarity and team productivity on large programs.

### Why It's Crucial for Maintainable Code
- **Easier to debug and update**
- Scalability: uncomplicated code can be **extended or modified with less effort**, supporting the project's long-term growth
- **Team productivity**: clear and concise code is easier for team collaboration as everyone can easily understand the code logic

### Potential Drawback of Oversimplification
- **Oversimplifying** the code can lead to a lack of functionality.
- **Too little complexity** makes the code rigid and inflexible and doesn't scale well
- **Example:**
    - When assigning a grade to students, we hardcode `student1 = 85;`, `student2 = 95;` instead of using a loop or a function to reuse
    - What if we have 1000 students? It's not very efficient as we would have to manually enter the student's grade 1000 times, creating unnecessary repetition (**violates DRY principle**)
 
## 3. Introduction to SOLID (High-level)
### Two (out of 5) SOLID Principles are:
### 1. Single Responsibility Principle (SRP)
- A class should have **only one reason to change**, meaning it should focus on **one responsibility or function** in the system

### 2. Open-Closed Principle (OCP)
- Classes and functions (software entities) should be **open for extension** but **closed for modification**, allowing adding new features **without changing existing code**
---

> Other 3 Principles are:
>  - Liskov Substitution Principle (LSP)
>  - Interface Segregation Principle (ISP)
>  - Dependency Inversion Principle (DIP)

### Why SOLID Principles Matter in Large Codebases
- In large codebases, SOLID principles help keep the system **modular, maintainable, and scalable.** They **reduce complexity, minimize bugs**, and make it easier for multiple developers to work on different parts of the code **without breaking each other's work.**

---

# Part B: Minimal Examples or Scenarios
## 1. Dry Violation & Fix 
- **Before:**
```c++
void printInfo(string name) {
    cout << "Student: " << name << endl;
}

void printMoreInfo(string name, int age) {
    cout << "Student: " << name << endl
         << "Age: << age << endl;
}
```

- **After (DRY Refactor):**
```c++
// One function handles both versions
void printInfo(string name, int age = -1) {
    cout << "Student: << name << endl;
    if (age != -1)
        cout << "Age: " << age << endl;
}
```
---

## 2. KISS Principle Example
- **Overcomplicated: Determine Coffee Size based on Button Pressed**
```c++
string getCoffeeSize(char button) {
    if (button == 'S')
        return "Small Coffee";
    else {
        if (button == 'M')
            return "Medium Coffee";
        else {
            if (button == 'L') 
                return "Large Coffee";
            else 
                return "Invalid selection";
            }
        }
}
```
- **KISS Version**:
```c++
string getCoffeeSize(char button) {
    if (button == 'S') return "Small Coffee";
    if (button == 'M') return "Medium Coffee";
    if (button == 'L') return "Large Coffee";
    return "Invalid selection";
}
```

### 3. SOLID Application
**Scenario: (Before SRP)**
- `Shape` interface has **2 unrelated things**:
      1. `draw()` for drawing the shape (related to graphics or UI)
      2. `computeArea()` for mathematical computation
- These are **2 separate responsibilities**
- If we need to change how **shapes are drawn**, we'd need to **change every class (`Circle`, `Rectangle`)
- If we want to add a shape (like `Line`) that can be drawn but **no area**, we're forced to **implement `calculateArea()` as well, and it doesn't make sense.

**After applying SRP: (Pseudo code)**
```c++
// Separate responsibilities
interface Draw {
    void draw();
}

interface AreaComputation {
    double computeArea();
}

class Circle implements Draw, AreaComputation {
    void draw() { // draw a circle... }
    double computeArea() { // area formula for circle... }
}

class Rectangle implements Draw, AreaComputation {
    void draw() { // draw a rectangle... }
    double computeArea() { // area formula for rectangle... }
}

class Line implements Draw {
    void draw() { // draw line... }
    // No need to implement computeArea() 
}
```
---

# Part C: Reflection & Short Discussion
### 1. Trade-Offs
- Sometime repeating code is actually **easier to read** than trying to be too clever
- **Example:**
  ```c++
    if (year == 1)
          cout << "Welcome, Freshman!" << endl;
    else if (year == 2)
          cout << "Welcome, Sophomore!" << endl;
    else if (year == 3)
          cout << "Welcome, Junior!" << endl;
    else
          cout << "Welcome, Senior!" << endl;
    ```

### 2. Combining DRY & KISS
- **DRY: don't repeat yourself**
- **KISS: don't overcomplicate things**
- Together they help us write **clean and understandable** code
- **Example:** combine a function to print a student's name and their age
  ```c++
  void printInfo(string name, double age = -1) {
      cout << Student's name: << name << endl;
      if (age != -1)
          cout << Student's age: << age << endl;
  }
  ```

### 3. SOLID in Practice: Do I Always Need It?
- **Not always!** For small projects or code snippets, **we don't need to follow every SOLID principle perfectly**
- **WHY?**
  - The main goal in small projects is usually to get something working quickly, not to build a perfect architecture.
  - Applying SOLID too early can overcomplicate things. For example, creating extra interfaces or classes when one simple class would be enough

- As the project grows and becomes long-term, that's when we need to apply SOLID because:
  - Easier to scale and extend
  - Cleaner separation of concerns
  - Safer to change without breaking things
