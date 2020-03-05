class PDFextract {
    /**
     * extract PDF
     * 
     * @type Array
     */
    data;


    /**
     * list PDF
     * 
     * @type Array
     */
    list;

    /**
     * EI in PDF
     * 
     * @type int
     */
    static ei;

    /**
     * Exec Date PDF
     * 
     * @type Array
     */
    static exec_date = [data.start_date, data.end_date];

    /**
     * Name of object list
     * @type Array
     * @param Array [{
                 name: string,
                 position: int //output position
             }]
     *  
     * 
     */
    static header;

    constructor(data) {
        this.data = data;
        this.list = this.getList();
        this.ei = this.getEI();
        this.exec_date = this.getExecDate();
        this.header = [header];
    }

    extractPDF() {
        var parsed_data = []
        list.forEach(row => {
            let _row = this.parseRow(row);
            parsed_data.push(_row);
        });

        return parsed_data;
    }

    getList() {
        data.forEach(page => {
            //concat all list in PDF for each page    
        });
    }

    getEI() {
        //get EI on first page
    }

    getExecDate() {
        //get exec date on first page
    }

    /**
     * 
     * @param {*} row 
     * 
     * @returns {
     *  ei, //static
     *  type,
     *  account,
     *  supplier,
     *  bill_numb,
     *  amount,
     *  tva,
     *  date,
     *  start_exc_date, //static
     *  end_exc_date //static
     * }
     */
    parseRow(row) {
        let _row = {};
        row.forEach((col, index) => {
            let title = this.header.find(title => title.position == index)
            if (index = tag.position) {
                col = this.parseTag(col); //return {title: value, title: value}
                _row.merge({
                    col
                });
            } else {
                _row.merge({
                    title: col
                });
            }
        });
        _row.merge({
            start_exc_date: this.exec_date.start,
            end_exc_date: this.exec_date.end,
            ei: this.ei
        })
        return _row;
    }

    parseTag(tag) {
        let _tag = {};
        if (tag.contains('Four')) {
            //exctract [supplier]
        } else if (tag.contains('Total compte')) {
            //exctract [account] && [type] 
        }

        return _tag;
    }
}