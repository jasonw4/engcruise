from tkinter import Tk, Button, Label

mechanical = 5
chemical = 5
civil = 5
electrical = 5


def rungame():
    root = Tk()
    root.wm_title("Engineering Cruising")
    root.geometry('800x800')
    root.configure(bg='light sky blue')

    def clickyesbutton14():
        global civil
        civil += 1
        question14.pack_forget()
        yesbutton14.pack_forget()
        nobutton14.pack_forget()
        notsurebutton14.pack_forget()
        if civil == 9:
            global civil_response
            civil_response.pack()
        else:
            global question14a
            question14a = Label(root, text="")

    def clicknobutton14():
        global civil
        civil -= 1

    def clicknotsurebutton14():
        global civil
        civil += 0

    def clickq13aanswer1():
        global electrical
        electrical += 1
        question13a.pack_forget()
        q13aanswer1.pack_forget()
        q13aanswer2.pack_forget()
        if electrical == 9:
            global electrical_response
            electrical_response.pack()
        else:
            global question14
            question14 = Label(root,
                               text="Is the idea of redesigning the infrastructure of New York City appealing to you?",
                               bg="Light sky blue")
            question14.pack(side="left", expand=True)
            global yesbutton14
            yesbutton14 = Button(root, text="Yes", height=3, width=5, command=clickyesbutton14)
            yesbutton14.pack(side="left", expand=True)
            global nobutton14
            nobutton14 = Button(root, text="No", height=3, width=5, command=clicknobutton14)
            nobutton14.pack(side="left", expand=True)
            global notsurebutton14
            notsurebutton14 = Button(root, text="Not Sure", height=3, width=5, command=clicknotsurebutton14)
            notsurebutton14.pack(side="left", expand=True)

    def clickq13aanswer2():
        global chemical
        chemical += 1
        question13a.pack_forget()
        q13aanswer1.pack_forget()
        q13aanswer2.pack_forget()
        if chemical == 9:
            global chemical_response
            chemical_response.pack()
        else:
            global question14
            question14 = Label(root,
                               text="Is the idea of redesigning the infrastructure of New York City appealing to you?",
                               bg="Light sky blue")
            question14.pack(side="left", expand=True)
            global yesbutton14
            yesbutton14 = Button(root, text="Yes", height=3, width=5, command=clickyesbutton14)
            yesbutton14.pack(side="left", expand=True)
            global nobutton14
            nobutton14 = Button(root, text="No", height=3, width=5, command=clicknobutton14)
            nobutton14.pack(side="left", expand=True)
            global notsurebutton14
            notsurebutton14 = Button(root, text="Not Sure", height=3, width=5, command=clicknotsurebutton14)
            notsurebutton14.pack(side="left", expand=True)

    def clickyesbutton13():
        global mechanical
        mechanical += 1
        question13.pack_forget()
        yesbutton13.pack_forget()
        nobutton13.pack_forget()
        notsurebutton13.pack_forget()
        global question13a
        question13a = Label(root,
                            text="Would you rather conduct research on electrical devices or pharmaceutical products and food?",
                            bg="Light sky blue")
        question13a.pack(side="left", expand=True)
        global q13aanswer1
        q13aanswer1 = Button(root, text="Electrical Devices", height=10, width=10, command=clickq13aanswer1)
        q13aanswer1.pack(side="left", expand=True)
        global q13aanswer2
        q13aanswer2 = Button(root, text="Pharmeceutical \n Products \n and Food", height=10, width=10,
                             command=clickq13aanswer2)
        q13aanswer2.pack(side="left", expand=True)

    def clicknobutton13():
        global mechanical
        mechanical -= 1
        question13.pack_forget()
        yesbutton13.pack_forget()
        nobutton13.pack_forget()
        notsurebutton13.pack_forget()
        global question13a
        question13a = Label(root,
                            text="Would you rather conduct research on electrical devices or pharmaceutical products and food?",
                            bg="Light sky blue")
        question13a.pack(side="left", expand=True)
        global q13aanswer1
        q13aanswer1 = Button(root, text="Electrical Devices", height=10, width=10, command=clickq13aanswer1)
        q13aanswer1.pack(side="left", expand=True)
        global q13aanswer2
        q13aanswer2 = Button(root, text="Pharmeceutical \n Products \n and Food", height=10, width=10,
                             command=clickq13aanswer2)
        q13aanswer2.pack(side="left", expand=True)

    def clicknotsurebutton13():
        global mechanical
        mechanical == 0
        question13.pack_forget()
        yesbutton13.pack_forget()
        nobutton13.pack_forget()
        notsurebutton13.pack_forget()
        global question13a
        question13a = Label(root,
                            text="Would you rather conduct research on electrical devices or pharmaceutical products and food?",
                            bg="Light sky blue")
        question13a.pack(side="left", expand=True)
        global q13aanswer1
        q13aanswer1 = Button(root, text="Electrical Devices", height=3, width=5, command=clickq13aanswer1)
        q13aanswer1.pack(side="left", expand=True)
        global q13aanswer2
        q13aanswer2 = Button(root, text="Pharmeceutical \n Products \n and Food", height=10, width=10,
                             command=clickq13aanswer2)
        q13aanswer2.pack(side="left", expand=True)

    def clickyesbutton12():
        global electrical
        electrical += 1
        question12.pack_forget()
        yesbutton12.pack_forget()
        nobutton12.pack_forget()
        notsurebutton12.pack_forget()
        if electrical == 9:
            global electrical_response
            electrical_response = Label(root,
                                        text="Electrical Engineering seems to be the best fit for you. \n Some classes/clubs you should try out are: \n - Robotics \n - Engineering 1 \n - Engineering 2 \n - Coding Club \n - RC Club \n - Computer Science \n Some subfields that you can look into are: \n -Telecommunications \n -Control Systems \n -Signal Processing \n - Microelectronics",
                                        bg="Light sky blue")
            electrical_response.pack()
        else:
            global question13
            question13 = Label(root, text="Are you interested in designing virtual reality systems?",
                               bg="Light sky blue")
            question13.pack(side="left", expand=True)
            global yesbutton13
            yesbutton13 = Button(root, text="Yes", height=3, width=5, command=clickyesbutton13)
            yesbutton13.pack(side="left", expand=True)
            global nobutton13
            nobutton13 = Button(root, text="No", height=3, width=5, command=clicknobutton13)
            nobutton13.pack(side="left", expand=True)
            global notsurebutton13
            notsurebutton13 = Button(root, text="Not Sure", height=3, width=5, command=clicknotsurebutton13)
            notsurebutton13.pack(side="left", expand=True)

    def clicknobutton12():
        global chemical
        chemical += 1
        question12.pack_forget()
        yesbutton12.pack_forget()
        nobutton12.pack_forget()
        notsurebutton12.pack_forget()
        if chemical == 9:
            global chemical_response
            chemical_response = Label(root,
                                      text="Chemical Engineering seems to be the best fit for you. Some classes/clubs you should consider are: \n - Calculus \n -Chemistry \n - Computer Science \n Some subfields that you can look into are: \n - Biotechnology \n - Mineral Processing \n - Ceramics \n - Chemical Processing",
                                      bg="light sky blue")
            chemical_response.pack()
        else:
            global question13
            question13 = Label(root, text="Are you interested in designing virtual reality systems?",
                               bg="Light sky blue")
            question13.pack(side="left", expand=True)
            global yesbutton13
            yesbutton13 = Button(root, text="Yes", height=3, width=5, command=clickyesbutton13)
            yesbutton13.pack(side="left", expand=True)
            global nobutton13
            nobutton13 = Button(root, text="No", height=3, width=5, command=clicknobutton13)
            nobutton13.pack(side="left", expand=True)
            global notsurebutton13
            notsurebutton13 = Button(root, text="Not Sure", height=3, width=5, command=clicknotsurebutton13)
            notsurebutton13.pack(side="left", expand=True)

    def clicknotsurebutton12():
        global mechanical
        mechanical += 1
        question12.pack_forget()
        yesbutton12.pack_forget()
        nobutton12.pack_forget()
        notsurebutton12.pack_forget()
        if mechanical == 9:
            global mechanical_response
            mechanical_response = Label(root,
                                        text="Mechanical Engineering seems to be the best fit for you. \n Some classes/clubs you should consider are: \n - Robotics \n - RC Club \n -DDP \n -CAD \n -Engineering 1 \n -Engineering 2 \n - Physics \n -Calculus \n Some subfields you might want to look into are: \n - Aerospace \n - Automation \n - Cybersecurity \n -Robotics \n -Data Analysis")
        global question13
        question13 = Label(root, text="Are you interested in designing virtual reality systems?", bg="Light sky blue")
        question13.pack(side="left", expand=True)
        global yesbutton13
        yesbutton13 = Button(root, text="Yes", height=3, width=5, command=clickyesbutton13)
        yesbutton13.pack(side="left", expand=True)
        global nobutton13
        nobutton13 = Button(root, text="No", height=3, width=5, command=clicknobutton13)
        nobutton13.pack(side="left", expand=True)
        global notsurebutton13
        notsurebutton13 = Button(root, text="Not Sure", height=3, width=5, command=clicknotsurebutton13)
        notsurebutton13.pack(side="left", expand=True)

    def clickyesbutton11():
        global civil
        civil += 1
        question11.pack_forget()
        yesbutton11.pack_forget()
        nobutton11.pack_forget()
        notsurebutton11.pack_forget()
        if civil == 9:
            global civil_response
            civil_response.pack()
        else:
            global question12
            question12 = Label(root, text="How would others describe you?", bg="Light sky blue")
            question12.pack(side="left", expand=True)
            global yesbutton12
            yesbutton12 = Button(root, text="Logical, Meticulous", height=3, width=5, command=clickyesbutton12)
            yesbutton12.pack(side="left", expand=True)
            global nobutton12
            nobutton12 = Button(root, text="Adventurous, Bold", height=3, width=5, command=clicknobutton12)
            nobutton12.pack(side="left", expand=True)
            global notsurebutton12
            notsurebutton12 = Button(root, text="Tinkerer, Crafty", height=3, width=5, command=clicknotsurebutton12)
            notsurebutton12.pack(side="left", expand=True)

    def clicknobutton11():
        global civil
        civil -= 1
        question11.pack_forget()
        yesbutton11.pack_forget()
        nobutton11.pack_forget()
        notsurebutton11.pack_forget()
        global question12
        question12 = Label(root, text="How would others describe you?", bg="Light sky blue")
        question12.pack(side="left", expand=True)
        global yesbutton12
        yesbutton12 = Button(root, text="Logical, Meticulous", height=3, width=5, command=clickyesbutton12)
        yesbutton12.pack(side="left", expand=True)
        global nobutton12
        nobutton12 = Button(root, text="Adventurous, Bold", height=3, width=5, command=clicknobutton12)
        nobutton12.pack(side="left", expand=True)
        global notsurebutton12
        notsurebutton12 = Button(root, text="Tinkerer, Crafty", height=3, width=5, command=clicknotsurebutton12)
        notsurebutton12.pack(side="left", expand=True)

    def clicknotsurebutton11():
        global civil
        civil += 0
        question11.pack_forget()
        yesbutton11.pack_forget()
        nobutton11.pack_forget()
        notsurebutton11.pack_forget()
        global question12
        question12 = Label(root, text="How would others describe you?", bg="Light sky blue")
        question12.pack(side="left", expand=True)
        global yesbutton12
        yesbutton12 = Button(root, text="Logical, Meticulous", height=3, width=5, command=clickyesbutton12)
        yesbutton12.pack(side="left", expand=True)
        global nobutton12
        nobutton12 = Button(root, text="Adventurous, Bold", height=3, width=5, command=clicknobutton12)
        nobutton12.pack(side="left", expand=True)
        global notsurebutton12
        notsurebutton12 = Button(root, text="Tinkerer, Crafty", height=3, width=5, command=clicknotsurebutton12)
        notsurebutton12.pack(side="left", expand=True)

    def clickyesbutton10():
        global chemical
        chemical += 1
        question10.pack_forget()
        yesbutton10.pack_forget()
        nobutton10.pack_forget()
        notsurebutton10.pack_forget()
        global question11
        question11 = Label(root, text="Are you interested in working at construction sites?", bg="Light sky blue")
        question11.pack(side="left", expand=True)
        global yesbutton11
        yesbutton11 = Button(root, text="Yes", height=3, width=5, command=clickyesbutton11)
        yesbutton11.pack(side="left", expand=True)
        global nobutton11
        nobutton11 = Button(root, text="No", height=3, width=5, command=clicknobutton11)
        nobutton11.pack(side="left", expand=True)
        global notsurebutton11
        notsurebutton11 = Button(root, text="Not Sure", height=3, width=5, command=clicknotsurebutton11)
        notsurebutton11.pack(side="left", expand=True)

    def clicknobutton10():
        global chemical
        chemical -= 1
        question10.pack_forget()
        yesbutton10.pack_forget()
        nobutton10.pack_forget()
        notsurebutton10.pack_forget()
        global question11
        question11 = Label(root, text="Are you interested in working at construction sites?", bg="Light sky blue")
        question11.pack(side="left", expand=True)
        global yesbutton11
        yesbutton11 = Button(root, text="Yes", height=3, width=5, command=clickyesbutton11)
        yesbutton11.pack(side="left", expand=True)
        global nobutton11
        nobutton11 = Button(root, text="No", height=3, width=5, command=clicknobutton11)
        nobutton11.pack(side="left", expand=True)
        global notsurebutton11
        notsurebutton11 = Button(root, text="Not Sure", height=3, width=5, command=clicknotsurebutton11)
        notsurebutton11.pack(side="left", expand=True)

    def clicknotsurebutton10():
        global chemical
        chemical += 0
        question10.pack_forget()
        yesbutton10.pack_forget()
        nobutton10.pack_forget()
        notsurebutton10.pack_forget()
        global question11
        question11 = Label(root, text="Are you interested in working at construction sites?", bg="Light sky blue")
        question11.pack(side="left", expand=True)
        global yesbutton11
        yesbutton11 = Button(root, text="Yes", height=3, width=5, command=clickyesbutton11)
        yesbutton11.pack(side="left", expand=True)
        global nobutton11
        nobutton11 = Button(root, text="No", height=3, width=5, command=clicknobutton11)
        nobutton11.pack(side="left", expand=True)
        global notsurebutton11
        notsurebutton11 = Button(root, text="Not Sure", height=3, width=5, command=clicknotsurebutton11)
        notsurebutton11.pack(side="left", expand=True)

    def clickyesbutton9():
        global chemical
        chemical += 1
        question9.pack_forget()
        yesbutton9.pack_forget()
        nobutton9.pack_forget()
        notsurebutton9.pack_forget()
        global question10
        question10 = Label(root, text="Would you like to do work in the food or pharmaceutical industry?",
                           bg="Light sky blue")
        question10.pack(side="left", expand=True)
        global yesbutton10
        yesbutton10 = Button(root, text="Yes", height=3, width=5, command=clickyesbutton10)
        yesbutton10.pack(side="left", expand=True)
        global nobutton10
        nobutton10 = Button(root, text="No", height=3, width=5, command=clicknobutton10)
        nobutton10.pack(side="left", expand=True)
        global notsurebutton10
        notsurebutton10 = Button(root, text="Not Sure", height=3, width=5, command=clicknotsurebutton10)
        notsurebutton10.pack(side="left", expand=True)

    def clicknobutton9():
        global chemical
        chemical -= 1
        question9.pack_forget()
        yesbutton9.pack_forget()
        nobutton9.pack_forget()
        notsurebutton9.pack_forget()
        global question10
        question10 = Label(root, text="Would you like to do work in the food or pharmaceutical industry?",
                           bg="Light sky blue")
        question10.pack(side="left", expand=True)
        global yesbutton10
        yesbutton10 = Button(root, text="Yes", height=3, width=5, command=clickyesbutton10)
        yesbutton10.pack(side="left", expand=True)
        global nobutton10
        nobutton10 = Button(root, text="No", height=3, width=5, command=clicknobutton10)
        nobutton10.pack(side="left", expand=True)
        global notsurebutton10
        notsurebutton10 = Button(root, text="Not Sure", height=3, width=5, command=clicknotsurebutton10)
        notsurebutton10.pack(side="left", expand=True)

    def clicknotsurebutton9():
        global chemical
        chemical += 0
        question9.pack_forget()
        yesbutton9.pack_forget()
        nobutton9.pack_forget()
        notsurebutton9.pack_forget()
        global question10
        question10 = Label(root, text="Would you like to do work in the food or pharmaceutical industry?",
                           bg="Light sky blue")
        question10.pack(side="left", expand=True)
        global yesbutton10
        yesbutton10 = Button(root, text="Yes", height=3, width=5, command=clickyesbutton10)
        yesbutton10.pack(side="left", expand=True)
        global nobutton10
        nobutton10 = Button(root, text="No", height=3, width=5, command=clicknobutton10)
        nobutton10.pack(side="left", expand=True)
        global notsurebutton10
        notsurebutton10 = Button(root, text="Not Sure", height=3, width=5, command=clicknotsurebutton10)
        notsurebutton10.pack(side="left", expand=True)

    def clickyesbutton8():
        global mechanical
        mechanical += 1
        question8.pack_forget()
        yesbutton8.pack_forget()
        nobutton8.pack_forget()
        notsurebutton8.pack_forget()
        global question9
        question9 = Label(root, text="Would you like your workday to be spent in a laboratory?", bg="Light sky blue")
        question9.pack(side="left", expand=True)
        global yesbutton9
        yesbutton9 = Button(root, text="Yes", height=3, width=5, command=clickyesbutton9)
        yesbutton9.pack(side="left", expand=True)
        global nobutton9
        nobutton9 = Button(root, text="No", height=3, width=5, command=clicknobutton9)
        nobutton9.pack(side="left", expand=True)
        global notsurebutton9
        notsurebutton9 = Button(root, text="Not Sure", height=3, width=5, command=clicknotsurebutton9)
        notsurebutton9.pack(side="left", expand=True)

    def clicknobutton8():
        global mechanical
        mechanical -= 1
        question8.pack_forget()
        yesbutton8.pack_forget()
        nobutton8.pack_forget()
        notsurebutton8.pack_forget()
        global question9
        question9 = Label(root, text="Would you like your workday to be spent in a laboratory?", bg="Light sky blue")
        question9.pack(side="left", expand=True)
        global yesbutton9
        yesbutton9 = Button(root, text="Yes", height=3, width=5, command=clickyesbutton9)
        yesbutton9.pack(side="left", expand=True)
        global nobutton9
        nobutton9 = Button(root, text="No", height=3, width=5, command=clicknobutton9)
        nobutton9.pack(side="left", expand=True)
        global notsurebutton9
        notsurebutton9 = Button(root, text="Not Sure", height=3, width=5, command=clicknotsurebutton9)
        notsurebutton9.pack(side="left", expand=True)

    def clicknotsurebutton8():
        global mechanical
        mechanical += 0
        question8.pack_forget()
        yesbutton8.pack_forget()
        nobutton8.pack_forget()
        notsurebutton8.pack_forget()
        global question9
        question9 = Label(root, text="Would you like your workday to be spent in a laboratory?", bg="Light sky blue")
        question9.pack(side="left", expand=True)
        global yesbutton9
        yesbutton9 = Button(root, text="Yes", height=3, width=5, command=clickyesbutton9)
        yesbutton9.pack(side="left", expand=True)
        global nobutton9
        nobutton9 = Button(root, text="No", height=3, width=5, command=clicknobutton9)
        nobutton9.pack(side="left", expand=True)
        global notsurebutton9
        notsurebutton9 = Button(root, text="Not Sure", height=3, width=5, command=clicknotsurebutton9)
        notsurebutton9.pack(side="left", expand=True)

    def clickyesbutton7():
        global civil
        civil += 1
        question7.pack_forget()
        yesbutton7.pack_forget()
        nobutton7.pack_forget()
        notsurebutton7.pack_forget()
        if civil == 9:
            global civil_response
            civil_response = Label(root,
                                   text="Civil Engineering seems to be the best fit for you. \n Some classes/clubs that you should consider are: \n -CAD \n - Engineering 1 \n - Engineering 2 \n -Robotics \n -Calculus \n -Physics \n - Communication Technology \n - Transportation Technology \n Some subfields that you can look into are: \n - Coastal Engineering \n - Geotechnical Engineering \n - Environmental Engineering \n - Structural Engineering ")
            civil_response.pack()
        else:
            global question8
            question8 = Label(root, text="Do/did you enjoy playing around with LEGOS?", bg='Light sky blue')
            question8.pack(side="left", expand=True)
            global yesbutton8
            yesbutton8 = Button(root, text="Yes", height=3, width=5, command=clickyesbutton8)
            yesbutton8.pack(side="left", expand=True)
            global nobutton8
            nobutton8 = Button(root, text="No", height=3, width=5, command=clicknobutton8)
            nobutton8.pack(side="left", expand=True)
            global notsurebutton8
            notsurebutton8 = Button(root, text="Not Sure", height=3, width=5, command=clicknotsurebutton8)
            notsurebutton8.pack(side="left", expand=True)

    def clicknobutton7():
        global civil
        civil -= 1
        question7.pack_forget()
        yesbutton7.pack_forget()
        nobutton7.pack_forget()
        notsurebutton7.pack_forget()
        global question8
        question8 = Label(root, text="Do/did you enjoy playing around with LEGOS?", bg='Light sky blue')
        question8.pack(side="left", expand=True)
        global yesbutton8
        yesbutton8 = Button(root, text="Yes", height=3, width=5, command=clickyesbutton8)
        yesbutton8.pack(side="left", expand=True)
        global nobutton8
        nobutton8 = Button(root, text="No", height=3, width=5, command=clicknobutton8)
        nobutton8.pack(side="left", expand=True)
        global notsurebutton8
        notsurebutton8 = Button(root, text="Not Sure", height=3, width=5, command=clicknotsurebutton8)
        notsurebutton8.pack(side="left", expand=True)

    def clicknotsurebutton7():
        global civil
        civil += 0
        question7.pack_forget()
        yesbutton7.pack_forget()
        nobutton7.pack_forget()
        notsurebutton7.pack_forget()
        global question8
        question8 = Label(root, text="Do/did you enjoy playing around with LEGOS?", bg='Light sky blue')
        question8.pack(side="left", expand=True)
        global yesbutton8
        yesbutton8 = Button(root, text="Yes", height=3, width=5, command=clickyesbutton8)
        yesbutton8.pack(side="left", expand=True)
        global nobutton8
        nobutton8 = Button(root, text="No", height=3, width=5, command=clicknobutton8)
        nobutton8.pack(side="left", expand=True)
        global notsurebutton8
        notsurebutton8 = Button(root, text="Not Sure", height=3, width=5, command=clicknotsurebutton8)
        notsurebutton8.pack(side="left", expand=True)

    def clickyesbutton6():
        global electrical
        electrical += 1
        question6.pack_forget()
        yesbutton6.pack_forget()
        nobutton6.pack_forget()
        notsurebutton6.pack_forget()
        global question7
        question7 = Label(root, text="Are you interested in using computer aided design (CAD) in the future?",
                          bg='Light sky blue')
        question7.pack(side="left", expand=True)
        global yesbutton7
        yesbutton7 = Button(root, text="Yes", height=3, width=5, command=clickyesbutton7)
        yesbutton7.pack(side="left", expand=True)
        global nobutton7
        nobutton7 = Button(root, text="No", height=3, width=5, command=clicknobutton7)
        nobutton7.pack(side="left", expand=True)
        global notsurebutton7
        notsurebutton7 = Button(root, text="Not Sure", height=3, width=5, command=clicknotsurebutton7)
        notsurebutton7.pack(side="left", expand=True)

    def clicknobutton6():
        global electrical
        electrical -= 1
        question6.pack_forget()
        yesbutton6.pack_forget()
        nobutton6.pack_forget()
        notsurebutton6.pack_forget()
        global question7
        question7 = Label(root, text="Are you interested in using computer aided design (CAD) in the future?",
                          bg='Light sky blue')
        question7.pack(side="left", expand=True)
        global yesbutton7
        yesbutton7 = Button(root, text="Yes", height=3, width=5, command=clickyesbutton7)
        yesbutton7.pack(side="left", expand=True)
        global nobutton7
        nobutton7 = Button(root, text="No", height=3, width=5, command=clicknobutton7)
        nobutton7.pack(side="left", expand=True)
        global notsurebutton7
        notsurebutton7 = Button(root, text="Not Sure", height=3, width=5, command=clicknotsurebutton7)
        notsurebutton7.pack(side="left", expand=True)

    def clicknotsurebutton6():
        global electrical
        electrical += 0
        question6.pack_forget()
        yesbutton6.pack_forget()
        nobutton6.pack_forget()
        notsurebutton6.pack_forget()
        global question7
        question7 = Label(root, text="Are you interested in using computer aided design (CAD) in the future?",
                          bg='Light sky blue')
        question7.pack(side="left", expand=True)
        global yesbutton7
        yesbutton7 = Button(root, text="Yes", height=3, width=5, command=clickyesbutton7)
        yesbutton7.pack(side="left", expand=True)
        global nobutton7
        nobutton7 = Button(root, text="No", height=3, width=5, command=clicknobutton7)
        nobutton7.pack(side="left", expand=True)
        global notsurebutton7
        notsurebutton7 = Button(root, text="Not Sure", height=3, width=5, command=clicknotsurebutton7)
        notsurebutton7.pack(side="left", expand=True)

    def clickyesbutton5():
        global chemical
        chemical += 1
        question5.pack_forget()
        yesbutton5.pack_forget()
        nobutton5.pack_forget()
        notsurebutton5.pack_forget()
        global question6
        question6 = Label(root, text="Are you interested in learning more about quantum physics and its applications?",
                          bg="Light sky blue")
        question6.pack(side="left", expand=True)
        global yesbutton6
        yesbutton6 = Button(root, text="Yes", height=3, width=5, command=clickyesbutton6)
        yesbutton6.pack(side="left", expand=True)
        global nobutton6
        nobutton6 = Button(root, text="No", height=3, width=5, command=clicknobutton6)
        nobutton6.pack(side="left", expand=True)
        global notsurebutton6
        notsurebutton6 = Button(root, text="Not Sure", height=3, width=5, command=clicknotsurebutton6)
        notsurebutton6.pack(side="left", expand=True)

    def clicknobutton5():
        global chemical
        chemical -= 1
        question5.pack_forget()
        yesbutton5.pack_forget()
        nobutton5.pack_forget()
        notsurebutton5.pack_forget()
        global question6
        question6 = Label(root, text="Are you interested in learning more about quantum physics and its applications?",
                          bg="Light sky blue")
        question6.pack(side="left", expand=True)
        global yesbutton6
        yesbutton6 = Button(root, text="Yes", height=3, width=5, command=clickyesbutton6)
        yesbutton6.pack(side="left", expand=True)
        global nobutton6
        nobutton6 = Button(root, text="No", height=3, width=5, command=clicknobutton6)
        nobutton6.pack(side="left", expand=True)
        global notsurebutton6
        notsurebutton6 = Button(root, text="Not Sure", height=3, width=5, command=clicknotsurebutton6)
        notsurebutton6.pack(side="left", expand=True)

    def clicknotsurebutton5():
        global chemical
        chemical += 0
        question5.pack_forget()
        yesbutton5.pack_forget()
        nobutton5.pack_forget()
        notsurebutton5.pack_forget()
        global question6
        question6 = Label(root, text="Are you interested in learning more about quantum physics and its applications?",
                          bg="Light sky blue")
        question6.pack(side="left", expand=True)
        global yesbutton6
        yesbutton6 = Button(root, text="Yes", height=3, width=5, command=clickyesbutton6)
        yesbutton6.pack(side="left", expand=True)
        global nobutton6
        nobutton6 = Button(root, text="No", height=3, width=5, command=clicknobutton6)
        nobutton6.pack(side="left", expand=True)
        global notsurebutton6
        notsurebutton6 = Button(root, text="Not Sure", height=3, width=5, command=clicknotsurebutton6)
        notsurebutton6.pack(side="left", expand=True)

    def clickyesbutton4():
        global civil
        civil += 1
        question4.pack_forget()
        yesbutton4.pack_forget()
        nobutton4.pack_forget()
        notsurebutton4.pack_forget()
        global question5
        question5 = Label(root, text="Do you like biology and chemistry?", bg="Light sky blue")
        question5.pack(side="left", expand=True)
        global yesbutton5
        yesbutton5 = Button(root, text="Yes", height=3, width=5, command=clickyesbutton5)
        yesbutton5.pack(side="left", expand=True)
        global nobutton5
        nobutton5 = Button(root, text="No", height=3, width=5, command=clicknobutton5)
        nobutton5.pack(side="left", expand=True)
        global notsurebutton5
        notsurebutton5 = Button(root, text="Not Sure", height=3, width=5, command=clicknotsurebutton5)
        notsurebutton5.pack(side="left", expand=True)

    def clicknobutton4():
        global civil
        civil -= 1
        question4.pack_forget()
        yesbutton4.pack_forget()
        nobutton4.pack_forget()
        notsurebutton4.pack_forget()
        global question5
        question5 = Label(root, text="Do you like biology and chemistry?", bg="Light sky blue")
        question5.pack(side="left", expand=True)
        global yesbutton5
        yesbutton5 = Button(root, text="Yes", height=3, width=5, command=clickyesbutton5)
        yesbutton5.pack(side="left", expand=True)
        global nobutton5
        nobutton5 = Button(root, text="No", height=3, width=5, command=clicknobutton5)
        nobutton5.pack(side="left", expand=True)
        global notsurebutton5
        notsurebutton5 = Button(root, text="Not Sure", height=3, width=5, command=clicknotsurebutton5)
        notsurebutton5.pack(side="left", expand=True)

    def clicknotsurebutton4():
        global civil
        civil += 0
        question4.pack_forget()
        yesbutton4.pack_forget()
        nobutton4.pack_forget()
        notsurebutton4.pack_forget()
        global question5
        question5 = Label(root, text="Do you like biology and chemistry?", bg="Light sky blue")
        question5.pack(side="left", expand=True)
        global yesbutton5
        yesbutton5 = Button(root, text="Yes", height=3, width=5, command=clickyesbutton5)
        yesbutton5.pack(side="left", expand=True)
        global nobutton5
        nobutton5 = Button(root, text="No", height=3, width=5, command=clicknobutton5)
        nobutton5.pack(side="left", expand=True)
        global notsurebutton5
        notsurebutton5 = Button(root, text="Not Sure", height=3, width=5, command=clicknotsurebutton5)
        notsurebutton5.pack(side="left", expand=True)

    def clickq3aanswer1():
        global electrical
        electrical += 1
        question3a.pack_forget()
        q3aanswer1.pack_forget()
        q3aanswer2.pack_forget()
        q3aanswer3.pack_forget()
        global question4
        question4 = Label(root,
                          text="Are you interested in working at maintaining infrastructure \n like bridges, roads, water systems and sea ports?",
                          bg="Light sky blue")
        question4.pack(side="left", expand=True)
        global yesbutton4
        yesbutton4 = Button(root, text="Yes", height=3, width=5, command=clickyesbutton4)
        yesbutton4.pack(side="left", expand=True)
        global nobutton4
        nobutton4 = Button(root, text="No", height=3, width=5, command=clicknobutton4)
        nobutton4.pack(side="left", expand=True)
        global notsurebutton4
        notsurebutton4 = Button(root, text="Not Sure", height=3, width=5, command=clicknotsurebutton4)
        notsurebutton4.pack(side="left", expand=True)

    def clickq3aanswer2():
        global civil
        civil += 1
        question3a.pack_forget()
        q3aanswer1.pack_forget()
        q3aanswer2.pack_forget()
        q3aanswer3.pack_forget()
        global question4
        question4 = Label(root,
                          text="Are you interested in working at maintaining infrastructure \n like bridges, roads, water systems and sea ports?",
                          bg="Light sky blue")
        question4.pack(side="left", expand=True)
        global yesbutton4
        yesbutton4 = Button(root, text="Yes", height=3, width=5, command=clickyesbutton4)
        yesbutton4.pack(side="left", expand=True)
        global nobutton4
        nobutton4 = Button(root, text="No", height=3, width=5, command=clicknobutton4)
        nobutton4.pack(side="left", expand=True)
        global notsurebutton4
        notsurebutton4 = Button(root, text="Not Sure", height=3, width=5, command=clicknotsurebutton4)
        notsurebutton4.pack(side="left", expand=True)

    def clickq3aanswer3():
        global mechanical
        mechanical += 1
        question3a.pack_forget()
        q3aanswer1.pack_forget()
        q3aanswer2.pack_forget()
        q3aanswer3.pack_forget()
        global question4
        question4 = Label(root,
                          text="Are you interested in working at maintaining infrastructure \n like bridges, roads, water systems and sea ports?",
                          bg="Light sky blue")
        question4.pack(side="left", expand=True)
        global yesbutton4
        yesbutton4 = Button(root, text="Yes", height=3, width=5, command=clickyesbutton4)
        yesbutton4.pack(side="left", expand=True)
        global nobutton4
        nobutton4 = Button(root, text="No", height=3, width=5, command=clicknobutton4)
        nobutton4.pack(side="left", expand=True)
        global notsurebutton4
        notsurebutton4 = Button(root, text="Not Sure", height=3, width=5, command=clicknotsurebutton4)
        notsurebutton4.pack(side="left", expand=True)

    def clickyesbutton3():
        global civil
        civil += 1
        question3.pack_forget()
        yesbutton3.pack_forget()
        nobutton3.pack_forget()
        notsurebutton3.pack_forget()
        global question3a
        question3a = Label(root, text="You are put in a room and asked to fix a robot.\n What do you do first?",
                           bg="light sky blue")
        question3a.pack(side="left", expand=True)
        global q3aanswer1
        q3aanswer1 = Button(root, text="Toy with the wires and \n start coding", height=10, width=10,
                            command=clickq3aanswer1)
        q3aanswer1.pack(side="left", expand=True)
        global q3aanswer2
        q3aanswer2 = Button(root, text="Get tools and sketch a blueprint of the bot", height=10, width=10,
                            command=clickq3aanswer2)
        q3aanswer2.pack(side="left", expand=True)
        global q3aanswer3
        q3aanswer3 = Button(root, text="Figure out how to robot parts move", height=10, width=10,
                            command=clickq3aanswer3)
        q3aanswer3.pack(side="left", expand=True)

    def clicknobutton3():
        global civil
        civil -= 1
        question3.pack_forget()
        yesbutton3.pack_forget()
        nobutton3.pack_forget()
        notsurebutton3.pack_forget()
        global question3a
        question3a = Label(root, text="You are put in a room and asked to fix a robot. \n What do you do first?",
                           bg="light sky blue")
        question3a.pack(side="left", expand=True)
        global q3aanswer1
        q3aanswer1 = Button(root, text="Toy with the wires and \n start coding", height=10, width=10,
                            command=clickq3aanswer1)
        q3aanswer1.pack(side="left", expand=True)
        global q3aanswer2
        q3aanswer2 = Button(root, text="Get tools and sketch a blueprint of the bot", height=10, width=10,
                            command=clickq3aanswer2)
        q3aanswer2.pack(side="left", expand=True)
        global q3aanswer3
        q3aanswer3 = Button(root, text="Figure out how to robot parts move", height=10, width=10,
                            command=clickq3aanswer3)
        q3aanswer3.pack(side="left", expand=True)

    def clicknotsurebutton3():
        global civil
        civil += 0
        question3.pack_forget()
        yesbutton3.pack_forget()
        nobutton3.pack_forget()
        notsurebutton3.pack_forget()
        global question3a
        question3a = Label(root, text="You are put in a room and asked to fix a robot. \n What do you do first?",
                           bg="light sky blue")
        question3a.pack(side="left", expand=True)
        global q3aanswer1
        q3aanswer1 = Button(root, text="Toy with the wires and \n start coding", height=10, width=10,
                            command=clickq3aanswer1)
        q3aanswer1.pack(side="left", expand=True)
        global q3aanswer2
        q3aanswer2 = Button(root, text="Get tools and sketch a blueprint of the bot", height=10, width=10,
                            command=clickq3aanswer2)
        q3aanswer2.pack(side="left", expand=True)
        global q3aanswer3
        q3aanswer3 = Button(root, text="Figure out how to robot parts move", height=10, width=10,
                            command=clickq3aanswer3)
        q3aanswer3.pack(side="left", expand=True)

    def clickyesbutton2():
        global electrical
        electrical += 1
        question2.pack_forget()
        yesbutton2.pack_forget()
        nobutton2.pack_forget()
        notsurebutton2.pack_forget()
        global question3
        question3 = Label(root, text=" Are you interested in designing buildings and other infrastructure?",
                          bg="light sky blue")
        question3.pack(side="left", expand=True)
        global yesbutton3
        yesbutton3 = Button(root, text="Yes", height=3, width=5, command=clickyesbutton3)
        yesbutton3.pack(side="left", expand=True)
        global nobutton3
        nobutton3 = Button(root, text="No", height=3, width=5, command=clicknobutton3)
        nobutton3.pack(side="left", expand=True)
        global notsurebutton3
        notsurebutton3 = Button(root, text="Not Sure", height=3, width=5, command=clicknotsurebutton3)
        notsurebutton3.pack(side="left", expand=True)

    def clicknobutton2():
        global electrical
        electrical -= 1
        question2.pack_forget()
        yesbutton2.pack_forget()
        nobutton2.pack_forget()
        notsurebutton2.pack_forget()
        global question3
        question3 = Label(root, text=" Are you interested in designing buildings and other infrastructure?",
                          bg="light sky blue")
        question3.pack(side="left", expand=True)
        global yesbutton3
        yesbutton3 = Button(root, text="Yes", height=3, width=5, command=clickyesbutton3)
        yesbutton3.pack(side="left", expand=True)
        global nobutton3
        nobutton3 = Button(root, text="No", height=3, width=5, command=clicknobutton3)
        nobutton3.pack(side="left", expand=True)
        global notsurebutton3
        notsurebutton3 = Button(root, text="Not Sure", height=3, width=5, command=clicknotsurebutton3)
        notsurebutton3.pack(side="left", expand=True)

    def clicknotsurebutton2():
        global electrical
        electrical += 0
        question2.pack_forget()
        yesbutton2.pack_forget()
        nobutton2.pack_forget()
        notsurebutton2.pack_forget()
        global question3
        question3 = Label(root, text=" Are you interested in designing buildings and other infrastructure?",
                          bg="light sky blue")
        question3.pack(side="left", expand=True)
        global yesbutton3
        yesbutton3 = Button(root, text="Yes", height=3, width=5, command=clickyesbutton3)
        yesbutton3.pack(side="left", expand=True)
        global nobutton3
        nobutton3 = Button(root, text="No", height=3, width=5, command=clicknobutton3)
        nobutton3.pack(side="left", expand=True)
        global notsurebutton3
        notsurebutton3 = Button(root, text="Not Sure", height=3, width=5, command=clicknotsurebutton3)
        notsurebutton3.pack(side="left", expand=True)
















    def clickyesbutton1():

    global mechanical
    mechanical += 1
    question1.pack_forget()
    yesbutton1.pack_forget()
    nobutton1.pack_forget()
    notsurebutton1.pack_forget()
    global question2
    question2 = Label(root, text="Would you like working with electrical devices and systems?", bg="Light sky blue")
    question2.pack(side="left")
    global yesbutton2
    yesbutton2 = Button(root, text="Yes", height=3, width=5, command=clickyesbutton2)
    yesbutton2.pack(side="left", expand=True)
    global nobutton2
    nobutton2 = Button(root, text="No", height=3, width=5, command=clicknobutton2)
    nobutton2.pack(side="left", expand=True)
    global notsurebutton2
    notsurebutton2 = Button(root, text="Not Sure", height=3, width=5, command=clicknotsurebutton2)
    notsurebutton2.pack(side="left", expand=True)

    def clicknobutton1():
        global mechanical
        mechanical -= 1
        question1.pack_forget()
        yesbutton1.pack_forget()
        nobutton1.pack_forget()
        notsurebutton1.pack_forget()
        global question2
        question2 = Label(root, text="Would you like working with electrical devices and systems?", bg="Light sky blue")
        question2.pack(side="left")
        global yesbutton2
        yesbutton2 = Button(root, text="Yes", height=3, width=5, command=clickyesbutton2)
        yesbutton2.pack(side="left", expand=True)
        global nobutton2
        nobutton2 = Button(root, text="No", height=3, width=5, command=clicknobutton2)
        nobutton2.pack(side="left", expand=True)
        global notsurebutton2
        notsurebutton2 = Button(root, text="Not Sure", height=3, width=5, command=clicknotsurebutton2)
        notsurebutton2.pack(side="left", expand=True)

    def clicknotsurebutton1():
        global mechanical
        mechanical += 0
        question1.pack_forget()
        yesbutton1.pack_forget()
        nobutton1.pack_forget()
        notsurebutton1.pack_forget()
        global question2
        question2 = Label(root, text="Would you like working with electrical devices and systems?", bg="Light sky blue")
        question2.pack(side="left")
        global yesbutton2
        yesbutton2 = Button(root, text="Yes", height=3, width=5, command=clickyesbutton2)
        yesbutton2.pack(side="left", expand=True)
        global nobutton2
        nobutton2 = Button(root, text="No", height=3, width=5, command=clicknobutton2)
        nobutton2.pack(side="left", expand=True)
        global notsurebutton2
        notsurebutton2 = Button(root, text="Not Sure", height=3, width=5, command=clicknotsurebutton2)
        notsurebutton2.pack(side="left", expand=True)

    def clickmyButton():
        global question1
        question1 = Label(root,
                          text="Would you like to apply physics and math in order to \n design/manufacture a mechanical system?",
                          bg='light sky blue')
        question1.pack(side="left")
        global yesbutton1
        yesbutton1 = Button(root, text="Yes", height=3, width=5, command=clickyesbutton1)
        yesbutton1.pack(side="left", expand=True)
        global nobutton1
        nobutton1 = Button(root, text="No", height=3, width=5, command=clicknobutton1)
        nobutton1.pack(side="left", expand=True)
        global notsurebutton1
        notsurebutton1 = Button(root, text="Not Sure", height=3, width=5, command=clicknotsurebutton1)
        notsurebutton1.pack(side="left", expand=True)

        myLabel.pack_forget()
        myButton.pack_forget()

    myLabel = Label(root, text="Welcome to Engineering Cruising", font=("Garamond", 18), bg='light sky blue')

    myLabel.pack()

    myButton = Button(root, text="", height=1, width=1, command=clickmyButton)
    myButton.pack()
    labell = Label(root, text="start quiz")
    labell.pack()

    root.mainloop()


rungame()