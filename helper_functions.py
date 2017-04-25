

bases = {'Duck Boat': 5,
         'Pontoon': 4}

components = {'Pinstripe': 5,
              'Runway': 5,
              'Both': 9,
              'Neither': 0}


def make_weights_from_input_dict(input_dict, bases, components):
    weights = []
    types_list = []
    for key, val in input_dict.items():
        this_items_trailers = [bases[key[0]] + components[key[1]] for _ in range(val)]
        weights.extend(this_items_trailers)
        this_items_types = [key[0] + ' ' + key[1] for _ in range(val)]
        types_list.extend(this_items_types)

    return weights, types_list

