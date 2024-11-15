"""Tests for the cleaning module"""
import pandas as pd

from life_expectancy.cleaning import load_data, clean_data, save_data
from . import OUTPUT_DIR


def test_clean_data(pt_life_expectancy_expected):
    """Run the `clean_data` function and compare the output to the expected output"""

    life_expectancy_data = load_data()
    processed_expectancy_data = clean_data(life_expectancy_data)
    save_data(processed_expectancy_data, "PT")

    pt_life_expectancy_actual = pd.read_csv(
        OUTPUT_DIR / "pt_life_expectancy.csv"
    )
    pd.testing.assert_frame_equal(
        pt_life_expectancy_actual, pt_life_expectancy_expected
    )
