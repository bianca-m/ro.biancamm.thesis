'''
Created on Feb 26, 2014

@author: Bianca
'''
from metadata.metadata_processor import MetadataProcessor
import os
from idlelib.run import exit_now
import sys
import csv

METADATA_DIR = 'e:\\Thesis\\Pictures\\City\\'

CSV_HEADERS = ['FILENAME', 'Photo URL', 'TITLE', 'Photographer', 'Views', 
               'Comments', 'Upload Date', 'Taken Date', 'TAGS', 'Geotag Info',
               'License',  'DESCRIPTION']
def write_to_csv(all_metadata, csv_filename):
    csvfile = open(csv_filename, 'wb')
    metadata_writer = csv.DictWriter(csvfile, fieldnames=CSV_HEADERS)
    metadata_writer.writeheader()
    for file_metadata in all_metadata:
        metadata_writer.writerow(file_metadata)
    
    
if __name__ == '__main__':
    processor = MetadataProcessor()
    all_metadata = []
    for file in os.listdir(METADATA_DIR):
        if (file.endswith('.txt')):
            processor.read_metadata(METADATA_DIR + file)
            processor.metavalues['FILENAME'] = file
            all_metadata.append(processor.metavalues.copy())
    write_to_csv(all_metadata, METADATA_DIR + 'metadata.csv')
    
        
    
    