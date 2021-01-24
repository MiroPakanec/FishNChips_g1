import os
import numpy as np
from ont_fast5_api.fast5_interface import get_fast5_file

class TestLoader():
    def __init__(self, directory, window_size, window_stride):
        self.directory = directory
        self.window_size = window_size
        self.window_stride = window_stride
        self.read_files = self.get_read_files()
        self.position = 0

    def get_read_files(self):
        filenames = []
        for file in os.listdir(self.directory):
            if file.endswith('.fast5') == False:
                continue
            filenames.append(file)
        return filenames

    def get_read(self):
        filepath = f'{self.directory}/{self.read_files[self.position]}'
        self.position += 1
        dacs, read_id = self.load_file(filepath)  
        dacs = self.normilize(dacs)     
        windows = self.segment_read(dacs)
        return windows, read_id
              
    def segment_read(self, dacs):
        windows = []
        while len(dacs) > self.window_size:
            window = dacs[:self.window_size]
            windows.append(window)
            dacs = dacs[self.window_stride:]
        return windows
    
    def normilize(self, dacs):
        dacs = np.array(dacs)
        mean = np.mean(dacs)
        standard_dev = np.std(dacs)
        return (dacs - mean)/standard_dev

    def load_file(self, filepath):
        with get_fast5_file(filepath, mode="r") as f5:
            read_ids = f5.get_read_ids()
            assert len(read_ids) == 1, f'File {filepath} contains multiple reads.'    
            
            for read in f5.get_reads():
                dacs = read.get_raw_data()
                return dacs, read.read_id
