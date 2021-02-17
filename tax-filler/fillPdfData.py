from PyPDF2 import PdfFileWriter, PdfFileReader
from PyPDF2.generic import BooleanObject, NameObject, IndirectObject


class fillPDFData:
    def __init__(self):
        pass

    def set_need_appearances_writer(self, writer: PdfFileWriter):
        # See 12.7.2 and 7.7.2 for more information: http://www.adobe.com/content/dam/acom/en/devnet/acrobat/pdfs/PDF32000_2008.pdf
        try:
            catalog = writer._root_object
            # get the AcroForm tree
            if "/AcroForm" not in catalog:
                writer._root_object.update({
                    NameObject("/AcroForm"): IndirectObject(len(writer._objects), 0, writer)
                })

            need_appearances = NameObject("/NeedAppearances")
            writer._root_object["/AcroForm"][need_appearances] = BooleanObject(True)
            # del writer._root_object["/AcroForm"]['NeedAppearances']
            return writer

        except Exception as e:
            print('set_need_appearances_writer() catch : ', repr(e))
            return writer

    def exec(self, raw_dict, form_name):
        myfile = PdfFileReader("tax-filler/form/f" + form_name + ".pdf")
        first_page = myfile.getPage(0)

        writer = PdfFileWriter()
        self.set_need_appearances_writer(writer)

        data_dict = {
            'f1_4[0]': raw_dict['name'].split()[0],
            'f1_5[0]': raw_dict['name'].split()[-1],
            'f1_9[0]': raw_dict['visa'],
            'f1_11[0]': raw_dict['countryOfCitizenship'],
            'f1_12[0]': raw_dict['countryOfCitizenship'],
            'f1_13[0]': raw_dict['passportNumber'],
            'f1_14[0]': raw_dict['days2020'],
            'f1_15[0]': raw_dict['days2019'],
            'f1_16[0]': raw_dict['days2018'],
            'f1_17[0]': raw_dict['days2020'],
        }

        writer.updatePageFormFieldValues(first_page, fields=data_dict)
        writer.addPage(first_page)

        with open("tax-filler/filled/f8843.pdf","wb") as new:
            writer.write(new)
