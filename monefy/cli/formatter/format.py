import typer

from monefy.download import GoogleDriveCSV
from monefy.preprocessing import Formatter


def format(
    url: str = typer.Option(
        None,
        help="Shared URL of a .csv data file of monefy in google drive.",
    ),
    file_id: str = typer.Option(
        None,
        help="File id of a .csv data file of monefy in google drive.",
    ),
    output: str = typer.Option(
        "monefy_data.csv",
        help="Output filaname of the formatted data.",
    ),
) -> None:
    """Format monefy data given a google drive .csv url."""

    if not url and not file_id:  # noqa
        raise typer.BadParameter(
            "You must provide either a shared url or a file id to download the data."
        )

    else:
        # Download data
        downloader = GoogleDriveCSV(url=url, file_id=file_id, output=output)
        data = downloader.download_data_from_shared_link()

        # Format and save data
        formatter = Formatter()
        dataframe = formatter.format_and_save(data, output)
