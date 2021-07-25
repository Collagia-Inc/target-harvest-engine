"""Tests standard target features using the built-in SDK tests library."""

from singer_sdk.testing import get_standard_target_tests
from target_harvest_engine.target import TargetHarvestEngine


# Run standard built-in target tests from the SDK:
def test_standard_target_tests(sample_config):
    """Run standard target tests from the SDK."""
    tests = get_standard_target_tests(
        TargetHarvestEngine,
        config=sample_config,
    )
    for test in tests:
        test()
