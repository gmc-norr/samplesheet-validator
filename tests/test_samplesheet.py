from pytest import raises

from samplesheet_validator.samplesheet import Samplesheet, ValidationError
from tests.fixtures import empty_samplesheet_path


def test_empty_samplesheet(empty_samplesheet_path):
    samplesheet = Samplesheet(empty_samplesheet_path)
    with raises(ValidationError):
        samplesheet.validate(["Sample_ID"])
