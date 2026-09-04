import matplotlib.pyplot as plt


def plot_sentiment_distribution(df):
    """
    Plot the distribution of sentiment scores.
    """

    fig, ax = plt.subplots(
        figsize=(8, 6)
    )

    ax.hist(
        df["sentiment"],
        bins=5,
        edgecolor="black"
    )

    plt.xticks(
        range(1, 6)
    )

    plt.xlabel(
        "Sentiment Score"
    )

    plt.ylabel(
        "Frequency"
    )

    plt.title(
        "Distribution of Sentiment Scores"
    )

    plt.show()
