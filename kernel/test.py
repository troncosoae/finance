from index import IndexFactory


def main():
    json = {
        "indexes": {
            "ivv": "ivv",
            "ezu": "ezu",
            "ewg": "ewg"
        },
        "index_groups": {
            "fintual": [
                "ivv",
                "ezu"
            ],
            "bchile": [
                "ivv",
                "ewg",
                "fintual"
            ]
        }
    }
    index_universe = {}
    # TODO: maybe make these a special class in order to separate what goes into each
    index_factory = IndexFactory(json, index_universe)

    print(index_universe)
    # print(index_group_universe)
    # for group_key in index_group_universe:
    #     for index_key in index_group_universe[group_key].indexes:
    #         print(index_group_universe[group_key].indexes[index_key])
    print(index_universe["fintual"].print_recursive())
    print(index_universe["bchile"].print_recursive())




if __name__ == "__main__":
    main()
