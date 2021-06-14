# -*- coding: utf-8 -*-
"""
Console script for {{cookiecutter.project_slug}}.
"""

import typer
import sys

app = typer.Typer(
    name="{{cookiecutter.project_slug}}",
    add_completion=False,
    help="{{cookiecutter.description}}",
)

@app.command()
def my_command(
    param1: str = typer.Argument(..., help="param1"),
    param2: float = typer.Argument(1, help="param2"),
):
    """
    my description
    """
    print(param1,param2)


if __name__ == "__main__":
    app()
