"""
Q.Python function to create the HTML string with tags around the
word(s).
"""
def add_tags(tag_name, words):
    return f"<{tag_name}>{words}</{tag_name}>"

print(add_tags("b", "anish"))
print(add_tags("i", "thapaliya"))