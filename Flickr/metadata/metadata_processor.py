'''
Created on Feb 26, 2014

@author: Bianca
'''

class MetadataProcessor():
    '''
    classdocs
    '''
    

    def __init__(self):
        '''
        Constructor
        '''
        self.metavalues = dict()
        self.block_names = ['INFO', 'TITLE', 'DESCRIPTION', 'TAGS']
        
        
    def read_metadata(self, metadata_filename):
        self.metavalues.clear()
        
        metadata_file = open(metadata_filename, 'r')
        comment_mode = False
        current_block_name = ''
        block_line = ''
        lines = metadata_file.read().splitlines()
        
        for line in lines:
            # Skip empty lines.
            if len(line.strip()) == 0:
                continue
            
            # Start or end of a comment line.
            if line.startswith('+-') and line.endswith('-+'):
                comment_mode = not comment_mode
                # We have probably finished a previous block and we want to
                # store the value in the metavalues.
                if len(current_block_name) > 0 and len(block_line) > 0:
                    self.metavalues[current_block_name] = block_line
                block_line = ''
                continue
            
            # Inside the comment; potentially get block name, if it's in the
            # allowed set of block names.
            if comment_mode:
                comment_line = line.strip(' |')
                if (self.block_names.count(comment_line) > 0):
                    current_block_name = comment_line
                continue
            
            # We are looking for values for the current block name, or 
            # key : value pairs for INFO metadata.
            if (current_block_name == 'INFO'):
                tokens = line.split(':', 1)
                if len(tokens) < 2:
                    self.metavalues['OTHERS'] = tokens[0].strip()
                else:
                    key = tokens[0].strip()
                    value = tokens[1].strip()
                    self.metavalues[key] = value
            else:
                # We have simple value for the current block name, but might 
                # extend over multiple lines, therefore we have to cache it
                # and store it at the end.
                block_line += line.strip()
                #print('Asigning key: ' + current_block_name + ' with value: '+ self.metavalues[current_block_name])
        
        # Residual attribution.
        if len(current_block_name) > 0 and len(block_line) > 0:
            self.metavalues[current_block_name] = block_line
    
