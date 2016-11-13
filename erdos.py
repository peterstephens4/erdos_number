import json

file_name = '/Users/peterstephens/Coursera Data Visualization/public/Erdos.txt'
out_file = '/Users/peterstephens/Coursera Data Visualization/public/Erdos.json'

with open(file_name) as f:
    lines = f.read().splitlines()

nodes = []
links = []
with open(out_file, 'w') as outfile:
    i = 0
    while i < len(lines):	 
        p = lines[i]
        vert = p[:4].strip()
        degree = p[5:8].strip()
        name = p[13:].strip()
        pubs = p[9:12].strip()
        edges = lines[i+1].split()
        
        data = {}
        data["id"] = int(vert)
        data["name"] = name
        data["group"] = int(degree)
        data["pubs"] = int(pubs)
        nodes.append(data)
        
        for j, val in enumerate(edges):
            data = {}
            data["source"] = int(vert)
            data["target"] = int(val)
            data["value"] = int(pubs)
            links.append(data)
            
        i +=2
        
    json_data = {}
    json_data["nodes"] = nodes
    json_data["links"] = links
    
    json.dump(json_data, outfile)
