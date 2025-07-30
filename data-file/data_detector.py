filename = input("Enter the name of the file you want to open: ")

try:
    with open(filename, 'r') as file:
        content = file.read()
        print("\nFile content:\n")
        print(content)

except FileNotFoundError:
    print(f"\nError: The file '{filename}' was not found. Please check the filename and try again.")