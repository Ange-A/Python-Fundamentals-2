def generate_code():
    code = ""

    code += "def greet(name):\n"
    code += "    print('Hello, ' + name + '!')\n"
    code += "greet('world')\n"

    return code


generated_code = generate_code()
print(generated_code)
