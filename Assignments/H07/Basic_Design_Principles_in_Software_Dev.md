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

**Refractor Code (Adhering to DRY):
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
- Simpler code is **easier to read, understand, and maintain which reduces bugs and increases clarity and team productivity on large programs.

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
**Two (out of 5) SOLID Principles are:**
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
