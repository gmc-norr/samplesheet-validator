from pytest import raises

from samplesheet_validator.samplesheet import Samplesheet, ValidationError
from tests.fixtures import empty_samplesheet


def test_empty_samplesheet(empty_samplesheet):
    samplesheet = Samplesheet(empty_samplesheet)
    with raises(ValidationError):
        samplesheet.validate(["Sample_ID"])
