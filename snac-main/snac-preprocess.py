import csv
from nltk.tokenize import sent_tokenize

def process_text_to_tsv(input_filename, chunk_size, output_filename):
    # Read the text file
    with open(input_filename, 'r') as file:
        text = file.read()
    
    # Use nltk's sent_tokenize to split text into sentences
    sentences = sent_tokenize(text)
    
    # Open the output TSV file
    with open(output_filename, 'w', newline='') as file:
        writer = csv.writer(file, delimiter='\t')
        
        # Write the header
        writer.writerow(['id', 'context', 'sentence'])
        
        n = len(sentences)
        for i in range(0, n, chunk_size):
            start_idx = i
            end_idx = i + chunk_size
            
            # Create the context by joining all previous sentences
            context = ' '.join(sentences[:start_idx])
            
            # Create the sentence chunk for the current row
            sentence_chunk = ' '.join(sentences[start_idx:end_idx])
            
            # Write the row to the TSV file
            writer.writerow(["{}-{}".format(start_idx, end_idx), context, sentence_chunk])

# Example usage
process_text_to_tsv('summary.txt', 1, 'output.tsv')
