
import array as arr
import re


# pdf file object


class PDF_extract(object):

    # ei = int

   # exec_date = [data.start_date, data.end_date]

    # param = np.array([{name: str, position: int}])

    def __init__(self, data):
        self.data = [data]
        self.List = self.get_list()
        self.ei = self.get_ei()
        self.exec_date = [self.get_exec_date()]
        self.header = data[1]

    def extract_PDF(self):
        parsed_data = []
        for row in (List):
            _row = self.Parse_row(row)
            parsed_data.append(_row)
        print(parsed_data)

        return parsed_data

    def get_list(self):
        all_lists = []
        for page in (self.data):
            all_lists += page
            print(all_lists)
        return all_lists

    def get_ei(self):

        all_lists = self.get_list()
        page_1st = all_lists[0]
        ei = re.search(r'\d\d\d\d', page_1st)

        print(ei)
        return ei

    def get_exec_date(self):
        all_lists = self.get_list()
        page_1st = all_lists[0]
        exec_date = re.match(
            r'^(0?[1-9]|[12][0-9]|3[01])[\/\-](0?[1-9]|1[012])[\/\-]\d{4}$', page_1st)
        return exec_date

    def parse_row(self, row):
        _row = {}
        for (col, index) in row:
            if self.header.position == index:  # x and y
                title = self.header  # => title pos == index
            if index == tag.position:
                col = self.parse_tag(col)
                _col += col
            if col:
                _row += col

        _row += ({start_exc_date: self.exec_date.start,
                  end_exc_date: self.exec_date.end,
                  ei: self.ei})
        return _row

    def parse_tag(tag):
        _tag = {}
        if 'Four' in tag:
            _tag += tag

        elif 'Total compte' in tag:
            _tag += tag

        return _tag
