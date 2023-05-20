"""Module for CLI commands to work with Monefy data formater."""

import typer
from .formatter import app as formatter

app = typer.Typer()
app.add_typer(formatter, name="formatter")
