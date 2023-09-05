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

    for line in lines:
        if "Predicted:" in line:
            predicted_splits = line.split("Predicted: ")
            if len(predicted_splits) > 1:
                extra_id_splits = predicted_splits[-1].split("<extra_id_0>")
                if len(extra_id_splits) > 1:
                    end_tag_splits = extra_id_splits[1].split("</s>")
                    if len(end_tag_splits) > 0:
                        tag_line = end_tag_splits[0]
                        tags.append(tag_line)
        else:
            sentence_line = line.split("<extra_id_0>")[0].strip()
            current_sentence += " " + sentence_line.strip()
            sentences.append(current_sentence.strip())

    for sentence, tag in zip(sentences[1:], tags):
        if tag == 'scene':
            html_output += f'<span style="{styles[tag]}">{sentence}</span> '
        else:
            words = sentence.split(" ")
            tagged_words = tag.split(" ")
            for word in words:
                if word in tagged_words:
                    html_output += f'<span style="{styles[tag]}">{word}</span> '
                else:
                    html_output += f'{word} '
        html_output += '. '

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
# file_path = 'snac.html'
# with open(file_path, 'w') as f:
#     f.write(html_output)

