import matplotlib.pyplot as plt

languages = [
"Python",
"JavaScript",
"TypeScript",
"Go",
"Rust",
"Java",
"C++"
]

popularity = [95,92,80,70,65,60,55]

plt.figure(figsize=(10,6))
plt.bar(languages, popularity)

plt.title("Programming Language Popularity")
plt.xlabel("Languages")
plt.ylabel("Popularity Score")

plt.xticks(rotation=30)

plt.savefig("assets/language-popularity.png")

print("Language stats chart updated.")
