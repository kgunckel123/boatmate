
def make_weights_from_input_dict(input_dict, bases, components):
    weights = []
    types_list = []
    for key, val in sorted(input_dict.items(), key=lambda x: x[0][0] + x[0][1]):
        this_items_trailers = [bases[key[0]] + components[key[1]] for _ in range(val)]
        weights.extend(this_items_trailers)
        this_items_types = [key[0] + ' ' + key[1] for _ in range(val)]
        types_list.extend(this_items_types)

    return weights, types_list

