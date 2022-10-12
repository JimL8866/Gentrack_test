import xml.etree.ElementTree as ET


class Reader:

    @staticmethod
    def xml_reader(filename):
        """
            use to reading .xml file with node of CSVIntervalData

        :param filename: xml file
        :return: boolean
        """
        tree = ET.parse(filename)
        root = tree.getroot()
        data = root.find("./Transactions/Transaction/MeterDataNotification/CSVIntervalData").text.strip()

        return data

    @staticmethod
    def data_validation(contents):
        """
            use to validating Data according to specific rules

        :param contents: list
        :return: boolean
        """
        start_with_100 = 0
        start_with_200 = 0
        start_with_300 = 0
        start_with_900 = 0
        for content in contents:
            # checking "200" and "300" can repeat and will be within the header and trailer rows
            if content.startswith("100"):
                if start_with_200 >= 1 or start_with_300 >= 1:
                    return False
                start_with_100 += 1
            elif content.startswith("200"):
                start_with_200 += 1
            elif content.startswith("300"):
                start_with_300 += 1
            elif content.startswith("900"):
                # checking "200" and "300" can repeat and will be within the header and trailer rows
                if start_with_200 == 0 or start_with_300 == 0 or start_with_100 == 0:
                    return False
                start_with_900 += 1

        # checking The CSVIntervalData element should contain at least 1 row for each of "100", "200", "300","900"
        if start_with_100 == 0 or start_with_200 == 0 or start_with_300 == 0 or start_with_900 == 0:
            return False
        # checking "100", "900" rows should only appear once inside the CSVIntervalData element
        if start_with_100 > 1 or start_with_900 > 1:
            return False

        # checking "200" row must be followed by at least 1 "300" row
        data_block_index = []
        for i in range(len(contents)):
            if contents[i].startswith("200"):
                data_block_index.append(i)
            if contents[i].startswith("900"):
                data_block_index.append(i)
        for m in range(len(data_block_index)-1):
            row_300 = 0
            for content in contents[data_block_index[m]:data_block_index[m+1]]:
                if content.startswith("300"):
                    row_300 += 1
            if row_300 == 0:
                return False

        return True
