
def flatten(d):
    res = {}
    for item in d:
        if isinstance(d[item], dict):
            for key, value in flatten(d[item]).items():
                key = "{}.{}".format(item, key)
                res.update({key: value})
        else:
            res.update({item: d[item]})
    return res


if __name__ == '__main__':
    test_dict = {
        "a": 5,
        "b": 6,
        "c": {
            "f": 9,
            "g": {
                "m": 17,
                "n": 3
            }
        }
    }
    print(flatten(test_dict))