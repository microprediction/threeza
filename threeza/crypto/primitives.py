import uuid

# Conventions used at www.3za.org
# Discuss at https://algorithmia.com/algorithms/threezakeys/Hash/discussion

def hash5(key):
	return str(uuid.uuid5(uuid.NAMESPACE_DNS, key))

def to_public(privateKey):
	return hash5(hash5(privateKey))

def random_key():
	return str(uuid.uuid4())
