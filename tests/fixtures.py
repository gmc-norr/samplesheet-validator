from pathlib import Path
from pytest import fixture


@fixture()
def empty_samplesheet(tmpdir):
    samplesheet = Path(tmpdir) / "samplesheet.csv"
    samplesheet.touch()
    return samplesheet
