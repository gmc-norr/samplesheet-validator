import csv


class ValidationError(Exception):
    pass


class Samplesheet:
    def __init__(self, path, data_section="Data"):
        self._path = path
        self._data_section = data_section

    def _get_data_section(self):
        data_csv = []
        found_data = False
        with open(self._path, "r") as f:
            for line in f:
                if not found_data and line.startswith(f"[{self._data_section}]"):
                    found_data = True
                    continue
                if found_data and line[0] == "[":
                    break
                if found_data:
                    data_csv.append(line.strip())

        if not found_data:
            return None

        return csv.DictReader(data_csv)

    def validate(self, required_data_columns):
        samplesheet_data = self._get_data_section()

        if samplesheet_data is None:
            raise ValidationError(f"no data section found")

        if samplesheet_data.fieldnames is None or len(samplesheet_data.fieldnames) == 0:
            raise ValidationError(f"data section is empty")

        for col in required_data_columns:
            if col not in samplesheet_data.fieldnames:
                raise ValidationError(f"missing required column: {col}")

        return True
