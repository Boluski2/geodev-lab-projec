# import pandas
import pandas as pd
import geopandas as gpd


def main():
    df = pd.read_csv("state.csv")
    print(df.info())



if __name__ == "__main__":
    main()