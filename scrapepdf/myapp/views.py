from django.shortcuts import render
import PyPDF2
import os

# Create your views here.
def Scrapepdf(request):
    current_path = os.path.dirname(os.path.realpath(__file__))
    rmmyapp = current_path.replace('\myapp', '')
    if request.method == 'POST':
        k = request.POST.get('keyword', '')
        keywords = [k]
        pdf_name = request.POST.get('myfile', '')
        Folder_path = f'{rmmyapp}' "\\" + pdf_name
        print(keywords)
        print(Folder_path)
        data_list = []
        pdfFileObj = open(pdf_name, 'rb')
        ReadPDF = PyPDF2.PdfReader(pdfFileObj)
        pages = len(ReadPDF.pages)
        for keyword in keywords:
            print(keyword)
            data = {}
            count = 0
            for i in range(pages):
                pageObj = ReadPDF.pages[i]
                text = pageObj.extract_text()
                count_page = text.count(keyword)
                count_lower_page = text.count(keyword.lower())
                final_page_count = count_page + count_lower_page
                count += final_page_count
            data['PDF Name'] = Folder_path
            data['Keyword'] = keyword
            data['Count'] = count

            datas = {
                'keyword': keyword,
                'count': count
            }

            data_list.append(datas)

        # print(data_list)
        pdfFileObj.close()

        print(datas)
        return render(request, 'scrapepdf.html', {'data':data_list})

    else:
        return render(request, 'scrapepdf.html', {'data':""})


# def keyword_search(pdf_name, keywords):
#     data_list = []
#     pdfFileObj = open(pdf_name, 'rb')
#     ReadPDF = PyPDF2.PdfReader(pdfFileObj)
#     pages = len(ReadPDF.pages)
#     for keyword in keywords:
#         data = {}
#         count = 0
#         for i in range(pages):
#             pageObj = ReadPDF.pages[i]
#             text = pageObj.extract_text()
#             count_page = text.count(keyword)
#             count_lower_page = text.count(keyword.lower())
#             final_page_count = count_page + count_lower_page
#             count += final_page_count
#         data['PDF Name'] = pdf_name
#         data['Keyword'] = keyword
#         data['Count'] = count
#         data_list.append(data)
#     pdfFileObj.close()
#     return data_list
#
# data = keyword_search('D:\Practic\scrapepdf\Petra-Diamonds-Limited-Annual-Report-and-Accounts-2022-1.pdf', ['inflection'])
# print(data)