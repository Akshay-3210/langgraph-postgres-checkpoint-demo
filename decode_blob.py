from pathlib import Path
import msgpack

# Postgresql me do layer me serialization implement ki gyi h "msgpack" ke through

blob = Path("message_blob.bin").read_bytes()

# pehli layer
outer = msgpack.unpackb(blob, raw=False, strict_map_key=False)

version, serialized = outer[0]

# dusri layer
message = msgpack.unpackb(serialized,raw=False,strict_map_key=False,)

print("version:", version)
print("decoded message:", message)