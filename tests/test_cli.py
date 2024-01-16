from click.testing import CliRunner

from samplesheet_validator.commands import cli
from tests.fixtures import empty_samplesheet_path, valid_samplesheet_path


def test_no_args():
    runner = CliRunner()
    result = runner.invoke(cli, [""])
    assert result.exit_code != 0


def test_empty_samplesheet(empty_samplesheet_path):
    runner = CliRunner(mix_stderr=False)
    result = runner.invoke(cli, [empty_samplesheet_path])
    assert result.stdout == ""
    assert "validation failed" in result.stderr
    assert result.exit_code != 0


def test_valid_samplesheet(valid_samplesheet_path):
    runner = CliRunner(mix_stderr=False)
    result = runner.invoke(cli, [valid_samplesheet_path])
    assert "validation: ok" in result.stdout
    assert result.exit_code == 0
