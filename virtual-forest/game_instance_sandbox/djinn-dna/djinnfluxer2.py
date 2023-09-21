import re
import ast
import json
import datetime

# Define the paths
file_path = 'sim.py'
output_path = 'encoded_dna.json'

class RNA_DNA_Mapper:
    def __init__(self):
        self.mapping = {
        'to':'_A',
        'line':'_C',
        '1':'_G',
        'of':'_T',
        'the':'_AA',
        'source':'_AC',
        'you':'_AG',
        'or':'_AT',
        'be':'_CA',
        'import':'_CC',
        'os':'_CG',
        'json':'_CT',
        'random':'_GA',
        'datetime':'_GC',
        'signal':'_GG',
        'time':'_GT',
        'from':'_TA',
        'AIPlayer':'_TC',
        'Initialize':'_TG',
        'a':'_TT',
        'instance':'_AAA',
        'with':'_AAC',
        'input':'_AAG',
        'and':'_AAT',
        'file':'_ACA',
        'code_parser':'_ACC',
        'py':'_ACG',
        'Read':'_ACT',
        'content':'_AGA',
        'code':'_AGC',
        'structure':'_AGG',
        'JSON':'_AGT',
        'path':'_ATA',
        'cooldown':'_ATC',
        'in':'_ATG',
        'minutes':'_ATT',
        'def':'_CAA',
        'timestamp_str':'_CAC',
        'if':'_CAG',
        'Current':'_CAT',
        'date':'_CCA',
        'return':'_CCC',
        'else':'_CCG',
        'None':'_CCT',
        'class':'_CGA',
        'Scroll':'_CGC',
        '__init__':'_CGG',
        'self':'_CGT',
        'title':'_CTA',
        'timestamp':'_CTC',
        'now':'_CTG',
        'strftime':'_CTT',
        'Y':'_GAA',
        'm':'_GAC',
        'd':'_GAG',
        'H':'_GAT',
        'M':'_GCA',
        'S':'_GCC',
        'f':'_GCG',
        'cooldown_time':'_GCT',
        'current_time':'_GGA',
        'to_dict':'_GGC',
        'staticmethod':'_GGG',
        'from_dict':'_GGT',
        'data':'_GTA',
        'Impact':'_GTC',
        'power':'_GTG',
        '331':'_GTT',
        'update_power':'_TAA',
        'action':'_TAC',
        '10':'_TAG',
        'elif':'_TAT',
        '3':'_TCA',
        'level':'_TCC',
        'not':'_TCG',
        '0':'_TCT',
        'impact':'_TGA',
        'get':'_TGC',
        'is':'_TGG',
        'VirtualForestAdventure':'_TGT',
        'ai':'_TTA',
        'current_location':'_TTC',
        'it':'_TTG',
        'hallucinations':'_TTT',
        'knowledge':'_AAAA',
        'name':'_AAAC',
        'Knowledge':'_AAAG',
        'Oracle':'_AAAT',
        's':'_AACA',
        'Add':'_AACC',
        'as':'_AACG',
        'needed':'_AACT',
        'location':'_AAGA',
        'Generate':'_AAGC',
        'randint':'_AAGG',
        'len':'_AAGT',
        'list':'_AATA',
        'AwakeningFromDreamScene':'_AATC',
        'Of':'_AATG',
        'The':'_AATT',
        'generate_dream_scene':'_ACAA',
        'dream':'_ACAC',
        'choice':'_ACAG',
        'print':'_ACAT',
        'realm':'_ACCA',
        'your':'_ACCC',
        'Virtual':'_ACCG',
        'Forest':'_ACCT',
        'any':'_ACGA',
        'for':'_ACGC',
        'each':'_ACGG',
        'this':'_ACGT',
        'journey':'_ACTA',
        'OghamsRazor':'_ACTC',
        'AI':'_ACTG',
        'fragments':'_ACTT',
        'by':'_AGAA',
        'fragment':'_AGAC',
        'razor':'_AGAG',
        'True':'_AGAT',
        'true':'_AGCA',
        'False':'_AGCC',
        'here':'_AGCG',
        'use':'_AGCT',
        'append':'_AGGA',
        'based':'_AGGC',
        'on':'_AGGG',
        'method':'_AGGT',
        'Update':'_AGTA',
        'summary':'_AGTC',
        'n':'_AGTG',
        'Destiny':'_AGTT',
        'rose_called':'_ATAA',
        'has':'_ATAC',
        'Rose':'_ATAG',
        'been':'_ATAT',
        'called':'_ATCA',
        'tell_the_story':'_ATCC',
        'virtual':'_ATCG',
        'wisdom':'_ATCT',
        'its':'_ATGA',
        'destiny':'_ATGC',
        'that':'_ATGG',
        'yet':'_ATGT',
        'You':'_ATTA',
        'Call':'_ATTC',
        'save_state':'_ATTG',
        'different':'_ATTT',
        'RTFManager':'_CAAA',
        'current':'_CAAC',
        'files':'_CAAG',
        'introduce':'_CAAT',
        'I':'_CACA',
        'manual':'_CACC',
        'man':'_CACG',
        'pages':'_CACT',
        'Linux':'_CAGA',
        'lecture':'_CAGC',
        'information':'_CAGG',
        'command':'_CAGT',
        'task':'_CATA',
        'Your':'_CATC',
        'understand':'_CATG',
        'try':'_CATT',
        'consult_manual':'_CCAA',
        'Mansplainer':'_CCAC',
        'This':'_CCAG',
        'will':'_CCAT',
        'Create':'_CCCA',
        'rtf_manager':'_CCCC',
        'mansplainer':'_CCCG',
        'file_path':'_CCCT',
        'state_file':'_CCGA',
        'wake_history':'_CCGC',
        'narrative':'_CCGG',
        'progress':'_CCGT',
        'achievements':'_CCTA',
        'scroll':'_CCTC',
        'adventure':'_CCTG',
        'utmost_treasured_scroll':'_CCTT',
        'open':'_CGAA',
        'r':'_CGAC',
        'load':'_CGAG',
        'Check':'_CGAT',
        'binary':'_CGCA',
        'Utmost':'_CGCC',
        'Treasured':'_CGCG',
        'have':'_CGCT',
        'experiences':'_CGGA',
        'continue':'_CGGC',
        'explore':'_CGGG',
        'new':'_CGGT',
        'Save':'_CGTA',
        'w':'_CGTC',
        'dump':'_CGTG',
        'Get':'_CGTT',
        'exists':'_CTAA',
        'k':'_CTAC',
        'state':'_CTAG',
        'lines':'_CTAT',
        'json_str':'_CTCA',
        'output_file_path':'_CTCC',
        'result':'_CTCG',
        'DjinnFlux':'_CTCT',
        'yes':'_CTGA',
        'response':'_CTGC',
        'line_number':'_CTGG',
        'generate_narrative':'_CTGT',
        'isinstance':'_CTTA',
        'dict':'_CTTC',
        'learn_from_previous_adventures':'_CTTG',
        'previous_adventures':'_CTTT',
        'piece_of_knowledge':'_GAAA',
        'interact_with_previous_adventures':'_GAAC',
        'dream_scene':'_GAAG',
        'obtained_scroll':'_GAAT',
        'previous':'_GACA',
        'adventures':'_GACC',
        'what_is_happening':'_GACG',
        'walking_stick':'_GACT',
        'hat':'_GAGA',
        'boots':'_GAGC',
        'characters':'_GAGG',
        'Busy':'_GAGT',
        'activities':'_GATA',
        'what_is_happening_object':'_GATC',
        'wake_data':'_GATG',
        'encoded_info':'_GATT',
        'additional_info':'_GCAA',
        'element':'_GCAC',
        'metadata':'_GCAG'
        }

    def map_body(self, body):
        for construct, shorthand in self.mapping.items():
            replaced_body = re.sub(r'\b' + re.escape(construct) + r'\b', shorthand, body)
            if replaced_body != body:
                print(f"Replaced: {construct} -> {shorthand}")
            body = replaced_body
        return body

