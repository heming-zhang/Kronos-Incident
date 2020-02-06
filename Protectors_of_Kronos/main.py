from parse import ParseFile
from analysis import Analyze

def parse_article():
    dir_name = "./A1_Data/articles/"
    ParseFile(dir_name, "0").read_article()

def parse_email():
    ParseFile("0", "0").filter_email()

def analyze():
    Analyze("0", "0").email_network()
    # Analyze("0", "0").email_site_search()
    # Analyze("0", "0").article_site_search()

if __name__ == "__main__":
    # parse_article()
    # parse_email()
    analyze()