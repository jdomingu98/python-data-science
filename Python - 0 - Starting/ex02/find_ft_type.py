def all_thing_is_obj(object: any) -> int:
	allowed_types = {
		list: "List",
		tuple: "Tuple",
		set: "Set",
		dict: "Dict",
		str: "String",
	}

	class_type = type(object)
	prelude = allowed_types.get(class_type, "Type not found")

	if class_type == str:
		prelude = f"{object} is in the kitchen"
	print(prelude if prelude == "Type not found" else f"{prelude} : {class_type}") 
	return 42