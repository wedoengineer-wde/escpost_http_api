import os
from datetime import datetime


class Logger():
    
    def __init__(self , output_folder:str , output_format:str ) :
        self.output_folder = output_folder
        self.output_format = output_format 
        
    def _get_file_path(self) -> str:
        file_name = datetime.now().strftime ( self.output_format ) 
        return os.path.join(self.output_folder , file_name)
        
    def print_to_file(self, output : str ) -> bool:
        file_path = self._get_file_path()

        f = open(file_path, "wb")
        f.write(output)
        f.close()