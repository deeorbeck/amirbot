from datetime import datetime
from reportlab.pdfgen.canvas import Canvas


def cv_doc(name, data, quant):
    canvas = Canvas(f"handlers/users/pdfs/{name}.pdf", pagesize=(600, 2000))
    canvas.drawImage(f"handlers/users/images/{name}_{quant}.jpg", 200, 1790, width=200, height=200)
    canvas.setFont('Helvetica', 25)
    eman = str(data['name']).replace("\n", ' ')
    canvas.drawString(100, 1750, eman.title())
    del data['name']
    canvas.setFont('Helvetica', 15)
    max_height = 1700
    interval = 20
    for i in data.keys():
        if data[i] == True:
            data[i] = "Turmushli"

        elif data[i] == False:
            data[i] = "Turmushsiz"
        a = 40
        quant = 0
        if len(data[i]) % 40 != 0:
            quant += 1
        for item in range(len(data[i]) // 40 +quant):
            te = str(data[i][a - 40:a]).replace('\n', " ")
            if item == 0:
                canvas.drawString(20, max_height, f"{i}: {te}")
            else:
                canvas.drawString(20, max_height, f"{te}")
            max_height -=interval
            a += 40

    canvas.drawString(10, 10, f'Date: {datetime.now().strftime("%d.%m.%Y")}')
    canvas.showPage()
    canvas.save()

