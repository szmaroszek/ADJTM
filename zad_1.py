import re

example_text_a = "Dzisiaj mamy 4 stopnie na plusie, 1 marca 2022 roku"
example_text_b = "<div><h2>Header</h2> <p>article<b>strong text</b> <a href="">link</a></p></div>"
example_text_c = """Lorem ipsum dolor sit amet, consectetur; adipiscing elit.
Sed eget mattis sem. Mauris egestas erat quam, ut faucibus eros congue et. In
blandit, mi eu porta; lobortis, tortor nisl facilisis leo, at tristique augue risus
eu risus."""

result_a = re.sub(r'\d', '', example_text_a) #remove digits
result_b = re.sub(r'<.*?>', '', example_text_b) #remove html tags
result_c = re.sub(r'[.,]', '', example_text_c) #remove non letter charachters

print(result_a)
print(result_b)
print(result_c)