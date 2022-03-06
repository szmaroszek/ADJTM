import re

example_text = """Lorem ipsum dolor
                  sit amet, consectetur adipiscing elit. Sed #texting eget mattis sem. Mauris #frasista
                  egestas erat #tweetext quam, ut faucibus eros #frasier congue et. In blandit, mi eu porta
                  lobortis, tortor nisl facilisis leo, at tristique #frasistas augue risus eu risus."""

results = re.findall(r'#(\w+)', example_text)

print(results)