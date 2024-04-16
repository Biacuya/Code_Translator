import re


def translate_code(function_print, message):
    new_code = ""
    if "print" in function_print:
        header_code = "# include <stdio.h>\n"
        body_code = "int main() {{\nprintf({});\n return 0;\n}}"
        insert_message = body_code.format('"' + message + '"')
        new_code = header_code + insert_message
    return new_code


# print(translate_code("print", "Hello"))

def translate_print_to_c(function_print):
    new_code = ""
    message = ""
    pattern = r"'([^']*)'" # Expresión regular encargada se extraer la palabra que se encuentra entre ' '
    if "print" in function_print:
        match = re.findall(pattern, function_print)
        message = match[0]
        header_code = "# include <stdio.h>\n"
        body_code = "int main() {{\nprintf({});\n return 0;\n}}"
        insert_message = body_code.format('"' + message + '"')
        new_code = header_code + insert_message
    return new_code


print(translate_print_to_c("print('hola')"))
