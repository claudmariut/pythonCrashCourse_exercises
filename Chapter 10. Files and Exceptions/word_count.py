def count_words(filename):
    """Count the approximate number of words in a file"""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        with open("text_files/missing_files.txt", 'a') as f:
            f.write(f"{filename}\n")
    else:
        words = contents.split()
        num_words = len(words)
        print(f"THe file {filename} has about {num_words} words.")


filename = ['text_files/learning_python.txt', 'hola.txt',
            'text_files/alice.txt']
for file in filename:
    count_words(file)

