
# Function for formatting
def formatter(symbol, text):
    sides = symbol * 3
    formatter_text = f"{sides}, {text}, {sides}"
    top_bottom = symbol * len(formatter_text)
    return f"{top_bottom}\n{formatter_text}\n{top_bottom}"


# main routine
print(formatter("-", "Welcome to the Unicorn Game"))
print()
print(formatter("$", "Congratulations, You Got The Unicorn"))
print()
print(formatter("", "Unlucky, You Got The Donkey"))
print()
