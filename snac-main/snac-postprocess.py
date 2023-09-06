# Further revised function to convert text to HTML with highlighted tags
def convert_to_html(text):
    sentences = []
    tags = []
    current_sentence = ""
    html_output = ""

    # CSS styles for different tags
    styles = {
        'character': 'background-color: yellow;',
        'scene': 'background-color: lightgreen;',
        'event': 'background-color: lightblue;',
        'inconsistent': 'background-color: pink;'
    }

    # Splitting the input text by lines
    lines = text.strip().split("\n")

    old_text_len = 0
    sentences = []
    html_output = ""
    for i, line in enumerate(lines):
        if i % 2 == 0: #sentence
            ix = line.index("<extra_id_0>") + len("<extra_id_0>") + 1
            sentences.append(line[ix:-4])
        else:
            var = len("Predicted: ")
            flag = line[var:]
            if flag.startswith("true"):
                html_output += sentences[-1] + " "
            else:
                var = len("false<extra_id_0> ")
                elements = flag[var:-4].split(" ")
                error_type = elements[0]
                if len(elements) == 1: #only error, highlight the whole sentence
                    html_output += f'<span style="{styles[error_type]}">{sentences[-1]}</span> '
                else:
                    for element in elements[1:]:
                        sentences[-1] = sentences[-1].replace(element, f'<span style="{styles[error_type]}">{element}</span>')
                    html_output += sentences[-1] + " "
    return f'<html><body>{html_output}</body></html>'

# Example text
text = '''
<extra_id_0> In his younger years, Hardy's father gave him advice that he has been turning over in his mind ever since.</s>
Predicted: false<extra_id_0> character Hardy</s>
In his younger years, Hardy's father gave him advice that he has been turning over in his mind ever since.<extra_id_0> Whenever he feels like criticizing anyone, he should remember that all people in the world haven't had the advantages he has.</s>
Predicted: true</s>
In his younger years, Hardy's father gave him advice that he has been turning over in his mind ever since. Whenever he feels like criticizing anyone, he should remember that all people in the world haven't had the advantages he has.<extra_id_0> Hardy lives at West Egg, the less fashionable of the two, and his house is an eyesore, but it has a view of the water and the comforting proximity of millionaires.</s>
Predicted: false<extra_id_0> scene</s>
In his younger years, Hardy's father gave him advice that he has been turning over in his mind ever since. Whenever he feels like criticizing anyone, he should remember that all people in the world haven't had the advantages he has. Hardy lives at West Egg, the less fashionable of the two, and his house is an eyesore, but it has a view of the water and the comforting proximity of millionaires.<extra_id_0> One evening, Hardy drives over to East Egg to see two old friends, Tom Buchanan and Daisy.</s>
Predicted: false<extra_id_0> character Tom Buchanan Daisy</s>
In his younger years, Hardy's father gave him advice that he has been turning over in his mind ever since. Whenever he feels like criticizing anyone, he should remember that all people in the world haven't had the advantages he has. Hardy lives at West Egg, the less fashionable of the two, and his house is an eyesore, but it has a view of the water and the comforting proximity of millionaires. One evening, Hardy drives over to East Egg to see two old friends, Tom Buchanan and Daisy.<extra_id_0> Tom and Daisy stroll back into the library as if to a vigil beside a perfectly tangible body.</s>
Predicted: true</s>'''

# Generate HTML output
html_output = convert_to_html(text)
print(html_output)
# Save HTML output to a file
file_path = 'snac.html'
with open(file_path, 'w') as f:
    f.write(html_output)

