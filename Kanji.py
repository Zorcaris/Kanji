import json
import os
from fpdf import FPDF
from fpdf.enums import XPos, YPos
from kanji_lists import JLPT,KYOIKU
from pathlib import Path

#print (KYOIKU.HEISEI4.GRADE1)

# Get Json data
with open('kanjiData.json','r',encoding='utf-8') as kanjiFile:
    dictionary = json.load(kanjiFile)

#print(dictionary)

# Fill in the table with data
def tableau(data):
    max_len = max(len(data["Kanji"]), len(data["Kun"]), len(data["On"]), len(data["Traduction"]))

    for i in range(max_len):  
        # Kanji 
        if i >= len(data["Kanji"]) or not data["Kanji"][i]: 
            pdf.cell(20, 12, " ", 1, align='C')
        else:
            pdf.cell(20, 12, data["Kanji"][i], 1, align='C')

        # Kun 
        if i >= len(data["Kun"]) or not data["Kun"][i]: 
            pdf.cell(48, 12, " ", 1, align='C')
        else:
            pdf.cell(48, 12, data["Kun"][i], 1, align='C')

        # On 
        if i >= len(data["On"]) or not data["On"][i]:  
            pdf.cell(48, 12, " ", 1, align='C')
        else:
            pdf.cell(48, 12, data["On"][i], 1, align='C')

        # Traduction 
        if i >= len(data["Traduction"]) or not data["Traduction"][i]:  
            pdf.cell(60, 12, " ", 1, align='C')
        else:
            pdf.cell(60, 12, data["Traduction"][i], 1, align='C')

        # Number 
        number = str(i + 1)
        pdf.cell(20, 12, number, 1, new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='C')


# Initialize FPDF object
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)

# Add fonts
pdf.add_font('noto', '', 'static\\NotoSansJP-Regular.ttf')

nbNiveau = ""

def niveauSelect(nbNiveau):
   #print("nbNiveau",int(nbNiveau))
    nbNiveauToInt = int(nbNiveau)

    if nbNiveauToInt == 6:
        #print("to header")
        header(6)
        pdf.set_font('noto', '', 15)
        print("Radical")
        tableau(dictionary["Radical"])
        pdf.ln()

    for k in range(5,0,-1) :
        if nbNiveau.find(str(k))!=-1 and k<6:
            header(k)
            pdf.set_font('noto', '', 15)
            #print("N"+str(k))
            tableau(dictionary["N"+str(k)])
            pdf.ln()



    # Folder where file will be saved
    desktop_path = Path(os.path.join(os.path.expanduser("~"), "Desktop"))
    output_dir = desktop_path / "Kanji"
    output_dir.mkdir(parents=True, exist_ok=True)

    pdf_file = output_dir / "Kanji_JLPT.pdf"
    
    # Avoid file already exist errors
    if pdf_file.exists():
        pdf_file.unlink()  
    
    # Ouput the final file
    pdf.output(str(pdf_file)) 
    print(f"Le PDF a été créé avec succès : {pdf_file}")


# Set the form of the file
def header(x):
    pdf.add_page()
    pdf.set_font("Helvetica", 'B', 19)
   #print("header",x)
    if x <= 5:
        pdf.cell(200, 20, text="Kanji Table N"+str(x), new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='C')
    elif x == 6:
        pdf.cell(200, 20, text="Kanji Table Radical", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='C')
    headers = ["Kanji", "Kun'Yomi", "On'Yomi", "Traduction", "NB"]
    pdf.cell(20, 12, headers[0], 1, new_x=XPos.RIGHT, new_y=YPos.TOP, align='C')
    pdf.cell(48, 12, headers[1], 1, new_x=XPos.RIGHT, new_y=YPos.TOP, align='C')
    pdf.cell(48, 12, headers[2], 1, new_x=XPos.RIGHT, new_y=YPos.TOP, align='C')
    pdf.cell(60, 12, headers[3], 1, new_x=XPos.RIGHT, new_y=YPos.TOP, align='C')
    pdf.cell(20, 12, headers[4], 1, new_x=XPos.RIGHT, new_y=YPos.TOP, align='C')
    pdf.ln()




