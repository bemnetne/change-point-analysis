import ruptures as rpt
import numpy as np


def detect_change_points(signal, model="l2", penalty=10):
    """
    Detect structural breaks using the PELT algorithm.

    Parameters
    ----------
    signal : array-like
        Time series (Price or LogReturn)

    model : str
        Cost model

    penalty : int
        Penalty controlling number of breakpoints

    Returns
    -------
    list
        Breakpoint indices
    """

    # algo = rpt.Pelt(model=model)

    # algo.fit(np.asarray(signal))

    # breakpoints = algo.predict(pen=penalty)
    algo = rpt.Binseg(model="rbf")

    algo.fit(np.asarray(signal))

    breakpoints = algo.predict(n_bkps=6)

    return breakpoints