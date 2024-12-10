input_strings = [
    "hello world",
    "Python is suspicious",
    "I don't know if I love programming",
    "Hello Python, my old friend",
    "Generators are powerful?"
]
substring_to_filter = "Python"

y = filter(lambda x: substring_to_filter in x, input_strings)
print(map(str.upper(), y))
