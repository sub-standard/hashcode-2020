import os.path

class Importer:
    def __init__(self, filename : str) -> None:
        self.filename: str = filename

    # Read the input from the input file
    def import_data_set(self):
        if os.path.isfile(self.filename):
            with open(self.filename, 'r') as file:
                content = file.readlines()

                line1 = content[0].strip()
                parts = line1.split(" ")
                M = int(parts[0])
                N = int(parts[1])

                line2 = content[1].strip()
                parts2 = line2.split(" ")
                slices = []
                for part in parts2:
                    slices.append(int(part))

                file.close()

                return M, N, slices
        else:
            print("Error: File not found")
            raise FileNotFoundError
