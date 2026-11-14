import matplotlib.pyplot as plt


def plot_age_gap(df):
    fig, ax = plt.subplots()
    for result, color in [("W", "tab:blue"), ("L", "tab:red")]:
        part = df[df["result"] == result]
        ax.scatter(part["player_age"], part["age_diff"], c=color, label=result, s=15)
    ax.set_xlabel("Player age")
    ax.set_ylabel("Age difference (player - opponent)")
    ax.legend()
    return fig
