import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch

# Read Excel File
file_path = "/content/Organised_Data_Sets.xlsx"

df = pd.read_excel(
    file_path,
    sheet_name="total_consolidated_data"
)

# Clean Column Names
df.columns = df.columns.str.strip()

# Conferences of Interest
selected_conferences = [
    "SenSys",
    "EWSN",
    "DCOSS-IoT",
    "WF-IoT",
    "BIOTC"
]

df = df[
    df["Conference"].isin(selected_conferences)
]

# Create Conference-Year Label
df["Conference_Year"] = (
    df["Conference"] + "-" +
    df["Conference year"].astype(str)
)

# Remove Missing Citation Values
df = df.dropna(
    subset=["Number of citations under Google Scholar"]
)

# Sort by Median Citation Count
citation_order = (
    df.groupby("Conference_Year")["Number of citations under Google Scholar"]
      .median()
      .sort_values(ascending=False)
)

conference_order = citation_order.index.tolist()

print("Conference Order:")
print(conference_order)

# Prepare Data
box_data = []

for conf in conference_order:
    citations = df[
        df["Conference_Year"] == conf
    ]["Number of citations under Google Scholar"]

    box_data.append(citations)

# Plot
fig, ax = plt.subplots(figsize=(9,6))

bp = ax.boxplot(
    box_data,
    positions=np.arange(1, len(conference_order)+1),
    widths=0.6,
    patch_artist=True,
    tick_labels=[""] * len(conference_order),
    showfliers=True
)

# Box Colors
for i, box in enumerate(bp["boxes"]):

    if "2023" in conference_order[i]:

        box.set(
            facecolor="lightcoral",
            edgecolor="darkred",
            hatch="//",
            linewidth=1.5
        )

    else:

        box.set(
            facecolor="lightblue",
            edgecolor="navy",
            hatch="\\\\",
            linewidth=1.5
        )

# Median Lines
for median in bp["medians"]:
    median.set(
        color="black",
        linewidth=2
    )

# Whiskers & Caps
for whisker in bp["whiskers"]:
    whisker.set(color="black", linewidth=1.2)

for cap in bp["caps"]:
    cap.set(color="black", linewidth=1.2)

# Outliers
for i, flier in enumerate(bp["fliers"]):

    if "2023" in conference_order[i]:

        flier.set(
            marker="o",
            markerfacecolor="red",
            markeredgecolor="darkred",
            markersize=6
        )

    else:

        flier.set(
            marker="s",
            markerfacecolor="blue",
            markeredgecolor="navy",
            markersize=6
        )

# X-axis Labels
conference_labels = [
    conf.rsplit("-", 1)[0]
    for conf in conference_order
]

year_labels = [
    conf.rsplit("-", 1)[1]
    for conf in conference_order
]

xtick_labels = [
    f"{conf}\n{year}"
    for conf, year in zip(conference_labels, year_labels)
]

ax.set_xticks(np.arange(1, len(conference_order)+1))

ax.set_xticklabels(
    xtick_labels,
    rotation=45,
    ha="right",
    fontsize=10
)

# Labels & Title
ax.set_ylabel(
    "Paper Citations",
    fontsize=12,
    fontweight="bold"
)

ax.set_xlabel(
    "Conference",
    fontsize=12,
    fontweight="bold"
)

ax.set_title(
    "Citation Distribution Across Major IoT Conferences",
    fontsize=14,
    fontweight="bold"
)

# Grid
ax.grid(
    axis="y",
    linestyle="--",
    alpha=0.4
)

# Legend
legend_elements = [
    Patch(
        facecolor="lightcoral",
        edgecolor="darkred",
        hatch="//",
        label="2023"
    ),
    Patch(
        facecolor="lightblue",
        edgecolor="navy",
        hatch="\\\\",
        label="2024"
    )
]

ax.legend(
    handles=legend_elements,
    loc="upper right",
    fontsize=10,
    frameon=True,
    edgecolor="black"
)

# Save Figure
plt.tight_layout()

plt.savefig(
    "Figure2_Selected_Conference_Boxplot.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("1. Figure2_Selected_Conference_Boxplot.png")