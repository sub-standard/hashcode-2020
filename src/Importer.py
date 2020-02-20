import os.path

class Importer:
    def __init__(self, filename : str) -> None:
        self.filename: str = filename

    # Read the input from the input file
    def import_data_set(self):
        if os.path.isfile(self.filename):
            with open(self.filename, 'r') as file:
                content = file.readlines()

                data = []

                # [Process the file here...]

                file.close()

                return data
        else:
            print("Error: File not found")
            raise FileNotFoundError