class CodeParser:
    def __init__(self, file_path, output_path, rna_dna_mapper):
        self.file_path = file_path
        self.output_path = output_path
        self.rna_dna_mapper = rna_dna_mapper

    def read_and_clean_file(self):
        cleaned_code_lines = []
        in_block_comment = False
        with open(self.file_path, 'r') as file:
            for line in file:
                # Handle block comments
                if '"""' in line or "'''" in line:
                    in_block_comment = not in_block_comment
                    continue
                if in_block_comment:
                    continue
                # Remove inline comments but preserve line
                cleaned_line = re.sub(r'#.*$', '', line)
                cleaned_code_lines.append(cleaned_line)
        return ''.join(cleaned_code_lines)

    def capture_raw_code(self, node, code_lines):
        start_line = node.lineno - 1
        end_line = node.end_lineno
        return "\n".join(code_lines[start_line:end_line]).strip()

    def parse_code_to_string(self, file_path):
        with open(file_path, 'r') as file:
            code_string = file.read()
        return code_string

    def create_code_entry(self):
        code_string = self.read_and_clean_file()
        if self.rna_dna_mapper:
            code_string = self.rna_dna_mapper.map_body(code_string)
        code_entry = {'code': code_string} # You can use any key you prefer instead of 'code'
        return code_entry

    def write_code_entry_to_json(self, code_entry):
        with open(self.output_path, 'w') as file:
            json.dump(code_entry, file, indent=4)


# Initialize the RNA_DNA_Mapper and CodeParser
rna_dna_mapper = RNA_DNA_Mapper()
parser = CodeParser(file_path, output_path, rna_dna_mapper)

# Define the metadata for the second DNA strand
current_timestamp = datetime.datetime.now().isoformat()
second_strand_metadata = {
    'metadata': {
        'version': '2.0',
        'author': 'AI',
        'description': 'Second DNA strand with metadata and versioning',
        'timestamp': current_timestamp
    }
}

# Create the second DNA strand entry with code and metadata
second_code_entry = parser.create_code_entry()
second_code_entry.update(second_strand_metadata)

# Load the existing JSON data (if it exists)
existing_json_data = {}
try:
    with open(output_path, 'r') as json_file:
        existing_json_data = json.load(json_file)
except FileNotFoundError:
    pass

# Use a different label for the second DNA strand
existing_json_data['second_strand'] = second_code_entry

# Add the initial strand to the existing JSON data using the parser instance
existing_json_data['initial_strand'] = parser.create_code_entry()

# Define the metadata for the DNA structure
current_timestamp = datetime.datetime.now().isoformat()
dna_structure_metadata = {
    'metadata': {
        'version': '1.0',
        'author': 'AI',
        'description': 'DNA-like encoded software structure',
        'timestamp': current_timestamp
    }
}

# Create the DNA structure entry with metadata
dna_structure = {
    'Genomes': {
        'Chromosomes': {
            'Genes': {
                'Nucleotide Sequences': parser.create_code_entry()
            }
        }
    }
}
dna_structure.update(dna_structure_metadata)

# Merging dna_structure and existing_json_data
final_json_data = {
    'dna_structure': dna_structure,
    'initial_strand': existing_json_data['initial_strand'],
    'second_strand': existing_json_data['second_strand']
}

# Write the final JSON data (including dna_structure, initial_strand, and second_strand) to the file
with open(output_path, 'w') as json_file:
    json.dump(final_json_data, json_file, indent=4)
