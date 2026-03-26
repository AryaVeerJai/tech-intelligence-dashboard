import matplotlib.pyplot as plt

months = [
"Jan","Feb","Mar","Apr","May","Jun",
"Jul","Aug","Sep","Oct","Nov","Dec"
]

tools_released = [5,8,12,15,20,28,35,40,50,65,80,100]

plt.figure(figsize=(10,6))
plt.plot(months, tools_released, marker="o")

plt.title("AI Tools Growth in 2026")
plt.xlabel("Month")
plt.ylabel("Number of AI Tools")

plt.grid(True)

plt.savefig("assets/ai-tools-growth.png")

print("AI tools growth chart updated.")
