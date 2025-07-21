import os

# Step 1: Folder path add karna hai jaha 10 text files hain
folder_path = r"C:\Users\Welcome\Desktop\Notepad FIles"  

# Step 2: Text likhna hai jo har file me add karna hai
text_to_add = "\nThis text was added to all files.\n"

# Step 3: Loop through all files in the folder means folder me sabhi files ko loop me lana hai
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)

    #Check if it's a file and ends with .txt means check karna hai ki sari file txt hai
    if os.path.isfile(file_path) and filename.endswith(".txt"):
        with open(file_path, "a", encoding="utf-8") as file:
            file.write(text_to_add)

print("Text added to all .txt files in the folder.")
