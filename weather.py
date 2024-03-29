import argparse
import configparser
def read_user_cli_args():
    """handles the climate user interactions
    Returns:
    argparse.NmaeSpace: Populated namespace object
    """
    parser=argparse.ArgumentParser(description="gets weather and temperature information fo a city")
    parser.add_argument("city", nargs="+", type=str, help="enter the city name")
    parser.add_argument("-i","--imperial", action="store_true", help="display the temperature in imperial units",)
    return parser.parse_args()
if __name__=="__main__":
    read_user_cli_args()
