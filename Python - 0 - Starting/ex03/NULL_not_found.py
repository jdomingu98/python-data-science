import math

def NULL_not_found(object: any) -> int:
	allowed_types = {
		None: "Nothing",
		0: "Zero",
		'': "Empty",
		False: "Fake",
	}

	class_type = type(object)
	prelude = allowed_types.get(object, "Type not found")
	result = 1 if prelude == "Type not found" else 0

	if class_type == str and object:
		prelude = "Type not found"
	elif class_type == float and math.isnan(object):
		prelude = "Cheese"
	print(prelude if prelude == "Type not found" else f"{prelude}: {object} {class_type}")
	return result