import matplotlib.pyplot as plt


def plot_price(df):

    plt.figure(figsize=(16,6))

    plt.plot(
        df["Date"],
        df["Price"],
        color="steelblue"
    )

    plt.title("Historical Brent Oil Prices")

    plt.xlabel("Year")

    plt.ylabel("Price (USD/Barrel)")

    plt.grid(True)

    plt.show()


def plot_log_returns(df):

    plt.figure(figsize=(16,5))

    plt.plot(
        df["Date"],
        df["LogReturn"],
        color="darkred",
        linewidth=0.7
    )

    plt.title("Daily Log Returns")

    plt.xlabel("Year")

    plt.ylabel("Log Return")

    plt.grid(True)

    plt.show()


def plot_volatility(df):

    plt.figure(figsize=(16,5))

    plt.plot(
        df["Date"],
        df["RollingVolatility"],
        color="purple"
    )

    plt.title("30-Day Rolling Volatility")

    plt.xlabel("Year")

    plt.ylabel("Volatility")

    plt.grid(True)

    plt.show()

def plot_change_point(df, tau):

    import matplotlib.pyplot as plt

    plt.figure(figsize=(16,6))

    plt.plot(
        df["Date"],
        df["Price"],
        label="Brent Price"
    )

    plt.axvline(
        df.iloc[tau]["Date"],
        color="red",
        linestyle="--",
        linewidth=2,
        label="Estimated Change Point"
    )

    plt.legend()

    plt.title("Estimated Bayesian Change Point")

    plt.show()
def plot_change_points(oil_df, breakpoints):

    plt.figure(figsize=(16,6))

    plt.plot(
        oil_df["Date"],
        oil_df["Price"],
        color="steelblue",
        linewidth=1.5,
        label="Brent Price"
    )

    for i, bp in enumerate(breakpoints[:-1]):
        plt.axvline(
            oil_df.iloc[bp]["Date"],
            color="red",
            linestyle="--",
            alpha=0.7,
            label="Change Point" if i == 0 else None
        )

    plt.title("Detected Structural Breaks in Brent Oil Prices")
    plt.xlabel("Year")
    plt.ylabel("Price (USD/Barrel)")
    plt.legend()
    plt.tight_layout()
    plt.show()

import matplotlib.pyplot as plt


def plot_change_points_with_events(
    oil_df,
    events_df,
    breakpoints,
    figsize=(18, 6)
):
    """
    Plot Brent oil prices with detected change points
    and historical events.

    Parameters
    ----------
    oil_df : pd.DataFrame
        Oil price dataframe.

    events_df : pd.DataFrame
        Historical events dataframe.

    breakpoints : list
        Detected breakpoint indices.

    figsize : tuple
        Figure size.
    """

    plt.figure(figsize=figsize)

    # Oil prices
    plt.plot(
        oil_df["Date"],
        oil_df["Price"],
        color="steelblue",
        linewidth=1.5,
        label="Brent Price"
    )

    # Detected change points
    for i, bp in enumerate(breakpoints[:-1]):

        plt.axvline(
            oil_df.iloc[bp]["Date"],
            color="red",
            linestyle="--",
            alpha=0.8,
            label="Detected Change Point" if i == 0 else None
        )

    # Historical events
    for i, row in events_df.iterrows():

        plt.axvline(
            row["Date"],
            color="green",
            linestyle=":",
            alpha=0.7,
            label="Historical Event" if i == 0 else None
        )

    plt.title("Detected Change Points vs Historical Events")

    plt.xlabel("Year")

    plt.ylabel("Brent Price (USD/Barrel)")

    plt.legend()

    plt.tight_layout()

    plt.show()