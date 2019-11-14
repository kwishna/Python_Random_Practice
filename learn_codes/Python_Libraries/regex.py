import re

pattern_one = ['one', 'is', 'wc2019']
text_one = 'one plus one is two, not one. but one multiplied by one is always one'
# search_one = re.search(pattern_one, text_one)
for pattern in pattern_one:
    print('searching for "%s" in "%s" ' %(pattern, text_one))

    if re.search(pattern, text_one):
        print("Match Found")
    else:
        print('Not Found Match')

pattern_two = 'one'
match_two = re.search(pattern_two, text_one)
print('First Matching Index :: ', match_two.start())
print('Last Matching Index :: ', match_two.end())
print("Splitting The Text Using Regex :: ", re.split(pattern_two, text_one))
print('Splitting The Sentence', text_one.split())
print('Final Regex :: ', re.findall(pattern_two, text_one))
print('Split By Special Characters :: ', re.split('[^a-zA-Z0-9]', text_one))