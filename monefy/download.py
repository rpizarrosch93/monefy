"""Download data from google drive."""

# Download a csv file from google drive
# https://stackoverflow.com/questions/38511444/python-download-files-from-google-drive-using-url


from pathlib import Path

import pandas as pd


class GoogleDriveCSV:
    """Class to download csv data from google drive."""

    def __init__(self, url: str, output: str, file_id: str = None):
        """Initialize class."""
        self.url = url
        self.file_id = file_id
        # Get data folder path from monefy/__init__.py
        __sources = ((Path(__file__).parent).resolve(),)

        self.output = str(__sources[0] / "data" / f"{output}")

        print("Downloading data from google drive...")
        self.dataframe = self.download_data_from_shared_link()
        print("Data downloaded!")

    def __get_id_from_url(self, url: str) -> str:
        """Parse url to get id."""

        # Get the second to last element from the url to get the file id
        file_id = url.split("/")[-2]

        return file_id

    def download_data_from_shared_link(self) -> pd.DataFrame:
        """Download data from shared link."""
        file_id = self.file_id if self.file_id else self.__get_id_from_url(self.url)

        download_url = "https://drive.google.com/uc?id=" + file_id
        df = pd.read_csv(download_url)

        # Save data to csv
        print(f"Saving data to {self.output}...")
        df.to_csv(self.output, index=False)

        return df
