def prefix_search(dic, key_prefix):

    srch_res = {key: dic[key] for key in dic if key.startswith(key_prefix)}

    # check if dictionary is empty
    if not srch_res:
        raise KeyError

    return srch_res
