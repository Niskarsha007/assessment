# assessment
# Package Sorting Function for Robotic Automation

This project implements a Python function `sort(width, height, length, mass)` that determines the appropriate stack for a package based on its dimensions and mass. The function is designed for use in a robotic automation factory to dispatch packages efficiently.

---

## Rules for Sorting Packages

A package is sorted into one of three stacks based on the following criteria:

1. **Bulky**: A package is considered bulky if:
   - Its volume (`width * height * length`) is ≥ 1,000,000 cm³, **or**
   - Any of its dimensions (`width`, `height`, or `length`) is ≥ 150 cm.

2. **Heavy**: A package is considered heavy if its mass is ≥ 20 kg.

3. **Stacks**:
   - **STANDARD**: For packages that are neither bulky nor heavy.
   - **SPECIAL**: For packages that are either bulky or heavy.
   - **REJECTED**: For packages that are both bulky and heavy.

---

## How to Use

### Function Signature
```python
def sort(width, height, length, mass):
    # Returns the stack name as a string: "STANDARD", "SPECIAL", or "REJECTED"
