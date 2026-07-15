import pymc as pm
import numpy as np
import arviz as az

def build_change_point_model(observed_data):
    """
    Build a Bayesian single change point model.

    Parameters
    ----------
    observed_data : numpy.ndarray
        Time series values (preferably log returns)

    Returns
    -------
    model : pm.Model
    """

    n = len(observed_data)

    with pm.Model() as model:

        # -------------------------------------------------
        # Prior for change point
        # -------------------------------------------------
        tau = pm.DiscreteUniform(
            "tau",
            lower=0,
            upper=n - 1
        )

        # -------------------------------------------------
        # Mean before change point
        # -------------------------------------------------
        mu_1 = pm.Normal(
            "mu_1",
            mu=np.mean(observed_data),
            sigma=np.std(observed_data) * 2
        )

        # -------------------------------------------------
        # Mean after change point
        # -------------------------------------------------
        mu_2 = pm.Normal(
            "mu_2",
            mu=np.mean(observed_data),
            sigma=np.std(observed_data) * 2
        )

        # -------------------------------------------------
        # Common standard deviation
        # -------------------------------------------------
        sigma = pm.HalfNormal(
            "sigma",
            sigma=np.std(observed_data)
        )

        # -------------------------------------------------
        # Time index
        # -------------------------------------------------
        time_index = np.arange(n)

        # -------------------------------------------------
        # Switch function
        # -------------------------------------------------
        mu = pm.math.switch(
            time_index < tau,
            mu_1,
            mu_2
        )

        # -------------------------------------------------
        # Likelihood
        # -------------------------------------------------
        pm.Normal(
            "likelihood",
            mu=mu,
            sigma=sigma,
            observed=observed_data
        )

    return model




def sample_model(model):

    with model:

        trace = pm.sample(
            draws=2000,
            tune=1000,
            chains=4,
            target_accept=0.95,
            random_seed=42,
            return_inferencedata=True
        )

    return trace

def summarize_trace(trace):

    return az.summary(
        trace,
        var_names=[
            "tau",
            "mu_1",
            "mu_2",
            "sigma"
        ]
    )

def plot_trace(trace):

    az.plot_trace(
        trace,
        var_names=[
            "tau",
            "mu_1",
            "mu_2",
            "sigma"
        ]
    )