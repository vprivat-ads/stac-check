import click
import json
from .lint.lint import Linter

def cli_message(file):
    linter = Linter(file)
    info = linter.parse_file()
    if info["stac_validator"]["version"] == "1.0.0":
        click.echo(click.style(info["update"], fg='green'))
    else:
        click.secho(info["update"], fg='red')
    click.echo(click.style("Validator: stac-validator 2.3.0 ", fg="blue"))
    if info["stac_validator"]["valid_stac"] == True:
        click.echo(click.style(f"Valid stac: {info['stac_validator']['valid_stac']}", fg='green'))
    else:
        click.echo(click.style(f"Valid stac: {info['stac_validator']['valid_stac']}", fg='red'))
    click.secho(json.dumps(info["stac_validator"], indent=4))

@click.command()
@click.argument('file')
def main(file):
    cli_message(file)