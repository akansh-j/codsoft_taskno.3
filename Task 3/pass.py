import random
import string

def generate_strong_password(length):
   
    character_pool = string.ascii_letters + string.digits + string.punctuation
    
    if length < 1:
        return "Error: Password length must be at least 1."

    password = ''.join(random.choice(character_pool) for i in range(length))
    return password

def run_password_generator():
    
    print("---Password Generator Tool---")
    
    
    while True:
        try:
            length_str = input("Enter the desired password length (e.g., 16): ")
            password_length = int(length_str)
            
            if password_length >= 8:
                break
            elif password_length > 0:
                print("Recommended password length is 8 or more for security.")
                break 
            else:
                print("Length must be a positive number. Try again.")
                
        except ValueError:
            print("Invalid input. Please enter a whole number.")
    
    generated_password = generate_strong_password(password_length)
    
    print("\nGenerated Password:")
    print(f"  {generated_password}")

if __name__ == "__main__":
    run_password_generator()