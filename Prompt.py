print("Welcome to the Image Idea Generator!")

subject = input("What do you want to see?")
color = input("Choose a color: ")
background = input("Choose a background: ")

prompt = (
    "Create an image of a "
    + color + " " + subject
    + " with " + background
)

print("\nYour AI prompt is:")
print(prompt)