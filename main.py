import pandas as pd

from session.session import IndexFactory
from extraction.interface import PandasInterface
from extraction.data_container import IndexDataExtractor
from analysis.analyzer import Analyzer


def main():
    json = {
        "indexes": {
            "ivv": "ivv",
            "ezu": "ezu",
            "ewg": "ewg",
            "ixc": "ixc",
            "tip": "tip",
            "aok": "aok",
            "swan": "swan",
            "icln": "icln",
            "mxi": "mxi",
            "iyh": "iyh",
            "iwv": "iwv",
            "iau": "iau",
            "xt": "xt"
        },
        "index_groups": {
            "bchile": {
                "ivv": 0.1,
                "ewg": 0.1,
                "ezu": 0.1,
                "ixc": 0.1,
                "tip": 0.1,
                "aok": 0.1,
                "swan": 0.1,
                "icln": 0.1,
                "mxi": 0.05,
                "iyh": 0.05,
                "iwv": 0.05,
                "iau": 0.05,
            },
            "fintual": {
                "ivv": 0.5,
                "ezu": 0.3,
                "bchile": 0.2
            },
            "total": {
                "bchile": 0.7,
                "fintual": 0.3
            }
        }
    }

    pandas_interface = PandasInterface()

    factory = IndexFactory()
    index_universe = factory.generate_session(json, pandas_interface)

    print(
        "index_universe is factory.index_session",
        index_universe is factory.index_session)

    print(index_universe)
    index_universe["total"].print_recursive()

    extractor = IndexDataExtractor(pandas_interface)

    print("extract")
    extractor.extract_data(
        index_universe["bchile"], "01-01-2015", "01-01-2022")

    print("total")
    print(extractor.index_data_container_map["ezu"].data)
    print(extractor.index_data_container_map["ivv"].data)

    print(extractor.index_data_container_map["bchile"].data["Close"])

    x = pd.DataFrame()
    x["ezu"] = extractor.index_data_container_map["ezu"].data
    x["ivv"] = extractor.index_data_container_map["ivv"].data
    print(x)

    print(extractor.index_data_container_map is index_universe.data_dict)

    analyzer = Analyzer()

    # TODO: add method to session to extract the data
    # analyzer.set_group(index_universe["bchile"], {
    #     "ezu": extractor.index_data_container_map["ezu"],
    #     "ivv": extractor.index_data_container_map["ivv"]
    # })
    # TODO: ensure that data has already been extrcted
    analyzer.set_group(
        index_universe["bchile"],
        index_universe.export_index_group_data("bchile")
    )

    print(analyzer.get_means())
    print(analyzer.get_correlations())
    print(analyzer.get_variances())


if __name__ == "__main__":
    main()
