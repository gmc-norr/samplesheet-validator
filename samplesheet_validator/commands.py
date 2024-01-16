import click
from pathlib import Path
import sys

from samplesheet_validator.samplesheet import Samplesheet, ValidationError


@click.command()
@click.version_option()
@click.argument(
    "samplesheet",
    type=click.Path(exists=True, dir_okay=False, resolve_path=True, path_type=Path),
)
def cli(samplesheet):
    """Validate an Illumina samplesheet"""
    ss = Samplesheet(samplesheet)
    try:
        ss.validate(["Sample_ID"])
    except ValidationError as ve:
        print("validation failed")
        print(ve)
        sys.exit(1)

    print("validation ok")
