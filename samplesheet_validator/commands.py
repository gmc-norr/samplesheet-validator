import click


@click.command()
@click.version_option()
@click.argument("samplesheet")
def cli(samplesheet):
    """Validate an Illumina samplesheet"""
    pass
