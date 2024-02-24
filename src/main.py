class CsvSearch:
    file_input: str = None  # 输入文件路径
    file_output: str = None  # 输出文件路径
    origin_data: list = None  # 输入文件数据（每行一个字符串）
    search_list: list = None  # 搜索的词的列表
    head_row: int = 0  # 旧表格表头行数
    new_head: str = None  # 新表格第一列的表头

    # 两个搜索的词
    # search_str1: str = None
    # search_str2: str = None

    def __init__(self, in_file_input, in_file_output, in_search_list, in_head_row, in_new_head):
        self.file_input = in_file_input
        self.file_output = in_file_output
        self.search_list = in_search_list
        self.head_row = in_head_row
        self.new_head = in_new_head

        # print(self.search_list)

    def read_csv(self):
        """
        读取文件
        :return:
        """
        with open(self.file_input, "r", encoding="UTF=8") as f:
            self.origin_data = f.readlines()

    def del_head(self):
        """
        删除原表头
        :return:
        """
        i = 0
        while i < self.head_row:
            del self.origin_data[0]
            i += 1
        # del self.origin_data[0]
        # del self.origin_data[0]

    def output_data(self):
        """
        处理数据并输出
        :return:
        """
        # 输出数据
        with open(self.file_output, "w", encoding="GB2312") as f:
            # 输出第一行表头
            f.write(
                self.new_head + ",出现字符串: " + str(self.search_list).replace("[", "").replace("]", "").replace("'",
                                                                                                                  "").replace(
                    '"', '').replace(",", "") + " 次数\n")

            i = 0
            while i < len(self.origin_data):
                j = 0
                search_num = 0  # 搜索到的数目
                while j < len(self.search_list):
                    search_num += self.origin_data[i].count(self.search_list[j])
                    j += 1

                f.write(
                    self.origin_data[i].split(",")[0].replace('\"', '').replace("\t", "").replace(" ", "") + "," + str(
                        search_num) + "\n")
                # print(self.origin_data[i].split(",")[0].replace('\"', '').replace("\t", ""))
                i += 1


def main():
    cs = CsvSearch("input.csv", "output.csv", ["已补交", "已提交"], 2, "姓名")
    cs.read_csv()
    cs.del_head()
    cs.output_data()


if __name__ == "__main__":
    main()
