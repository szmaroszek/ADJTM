import re

def extract_emoticons(input_text):
    return (re.sub(r'[:;][^\s]{1,2}', '', input_text), re.findall(r'[:;][^\s]{1,2}', input_text))

def remove_digits(input_text):
    return re.sub(r'\d', '', input_text)

def remove_html(input_text):
    return re.sub(r'<.*?>', '', input_text)

def remove_punctuation(input_text):
    return re.sub(r'[.,]', '', input_text)

def remove_whitespace(input_text):
    return " ".join(input_text.split())

def clean_text(input_text):
    (result, emoticons_array) = extract_emoticons(input_text)
    result = result.lower()
    result = remove_digits(result)
    result = remove_html(result)
    result = remove_punctuation(result)
    result = remove_whitespace(result)

    result += "\nemoticons: " + str(emoticons_array)
    return result

example_text = """Lorem ipsum dolor :) sit amet, consectetur; adipiscing elit. Sed eget mattis sem. ;)
                  Mauris ;( egestas erat quam, :< ut faucibus eros congue :> et. In blandit, mi eu porta;
                  lobortis, tortor :-) nisl facilisis leo, at ;< tristique augue risus eu risus ;-).
                  333232323232323 312312 12309123 120391203 123 123123 123331 """


print(clean_text(example_text))