# coding=utf-8
import xlwt

workbook = xlwt.Workbook()
sheet1 = workbook.add_sheet('tmmr', cell_overwrite_ok=True)


row0 = [u"times", u"prepower", u"upper", u"lower"]
for i in range(0 , len(row0)):
    sheet1.write(0, i, row0[i])


f = open('test.txt')
next(f)
index = 1
for line in f:
    data = line.strip('\n').split(' ')
    # data = line.split(' ')
    print(data)
    print(data[0])
    # datas = data[0].split('\t')
    # if data[7] == "tmmr":
    #     # print "********************************"
    #     # print data
    #     data[7], data[12] = data[12], data[7]
    #     data[8], data[13] = data[13], data[8]
    #     data[9], data[14] = data[14], data[9]
    #     data[10], data[15] = data[15], data[10]
    #     data[11], data[16] = data[16], data[11]
    # print data
    # print "********************************"
    sheet1.write(index, 0, data[0])
    # print(data[0].split('\t'))
    sheet1.write(index, 1, data[1])
    sheet1.write(index, 2, data[2])
    sheet1.write(index, 3, data[3])

    index = index + 1

workbook.save('perf.xls')