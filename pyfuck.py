def text_file_to_ascii_list(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            contents = file.read()
            ascii_values = [ord(char) for char in contents]
            return ascii_values
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return []
    except Exception as e:
        print("Error:", e)
        return []


filename = input("filename(.py): ")
ascii_list = text_file_to_ascii_list(filename)
output='exec('
for i in ascii_list:
    i=str(i)
    template='chr('
    template+=i+')+'
    output+=template
print(output)
