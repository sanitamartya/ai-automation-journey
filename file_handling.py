# ============ FILE HANDLING BASICS ============
import json


# 1. Write text file
print("=== Write text file ===")
with open("test.txt", "w") as f:
    f.write("Hello, file!\n")
    f.write("This is line 2.\n")
    f.write("This is line 3.\n")
print("✅ Written to test.txt")


# 2. Read text file
print("\n=== Read text file ===")
with open("test.txt", "r") as f:
    content = f.read()
print("Content:")
print(content)


# 3. Read line by line
print("=== Read line by line ===")
with open("test.txt", "r") as f:
    for line in f:
        print(f"  Line: {line.strip()}")


# 4. Write JSON file
print("\n=== Write JSON file ===")
data = {
    "name": "Sanit",
    "skills": ["python", "javascript"],
    "learning": True,
    "day": 3
}
with open("data.json", "w") as f:
    json.dump(data, f, indent=2)
print("✅ Written to data.json")


# 5. Read JSON file
print("\n=== Read JSON file ===")
with open("data.json", "r") as f:
    loaded = json.load(f)
print("Loaded data:")
print(loaded)
print(f"Name: {loaded['name']}")
print(f"Skills: {loaded['skills']}")


# 6. Append to file (not overwrite)
print("\n=== Append to file ===")
with open("test.txt", "a") as f:
    f.write("This line was appended.\n")
print("✅ Appended")

with open("test.txt", "r") as f:
    print(f.read())


# 7. Check if file exists
import os
print("=== Check file exists ===")
print(f"test.txt exists: {os.path.exists('test.txt')}")
print(f"nonexistent.txt exists: {os.path.exists('nonexistent.txt')}")

