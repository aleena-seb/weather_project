"""weather data reader csv, station rdu"""

import sys
from typing import List, Dict
from csv import DictReader

def main() -> None:
    """entry point of program"""
    args : Dict[str, str] = read_args()
    file = args["file_path"]
    col_name = args["column_name"]
    oper = args["operation"]

    if col_name not in headers(file):
            print("Invalid column: " + col_name)
            exit()

    values = lists(file, col_name)
    if oper == "list":
        print(values)
    elif oper == "min":
        print(min(values))
    elif oper == "max":
        print(max(values))
    elif oper == "avg":
        print(sum(values)/(len(values)))
    else: 
        print("Invalid operation: " + oper)
        exit()
    

def read_args()  -> Dict[str, str]:
    """checks for valid CLI args and returns dict"""
    if len(sys.argv ) != 4:
        print("Usage: python -m projects.pj01.weather [FILE] [COLUMN] [OPERATION]]")
        exit()

    return{
        "file_path" : sys.argv[1],
        "column_name" : sys.argv[2],
        "operation" : sys.argv[3]
    }

def lists(file_path: str, column : str)-> List:
    file_handle = open(file_path, "r", encoding = "utf8")
    csv_reader = DictReader(file_handle)
    
    results_list : List[float] = []

    for row in csv_reader:
        if row["REPORT_TYPE"] == "SOD  ":
                try:
                    results_list.append(float(row[column]))
                except ValueError:
                    ... # Ignore an invalid value!     
    file_handle.close()
    return results_list

def headers(file_path : str) -> List[str]:
    file_handle = open(file_path, "r", encoding = "utf8")
    csv_reader = DictReader(file_handle)
    header_list = (list(csv_reader)[0]).keys()
    return header_list
         

if __name__ =="__main__":
    main()