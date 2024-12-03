import os
import click
from rich import print
from files.walk import walk
from files.filter import filter_code_files
from rich.progress import BarColumn, Progress, TextColumn, TimeElapsedColumn
from pathlib import Path


@click.group()
def cli():
    pass


@cli.command()
def version():
    print("Readagen [green]0.1.0[/green]")


@cli.command()
@click.option(
    "--dir",
    "-d",
    default=".",
    help="List the files that are taken into context.",
    type=click.Path(exists=True),
)
def peek(dir):
    dir = walk(dir)
    files = []
    with Progress(
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TimeElapsedColumn(),
        transient=True,
    ) as progress:
        task = progress.add_task("[cyan]Peeking...", total=os.path.getsize("."))
        for p in dir:
            progress.update(task, advance=1)
            files.append(Path(p))

    code_files = filter_code_files(files)
    print(code_files)

@cli.command()
@click.option("--template", "-t", help="The template to use.", default="default", required=False, show_default=True)
@click.option("--output", "-o", help="The output file.", default="README.md", type=click.File("w"), required=False, show_default=True)
@click.option("--dir", "-d", help="The directory to generate the README.md from.", default=".", type=click.Path(exists=True), required=False, show_default=True)
@click.option("--ollama", help="Enable the use of Ollama", is_flag=True)
@click.option("--model", help="The model to use for Ollama", default="llama7", show_default=True)
def generate(template, output, dir, ollama, model):
    print("Generating README.md")
    print(template, output, dir, ollama, model)
