import matplotlib.pyplot as plt

# Define the stops and routes
stops = ["Portorosa", "Vulcano", "Stromboli", "Salina", "Panarea", "Lipari", "Portorosa"]
distances = [18, 22, 17, 9, 12, 18]
colors = ["blue", "green", "red", "orange", "purple", "cyan"]

# Coordinates for the stops (example coordinates for visualization purposes)
coordinates = {
    "Portorosa": (0, 0),
    "Vulcano": (1, 2),
    "Stromboli": (3, 5),
    "Salina": (5, 3),
    "Panarea": (6, 1),
    "Lipari": (4, 0)
}

# Plot the chart
plt.figure(figsize=(10, 8))

for i in range(len(stops) - 1):
    start = stops[i]
    end = stops[i + 1]
    x_values = [coordinates[start][0], coordinates[end][0]]
    y_values = [coordinates[start][1], coordinates[end][1]]
    plt.plot(x_values, y_values, color=colors[i], label=f"{start} → {end} ({distances[i]} NM)")
    plt.scatter(coordinates[start][0], coordinates[start][1], color=colors[i], s=100, label=f"{start}")

# Add the last stop
plt.scatter(coordinates["Portorosa"][0], coordinates["Portorosa"][1], color="blue", s=100, label="Portorosa")

# Add labels and legend
plt.title("Maritime Routes Chart")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.legend()
plt.grid()

# Save and show the chart
plt.savefig("maritime_chart.png")
plt.show()