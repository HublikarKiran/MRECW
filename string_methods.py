# Create string
my_string = "Hello, World!"
print(my_string)

# Multi-line string
multi_line = """This is
a multi-line
string"""
print(multi_line)

# Raw string
raw_string = r"C:\Users\John"
print(raw_string)

# f-string
name = "John"
greeting = f"Hello, {name}!"
print(greeting)

# Access char
char = my_string[1]
print(char)

# String slicing
slice_ = my_string[7:12]
print(slice_)

# Reverse string
reversed_str = my_string[::-1]
print(reversed_str)

# Concatenate
new_string = "Hello" + " " + "World"
print(new_string)

# Repeat
repeated = "Ha" * 3
print(repeated)

# Length
print(len(my_string))

# Case conversions
print(my_string.upper())
print(my_string.lower())
print(my_string.capitalize())
print(my_string.title())
print(my_string.swapcase())

# Strip whitespace/characters
print("   hello   ".strip())
print("   hello   ".lstrip())
print("   hello   ".rstrip())
print("...Hello!!!".strip('!.'))

# Replace
print(my_string.replace("Hello", "Hi"))

# Split and join
print(my_string.split(","))
print("a-b-c".split("-"))
print("-".join(["a", "b", "c"]))

# Alignments
print(my_string.center(20, '*'))
print(my_string.ljust(20, '*'))
print(my_string.rjust(20, '*'))

# Tabs
print("Hello\tWorld".expandtabs(8))

# Startswith, endswith
print(my_string.startswith("Hello"))
print(my_string.endswith("!"))

# Find, rfind, index
print(my_string.find("World"))
print(my_string.rfind("o"))
print(my_string.index("World"))

# Count
print(my_string.count("l"))

# String checks
print("abc123".isalnum())
print("abc".isalpha())
print("123".isdigit())
print("Ⅻ".isnumeric())
print("42".isdecimal())
print("hello".islower())
print("HELLO".isupper())
print("Hello".istitle())
print("   ".isspace())
print("hello".isprintable())
print("var_1".isidentifier())

# Encode / Decode
encoded = my_string.encode('utf-8')
print(encoded)
decoded = encoded.decode('utf-8')
print(decoded)

# Remove prefix/suffix
print("Hello, World!".removeprefix("Hello, "))
print("Hello, World!".removesuffix("!"))

# Partition / rpartition
print("a,b,c".partition(","))
print("a,b,c".rpartition(","))

# Translate
trans_table = str.maketrans('aeiou', '12345')
print("hello".translate(trans_table))

# Format strings
print("Hello, {}!".format("World"))
print("Hello, {name}!".format(name="John"))
print("{0} {1} {0}".format("Hello", "World"))
print("{first} {last}".format({"first": "John", "last": "Doe"}))

# Formatting width / alignment
print("{:<10}".format("left"))
print("{:^10}".format("center"))
print("{:>10}".format("right"))

# Padding, signs, numbers
print("{:05}".format(42))
print("{:+}".format(42))
print("{:.2%}".format(0.12345))
print("{:,}".format(1234567))

# Binary, Octal, Hex, Scientific
print("{:b}".format(42))
print("{:o}".format(42))
print("{:x}".format(42))
print("{:e}".format(1234.5678))

# Zfill
print("42".zfill(5))