import sympy as sp

def compute_derivative():
    print(" Simple Derivative Calculator ")
    
    try:
        # 1. Get the variable name
        var_name = input("Enter the variable (e.g., x): ").strip()
        if not var_name:
            print("You must enter a variable name.")
            return

        # Create a SymPy symbol
        x = sp.symbols(var_name)

        # 2. Get the function
        expr_input = input(f"Enter the function: ")
        
        # sp.sympify converts a string into a math expression safely
        expr = sp.sympify(expr_input)

        # 3. Check if the variable is actually in the math
        if x not in expr.free_symbols:
            print(f"Note: '{var_name}' isn't in that expression, so the derivative will be 0.")

        # 4. Calculate the derivative
        result = sp.diff(expr, x)

        print("\nResult:")
        sp.pprint(result)

    except Exception as e:
        print(f"Error: That doesn't look like a valid math expression. ({e})")

if __name__ == "__main__":
    compute_derivative()