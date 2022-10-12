from solution.reader import Reader
import csv


def create_csv(xml_file):
    filename = xml_file

    # create reader object
    reader = Reader()
    csv_file = ""
    csv_header = ""
    continue_writing = False

    # calling xml_reader function
    data = reader.xml_reader(filename)
    data_list = data.strip().split("\n")

    # calling data_validation function
    if reader.data_validation(data_list):
        for line in data_list:
            if line.strip().startswith("100"):
                csv_header = line
            # if line start with 200 create a csv file
            elif line.strip().startswith("200"):
                row_200 = line
                csv_filename = row_200.split(",")[1] + ".csv"
                if csv_file:
                    csv_file.write("900")
                    csv_file.close()
                csv_file = open(csv_filename, "w", encoding="utf-8")
                csv_file.write(csv_header)
                csv_file.write("\n")
                csv_file.write(row_200)
                csv_file.write("\n")
                continue_writing = True
            elif line.strip().startswith("300"):
                if continue_writing:
                    csv_file.write(line)
                    csv_file.write("\n")
            elif line.strip().startswith("900"):
                csv_file.write("900")
                break
        csv_file.close()
        return "CSV files generated successfully!"
    else:
        return False


if __name__ == "__main__":
    xml = "testfile.xml"
    print(create_csv(xml))
