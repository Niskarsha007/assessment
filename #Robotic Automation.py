#Robotic Automation

def sort(width, height, length, mass):
    # Calculate the volume of the package
    volume = width * height * length
    
    # Check if the package is bulky:
    # - Volume >= 1,000,000 cm³ OR any dimension >= 150 cm
    is_bulky = (volume >= 1000000) or (width >= 150) or (height >= 150) or (length >= 150)
    
    # Check if the package is heavy: mass >= 20 kg
    is_heavy = mass >= 20
    
    # Determine the stack based on the rules:
    # - REJECTED if both bulky and heavy
    # - SPECIAL if either bulky or heavy
    # - STANDARD otherwise
    stack = (
        "REJECTED" if is_bulky and is_heavy else
        "SPECIAL" if is_bulky or is_heavy else
        "STANDARD"
    )
    
    return stack

# Example usage and testing
print(sort(50, 50, 50, 10))    # Output: STANDARD (not bulky, not heavy)
print(sort(150, 50, 50, 10))   # Output: SPECIAL (bulky, not heavy)
print(sort(50, 50, 50, 25))    # Output: SPECIAL (not bulky, heavy)
print(sort(200, 200, 200, 25)) # Output: REJECTED (bulky and heavy)