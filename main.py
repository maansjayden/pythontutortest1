def customs_check(name, item, passcode):
    # TODO 1: Create a greeting using an f-string. 
    # It must exactly say: "Welcome to Schiphol Customs, Agent [name]."
    greeting = "" 
    
    # TODO 2: Write an IF statement that checks if the passcode (in lowercase) is NOT "stroopwafel".
    # If it is wrong, return: f"{greeting}\n[!] ACCESS DENIED: Invalid secret passcode."
    pass # Replace this with your if statement
    
    # TODO 3: Write an IF/ELIF/ELSE block to check the item (remember to use .lower()!)
    # - IF the item is "easter eggs": return f"{greeting}\n[✓] CLEARED. But you owe €15.00 in tax for the {item}!"
    # - ELIF the item is "wasabi": return f"{greeting}\n[!] ACCESS DENIED: Contraband detected."
    # - ELSE (any other item): return f"{greeting}\n[✓] CLEARED. Enjoy your {item}."
    pass # Replace this with your if/elif/else block

    return "Code not finished yet! Follow the TODOs above."

if __name__ == "__main__":
    print("--- 🇳🇱 Terminal 1 Checkpoint ---")
    
    # TODO 4: Use input() to ask the user for these three values instead of hardcoding them.
    traveler_name = "DefaultName" 
    declared_item = "DefaultItem" 
    secret_code = "1234" 
    
    result = customs_check(traveler_name, declared_item, secret_code)
    print(f"\n{result}")
