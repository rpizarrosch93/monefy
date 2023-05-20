"""Package with commands to format monefy data."""
import typer

from .format import format


app = typer.Typer(help="Commands to format monefy data given a google drive .csv url.")
app.command()(format)
