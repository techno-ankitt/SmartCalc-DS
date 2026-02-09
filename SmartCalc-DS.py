import numexpr as ne
# ye main function hai, jiya koi dukandar ko (hunar)
def ankit_calculator(query):
    """
    Ye function kisi bhi math string ko solve kar sakta hai.
    Example: '2 + 3 * 4' -> 14
    """
    try:
        result = ne.evaluate(query)
        return result
    except Exception:
        return "Invalid Expression"

# 2. ye Execution Block (Dukaan) hai
def main():
    print("--- Ankit's Smart Calculator (powered by NumExpr) ---")
    print("Type 'exit' to quit.")
    
    while True:
        user_input = input("\nApna sawal likhein: ")
        
        if user_input.lower() == 'exit':
            break
            
        # athu function call hu ryo hai
        ans = ankit_calculator(user_input)
        print(f"Result: {ans}")

# 3.O to tu jane hi hai wa, Entry Point
if __name__ == "__main__":
    main()



