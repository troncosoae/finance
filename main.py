from kernel.index import IndexFactory
from extraction.interface import PandasInterface


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
    print(index_universe["fintual"].print_recursive())
    print(index_universe["bchile"].print_recursive())

    pandas_interface = PandasInterface()
    x = pandas_interface.extract_index(index_universe["ezu"], "01-01-2021", "01-01-2022")
    print(x)
    # pandas_interface.extract_index(index_universe["bchile"], "01-01-2021", "01-01-2022")


if __name__ == "__main__":
    main()
