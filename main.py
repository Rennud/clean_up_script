import sys
from parser import main_parser


def main():
    # Which XML we want to parse
    specify_xml = sys.argv[1]
    # -s show desired files, -d delete desired files
    specify_option = sys.argv[2]
    # png for images, src for exercises 
    specify_file_type = sys.argv[3]
    main_parser(specify_xml, specify_option, specify_file_type)

if __name__ == "__main__":
    main()

