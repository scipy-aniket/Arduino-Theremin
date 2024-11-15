import json

def read(path):
    with open(path, 'r') as f:
        return f.read()
    
def read_json(path):
    return json.loads(read(path))

NOTE_MAP = read_json(r'C:\arduino code\Theremin\note_map.json')