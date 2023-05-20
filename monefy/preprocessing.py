"""Module to preprocess data for the monefy app."""

import pandas as pd
from datetime import datetime

from pathlib import Path


class Formatter:
    """Class to preprocess raw data."""

    def __init__(
        self,
    ):
        """Initialize class."""

    def __filter_months_until_current_month(self, df: pd.DataFrame) -> pd.DataFrame:
        """Filter months until current month."""
        # Get current month from system date.
        current_month = datetime.now().replace(day=1).strftime("%Y-%m-%d")
        df = df[df["month"] <= current_month]
        return df

    def __format_date(self, df: pd.DataFrame) -> pd.DataFrame:
        """Format date column."""

        df["date"] = pd.to_datetime(df["date"], format="%d/%m/%Y")
        # Get start of the month for each date row.
        df["month"] = (
            df["date"] + pd.offsets.MonthEnd(0) - pd.offsets.MonthBegin(normalize=True)
        )

        return df

    def __str_to_float(self, column: pd.Series) -> pd.Series:
        column = column.apply(lambda x: x.replace('"', ""))
        column = column.apply(lambda x: x.replace('.', ""))
        column = column.apply(lambda x: x.replace(',', ""))
        column = column.apply(lambda x: float(x))

        return column

    def __format_amount(self, df: pd.DataFrame) -> pd.DataFrame:
        """Format amount column."""
        df_copy = df.copy()
        # Get rid of quotes and dots and commas from amount column to convert it to float.
        df_copy["amount"] = self.__str_to_float(df_copy["amount"])

        return df_copy

    def __aggregate_dataframe(self, df: pd.DataFrame) -> pd.DataFrame:
        """Group by month and category."""
        df = df.groupby(["month", "category"]).agg({"amount": "sum"})
        df = df.reset_index()
        return df

    def __pivot_grouped_dataframe(self, df: pd.DataFrame) -> pd.DataFrame:
        """Pivot grouped dataframe."""
        df = df.pivot(index="category", columns="month", values="amount")
        df = df.reset_index()
        df.fillna(0, inplace=True)
        return df

    def __save_dataframe(self, df: pd.DataFrame, output: str) -> None:
        """Save dataframe to csv."""

        __sources = ((Path(__file__).parent).resolve(),)

        output = str(__sources[0] / "data" / f"{output}")

        df.to_csv(output, index=False)

    def format_and_save(self, df: pd.DataFrame, output: str) -> pd.DataFrame:
        """Format data."""
        df = self.__format_date(df)
        df = self.__filter_months_until_current_month(df)
        df = self.__format_amount(df)

        df = self.__aggregate_dataframe(df)
        df = self.__pivot_grouped_dataframe(df)

        self.__save_dataframe(df, output)
        return df
