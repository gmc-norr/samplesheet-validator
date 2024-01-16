from pathlib import Path
from pytest import fixture

VALID_SAMPLESHEET_STR = """
[Header]
IEMFileVersion,4
Institute,NUS
Instrument,NextSeq
[Settings]
Adapter,CTGTCTCTTATACACATCT
[Reads]
151
151
[Data]
Sample_ID,Sample_Name
S1,Sample1
S2,Sample2
S3,Sample3
S4,Sample4
"""


@fixture()
def empty_samplesheet_path(tmpdir):
    samplesheet = Path(tmpdir) / "empty_samplesheet.csv"
    samplesheet.touch()
    return samplesheet


@fixture()
def valid_samplesheet_path(tmpdir):
    samplesheet = Path(tmpdir) / "valid_samplesheet.csv"
    with samplesheet.open("w") as f:
        f.write(VALID_SAMPLESHEET_STR)
    return samplesheet
