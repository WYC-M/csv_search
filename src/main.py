class CsvSearch:
    file_input: str = None  # 输入文件路径
    file_output: str = None  # 输出文件路径

    origin_data: list = None  # 输入文件数据（每行一个字符串）

    # 两个搜索的词
    search_str1: str = None
    search_str2: str = None

    def __init__(self, input_path, output_path, input_str1, input_str2):
        self.file_input = input_path
        self.file_output = output_path
        self.search_str1 = input_str1
        self.search_str2 = input_str2

    def read_csv(self):
        """
        读取文件
        :return:
        """
        with open(self.file_input, "r", encoding="UTF=8") as f:
            self.origin_data = f.readlines()

    def output_and_processing_data(self):
        """
        处理数据并输出
        :return:
        """
        # 删除原表头
        del self.origin_data[0]
        del self.origin_data[0]

        # 输出数据
        with open(self.file_output, "w", encoding="GB2312") as f:
            i = 0
            f.write("姓名,出现字符串: " + self.search_str1 + " 和 " + self.search_str2 + " 次数\n")
            while i < len(self.origin_data):
                f.write(self.origin_data[i].split(",")[0].replace('\"', '').replace("\t", "") + "," + str(
                    self.origin_data[i].count(self.search_str1) + self.origin_data[i].count(
                        self.search_str2)) + "\n")
                # print(self.origin_data[i].split(",")[0].replace('\"', '').replace("\t", ""))
                i += 1


if __name__ == "__main__":
    cs = CsvSearch("input.csv", "output.csv", "已补交", "已提交")
    cs.read_csv()
    cs.output_and_processing_data()
