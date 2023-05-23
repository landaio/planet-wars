import os
import re
import sys
import webbrowser


def generate(data, save_path, player_a, player_b):
    path = os.path.dirname(__file__)
    template_path = os.path.join(path, "index.php")
    with open(template_path, "r") as template:
        content = template.read()

    print(data)
    php_re = re.compile(r"<\? php \?>", re.S)
    javascript = f"const data = '{data}'; const players = ['{player_a}', '{player_b}']"
    content = php_re.sub(javascript, content)

    output = open(save_path, "w+")
    output.write(content)
    output.close()


if __name__ == "__main__":
    player_a, player_b = sys.argv[1], sys.argv[2]

    input_data = input()

    current_path = os.path.dirname(__file__)
    generated_path = os.path.realpath(os.path.join(current_path, "generated.html"))

    generate(input_data, generated_path, player_a, player_b)
    webbrowser.open("file://" + generated_path)
