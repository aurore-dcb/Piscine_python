def all_thing_is_obj(object: any = None) -> int:
    obj_type = type(object)
    if obj_type is list:
        print("List :", obj_type)
    elif obj_type is tuple:
        print("Tuple :", obj_type)
    elif obj_type is set:
        print("Set :", obj_type)
    elif obj_type is dict:
        print("Dict :", obj_type)
    elif obj_type is str:
        print(f"{object} is in the kitchen : {obj_type}")
    else:
        print("Type not found")
    return (42)
