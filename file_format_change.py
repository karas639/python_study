import json, os
import Proto import Tweet_pb2 as LogDataProto
import protobuf_to_dict import protobuf_to_dict

# text to json file
# input
output = os.popen('dir').read()
print(output)
filename=input("filename: ") # proto type

# read protobuf file
f = open(filename, "r")
try:
    logfile = LogDataProto.LogDataFile()
    logfile.ParseFromString(f.read())
except (IndexError, TypeError):
    print('index, type error')


# protobuf to json
logfile_dict = protobuf_to_dict(logfile)
json_string = json.dumps(logfile_dict, encoding='utf-8')

# write json file
new_filename = os.path.splittext(filename)[0] + '.json'
f = open(new_filename, 'w')
f.write(json_string.encode("utf-8"))
