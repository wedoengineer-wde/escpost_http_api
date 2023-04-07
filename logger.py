import os
from datetime import datetime


class Logger():

    def __init__(self, output_folder: str, output_format: str):
        self.output_folder = output_folder
        self.output_format = output_format
        self.create_output_folder(self.output_folder)

    def _get_file_path(self) -> str:
        file_name = datetime.now().strftime(self.output_format)
        return os.path.join(self.output_folder, file_name)

    def create_output_folder(self, folder: str):
        if not os.path.exists(folder):
            print(f"Creating {folder} folder")
            os.makedirs(folder)

    def print_to_file(self, output: bytes) -> bool:
        file_path = self._get_file_path()

        f = open(file_path, "ab")
        f.write(output)
        f.close()
