"""
Sample Test
"""
# pylint: disable=redefined-outer-name, unused-argument

import pytest
from buggycode.script3 import big_calc


@pytest.mark.parametrize("a,b", [(1, 2)])
def test_big_calc(a, b):
    """((a + b) * (a / b)) * ((a + b) * (a / b)) 
    (1 + 2) * (1 / 2) ^2  (3 * 0.5)^2 = (1.5)^2 = 2.25
    """
    assert(big_calc(a, b) == pytest.approx(2.25, 0.01))
    