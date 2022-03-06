import re

example_text = """Lorem ipsum dolor :) sit amet, consectetur; adipiscing elit. Sed eget mattis sem. ;)
                  Mauris ;( egestas erat quam, :< ut faucibus eros congue :> et. In blandit, mi eu porta;
                  lobortis, tortor :-) nisl facilisis leo, at ;< tristique augue risus eu risus ;-)."""

results = re.findall(r'[:;][^\s]{1,2}', example_text)

print(results)