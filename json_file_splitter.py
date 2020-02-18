import json

with open('<FILE_NAME>.json', 'r') as infile:
    o = json.load(infile)
    chunkSize = 10000  # Adjust as per your requirement
    for i in range(0, len(o), chunkSize):
        with open('p_temp' + '_' + str(i//chunkSize) + '.json', 'w') as outfile:
            json.dump(o[i:i+chunkSize], outfile)
