"""Keep descriptive budget uncertainty at the scale of the observed values."""
from __future__ import annotations

import math
import numpy as np
import pytest
from multiagent_elbo.realizations.gaussian.continuous_budget_experiment import _estimate


@pytest.mark.parametrize("scale", [1., 1e-216])
def test_standard_error_preserves_the_scale_of_three_distinct_values(scale: float) -> None:
    values = scale*np.array([1., 2., 3.])
    estimate = _estimate(values)
    assert math.isclose(estimate["mean"], 2*scale, rel_tol=1e-14, abs_tol=0.)
    assert math.isclose(estimate["standard_error"], scale/math.sqrt(3.), rel_tol=1e-14, abs_tol=0.)


def test_zero_budget_has_zero_empirical_uncertainty() -> None:
    assert _estimate(np.zeros(3)) == {"mean": 0., "standard_error": 0.}
