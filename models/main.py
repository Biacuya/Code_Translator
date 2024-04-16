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
    pattern = r"'([^']*)'"  # Expresión regular encargada se extraer la palabra que se encuentra entre ' '
    if "print" in function_print:
        match = re.findall(pattern, function_print)
        message = match[0]
        header_code = "# include <stdio.h>\n"
        body_code = "int main() {{\nprintf({});\n return 0;\n}}"
        message_inserted = body_code.format('"' + message + '"')
        new_code = header_code + message_inserted
    return new_code


print(translate_print_to_c("print('hola')"))


def translate_if_python_to_if_c(funtion_if):
    pattern_nums = r"if\s+(\d+)\s+<\s+(\d+)"
    pattern = r"'([^']*)'"

    match = re.search(pattern_nums, funtion_if)
    if match:
        value1 = match.group(1)
        value2 = match.group(2)
    else:
        pattern_nums = r"if\s+(\d+)\s+>\s+(\d+)"
        match = re.search(pattern_nums, funtion_if)
        value1 = match.group(1)
        value2 = match.group(2)

    match_sting = re.findall(pattern, funtion_if)
    string1 = match_sting[0]
    string2 = match_sting[1]

    if "if" and "<" in funtion_if:
        header_code = "# include <stdio.h>\n"
        body_code = "int main() {{\nif ({} < {}){{\nprintf({});\n}}else{{\nprintf({});\n}}\nreturn 0;\n}}"
        value_inserted = body_code.format(
            value1, value2, '"' + string1 + '"', '"' + string2 + '"'
        )
        new_code = header_code + value_inserted
    elif "if" and ">" in funtion_if:
        header_code = "# include <stdio.h>\n"
        body_code = "int main() {{\nif ({} > {}){{\nprintf({});\n}}else{{\nprintf({});\n}}\nreturn 0;\n}}"
        value_inserted = body_code.format(
            value1, value2, '"' + string1 + '"', '"' + string2 + '"'
        )
        new_code = header_code + value_inserted

    return new_code


fun_if = "if 1 < 2:\n print('Es menor')\n  else:\n print('Es mayor')"
fun_if_two = "if 3 > 2:\n print('Es mayor')\n  else:\n print('Es menor')"
# print(fun_if)

print(translate_if_python_to_if_c(fun_if_two))
