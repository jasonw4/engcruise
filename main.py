from tkinter import Tk, Button, Label

mechanical = 5
chemical = 5
civil = 5
electrical = 5



def rungame():
  root = Tk()
  root.wm_title("Engineering Cruising")
  root.geometry('1080x1080')
  root.configure(bg='white')

  def clickyesbutton17():
    global chemical
    chemical += 1
    question17.pack_forget()
    yesbutton17.pack_forget()
    nobutton17.pack_forget()
    notsurebutton17.pack_forget()
    labelyesbutton17.pack_forget()
    labelnobutton17.pack_forget()
    labelnotsurebutton17.pack_forget()
    if chemical == 9 :
      




      def clickchempro():
        ceramicsinfo.pack_forget()
        next3.pack_forget()
        global chemproinfo
        chemproinfo = Label(root, text = "The main role of chemical engineers is to design and troubleshoot processes for the production \n  of chemicals, fuels, foods, pharmaceuticals, and biologicals. \n Median Salary : $108,700 \n Job Demand expected to increase 4% in the next 10 years. \n Top Colleges in NY : \n Columbia University \n Cornell University \n NYU \n University of Rochester", bg = "white", fg = "crimson", font=("EB Garamond", 24) )

  

        

      def clickceramics():
        mineralproinfo.pack_forget()
        next2.pack_forget()
        global ceramicsinfo
        ceramicsinfo = Label(root, text = "Ceramic engineering is the science and technology \n of creating objects from inorganic, non-metallic materials. \n Median Salary: $83,000 \n Job Demand expected to grow 6.8% in next 10 years. \n Top Colleges in NY : \n Alfred University ", bg = "white", fg = "crimson", font=("EB Garamond", 24))
        ceramicsinfo.pack()

        global next3
        next3 = Button(root, text = "NEXT", height = 5, width = 8, command = clickchempro)
        next3.pack()



      def clickmineralpro():
        biotechinfo.pack_forget()
        next1.pack_forget()
        global mineralproinfo
        mineralproinfo = Label(root, text = "Mineral Processing Engineering deals with the extraction, \n  separation, and concentration of minerals from raw ores. \n Median Salary : $60,000 \n Job Demand expected to grow 4% in the next 10 years. \n Top Colleges : \n Colorado School of Mines", bg = "white", fg = "crimson", font=("EB Garamond", 24))
        mineralproinfo.pack()

        global next2
        next2 = Button(root, text = "NEXT", height = 5, width = 8, command = clickceramics)
        next2.pack()
        



      def clickbiotech():
        chemical_response.pack_forget()
        subfields.pack_forget()
        global biotechinfo
        biotechinfo = Label(root, text = "Biotechnology engineering is the research and study \n of micro-organism, bio-organisms, cell functions in living beings. \n Median Salary : $108,696 \n Job Demand expected to grow 5% in the next 10 years. \n Top Colleges in NY : \n Columbia University \n Cornell University \n Syracuse University \n RPI", bg = "white", fg = "crimson", font=("EB Garamond", 24))
        biotechinfo.pack()

        global next1
        next1 = Button(root, text = "NEXT", height = 5, width = 8, command = clickmineralpro)
        next1.pack()






      def chemicalwin():

        global chemical_response
        chemical_response = Label(root, text="Chemical Engineering seems to be the best fit for you. \n Chemical engineering is the branch of engineering that deals \n with chemical production and the manufacture of products through chemical processes.\n Some classes/clubs you should consider are: \n - Calculus \n -Chemistry \n - Computer Science \n Some subfields that you can look into are: \n - Biotechnology \n - Mineral Processing \n - Ceramics \n - Chemical Processing", bg="white", fg = "crimson", font=("EB Garamond", 24))
        chemical_response.pack()
        

        global subfields
        subfields = Button(root, text = "Subfields", height = 5, width = 8, command = clickbiotech)
        subfields.pack()

      chemicalwin()
    else:
      def clickstructural():
        environment.pack_forget()
        next13.pack_forget()

        global structural
        structural = Label(root, text = "Structural engineers focus on the physical integrity and \n design of projects such as buildings, bridges, and tunnels.\n Median Salary: $78,460 \n Job Demand expected to increase 6% in the next 10 years. \n Top Colleges in NY: \n NYU \n UBuffalo", bg = "white", fg = "crimson", font=("EB Garamond", 24))
        structural.pack()

    


      def clickenvironment():
        geotech.pack_forget()
        next12.pack_forget()

        global environment
        environment = Label(root, text = "Environmental engineers use the principles of engineering, soil science, biology, \n and chemistry to develop solutions to environmental problems. They work to improve \n recycling, waste disposal, public health, and water and air pollution control. \n Median Salary : $84,560 \n Job Demand expected to increase 3% in the next 10 years. \n Top Colleges in NY: \n Columbia University \n Cornell University \n RPI \n RIT", bg = "white", fg = "crimson", font=("EB Garamond", 24))
        environment.pack()

        global next13
        next13 = Button(root, text = "NEXT" , height = 5, width = 8, command = clickstructural)
        next13.pack()


      def clickgeotech():
        coastaleng.pack_forget()
        next11.pack_forget()

        global geotech
        geotech = Label(root, text = "Geotechnical engineering, also known as geotechnics, is the branch \n of civil engineering concerned with the engineering behavior of earth materials.\n Median Salary: $65,497 \n Job Demand expected to increase 11% in the next 10 years. \n Top Colleges in NY: \n Columbia University \n Cornell University \n RPI", bg = "white", fg = "crimson", font=("EB Garamond", 24))
        geotech.pack()

        global next12
        next12 = Button(root, text = "NEXT" , height = 5, width = 8, command = clickenvironment)
        next12.pack()



      def clickcoastaleng():
        civil_response.pack_forget()
        subfields4.pack_forget()

        global coastaleng
        coastaleng = Label(root, text = "Coastal engineering is a division of civil engineering responsible for \n the organization, conception, development and preservation of works in the coastal area. \n Median Salary: $98,000 \n Job Demand expected to increase 1% in the next 10 years. \n Top Colleges in NY : \n Columbia University \n Cornell University \n RPI", bg = "white", fg = "crimson", font=("EB Garamond", 24))
        coastaleng.pack()

        global next11
        next11 = Button(root, text = "NEXT" , height = 5, width = 8, command = clickgeotech)
        next11.pack()




      def civilwin():
        finalstatement.pack_forget()
        endmechanical.pack_forget()
        endcivil.pack_forget()
        endelectrical.pack_forget()
        endchemical.pack_forget()
        global civil_response
        civil_response = Label(root, text="Civil Engineering seems to be the best fit for you.\nCivil engineering is a professional engineering discipline that deals \n with the design, construction, and maintenance of the physical and naturally built environment. \n Some classes/clubs that you should consider are: \n -CAD \n - Engineering 1 \n - Engineering 2 \n -Robotics \n -Calculus \n -Physics \n - Communication Technology \n - Transportation Technology \n Some subfields that you can look into are: \n - Coastal Engineering \n - Geotechnical Engineering \n - Environmental Engineering \n - Structural Engineering ", bg = "white", fg = "crimson", font=("EB Garamond", 24))
        civil_response.pack()
       

        global subfields4
        subfields4 = Button(root, text = "NEXT", height = 5, width = 8, command = clickcoastaleng)
        subfields4.pack()








      def clickmicroelec():
        signalproinfo.pack_forget()
        next10.pack_forget()
        global microelecinfo
        microelecinfo = Label(root, text = "Microelectronics engineers develop plans and construct prototypes of \n electronic circuit chips, circuit boards, and semiconductors. \n Median Salary: $76,100 \n Job Demand expected to increase roughly 1% in the next 10 years. \n Top Colleges in NY : \n Cornell University \n RPI \n Columbia University \n Clarkson University ", bg = "white", fg = "crimson", font=("EB Garamond", 24))
        microelecinfo.pack()


      def clicksignalpro():
        controlsysinfo.pack_forget()
        next9.pack_forget()
        global signalproinfo
        signalproinfo = Label(root, text = "A signal processing engineer is an information technologies expert \n that analyzes and alters digital signals to make them more accurate and reliable.\n Median Salary: $105,000 \n Top Colleges in NY : \n Cornell University \n RIT \n Syracuse University ", bg = "white", fg = "crimson", font=("EB Garamond", 24))
        signalproinfo.pack()
        global next10
        next10 = Button(root, text = "NEXT", height = 5, width = 8, command = clickmicroelec)
        next10.pack()



      def clickcontrolsys():
        telecominfo.pack_forget()
        next8.pack_forget()
        global controlsysinfo
        controlsysinfo = Label(root, text = "A Control Systems Engineer is responsible for designing, developing, \n and implementing solutions that control dynamic systems. \n Median Salary : $88, 616 \n Job Demand expected to increase 2% in the next 10 yearss. \n Top Colleges in NY : \n RPI \n Cornell University \n West Point \n Binghamton ", bg = "white", fg = "crimson", font=("EB Garamond", 24))
        controlsysinfo.pack()

        global next9
        next9 = Button(root, text = "NEXT", height = 5, width = 8, command = clicksignalpro)
        next9.pack()




      def clicktelecom():
        electrical_response.pack_forget()
        subfields3.pack_forget()
        global telecominfo
        telecominfo = Label(root, text = "Telecommunications engineers or telecom engineers are expert in managing data \n such as voice, video, calls, and text over different modes of communication. \n Median Salary: $76, 524 \n Job Demand expected to increase around 5% in the next 10 years. \n Top Colleges in NY : \n SUNY Stonybrook", bg = "white", fg = "crimson", font=("EB Garamond", 24))
        telecominfo.pack()

        global next8
        next8 = Button(root, text = "NEXT", height = 5, width = 8, command = clickcontrolsys)
        next8.pack()



      def electricalwin():
        finalstatement.pack_forget()
        endmechanical.pack_forget()
        endcivil.pack_forget()
        endelectrical.pack_forget()
        endchemical.pack_forget()
        global electrical_response
        electrical_response = Label(root, text="Electrical Engineering seems to be the best fit for you.\nElectrical Engineering is an engineering discipline concerned \n with the study, design and application of equipment, devices \n and systems which use electricity, electronics, and electromagnetism. \n Some classes/clubs you should try out are: \n - Robotics \n - Engineering 1 \n - Engineering 2 \n - Coding Club \n - RC Club \n - Computer Science \n Some subfields that you can look into are: \n -Telecommunications \n -Control Systems \n -Signal Processing \n - Microelectronics", bg="white", fg = "crimson" , font=("EB Garamond", 24))
        electrical_response.pack()


        global subfields3
        subfields3 = Button(root, text = "Subfields", height = 5, width = 8, command = clicktelecom)
        subfields3.pack()


      def clickchempro():
        ceramicsinfo.pack_forget()
        next7.pack_forget()
        global chemproinfo
        chemproinfo = Label(root, text = "The main role of chemical engineers is to design and troubleshoot processes for the production \n  of chemicals, fuels, foods, pharmaceuticals, and biologicals. \n Median Salary : $108,700 \n Job Demand expected to increase 4% in the next 10 years. \n Top Colleges in NY : \n Columbia University \n Cornell University \n NYU \n University of Rochester", bg = "white", fg = "crimson" , font=("EB Garamond", 24))

  

        

      def clickceramics():
        mineralproinfo.pack_forget()
        next6.pack_forget()
        global ceramicsinfo
        ceramicsinfo = Label(root, text = "Ceramic engineering is the science and technology \n of creating objects from inorganic, non-metallic materials. \n Median Salary: $83,000 \n Job Demand expected to grow 6.8% in next 10 years. \n Top Colleges in NY : \n Alfred University ", bg = "white", fg = "crimson", font=("EB Garamond", 24))
        ceramicsinfo.pack()

        global next7
        next7 = Button(root, text = "NEXT", height = 5, width = 8, command = clickchempro)
        next7.pack()



      def clickmineralpro():
        biotechinfo.pack_forget()
        next5.pack_forget()
        global mineralproinfo
        mineralproinfo = Label(root, text = "Mineral Processing Engineering deals with the extraction, \n  separation, and concentration of minerals from raw ores. \n Median Salary : $60,000 \n Job Demand expected to grow 4% in the next 10 years. \n Top Colleges : \n Colorado School of Mines", bg = "white", fg = "crimson", font=("EB Garamond", 24))
        mineralproinfo.pack()

        global next6
        next6 = Button(root, text = "NEXT", height = 5, width = 8, command = clickceramics)
        next6.pack()
        



      def clickbiotech():
        chemical_response.pack_forget()
        subfields2.pack_forget()
        global biotechinfo
        biotechinfo = Label(root, text = "Biotechnology engineering is the research and study \n of micro-organism, bio-organisms, cell functions in living beings. \n Median Salary : $108,696 \n Job Demand expected to grow 5% in the next 10 years. \n Top Colleges in NY : \n Columbia University \n Cornell University \n Syracuse University \n RPI", bg = "white", fg = "crimson", font=("EB Garamond", 24))
        biotechinfo.pack()

        global next5
        next5 = Button(root, text = "NEXT", height = 5, width = 8, command = clickmineralpro)
        next5.pack()






      def chemicalwin():
        finalstatement.pack_forget()
        endmechanical.pack_forget()
        endcivil.pack_forget()
        endelectrical.pack_forget()
        endchemical.pack_forget()

        global chemical_response
        chemical_response = Label(root, text="Chemical Engineering seems to be the best fit for you. \n Chemical engineering is the branch of engineering that deals \n with chemical production and the manufacture of products through chemical processes.\n Some classes/clubs you should consider are: \n - Calculus \n -Chemistry \n - Computer Science \n Some subfields that you can look into are: \n - Biotechnology \n - Mineral Processing \n - Ceramics \n - Chemical Processing", bg="white", fg = "crimson", font=("EB Garamond", 24))
        chemical_response.pack()
        

        global subfields2
        subfields2 = Button(root, text = "Subfields", height = 5, width = 8, command = clickbiotech)
        subfields2.pack()














      def clickrobotics():
        datainfo.pack_forget()
        next4.pack_forget()
        global roboticsinfo
        roboticsinfo = Label(root, text = "Robotics engineering is a field of engineering \n which centers on building machines that replicate human actions. \n Median Salary : $99,040 \n Job Demand expected to grow 9% in the next 10 years. \n Top Colleges in NY : \n Cornell University \n NYU ", bg = "white", fg = "crimson", font=("EB Garamond", 24))
        roboticsinfo.pack()
                
 


      def clickdataanalysis():
        cybersecurityinfo.pack_forget()
        next3.pack_forget()
        global datainfo
        datainfo = Label(root, text = "Data engineers are responsible for finding trends in data sets \n and developing algorithms to help make raw data more useful to the enterprise. \n Median Salary : $137,776 \n Job Demand expected to increase 21% in the next 10 years. \n Top Colleges in NY : \n Columbia University \n Cornell University \n NYU \n Syracuse \n NYIT ", bg = "white", fg = "crimson", font=("EB Garamond", 24))
        datainfo.pack()
        global next4
        next4 = Button(root, text = "NEXT", height = 5, width = 8, command = clickrobotics)
        next4.pack()
     

      
      def clickcybersecurity():
        automationinfo.pack_forget()
        next2.pack_forget()
        global cybersecurityinfo
        cybersecurityinfo = Label(root, text = "Cybersecurity engineers, sometimes called information security engineers,\n identify threats and vulnerabilities in systems and software, \n then apply their skills to developing and implementing high-tech solutions \n to defend against hacking, malware and ransomware, \n insider threats and all types of cybercrime. \n Median Salary: $90,120 \n Job Demand expected to grow 31% in the next 10 years. \n Top Colleges in NY : \n NYU \n Syracuse University \n RIT \n Pace University", bg = "white", fg = "crimson", font=("EB Garamond", 24))
        cybersecurityinfo.pack()
        global next3
        next3 = Button(root, text = "NEXT", height = 5, width = 8, command = clickdataanalysis)
        next3.pack()
     


      def clickautomation():
        aeroinfo.pack_forget()
        next1.pack_forget()

        global automationinfo
        automationinfo = Label(root, text = "An Automation Engineer utilizes technology \n to improve, streamline and automate a manufacturing process. \n Median Salary : $88,100 \n Job Demand expected to grow around 4% in the next 10 years \n Top Colleges in NY : \n SUNY Farmingdale \n SUNY College of Tech at Alfred", bg = "white", fg = "crimson", font=("EB Garamond", 24))
        automationinfo.pack()
        global next2
        next2 = Button(root, text = "NEXT", height = 5, width = 8, command = clickcybersecurity)
        next2.pack()
     


      def clickaerospace():
        subfields1.pack_forget()
        mechanical_response.pack_forget()
        global aeroinfo
        aeroinfo = Label(root, text = "Aerospace engineering is the primary field of engineering \n concerned with the development of aircraft and spacecraft.\n Median Salary : $116,500 \n Job Demand expected to grow around 3% in the next 10 years \n Top Colleges in NY : \n Cornell University \n RPI \n Syracuse University \n SUNY Buffalo", bg = "white", fg = "crimson", font=("EB Garamond", 24))
        aeroinfo.pack()
        global next1
        next1 = Button(root, text = "NEXT", height = 5, width = 8, command = clickautomation)
        next1.pack()

        


      def mechanicalwin():
        finalstatement.pack_forget()
        endmechanical.pack_forget()
        endcivil.pack_forget()
        endelectrical.pack_forget()
        endchemical.pack_forget()
        
        
        global mechanical_response
        mechanical_response = Label(root, text="Mechanical Engineering seems to be the best fit for you.\n Mechanical Engineering is the branch of engineering dealing \n with the design, construction, and use of machines. \n Some classes/clubs you should consider are: \n - Robotics \n - RC Club \n -DDP \n -CAD \n -Engineering 1 \n -Engineering 2 \n - Physics \n -Calculus \n Some subfields you might want to look into are: \n - Aerospace \n - Automation \n - Cybersecurity \n -Robotics \n -Data Analysis", bg = "white", fg = "crimson", font=("EB Garamond", 24))
        mechanical_response.pack()


        global subfields1
        subfields1 = Button(root, text = "Subfields", height = 5, width = 8, command = clickaerospace)
        subfields1.pack()



      def endgame():
        global finalstatement
        finalstatement = Label(root, text = "Unfortunately, we were unable to get a definite choice for you.\n  However, you can still check out each of the fields down below.", bg="white", fg = "crimson", font=("EB Garamond", 24))
        finalstatement.pack()

        global endmechanical
        endmechanical = Button(root, text = "Mechanical \n Engineering", height = 8, width = 8, fg = "crimson", command = mechanicalwin)
        endmechanical.pack(side = "top", expand = True)

        global endcivil
        endcivil = Button(root, text = "Civil \n Engineering", height = 8, width = 8,  fg = "crimson", command = civilwin )
        endcivil.pack(side = "top", expand = True)

        global endelectrical
        endelectrical = Button(root, text = "Electrical \n Engineering", height = 8, width = 8,  fg = "crimson", command = electricalwin)
        endelectrical.pack(side = "top", expand = True)

        global endchemical
        endchemical = Button(root, text = "Chemical \n Engineering", height = 8, width = 8,  fg = "crimson", command = chemicalwin)
        endchemical.pack(side = "top", expand = True)



      endgame()


  def clicknobutton17():
    question17.pack_forget()
    yesbutton17.pack_forget()
    nobutton17.pack_forget()
    notsurebutton17.pack_forget()
    labelyesbutton17.pack_forget()
    labelnobutton17.pack_forget()
    labelnotsurebutton17.pack_forget()
    def clickstructural():
      environment.pack_forget()
      next13.pack_forget()

      global structural
      structural = Label(root, text = "Structural engineers focus on the physical integrity and \n design of projects such as buildings, bridges, and tunnels.\n Median Salary: $78,460 \n Job Demand expected to increase 6% in the next 10 years. \n Top Colleges in NY: \n NYU \n UBuffalo", bg = "white", fg = "crimson", font=("EB Garamond", 24))
      structural.pack()

    


    def clickenvironment():
      geotech.pack_forget()
      next12.pack_forget()

      global environment
      environment = Label(root, text = "Environmental engineers use the principles of engineering, soil science, biology, \n and chemistry to develop solutions to environmental problems. They work to improve \n recycling, waste disposal, public health, and water and air pollution control. \n Median Salary : $84,560 \n Job Demand expected to increase 3% in the next 10 years. \n Top Colleges in NY: \n Columbia University \n Cornell University \n RPI \n RIT", bg = "white", fg = "crimson", font=("EB Garamond", 24))
      environment.pack()

      global next13
      next13 = Button(root, text = "NEXT" , height = 5, width = 8, command = clickstructural)
      next13.pack()


    def clickgeotech():
      coastaleng.pack_forget()
      next11.pack_forget()

      global geotech
      geotech = Label(root, text = "Geotechnical engineering, also known as geotechnics, is the branch \n of civil engineering concerned with the engineering behavior of earth materials.\n Median Salary: $65,497 \n Job Demand expected to increase 11% in the next 10 years. \n Top Colleges in NY: \n Columbia University \n Cornell University \n RPI", bg = "white", fg = "crimson", font=("EB Garamond", 24))
      geotech.pack()

      global next12
      next12 = Button(root, text = "NEXT" , height = 5, width = 8, command = clickenvironment)
      next12.pack()



    def clickcoastaleng():
      civil_response.pack_forget()
      subfields4.pack_forget()

      global coastaleng
      coastaleng = Label(root, text = "Coastal engineering is a division of civil engineering responsible for \n the organization, conception, development and preservation of works in the coastal area. \n Median Salary: $98,000 \n Job Demand expected to increase 1% in the next 10 years. \n Top Colleges in NY : \n Columbia University \n Cornell University \n RPI", bg = "white", fg = "crimson", font=("EB Garamond", 24))
      coastaleng.pack()

      global next11
      next11 = Button(root, text = "NEXT" , height = 5, width = 8, command = clickgeotech)
      next11.pack()




    def civilwin():
      finalstatement.pack_forget()
      endmechanical.pack_forget()
      endcivil.pack_forget()
      endelectrical.pack_forget()
      endchemical.pack_forget()
      global civil_response
      civil_response = Label(root, text="Civil Engineering seems to be the best fit for you.\nCivil engineering is a professional engineering discipline that deals \n with the design, construction, and maintenance of the physical and naturally built environment. \n Some classes/clubs that you should consider are: \n -CAD \n - Engineering 1 \n - Engineering 2 \n -Robotics \n -Calculus \n -Physics \n - Communication Technology \n - Transportation Technology \n Some subfields that you can look into are: \n - Coastal Engineering \n - Geotechnical Engineering \n - Environmental Engineering \n - Structural Engineering ", bg = "white", fg = "crimson", font=("EB Garamond", 24))
      civil_response.pack()
      

      global subfields4
      subfields4 = Button(root, text = "NEXT", height = 5, width = 8, command = clickcoastaleng)
      subfields4.pack()








    def clickmicroelec():
      signalproinfo.pack_forget()
      next10.pack_forget()
      global microelecinfo
      microelecinfo = Label(root, text = "Microelectronics engineers develop plans and construct prototypes of \n electronic circuit chips, circuit boards, and semiconductors. \n Median Salary: $76,100 \n Job Demand expected to increase roughly 1% in the next 10 years. \n Top Colleges in NY : \n Cornell University \n RPI \n Columbia University \n Clarkson University ", bg = "white", fg = "crimson", font=("EB Garamond", 24))
      microelecinfo.pack()


    def clicksignalpro():
      controlsysinfo.pack_forget()
      next9.pack_forget()
      global signalproinfo
      signalproinfo = Label(root, text = "A signal processing engineer is an information technologies expert \n that analyzes and alters digital signals to make them more accurate and reliable.\n Median Salary: $105,000 \n Top Colleges in NY : \n Cornell University \n RIT \n Syracuse University ", bg = "white", fg = "crimson", font=("EB Garamond", 24))
      signalproinfo.pack()
      global next10
      next10 = Button(root, text = "NEXT", height = 5, width = 8, command = clickmicroelec)
      next10.pack()



    def clickcontrolsys():
      telecominfo.pack_forget()
      next8.pack_forget()
      global controlsysinfo
      controlsysinfo = Label(root, text = "A Control Systems Engineer is responsible for designing, developing, \n and implementing solutions that control dynamic systems. \n Median Salary : $88, 616 \n Job Demand expected to increase 2% in the next 10 yearss. \n Top Colleges in NY : \n RPI \n Cornell University \n West Point \n Binghamton ", bg = "white", fg = "crimson", font=("EB Garamond", 24))
      controlsysinfo.pack()

      global next9
      next9 = Button(root, text = "NEXT", height = 5, width = 8, command = clicksignalpro)
      next9.pack()




    def clicktelecom():
      electrical_response.pack_forget()
      subfields3.pack_forget()
      global telecominfo
      telecominfo = Label(root, text = "Telecommunications engineers or telecom engineers are expert in managing data \n such as voice, video, calls, and text over different modes of communication. \n Median Salary: $76, 524 \n Job Demand expected to increase around 5% in the next 10 years. \n Top Colleges in NY : \n SUNY Stonybrook", bg = "white", fg = "crimson", font=("EB Garamond", 24))
      telecominfo.pack()

      global next8
      next8 = Button(root, text = "NEXT", height = 5, width = 8, command = clickcontrolsys)
      next8.pack()



    def electricalwin():
      finalstatement.pack_forget()
      endmechanical.pack_forget()
      endcivil.pack_forget()
      endelectrical.pack_forget()
      endchemical.pack_forget()
      global electrical_response
      electrical_response = Label(root, text="Electrical Engineering seems to be the best fit for you. \nElectrical Engineering is an engineering discipline concerned \n with the study, design and application of equipment, devices \n and systems which use electricity, electronics, and electromagnetism.\n Some classes/clubs you should try out are: \n - Robotics \n - Engineering 1 \n - Engineering 2 \n - Coding Club \n - RC Club \n - Computer Science \n Some subfields that you can look into are: \n -Telecommunications \n -Control Systems \n -Signal Processing \n - Microelectronics", bg="white", fg = "crimson", font=("EB Garamond", 24) )
      electrical_response.pack()


      global subfields3
      subfields3 = Button(root, text = "Subfields", height = 5, width = 8, command = clicktelecom)
      subfields3.pack()


    def clickchempro():
      ceramicsinfo.pack_forget()
      next7.pack_forget()
      global chemproinfo
      chemproinfo = Label(root, text = "The main role of chemical engineers is to design and troubleshoot processes for the production \n  of chemicals, fuels, foods, pharmaceuticals, and biologicals. \n Median Salary : $108,700 \n Job Demand expected to increase 4% in the next 10 years. \n Top Colleges in NY : \n Columbia University \n Cornell University \n NYU \n University of Rochester", bg = "white", fg = "crimson" , font=("EB Garamond", 24))



      

    def clickceramics():
      mineralproinfo.pack_forget()
      next6.pack_forget()
      global ceramicsinfo
      ceramicsinfo = Label(root, text = "Ceramic engineering is the science and technology \n of creating objects from inorganic, non-metallic materials. \n Median Salary: $83,000 \n Job Demand expected to grow 6.8% in next 10 years. \n Top Colleges in NY : \n Alfred University ", bg = "white", fg = "crimson", font=("EB Garamond", 24))
      ceramicsinfo.pack()

      global next7
      next7 = Button(root, text = "NEXT", height = 5, width = 8, command = clickchempro)
      next7.pack()



    def clickmineralpro():
      biotechinfo.pack_forget()
      next5.pack_forget()
      global mineralproinfo
      mineralproinfo = Label(root, text = "Mineral Processing Engineering deals with the extraction, \n  separation, and concentration of minerals from raw ores. \n Median Salary : $60,000 \n Job Demand expected to grow 4% in the next 10 years. \n Top Colleges : \n Colorado School of Mines", bg = "white", fg = "crimson", font=("EB Garamond", 24))
      mineralproinfo.pack()

      global next6
      next6 = Button(root, text = "NEXT", height = 5, width = 8, command = clickceramics)
      next6.pack()
      



    def clickbiotech():
      chemical_response.pack_forget()
      subfields2.pack_forget()
      global biotechinfo
      biotechinfo = Label(root, text = "Biotechnology engineering is the research and study \n of micro-organism, bio-organisms, cell functions in living beings. \n Median Salary : $108,696 \n Job Demand expected to grow 5% in the next 10 years. \n Top Colleges in NY : \n Columbia University \n Cornell University \n Syracuse University \n RPI", bg = "white", fg = "crimson", font=("EB Garamond", 24))
      biotechinfo.pack()

      global next5
      next5 = Button(root, text = "NEXT", height = 5, width = 8, command = clickmineralpro)
      next5.pack()






    def chemicalwin():
      finalstatement.pack_forget()
      endmechanical.pack_forget()
      endcivil.pack_forget()
      endelectrical.pack_forget()
      endchemical.pack_forget()

      global chemical_response
      chemical_response = Label(root, text="Chemical Engineering seems to be the best fit for you. \n Chemical engineering is the branch of engineering that deals \n with chemical production and the manufacture of products through chemical processes.\n Some classes/clubs you should consider are: \n - Calculus \n -Chemistry \n - Computer Science \n Some subfields that you can look into are: \n - Biotechnology \n - Mineral Processing \n - Ceramics \n - Chemical Processing", bg="white", fg = "crimson", font=("EB Garamond", 24))
      chemical_response.pack()
      

      global subfields2
      subfields2 = Button(root, text = "Subfields", height = 5, width = 8, command = clickbiotech)
      subfields2.pack()














    def clickrobotics():
      datainfo.pack_forget()
      next4.pack_forget()
      global roboticsinfo
      roboticsinfo = Label(root, text = "Robotics engineering is a field of engineering \n which centers on building machines that replicate human actions. \n Median Salary : $99,040 \n Job Demand expected to grow 9% in the next 10 years. \n Top Colleges in NY : \n Cornell University \n NYU ", bg = "white", fg = "crimson", font=("EB Garamond", 24))
      roboticsinfo.pack()
              



    def clickdataanalysis():
      cybersecurityinfo.pack_forget()
      next3.pack_forget()
      global datainfo
      datainfo = Label(root, text = "Data engineers are responsible for finding trends in data sets \n and developing algorithms to help make raw data more useful to the enterprise. \n Median Salary : $137,776 \n Job Demand expected to increase 21% in the next 10 years. \n Top Colleges in NY : \n Columbia University \n Cornell University \n NYU \n Syracuse \n NYIT ", bg = "white", fg = "crimson", font=("EB Garamond", 24))
      datainfo.pack()
      global next4
      next4 = Button(root, text = "NEXT", height = 5, width = 8, command = clickrobotics)
      next4.pack()
    

    
    def clickcybersecurity():
      automationinfo.pack_forget()
      next2.pack_forget()
      global cybersecurityinfo
      cybersecurityinfo = Label(root, text = "Cybersecurity engineers, sometimes called information security engineers,\n identify threats and vulnerabilities in systems and software, \n then apply their skills to developing and implementing high-tech solutions \n to defend against hacking, malware and ransomware, \n insider threats and all types of cybercrime. \n Median Salary: $90,120 \n Job Demand expected to grow 31% in the next 10 years. \n Top Colleges in NY : \n NYU \n Syracuse University \n RIT \n Pace University", bg = "white", fg = "crimson", font=("EB Garamond", 24))
      cybersecurityinfo.pack()
      global next3
      next3 = Button(root, text = "NEXT", height = 5, width = 8, command = clickdataanalysis)
      next3.pack()
    


    def clickautomation():
      aeroinfo.pack_forget()
      next1.pack_forget()

      global automationinfo
      automationinfo = Label(root, text = "An Automation Engineer utilizes technology \n to improve, streamline and automate a manufacturing process. \n Median Salary : $88,100 \n Job Demand expected to grow around 4% in the next 10 years \n Top Colleges in NY : \n SUNY Farmingdale \n SUNY College of Tech at Alfred", bg = "white", fg = "crimson", font=("EB Garamond", 24))
      automationinfo.pack()
      global next2
      next2 = Button(root, text = "NEXT", height = 5, width = 8, command = clickcybersecurity)
      next2.pack()
    


    def clickaerospace():
      subfields1.pack_forget()
      mechanical_response.pack_forget()
      global aeroinfo
      aeroinfo = Label(root, text = "Aerospace engineering is the primary field of engineering \n concerned with the development of aircraft and spacecraft.\n Median Salary : $116,500 \n Job Demand expected to grow around 3% in the next 10 years \n Top Colleges in NY : \n Cornell University \n RPI \n Syracuse University \n SUNY Buffalo", bg = "white", fg = "crimson", font=("EB Garamond", 24))
      aeroinfo.pack()
      global next1
      next1 = Button(root, text = "NEXT", height = 5, width = 8, command = clickautomation)
      next1.pack()

      


    def mechanicalwin():
      finalstatement.pack_forget()
      endmechanical.pack_forget()
      endcivil.pack_forget()
      endelectrical.pack_forget()
      endchemical.pack_forget()
      
      global mechanical_response
      mechanical_response = Label(root, text="Mechanical Engineering seems to be the best fit for you.\n Mechanical Engineering is the branch of engineering dealing \n with the design, construction, and use of machines. \n Some classes/clubs you should consider are: \n - Robotics \n - RC Club \n -DDP \n -CAD \n -Engineering 1 \n -Engineering 2 \n - Physics \n -Calculus \n Some subfields you might want to look into are: \n - Aerospace \n - Automation \n - Cybersecurity \n -Robotics \n -Data Analysis", bg = "white", fg = "crimson", font=("EB Garamond", 24))
      mechanical_response.pack()


      global subfields1
      subfields1 = Button(root, text = "Subfields", height = 5, width = 8, command = clickaerospace)
      subfields1.pack()



    def endgame():
      global finalstatement
      finalstatement = Label(root, text = "Unfortunately, we were unable to get a definite choice for you.\n  However, you can still check out each of the fields down below.", bg="white", fg = "crimson", font=("EB Garamond", 24))
      finalstatement.pack()

      global endmechanical
      endmechanical = Button(root, text = "Mechanical \n Engineering", height = 8, width = 8, fg = "crimson", command = mechanicalwin)
      endmechanical.pack(side = "top", expand = True)

      global endcivil
      endcivil = Button(root, text = "Civil \n Engineering", height = 8, width = 8, fg = "crimson", command = civilwin )
      endcivil.pack(side = "top", expand = True)

      global endelectrical
      endelectrical = Button(root, text = "Electrical \n Engineering", height = 8, width = 8, fg = "crimson", command = electricalwin)
      endelectrical.pack(side = "top", expand = True)

      global endchemical
      endchemical = Button(root, text = "Chemical \n Engineering", height = 8, width = 8, fg = "crimson", command = chemicalwin)
      endchemical.pack(side = "top", expand = True)



    endgame()

  def clicknotsurebutton17():
    question17.pack_forget()
    yesbutton17.pack_forget()
    nobutton17.pack_forget()
    notsurebutton17.pack_forget()
    labelyesbutton17.pack_forget()
    labelnobutton17.pack_forget()
    labelnotsurebutton17.pack_forget()
    def clickstructural():
      environment.pack_forget()
      next13.pack_forget()

      global structural
      structural = Label(root, text = "Structural engineers focus on the physical integrity and \n design of projects such as buildings, bridges, and tunnels.\n Median Salary: $78,460 \n Job Demand expected to increase 6% in the next 10 years. \n Top Colleges in NY: \n NYU \n UBuffalo", bg = "white", fg = "crimson", font=("EB Garamond", 24))
      structural.pack()

    


    def clickenvironment():
      geotech.pack_forget()
      next12.pack_forget()

      global environment
      environment = Label(root, text = "Environmental engineers use the principles of engineering, soil science, biology, \n and chemistry to develop solutions to environmental problems. They work to improve \n recycling, waste disposal, public health, and water and air pollution control. \n Median Salary : $84,560 \n Job Demand expected to increase 3% in the next 10 years. \n Top Colleges in NY: \n Columbia University \n Cornell University \n RPI \n RIT", bg = "white", fg = "crimson", font=("EB Garamond", 24))
      environment.pack()

      global next13
      next13 = Button(root, text = "NEXT" , height = 5, width = 8, command = clickstructural)
      next13.pack()


    def clickgeotech():
      coastaleng.pack_forget()
      next11.pack_forget()

      global geotech
      geotech = Label(root, text = "Geotechnical engineering, also known as geotechnics, is the branch \n of civil engineering concerned with the engineering behavior of earth materials.\n Median Salary: $65,497 \n Job Demand expected to increase 11% in the next 10 years. \n Top Colleges in NY: \n Columbia University \n Cornell University \n RPI", bg = "white", fg = "crimson", font=("EB Garamond", 24))
      geotech.pack()

      global next12
      next12 = Button(root, text = "NEXT" , height = 5, width = 8, command = clickenvironment)
      next12.pack()



    def clickcoastaleng():
      civil_response.pack_forget()
      subfields4.pack_forget()

      global coastaleng
      coastaleng = Label(root, text = "Coastal engineering is a division of civil engineering responsible for \n the organization, conception, development and preservation of works in the coastal area. \n Median Salary: $98,000 \n Job Demand expected to increase 1% in the next 10 years. \n Top Colleges in NY : \n Columbia University \n Cornell University \n RPI", bg = "white", fg = "crimson", font=("EB Garamond", 24))
      coastaleng.pack()

      global next11
      next11 = Button(root, text = "NEXT" , height = 5, width = 8, command = clickgeotech)
      next11.pack()




    def civilwin():
      finalstatement.pack_forget()
      endmechanical.pack_forget()
      endcivil.pack_forget()
      endelectrical.pack_forget()
      endchemical.pack_forget()
      global civil_response
      civil_response = Label(root, text="Civil Engineering seems to be the best fit for you. \nCivil engineering is a professional engineering discipline that deals \n with the design, construction, and maintenance of the physical and naturally built environment.\n Some classes/clubs that you should consider are: \n -CAD \n - Engineering 1 \n - Engineering 2 \n -Robotics \n -Calculus \n -Physics \n - Communication Technology \n - Transportation Technology \n Some subfields that you can look into are: \n - Coastal Engineering \n - Geotechnical Engineering \n - Environmental Engineering \n - Structural Engineering ", bg = "white", fg = "crimson", font=("EB Garamond", 24))
      civil_response.pack()
      

      global subfields4
      subfields4 = Button(root, text = "NEXT", height = 5, width = 8, command = clickcoastaleng)
      subfields4.pack()








    def clickmicroelec():
      signalproinfo.pack_forget()
      next10.pack_forget()
      global microelecinfo
      microelecinfo = Label(root, text = "Microelectronics engineers develop plans and construct prototypes of \n electronic circuit chips, circuit boards, and semiconductors. \n Median Salary: $76,100 \n Job Demand expected to increase roughly 1% in the next 10 years. \n Top Colleges in NY : \n Cornell University \n RPI \n Columbia University \n Clarkson University ", bg="white", fg = "crimson", font=("EB Garamond", 24))
      microelecinfo.pack()


    def clicksignalpro():
      controlsysinfo.pack_forget()
      next9.pack_forget()
      global signalproinfo
      signalproinfo = Label(root, text = "A signal processing engineer is an information technologies expert \n that analyzes and alters digital signals to make them more accurate and reliable.\n Median Salary: $105,000 \n Top Colleges in NY : \n Cornell University \n RIT \n Syracuse University ", bg="white", fg = "crimson", font=("EB Garamond", 24))
      signalproinfo.pack()
      global next10
      next10 = Button(root, text = "NEXT", height = 5, width = 8, command = clickmicroelec)
      next10.pack()



    def clickcontrolsys():
      telecominfo.pack_forget()
      next8.pack_forget()
      global controlsysinfo
      controlsysinfo = Label(root, text = "A Control Systems Engineer is responsible for designing, developing, \n and implementing solutions that control dynamic systems. \n Median Salary : $88, 616 \n Job Demand expected to increase 2% in the next 10 yearss. \n Top Colleges in NY : \n RPI \n Cornell University \n West Point \n Binghamton ", bg="white", fg = "crimson", font=("EB Garamond", 24))
      controlsysinfo.pack()

      global next9
      next9 = Button(root, text = "NEXT", height = 5, width = 8, command = clicksignalpro)
      next9.pack()




    def clicktelecom():
      electrical_response.pack_forget()
      subfields3.pack_forget()
      global telecominfo
      telecominfo = Label(root, text = "Telecommunications engineers or telecom engineers are expert in managing data \n such as voice, video, calls, and text over different modes of communication. \n Median Salary: $76, 524 \n Job Demand expected to increase around 5% in the next 10 years. \n Top Colleges in NY : \n SUNY Stonybrook", bg="white", fg = "crimson", font=("EB Garamond", 24))
      telecominfo.pack()

      global next8
      next8 = Button(root, text = "NEXT", height = 5, width = 8, command = clickcontrolsys)
      next8.pack()



    def electricalwin():
      finalstatement.pack_forget()
      endmechanical.pack_forget()
      endcivil.pack_forget()
      endelectrical.pack_forget()
      endchemical.pack_forget()
      global electrical_response
      electrical_response = Label(root, text="Electrical Engineering seems to be the best fit for you.\nElectrical Engineering is an engineering discipline concerned \n with the study, design and application of equipment, devices \n and systems which use electricity, electronics, and electromagnetism. \n Some classes/clubs you should try out are: \n - Robotics \n - Engineering 1 \n - Engineering 2 \n - Coding Club \n - RC Club \n - Computer Science \n Some subfields that you can look into are: \n -Telecommunications \n -Control Systems \n -Signal Processing \n - Microelectronics", bg="white", fg = "crimson", font=("EB Garamond", 24) )
      electrical_response.pack()


      global subfields3
      subfields3 = Button(root, text = "Subfields", height = 5, width = 8, command = clicktelecom)
      subfields3.pack()


    def clickchempro():
      ceramicsinfo.pack_forget()
      next7.pack_forget()
      global chemproinfo
      chemproinfo = Label(root, text = "The main role of chemical engineers is to design and troubleshoot processes for the production \n  of chemicals, fuels, foods, pharmaceuticals, and biologicals. \n Median Salary : $108,700 \n Job Demand expected to increase 4% in the next 10 years. \n Top Colleges in NY : \n Columbia University \n Cornell University \n NYU \n University of Rochester", bg = "white", fg = "crimson", font=("EB Garamond", 24) )



      

    def clickceramics():
      mineralproinfo.pack_forget()
      next6.pack_forget()
      global ceramicsinfo
      ceramicsinfo = Label(root, text = "Ceramic engineering is the science and technology \n of creating objects from inorganic, non-metallic materials. \n Median Salary: $83,000 \n Job Demand expected to grow 6.8% in next 10 years. \n Top Colleges in NY : \n Alfred University ", bg = "white", fg = "crimson", font=("EB Garamond", 24))
      ceramicsinfo.pack()

      global next7
      next7 = Button(root, text = "NEXT", height = 5, width = 8, command = clickchempro)
      next7.pack()



    def clickmineralpro():
      biotechinfo.pack_forget()
      next5.pack_forget()
      global mineralproinfo
      mineralproinfo = Label(root, text = "Mineral Processing Engineering deals with the extraction, \n  separation, and concentration of minerals from raw ores. \n Median Salary : $60,000 \n Job Demand expected to grow 4% in the next 10 years. \n Top Colleges : \n Colorado School of Mines", bg = "white", fg = "crimson", font=("EB Garamond", 24))
      mineralproinfo.pack()

      global next6
      next6 = Button(root, text = "NEXT", height = 5, width = 8, command = clickceramics)
      next6.pack()
      



    def clickbiotech():
      chemical_response.pack_forget()
      subfields2.pack_forget()
      global biotechinfo
      biotechinfo = Label(root, text = "Biotechnology engineering is the research and study \n of micro-organism, bio-organisms, cell functions in living beings. \n Median Salary : $108,696 \n Job Demand expected to grow 5% in the next 10 years. \n Top Colleges in NY : \n Columbia University \n Cornell University \n Syracuse University \n RPI", bg = "white", fg = "crimson" , font=("EB Garamond", 24))
      biotechinfo.pack()

      global next5
      next5 = Button(root, text = "NEXT", height = 5, width = 8, command = clickmineralpro)
      next5.pack()






    def chemicalwin():
      finalstatement.pack_forget()
      endmechanical.pack_forget()
      endcivil.pack_forget()
      endelectrical.pack_forget()
      endchemical.pack_forget()

      global chemical_response
      chemical_response = Label(root, text="Chemical Engineering seems to be the best fit for you.\n Chemical engineering is the branch of engineering that deals \n with chemical production and the manufacture of products through chemical processes.\n  Some classes/clubs you should consider are: \n - Calculus \n -Chemistry \n - Computer Science \n Some subfields that you can look into are: \n - Biotechnology \n - Mineral Processing \n - Ceramics \n - Chemical Processing", bg="white", fg = "crimson", font=("EB Garamond", 24))
      chemical_response.pack()
      

      global subfields2
      subfields2 = Button(root, text = "Subfields", height = 5, width = 8, command = clickbiotech)
      subfields2.pack()














    def clickrobotics():
      datainfo.pack_forget()
      next4.pack_forget()
      global roboticsinfo
      roboticsinfo = Label(root, text = "Robotics engineering is a field of engineering \n which centers on building machines that replicate human actions. \n Median Salary : $99,040 \n Job Demand expected to grow 9% in the next 10 years. \n Top Colleges in NY : \n Cornell University \n NYU ", bg = "white", fg = "crimson", font=("EB Garamond", 24))
      roboticsinfo.pack()
              



    def clickdataanalysis():
      cybersecurityinfo.pack_forget()
      next3.pack_forget()
      global datainfo
      datainfo = Label(root, text = "Data engineers are responsible for finding trends in data sets \n and developing algorithms to help make raw data more useful to the enterprise. \n Median Salary : $137,776 \n Job Demand expected to increase 21% in the next 10 years. \n Top Colleges in NY : \n Columbia University \n Cornell University \n NYU \n Syracuse \n NYIT ", bg = "white", fg = "crimson", font=("EB Garamond", 24))
      datainfo.pack()
      global next4
      next4 = Button(root, text = "NEXT", height = 5, width = 8, command = clickrobotics)
      next4.pack()
    

    
    def clickcybersecurity():
      automationinfo.pack_forget()
      next2.pack_forget()
      global cybersecurityinfo
      cybersecurityinfo = Label(root, text = "Cybersecurity engineers, sometimes called information security engineers,\n identify threats and vulnerabilities in systems and software, \n then apply their skills to developing and implementing high-tech solutions \n to defend against hacking, malware and ransomware, \n insider threats and all types of cybercrime. \n Median Salary: $90,120 \n Job Demand expected to grow 31% in the next 10 years. \n Top Colleges in NY : \n NYU \n Syracuse University \n RIT \n Pace University", bg = "white", fg = "crimson", font=("EB Garamond", 24))
      cybersecurityinfo.pack()
      global next3
      next3 = Button(root, text = "NEXT", height = 5, width = 8, command = clickdataanalysis)
      next3.pack()
    


    def clickautomation():
      aeroinfo.pack_forget()
      next1.pack_forget()

      global automationinfo
      automationinfo = Label(root, text = "An Automation Engineer utilizes technology \n to improve, streamline and automate a manufacturing process. \n Median Salary : $88,100 \n Job Demand expected to grow around 4% in the next 10 years \n Top Colleges in NY : \n SUNY Farmingdale \n SUNY College of Tech at Alfred", bg = "white", fg = "crimson", font=("EB Garamond", 24))
      automationinfo.pack()
      global next2
      next2 = Button(root, text = "NEXT", height = 5, width = 8, command = clickcybersecurity)
      next2.pack()
    


    def clickaerospace():
      subfields1.pack_forget()
      mechanical_response.pack_forget()
      global aeroinfo
      aeroinfo = Label(root, text = "Aerospace engineering is the primary field of engineering \n concerned with the development of aircraft and spacecraft.\n Median Salary : $116,500 \n Job Demand expected to grow around 3% in the next 10 years \n Top Colleges in NY : \n Cornell University \n RPI \n Syracuse University \n SUNY Buffalo", bg = "white", fg = "crimson", font=("EB Garamond", 24))
      aeroinfo.pack()
      global next1
      next1 = Button(root, text = "NEXT", height = 5, width = 8, command = clickautomation)
      next1.pack()

      


    def mechanicalwin():
      finalstatement.pack_forget()
      endmechanical.pack_forget()
      endcivil.pack_forget()
      endelectrical.pack_forget()
      endchemical.pack_forget()
      global mechanical_response
      mechanical_response = Label(root, text="Mechanical Engineering seems to be the best fit for you.\n Mechanical Engineering is the branch of engineering dealing \n with the design, construction, and use of machines. \n Some classes/clubs you should consider are: \n - Robotics \n - RC Club \n -DDP \n -CAD \n -Engineering 1 \n -Engineering 2 \n - Physics \n -Calculus \n Some subfields you might want to look into are: \n - Aerospace \n - Automation \n - Cybersecurity \n -Robotics \n -Data Analysis", bg="white", fg = "crimson", font=("EB Garamond", 24))
      mechanical_response.pack()


      global subfields1
      subfields1 = Button(root, text = "Subfields", height = 5, width = 8, command = clickaerospace)
      subfields1.pack()



    def endgame():
      global finalstatement
      finalstatement = Label(root, text = "Unfortunately, we were unable to get a definite choice for you.\n  However, you can still check out each of the fields down below.", bg="white", fg = "crimson", font=("EB Garamond", 24))
      finalstatement.pack()

      global endmechanical
      endmechanical = Button(root, text = "Mechanical \n Engineering", height = 8, width = 8, fg = "crimson", command = mechanicalwin)
      endmechanical.pack(side = "top", expand = True)

      global endcivil
      endcivil = Button(root, text = "Civil \n Engineering", height = 8, width = 8, fg = "crimson", command = civilwin )
      endcivil.pack(side = "top", expand = True)

      global endelectrical
      endelectrical = Button(root, text = "Electrical \n Engineering", height = 8, width = 8, fg = "crimson", command = electricalwin)
      endelectrical.pack(side = "top", expand = True)

      global endchemical
      endchemical = Button(root, text = "Chemical \n Engineering", height = 8, width = 8, fg = "crimson", command = chemicalwin)
      endchemical.pack(side = "top", expand = True)



    endgame()









  def clickyesbutton16():
    global electrical
    electrical += 1
    question16.pack_forget()
    yesbutton16.pack_forget()
    nobutton16.pack_forget()
    notsurebutton16.pack_forget()
    labelyesbutton16.pack_forget()
    labelnobutton16.pack_forget()
    labelnotsurebutton16.pack_forget()
    if electrical == 9:

      
      def clickmicroelec():
        signalproinfo.pack_forget()
        next3.pack_forget()
        global microelecinfo
        microelecinfo = Label(root, text = "Microelectronics engineers develop plans and construct prototypes of \n electronic circuit chips, circuit boards, and semiconductors. \n Median Salary: $76,100 \n Job Demand expected to increase roughly 1% in the next 10 years. \n Top Colleges in NY : \n Cornell University \n RPI \n Columbia University \n Clarkson University ", bg="white", fg = "crimson", font=("EB Garamond", 24))
        microelecinfo.pack()


      def clicksignalpro():
        controlsysinfo.pack_forget()
        next2.pack_forget()
        global signalproinfo
        signalproinfo = Label(root, text = "A signal processing engineer is an information technologies expert \n that analyzes and alters digital signals to make them more accurate and reliable.\n Median Salary: $105,000 \n Top Colleges in NY : \n Cornell University \n RIT \n Syracuse University ", bg="white", fg = "crimson", font=("EB Garamond", 24))
        signalproinfo.pack()
        global next3
        next3 = Button(root, text = "NEXT", height = 5, width = 8, command = clickmicroelec)
        next3.pack()



      def clickcontrolsys():
        telecominfo.pack_forget()
        next1.pack_forget()
        global controlsysinfo
        controlsysinfo = Label(root, text = "A Control Systems Engineer is responsible for designing, developing, \n and implementing solutions that control dynamic systems. \n Median Salary : $88, 616 \n Job Demand expected to increase 2% in the next 10 yearss. \n Top Colleges in NY : \n RPI \n Cornell University \n West Point \n Binghamton ", bg="white", fg = "crimson", font=("EB Garamond", 24))
        controlsysinfo.pack()

        global next2
        next2 = Button(root, text = "NEXT", height = 5, width = 8, command = clicksignalpro)
        next2.pack()




      def clicktelecom():
        electrical_response.pack_forget()
        subfields.pack_forget()
        global telecominfo
        telecominfo = Label(root, text = "Telecommunications engineers or telecom engineers are expert in managing data \n such as voice, video, calls, and text over different modes of communication. \n Median Salary: $76, 524 \n Job Demand expected to increase around 5% in the next 10 years. \n Top Colleges in NY : \n SUNY Stonybrook", bg="white", fg = "crimson", font=("EB Garamond", 24))
        telecominfo.pack()

        global next1
        next1 = Button(root, text = "NEXT", height = 5, width = 8, command = clickcontrolsys)
        next1.pack()



      def electricalwin():
        global electrical_response
        electrical_response = Label(root, text="Electrical Engineering seems to be the best fit for you. \nElectrical Engineering is an engineering discipline concerned \n with the study, design and application of equipment, devices \n and systems which use electricity, electronics, and electromagnetism.\n Some classes/clubs you should try out are: \n - Robotics \n - Engineering 1 \n - Engineering 2 \n - Coding Club \n - RC Club \n - Computer Science \n Some subfields that you can look into are: \n -Telecommunications \n -Control Systems \n -Signal Processing \n - Microelectronics", bg="white", fg = "crimson", font=("EB Garamond", 24) )
        electrical_response.pack()


        global subfields
        subfields = Button(root, text = "Subfields", height = 5, width = 8, command = clicktelecom)
        subfields.pack()

        


      electricalwin()
    else:
      global question17
      question17 = Label(root, text="Do you enjoy \n cooking and baking?", bg = "white", fg = "crimson", font=("EB Garamond", 24))
      question17.pack(side = "top", expand = True)

      global yesbutton17
      yesbutton17 = Button(root, text="", height=2, width=2, bg="red", command=clickyesbutton17)
      yesbutton17.pack(side="top", expand=True)

      global labelyesbutton17
      labelyesbutton17 = Label(root, text = "Yes", bg = "white", fg = "crimson" , font=("EB Garamond", 24))
      labelyesbutton17.pack(side = "top", expand = True)

      global nobutton17
      nobutton17 = Button(root, text="", height=2, width=2, bg="red", command=clicknobutton17)
      nobutton17.pack(side="top", expand=True)

      global labelnobutton17
      labelnobutton17 = Label(root, text = "No", bg = "white" , fg = "crimson", font=("EB Garamond", 24))
      labelnobutton17.pack(side = "top", expand = True)

      global notsurebutton17
      notsurebutton17 = Button(root, text="", height=2, width=2, bg="red", command=clicknotsurebutton17)
      notsurebutton17.pack(side="top", expand=True)

      global labelnotsurebutton17
      labelnotsurebutton17 = Label(root, text = "Not Sure", bg = "white", fg = "crimson" , font=("EB Garamond", 24))
      labelnotsurebutton17.pack(side = "top", expand = True)


  def clicknobutton16():
    global electrical
    electrical -= 1
    question16.pack_forget()
    yesbutton16.pack_forget()
    nobutton16.pack_forget()
    notsurebutton16.pack_forget()
    labelyesbutton16.pack_forget()
    labelnobutton16.pack_forget()
    labelnotsurebutton16.pack_forget()
    global question17
    question17 = Label(root, text="Do you enjoy \n cooking and baking?", bg = "white", fg = "crimson", font=("EB Garamond", 24))
    question17.pack(side = "top", expand = True)

    global yesbutton17
    yesbutton17 = Button(root, text="", height=2, width=2, bg="red", command=clickyesbutton17)
    yesbutton17.pack(side="top", expand=True)

    global labelyesbutton17
    labelyesbutton17 = Label(root, text = "Yes", bg = "white" , fg = "crimson", font=("EB Garamond", 24))
    labelyesbutton17.pack(side = "top", expand = True)

    global nobutton17
    nobutton17 = Button(root, text="", height=2, width=2, bg="red", command=clicknobutton17)
    nobutton17.pack(side="top", expand=True)

    global labelnobutton17
    labelnobutton17 = Label(root, text = "No", bg = "white" , fg = "crimson", font=("EB Garamond", 24))
    labelnobutton17.pack(side = "top", expand = True)

    global notsurebutton17
    notsurebutton17 = Button(root, text="", height=2, width=2, bg="red", command=clicknotsurebutton17)
    notsurebutton17.pack(side="top", expand=True)

    global labelnotsurebutton17
    labelnotsurebutton17 = Label(root, text = "Not Sure", bg = "white" , fg = "crimson", font=("EB Garamond", 24))
    labelnotsurebutton17.pack(side = "top", expand = True)

  def clicknotsurebutton16():
    question16.pack_forget()
    yesbutton16.pack_forget()
    nobutton16.pack_forget()
    notsurebutton16.pack_forget()
    labelyesbutton16.pack_forget()
    labelnobutton16.pack_forget()
    labelnotsurebutton16.pack_forget()
    global question17
    question17 = Label(root, text="Do you enjoy \n cooking and baking?", bg = "white", fg = "crimson", font=("EB Garamond", 24))
    question17.pack(side = "top", expand = True)

    global yesbutton17
    yesbutton17 = Button(root, text="", height=2, width=2, bg="red", command=clickyesbutton17)
    yesbutton17.pack(side="top", expand=True)

    global labelyesbutton17
    labelyesbutton17 = Label(root, text = "Yes", bg = "white" , fg = "crimson", font=("EB Garamond", 24))
    labelyesbutton17.pack(side = "top", expand = True)

    global nobutton17
    nobutton17 = Button(root, text="", height=2, width=2, bg="red", command=clicknobutton17)
    nobutton17.pack(side="top", expand=True)

    global labelnobutton17
    labelnobutton17 = Label(root, text = "No", bg = "white" , fg = "crimson", font=("EB Garamond", 24))
    labelnobutton17.pack(side = "top", expand = True)

    global notsurebutton17
    notsurebutton17 = Button(root, text="", height=2, width=2, bg="red", command=clicknotsurebutton17)
    notsurebutton17.pack(side="top", expand=True)

    global labelnotsurebutton17
    labelnotsurebutton17 = Label(root, text = "Not Sure", bg = "white" , fg = "crimson", font=("EB Garamond", 24))
    labelnotsurebutton17.pack(side = "top", expand = True)






  def clickyesbutton15():
    global mechanical
    mechanical += 1
    question15.pack_forget()
    yesbutton15.pack_forget()
    nobutton15.pack_forget()
    notsurebutton15.pack_forget()
    labelyesbutton15.pack_forget()
    labelnobutton15.pack_forget()
    labelnotsurebutton15.pack_forget()
    if mechanical == 9:


      def clickrobotics():
        datainfo.pack_forget()
        next4.pack_forget()
        global roboticsinfo
        roboticsinfo = Label(root, text = "Robotics engineering is a field of engineering \n which centers on building machines that replicate human actions. \n Median Salary : $99,040 \n Job Demand expected to grow 9% in the next 10 years. \n Top Colleges in NY : \n Cornell University \n NYU ", bg="white", fg = "crimson", font=("EB Garamond", 24))
        roboticsinfo.pack()
                
 


      def clickdataanalysis():
        cybersecurityinfo.pack_forget()
        next3.pack_forget()
        global datainfo
        datainfo = Label(root, text = "Data engineers are responsible for finding trends in data sets \n and developing algorithms to help make raw data more useful to the enterprise. \n Median Salary : $137,776 \n Job Demand expected to increase 21% in the next 10 years. \n Top Colleges in NY : \n Columbia University \n Cornell University \n NYU \n Syracuse \n NYIT ", bg="white", fg = "crimson", font=("EB Garamond", 24))
        datainfo.pack()
        global next4
        next4 = Button(root, text = "NEXT", height = 5, width = 8, command = clickrobotics)
        next4.pack()
     

      
      def clickcybersecurity():
        automationinfo.pack_forget()
        next2.pack_forget()
        global cybersecurityinfo
        cybersecurityinfo = Label(root, text = "Cybersecurity engineers, sometimes called information security engineers,\n identify threats and vulnerabilities in systems and software, \n then apply their skills to developing and implementing high-tech solutions \n to defend against hacking, malware and ransomware, \n insider threats and all types of cybercrime. \n Median Salary: $90,120 \n Job Demand expected to grow 31% in the next 10 years. \n Top Colleges in NY : \n NYU \n Syracuse University \n RIT \n Pace University", bg="white", fg = "crimson", font=("EB Garamond", 24))
        cybersecurityinfo.pack()
        global next3
        next3 = Button(root, text = "NEXT", height = 5, width = 8, command = clickdataanalysis)
        next3.pack()
     


      def clickautomation():
        aeroinfo.pack_forget()
        next1.pack_forget()

        global automationinfo
        automationinfo = Label(root, text = "An Automation Engineer utilizes technology \n to improve, streamline and automate a manufacturing process. \n Median Salary : $88,100 \n Job Demand expected to grow around 4% in the next 10 years \n Top Colleges in NY : \n SUNY Farmingdale \n SUNY College of Tech at Alfred", bg="white", fg = "crimson", font=("EB Garamond", 24))
        automationinfo.pack()
        global next2
        next2 = Button(root, text = "NEXT", height = 5, width = 8, command = clickcybersecurity)
        next2.pack()
     


      def clickaerospace():
        subfields.pack_forget()
        mechanical_response.pack_forget()
        global aeroinfo
        aeroinfo = Label(root, text = "Aerospace engineering is the primary field of engineering \n concerned with the development of aircraft and spacecraft.\n Median Salary : $116,500 \n Job Demand expected to grow around 3% in the next 10 years \n Top Colleges in NY : \n Cornell University \n RPI \n Syracuse University \n SUNY Buffalo", bg = "white", fg = "crimson", font=("EB Garamond", 24))
        aeroinfo.pack()
        global next1
        next1 = Button(root, text = "NEXT", height = 5, width = 8, command = clickautomation)
        next1.pack()

        


      def mechanicalwin():
        
        global mechanical_response
        mechanical_response = Label(root, text="Mechanical Engineering seems to be the best fit for you.\n Mechanical Engineering is the branch of engineering dealing \n with the design, construction, and use of machines. \n Some classes/clubs you should consider are: \n - Robotics \n - RC Club \n -DDP \n -CAD \n -Engineering 1 \n -Engineering 2 \n - Physics \n -Calculus \n Some subfields you might want to look into are: \n - Aerospace \n - Automation \n - Cybersecurity \n -Robotics \n -Data Analysis", bg="white", fg = "crimson", font=("EB Garamond", 24))
        mechanical_response.pack()


        global subfields
        subfields = Button(root, text = "Subfields", height = 5, width = 8, command = clickaerospace)
        subfields.pack()

        



        

      mechanicalwin()
    else:
      global question16
      question16 = Label(root, text="Have you ever wondered \n about how your microwave \n or refrigerator works?", bg = "white", fg = "crimson", font=("EB Garamond", 24))
      question16.pack(side = "top", expand = True)

      global yesbutton16
      yesbutton16 = Button(root, text="", height=2, width=2, bg="red", command=clickyesbutton16)
      yesbutton16.pack(side="top", expand=True)

      global labelyesbutton16
      labelyesbutton16 = Label(root, text = "Yes", bg = "white", fg = "crimson", font=("EB Garamond", 24) )
      labelyesbutton16.pack(side = "top", expand = True)

      global nobutton16
      nobutton16 = Button(root, text="", height=2, width=2, bg="red", command=clicknobutton16)
      nobutton16.pack(side="top", expand=True)

      global labelnobutton16
      labelnobutton16 = Label(root, text = "No", bg = "white", fg = "crimson", font=("EB Garamond", 24) )
      labelnobutton16.pack(side = "top", expand = True)

      global notsurebutton16
      notsurebutton16 = Button(root, text="", height=2, width=2, bg="red", command=clicknotsurebutton16)
      notsurebutton16.pack(side="top", expand=True)

      global labelnotsurebutton16
      labelnotsurebutton16 = Label(root, text = "Not Sure", bg = "white" , fg = "crimson", font=("EB Garamond", 24))
      labelnotsurebutton16.pack(side = "top", expand = True)


  def clicknobutton15():
    global mechanical
    mechanical -= 1
    question15.pack_forget()
    yesbutton15.pack_forget()
    nobutton15.pack_forget()
    notsurebutton15.pack_forget()
    labelyesbutton15.pack_forget()
    labelnobutton15.pack_forget()
    labelnotsurebutton15.pack_forget()
    global question16
    question16 = Label(root, text="Have you ever wondered \n about how your microwave \n or refrigerator works?", bg = "white", fg = "crimson", font=("EB Garamond", 24))
    question16.pack(side = "top", expand = True)

    global yesbutton16
    yesbutton16 = Button(root, text="", height=2, width=2, bg="red", command=clickyesbutton16)
    yesbutton16.pack(side="top", expand=True)

    global labelyesbutton16
    labelyesbutton16 = Label(root, text = "Yes", bg = "white" , fg = "crimson", font=("EB Garamond", 24))
    labelyesbutton16.pack(side = "top", expand = True)

    global nobutton16
    nobutton16 = Button(root, text="", height=2, width=2, bg="red", command=clicknobutton16)
    nobutton16.pack(side="top", expand=True)

    global labelnobutton16
    labelnobutton16 = Label(root, text = "No", bg = "white" , fg = "crimson", font=("EB Garamond", 24))
    labelnobutton16.pack(side = "top", expand = True)

    global notsurebutton16
    notsurebutton16 = Button(root, text="", height=2, width=2, bg="red", command=clicknotsurebutton16)
    notsurebutton16.pack(side="top", expand=True)

    global labelnotsurebutton16
    labelnotsurebutton16 = Label(root, text = "Not Sure", bg = "white", fg = "crimson" , font=("EB Garamond", 24))
    labelnotsurebutton16.pack(side = "top", expand = True)


  def clicknotsurebutton15():
    question15.pack_forget()
    yesbutton15.pack_forget()
    nobutton15.pack_forget()
    notsurebutton15.pack_forget()
    labelyesbutton15.pack_forget()
    labelnobutton15.pack_forget()
    labelnotsurebutton15.pack_forget()
    global question16
    question16 = Label(root, text="Have you ever wondered \n about how your microwave \n or refrigerator works?", bg = "white", fg = "crimson", font=("EB Garamond", 24))
    question16.pack(side = "top", expand = True)

    global yesbutton16
    yesbutton16 = Button(root, text="", height=2, width=2, bg="red", command=clickyesbutton16)
    yesbutton16.pack(side="top", expand=True)

    global labelyesbutton16
    labelyesbutton16 = Label(root, text = "Yes", bg = "white", fg = "crimson", font=("EB Garamond", 24) )
    labelyesbutton16.pack(side = "top", expand = True)

    global nobutton16
    nobutton16 = Button(root, text="", height=2, width=2, bg="red", command=clicknobutton16)
    nobutton16.pack(side="top", expand=True)

    global labelnobutton16
    labelnobutton16 = Label(root, text = "No", bg = "white" , fg = "crimson", font=("EB Garamond", 24))
    labelnobutton16.pack(side = "top", expand = True)

    global notsurebutton16
    notsurebutton16 = Button(root, text="", height=2, width=2, bg="red", command=clicknotsurebutton16)
    notsurebutton16.pack(side="top", expand=True)

    global labelnotsurebutton16
    labelnotsurebutton16 = Label(root, text = "Not Sure", bg = "white" , fg = "crimson", font=("EB Garamond", 24))
    labelnotsurebutton16.pack(side = "top", expand = True)




  #MARKER FOR DONE WORK-ALL WORK BELOW IS DONE DO NOT TOUCH
  def clickyesbutton14():
    global civil
    civil += 1
    question14.pack_forget()
    yesbutton14.pack_forget()
    nobutton14.pack_forget()
    notsurebutton14.pack_forget()
    labelyesbutton14.pack_forget()
    labelnobutton14.pack_forget()
    labelnotsurebutton14.pack_forget()
    if civil == 9:

      def clickstructural():
        environment.pack_forget()
        next3.pack_forget()

        global structural
        structural = Label(root, text = "Structural engineers focus on the physical integrity and \n design of projects such as buildings, bridges, and tunnels.\n Median Salary: $78,460 \n Job Demand expected to increase 6% in the next 10 years. \n Top Colleges in NY: \n NYU \n UBuffalo", bg="white", fg = "crimson", font=("EB Garamond", 24))
        structural.pack()

    


      def clickenvironment():
        geotech.pack_forget()
        next2.pack_forget()

        global environment
        environment = Label(root, text = "Environmental engineers use the principles of engineering, soil science, biology, \n and chemistry to develop solutions to environmental problems. They work to improve \n recycling, waste disposal, public health, and water and air pollution control. \n Median Salary : $84,560 \n Job Demand expected to increase 3% in the next 10 years. \n Top Colleges in NY: \n Columbia University \n Cornell University \n RPI \n RIT", bg="white", fg = "crimson", font=("EB Garamond", 24))
        environment.pack()

        global next3
        next3 = Button(root, text = "NEXT" , height = 5, width = 8, command = clickstructural)
        next3.pack()


      def clickgeotech():
        coastaleng.pack_forget()
        next1.pack_forget()

        global geotech
        geotech = Label(root, text = "Geotechnical engineering, also known as geotechnics, is the branch \n of civil engineering concerned with the engineering behavior of earth materials.\n Median Salary: $65,497 \n Job Demand expected to increase 11% in the next 10 years. \n Top Colleges in NY: \n Columbia University \n Cornell University \n RPI", bg="white", fg = "crimson", font=("EB Garamond", 24))
        geotech.pack()

        global next2
        next2 = Button(root, text = "NEXT" , height = 5, width = 8, command = clickenvironment)
        next2.pack()



      def clickcoastaleng():
        civil_response.pack_forget()
        subfields.pack_forget()

        global coastaleng
        coastaleng = Label(root, text = "Coastal engineering is a division of civil engineering responsible for \n the organization, conception, development and preservation of works in the coastal area. \n Median Salary: $98,000 \n Job Demand expected to increase 1% in the next 10 years. \n Top Colleges in NY : \n Columbia University \n Cornell University \n RPI", bg="white", fg = "crimson", font=("EB Garamond", 24))
        coastaleng.pack()

        global next1
        next1 = Button(root, text = "NEXT" , height = 5, width = 8, command = clickgeotech)
        next1.pack()




      def civilwin():
        global civil_response
        civil_response = Label(root, text="Civil Engineering seems to be the best fit for you.\nCivil engineering is a professional engineering discipline that deals \n with the design, construction, and maintenance of the physical and naturally built environment. \n Some classes/clubs that you should consider are: \n -CAD \n - Engineering 1 \n - Engineering 2 \n -Robotics \n -Calculus \n -Physics \n - Communication Technology \n - Transportation Technology \n Some subfields that you can look into are: \n - Coastal Engineering \n - Geotechnical Engineering \n - Environmental Engineering \n - Structural Engineering ", bg = "white", fg = "crimson", font=("EB Garamond", 24))
        civil_response.pack()
       

        global subfields
        subfields = Button(root, text = "NEXT", height = 5, width = 8, command = clickcoastaleng)
        subfields.pack()
      civilwin()
    else:
      global question15
      question15 = Label(root, text=" Have you ever taken \n a pen apart and \n played around with it?", bg = "white", fg = "crimson", font=("EB Garamond", 24))
      question15.pack(side = "top", expand = True)

      global yesbutton15
      yesbutton15 = Button(root, text="", height=2, width=2, bg="red", command=clickyesbutton15)
      yesbutton15.pack(side="top", expand=True)

      global labelyesbutton15
      labelyesbutton15 = Label(root, text = "Yes", bg = "white", fg = "crimson", font=("EB Garamond", 24) )
      labelyesbutton15.pack(side = "top", expand = True)

      global nobutton15
      nobutton15 = Button(root, text="", height=2, width=2, bg="red", command=clicknobutton15)
      nobutton15.pack(side="top", expand=True)

      global labelnobutton15
      labelnobutton15 = Label(root, text = "No", bg = "white" , fg = "crimson", font=("EB Garamond", 24))
      labelnobutton15.pack(side = "top", expand = True)

      global notsurebutton15
      notsurebutton15 = Button(root, text="", height=2, width=2, bg="red", command=clicknotsurebutton15)
      notsurebutton15.pack(side="top", expand=True)

      global labelnotsurebutton15
      labelnotsurebutton15 = Label(root, text = "Not Sure", bg = "white" , fg = "crimson", font=("EB Garamond", 24))
      labelnotsurebutton15.pack(side = "top", expand = True)

  def clicknobutton14():
    global civil
    civil -= 1
    question14.pack_forget()
    yesbutton14.pack_forget()
    nobutton14.pack_forget()
    notsurebutton14.pack_forget()
    labelyesbutton14.pack_forget()
    labelnobutton14.pack_forget()
    labelnotsurebutton14.pack_forget()

    global question15
    question15 = Label(root, text=" Have you ever taken \n a pen apart and \n played around with it?", bg = "white", fg = "crimson", font=("EB Garamond", 24))
    question15.pack(side = "top", expand = True)

    global yesbutton15
    yesbutton15 = Button(root, text="", height=2, width=2, bg="red", command=clickyesbutton15)
    yesbutton15.pack(side="top", expand=True)

    global labelyesbutton15
    labelyesbutton15 = Label(root, text = "Yes", bg = "white", fg = "crimson" , font=("EB Garamond", 24))
    labelyesbutton15.pack(side = "top", expand = True)

    global nobutton15
    nobutton15 = Button(root, text="", height=2, width=2, bg="red", command=clicknobutton15)
    nobutton15.pack(side="top", expand=True)

    global labelnobutton15
    labelnobutton15 = Label(root, text = "No", bg = "white", fg = "crimson" , font=("EB Garamond", 24))
    labelnobutton15.pack(side = "top", expand = True)

    global notsurebutton15
    notsurebutton15 = Button(root, text="", height=2, width=2, bg="red", command=clicknotsurebutton15)
    notsurebutton15.pack(side="top", expand=True)

    global labelnotsurebutton15
    labelnotsurebutton15 = Label(root, text = "Not Sure", bg = "white", fg = "crimson" , font=("EB Garamond", 24))
    labelnotsurebutton15.pack(side = "top", expand = True)

  def clicknotsurebutton14():
    question14.pack_forget()
    yesbutton14.pack_forget()
    nobutton14.pack_forget()
    notsurebutton14.pack_forget()
    labelyesbutton14.pack_forget()
    labelnobutton14.pack_forget()
    labelnotsurebutton14.pack_forget()

    global question15
    question15 = Label(root, text=" Have you ever taken \n a pen apart and \n played around with it?", bg = "white", fg = "crimson" , font=("EB Garamond", 24))
    question15.pack(side = "top", expand = True)

    global yesbutton15
    yesbutton15 = Button(root, text="", height=2, width=2, bg="red", command=clickyesbutton15)
    yesbutton15.pack(side="top", expand=True)

    global labelyesbutton15
    labelyesbutton15 = Label(root, text = "Yes", bg = "white", fg = "crimson" , font=("EB Garamond", 24))
    labelyesbutton15.pack(side = "top", expand = True)

    global nobutton15
    nobutton15 = Button(root, text="", height=2, width=2, bg="red", command=clicknobutton15)
    nobutton15.pack(side="top", expand=True)

    global labelnobutton15
    labelnobutton15 = Label(root, text = "No", bg = "white", fg = "crimson", font=("EB Garamond", 24) )
    labelnobutton15.pack(side = "top", expand = True)

    global notsurebutton15
    notsurebutton15 = Button(root, text="", height=2, width=2, bg="red", command=clicknotsurebutton15)
    notsurebutton15.pack(side="top", expand=True)

    global labelnotsurebutton15
    labelnotsurebutton15 = Label(root, text = "Not Sure", bg = "white", fg = "crimson" , font=("EB Garamond", 24))
    labelnotsurebutton15.pack(side = "top", expand = True)



      




  def clickq13aanswer1():
    global electrical
    electrical += 1
    question13a.pack_forget()
    q13aanswer1.pack_forget()
    q13aanswer2.pack_forget()
    labelq13aanswer1.pack_forget()
    labelq13aanswer2.pack_forget()
    if electrical == 9:


      def clickmicroelec():
        signalproinfo.pack_forget()
        next3.pack_forget()
        global microelecinfo
        microelecinfo = Label(root, text = "Microelectronics engineers develop plans and construct prototypes of \n electronic circuit chips, circuit boards, and semiconductors. \n Median Salary: $76,100 \n Job Demand expected to increase roughly 1% in the next 10 years. \n Top Colleges in NY : \n Cornell University \n RPI \n Columbia University \n Clarkson University ", bg="white", fg = "crimson", font=("EB Garamond", 24))
        microelecinfo.pack()


      def clicksignalpro():
        controlsysinfo.pack_forget()
        next2.pack_forget()
        global signalproinfo
        signalproinfo = Label(root, text = "A signal processing engineer is an information technologies expert \n that analyzes and alters digital signals to make them more accurate and reliable.\n Median Salary: $105,000 \n Top Colleges in NY : \n Cornell University \n RIT \n Syracuse University ", bg="white", fg = "crimson", font=("EB Garamond", 24))
        signalproinfo.pack()
        global next3
        next3 = Button(root, text = "NEXT", height = 5, width = 8, command = clickmicroelec)
        next3.pack()



      def clickcontrolsys():
        telecominfo.pack_forget()
        next1.pack_forget()
        global controlsysinfo
        controlsysinfo = Label(root, text = "A Control Systems Engineer is responsible for designing, developing, \n and implementing solutions that control dynamic systems. \n Median Salary : $88, 616 \n Job Demand expected to increase 2% in the next 10 yearss. \n Top Colleges in NY : \n RPI \n Cornell University \n West Point \n Binghamton ", bg="white", fg = "crimson", font=("EB Garamond", 24))
        controlsysinfo.pack()

        global next2
        next2 = Button(root, text = "NEXT", height = 5, width = 8, command = clicksignalpro)
        next2.pack()




      def clicktelecom():
        electrical_response.pack_forget()
        subfields.pack_forget()
        global telecominfo
        telecominfo = Label(root, text = "Telecommunications engineers or telecom engineers are expert in managing data \n such as voice, video, calls, and text over different modes of communication. \n Median Salary: $76, 524 \n Job Demand expected to increase around 5% in the next 10 years. \n Top Colleges in NY : \n SUNY Stonybrook", bg="white", fg = "crimson", font=("EB Garamond", 24))
        telecominfo.pack()

        global next1
        next1 = Button(root, text = "NEXT", height = 5, width = 8, command = clickcontrolsys)
        next1.pack()



      def electricalwin():
        global electrical_response
        electrical_response = Label(root, text="Electrical Engineering seems to be the best fit for you. \nElectrical Engineering is an engineering discipline concerned \n with the study, design and application of equipment, devices \n and systems which use electricity, electronics, and electromagnetism.\n Some classes/clubs you should try out are: \n - Robotics \n - Engineering 1 \n - Engineering 2 \n - Coding Club \n - RC Club \n - Computer Science \n Some subfields that you can look into are: \n -Telecommunications \n -Control Systems \n -Signal Processing \n - Microelectronics", bg="white", fg = "crimson" , font=("EB Garamond", 24))
        electrical_response.pack()


        global subfields
        subfields = Button(root, text = "Subfields", height = 5, width = 8, command = clicktelecom)
        subfields.pack()

        


      electricalwin()
    else:
      global question14
      question14 = Label(root, text="Is the idea of redesigning \n the infrastructure of \n New York City \n appealing to you?",bg = "white", fg = "crimson", font=("EB Garamond", 24) )
      question14.pack(side="top", expand=True)

      global yesbutton14
      yesbutton14 = Button(root, text="", height=2, width=2, bg="red", command=clickyesbutton14)
      yesbutton14.pack(side="top", expand=True)

      global labelyesbutton14
      labelyesbutton14 = Label(root, text = "Yes", bg = "white", fg = "crimson", font=("EB Garamond", 24) )
      labelyesbutton14.pack(side = "top", expand = True)

      global nobutton14
      nobutton14 = Button(root, text="", height=2, width=2, bg="red", command=clicknobutton14)
      nobutton14.pack(side="top", expand=True)

      global labelnobutton14
      labelnobutton14 = Label(root, text = "No", bg = "white", fg = "crimson" , font=("EB Garamond", 24))
      labelnobutton14.pack(side = "top", expand = True)

      global notsurebutton14
      notsurebutton14 = Button(root, text="", height=2, width=2, bg="red", command=clicknotsurebutton14)
      notsurebutton14.pack(side="top", expand=True)

      global labelnotsurebutton14
      labelnotsurebutton14 = Label(root, text = "Not Sure", bg = "white", fg = "crimson", font=("EB Garamond", 24) )
      labelnotsurebutton14.pack(side = "top", expand = True)

  def clickq13aanswer2():
    global chemical
    chemical += 1
    question13a.pack_forget()
    q13aanswer1.pack_forget()
    q13aanswer2.pack_forget()
    labelq13aanswer1.pack_forget()
    labelq13aanswer2.pack_forget()
    if chemical == 9:

      def clickchempro():
        ceramicsinfo.pack_forget()
        next3.pack_forget()
        global chemproinfo
        chemproinfo = Label(root, text = "The main role of chemical engineers is to design and troubleshoot processes for the production \n  of chemicals, fuels, foods, pharmaceuticals, and biologicals. \n Median Salary : $108,700 \n Job Demand expected to increase 4% in the next 10 years. \n Top Colleges in NY : \n Columbia University \n Cornell University \n NYU \n University of Rochester", bg="white", fg = "crimson", font=("EB Garamond", 24) )
        chemproinfo.pack()

  

        

      def clickceramics():
        mineralproinfo.pack_forget()
        next2.pack_forget()
        global ceramicsinfo
        ceramicsinfo = Label(root, text = "Ceramic engineering is the science and technology \n of creating objects from inorganic, non-metallic materials. \n Median Salary: $83,000 \n Job Demand expected to grow 6.8% in next 10 years. \n Top Colleges in NY : \n Alfred University ", bg="white", fg = "crimson", font=("EB Garamond", 24))
        ceramicsinfo.pack()

        global next3
        next3 = Button(root, text = "NEXT", height = 5, width = 8, command = clickchempro)
        next3.pack()



      def clickmineralpro():
        biotechinfo.pack_forget()
        next1.pack_forget()
        global mineralproinfo
        mineralproinfo = Label(root, text = "Mineral Processing Engineering deals with the extraction, \n  separation, and concentration of minerals from raw ores. \n Median Salary : $60,000 \n Job Demand expected to grow 4% in the next 10 years. \n Top Colleges : \n Colorado School of Mines", bg="white", fg = "crimson", font=("EB Garamond", 24))
        mineralproinfo.pack()

        global next2
        next2 = Button(root, text = "NEXT", height = 5, width = 8, command = clickceramics)
        next2.pack()
        



      def clickbiotech():
        chemical_response.pack_forget()
        subfields.pack_forget()
        global biotechinfo
        biotechinfo = Label(root, text = "Biotechnology engineering is the research and study \n of micro-organism, bio-organisms, cell functions in living beings. \n Median Salary : $108,696 \n Job Demand expected to grow 5% in the next 10 years. \n Top Colleges in NY : \n Columbia University \n Cornell University \n Syracuse University \n RPI", bg="white", fg = "crimson", font=("EB Garamond", 24))
        biotechinfo.pack()

        global next1
        next1 = Button(root, text = "NEXT", height = 5, width = 8, command = clickmineralpro)
        next1.pack()






      def chemicalwin():

        global chemical_response
        chemical_response = Label(root, text="Chemical Engineering seems to be the best fit for you. \n Chemical engineering is the branch of engineering that deals \n with chemical production and the manufacture of products through chemical processes.\n Some classes/clubs you should consider are: \n - Calculus \n -Chemistry \n - Computer Science \n Some subfields that you can look into are: \n - Biotechnology \n - Mineral Processing \n - Ceramics \n - Chemical Processing", bg = "white", fg = "crimson", font=("EB Garamond", 24) )
        chemical_response.pack()
        

        global subfields
        subfields = Button(root, text = "Subfields", height = 5, width = 8, command = clickbiotech)
        subfields.pack()

      chemicalwin()
    else:
      global question14
      question14 = Label(root, text="Is the idea of redesigning \n the infrastructure of \n New York City \n appealing to you?",bg = "white", fg = "crimson" , font=("EB Garamond", 24))
      question14.pack(side="top", expand=True)

      global yesbutton14
      yesbutton14 = Button(root, text="", height=2, width=2, bg="red", command=clickyesbutton14)
      yesbutton14.pack(side="top", expand=True)

      global labelyesbutton14
      labelyesbutton14 = Label(root, text = "Yes", bg = "white", fg = "crimson", font=("EB Garamond", 24) )
      labelyesbutton14.pack(side = "top", expand = True)

      global nobutton14
      nobutton14 = Button(root, text="", height=2, width=2, bg="red", command=clicknobutton14)
      nobutton14.pack(side="top", expand=True)

      global labelnobutton14
      labelnobutton14 = Label(root, text = "No", bg = "white", fg = "crimson" , font=("EB Garamond", 24))
      labelnobutton14.pack(side = "top", expand = True)

      global notsurebutton14
      notsurebutton14 = Button(root, text="", height=2, width=2, bg="red", command=clicknotsurebutton14)
      notsurebutton14.pack(side="top", expand=True)

      global labelnotsurebutton14
      labelnotsurebutton14 = Label(root, text = "Not Sure", bg = "white", fg = "crimson", font=("EB Garamond", 24) )
      labelnotsurebutton14.pack(side = "top", expand = True)

  def clickyesbutton13():
    global mechanical
    mechanical += 1
    question13.pack_forget()
    yesbutton13.pack_forget()
    nobutton13.pack_forget()
    notsurebutton13.pack_forget()
    labelyesbutton13.pack_forget()
    labelnobutton13.pack_forget()
    labelnotsurebutton13.pack_forget()

    if mechanical == 9:


      def clickrobotics():
        datainfo.pack_forget()
        next4.pack_forget()
        global roboticsinfo
        roboticsinfo = Label(root, text = "Robotics engineering is a field of engineering \n which centers on building machines that replicate human actions. \n Median Salary : $99,040 \n Job Demand expected to grow 9% in the next 10 years. \n Top Colleges in NY : \n Cornell University \n NYU ", bg="white", fg = "crimson", font=("EB Garamond", 24))
        roboticsinfo.pack()
                
 


      def clickdataanalysis():
        cybersecurityinfo.pack_forget()
        next3.pack_forget()
        global datainfo
        datainfo = Label(root, text = "Data engineers are responsible for finding trends in data sets \n and developing algorithms to help make raw data more useful to the enterprise. \n Median Salary : $137,776 \n Job Demand expected to increase 21% in the next 10 years. \n Top Colleges in NY : \n Columbia University \n Cornell University \n NYU \n Syracuse \n NYIT ", bg="white", fg = "crimson", font=("EB Garamond", 24))
        datainfo.pack()
        global next4
        next4 = Button(root, text = "NEXT", height = 5, width = 8, command = clickrobotics)
        next4.pack()
     

      
      def clickcybersecurity():
        automationinfo.pack_forget()
        next2.pack_forget()
        global cybersecurityinfo
        cybersecurityinfo = Label(root, text = "Cybersecurity engineers, sometimes called information security engineers,\n identify threats and vulnerabilities in systems and software, \n then apply their skills to developing and implementing high-tech solutions \n to defend against hacking, malware and ransomware, \n insider threats and all types of cybercrime. \n Median Salary: $90,120 \n Job Demand expected to grow 31% in the next 10 years. \n Top Colleges in NY : \n NYU \n Syracuse University \n RIT \n Pace University", bg="white", fg = "crimson", font=("EB Garamond", 24))
        cybersecurityinfo.pack()
        global next3
        next3 = Button(root, text = "NEXT", height = 5, width = 8, command = clickdataanalysis)
        next3.pack()
     


      def clickautomation():
        aeroinfo.pack_forget()
        next1.pack_forget()

        global automationinfo
        automationinfo = Label(root, text = "An Automation Engineer utilizes technology \n to improve, streamline and automate a manufacturing process. \n Median Salary : $88,100 \n Job Demand expected to grow around 4% in the next 10 years \n Top Colleges in NY : \n SUNY Farmingdale \n SUNY College of Tech at Alfred", bg="white", fg = "crimson", font=("EB Garamond", 24))
        automationinfo.pack()
        global next2
        next2 = Button(root, text = "NEXT", height = 5, width = 8, command = clickcybersecurity)
        next2.pack()
     


      def clickaerospace():
        subfields.pack_forget()
        mechanical_response.pack_forget()
        global aeroinfo
        aeroinfo = Label(root, text = "Aerospace engineering is the primary field of engineering \n concerned with the development of aircraft and spacecraft.\n Median Salary : $116,500 \n Job Demand expected to grow around 3% in the next 10 years \n Top Colleges in NY : \n Cornell University \n RPI \n Syracuse University \n SUNY Buffalo", bg = "white", fg = "crimson" , font=("EB Garamond", 24))
        aeroinfo.pack()
        global next1
        next1 = Button(root, text = "NEXT", height = 5, width = 8, command = clickautomation)
        next1.pack()

        


      def mechanicalwin():
        
        global mechanical_response
        mechanical_response = Label(root, text="Mechanical Engineering seems to be the best fit for you.\n Mechanical Engineering is the branch of engineering dealing \n with the design, construction, and use of machines. \n Some classes/clubs you should consider are: \n - Robotics \n - RC Club \n -DDP \n -CAD \n -Engineering 1 \n -Engineering 2 \n - Physics \n -Calculus \n Some subfields you might want to look into are: \n - Aerospace \n - Automation \n - Cybersecurity \n -Robotics \n -Data Analysis", bg="white", fg = "crimson", font=("EB Garamond", 24))
        mechanical_response.pack()


        global subfields
        subfields = Button(root, text = "Subfields", height = 5, width = 8, command = clickaerospace)
        subfields.pack()

        



        

      mechanicalwin()
    else:
      global question13a
      question13a = Label(root, text="Would you rather conduct research \n on electrical devices or \n pharmaceutical products and food?", bg = "white", fg = "crimson" , font=("EB Garamond", 24))
      question13a.pack(side="top", expand=True)

      global q13aanswer1
      q13aanswer1 = Button(root, text="", height=2, width=2, bg="red", command=clickq13aanswer1)
      q13aanswer1.pack(side="top", expand=True)

      global labelq13aanswer1
      labelq13aanswer1 = Label(root, text="Electrical Devices", bg = "white", fg = "crimson", font=("EB Garamond", 24) )
      labelq13aanswer1.pack(side = "top", expand = True)

      global q13aanswer2
      q13aanswer2 = Button(root, text="", height=2, width=2, bg="red", command=clickq13aanswer2)
      q13aanswer2.pack(side="top", expand=True)

      global labelq13aanswer2
      labelq13aanswer2 = Label(root, text="Pharmeceutical \n Products \n and Food", bg = "white", fg = "crimson" , font=("EB Garamond", 24))
      labelq13aanswer2.pack(side = "top", expand = True)

  def clicknobutton13():
    global mechanical
    mechanical -= 1
    question13.pack_forget()
    yesbutton13.pack_forget()
    nobutton13.pack_forget()
    notsurebutton13.pack_forget()
    labelyesbutton13.pack_forget()
    labelnobutton13.pack_forget()
    labelnotsurebutton13.pack_forget()
    global question13a
    question13a = Label(root, text="Would you rather conduct research \n on electrical devices or \n pharmaceutical products and food?", bg="white", fg = "crimson" , font=("EB Garamond", 24))
    question13a.pack(side="top", expand=True)

    global q13aanswer1
    q13aanswer1 = Button(root, text="", height=2, width=2, bg="red", command=clickq13aanswer1)
    q13aanswer1.pack(side="top", expand=True)

    global labelq13aanswer1
    labelq13aanswer1 = Label(root, text="Electrical Devices", bg = "white", fg = "crimson" , font=("EB Garamond", 24))
    labelq13aanswer1.pack(side = "top", expand = True)

    global q13aanswer2
    q13aanswer2 = Button(root, text="", height=2, width=2, bg="red", command=clickq13aanswer2)
    q13aanswer2.pack(side="top", expand=True)

    global labelq13aanswer2
    labelq13aanswer2 = Label(root, text="Pharmeceutical \n Products \n and Food", bg = "white", fg = "crimson" , font=("EB Garamond", 24))
    labelq13aanswer2.pack(side = "top", expand = True)

  def clicknotsurebutton13():
    question13.pack_forget()
    yesbutton13.pack_forget()
    nobutton13.pack_forget()
    notsurebutton13.pack_forget()
    labelyesbutton13.pack_forget()
    labelnobutton13.pack_forget()
    labelnotsurebutton13.pack_forget()
    global question13a
    question13a = Label(root, text="Would you rather conduct research \n on electrical devices or \n pharmaceutical products and food?", bg = "white", fg = "crimson", font=("EB Garamond", 24) )
    question13a.pack(side="top", expand=True)

    global q13aanswer1
    q13aanswer1 = Button(root, text="", height=2, width=2, bg="red", command=clickq13aanswer1)
    q13aanswer1.pack(side="top", expand=True)

    global labelq13aanswer1
    labelq13aanswer1 = Label(root, text="Electrical Devices", bg = "white", fg = "crimson" , font=("EB Garamond", 24))
    labelq13aanswer1.pack(side = "top", expand = True)

    global q13aanswer2
    q13aanswer2 = Button(root, text="", height=2, width=2, bg="red", command=clickq13aanswer2)
    q13aanswer2.pack(side="top", expand=True)

    global labelq13aanswer2
    labelq13aanswer2 = Label(root, text="Pharmeceutical \n Products \n and Food", bg = "white", fg = "crimson" , font=("EB Garamond", 24))
    labelq13aanswer2.pack(side = "top", expand = True)






  def clickyesbutton12():
    global electrical
    electrical += 1
    question12.pack_forget()
    yesbutton12.pack_forget()
    nobutton12.pack_forget()
    notsurebutton12.pack_forget()
    labelyesbutton12.pack_forget()
    labelnobutton12.pack_forget()
    labelnotsurebutton12.pack_forget()

    if electrical == 9:


      def clickmicroelec():
        signalproinfo.pack_forget()
        next3.pack_forget()
        global microelecinfo
        microelecinfo = Label(root, text = "Microelectronics engineers develop plans and construct prototypes of \n electronic circuit chips, circuit boards, and semiconductors. \n Median Salary: $76,100 \n Job Demand expected to increase roughly 1% in the next 10 years. \n Top Colleges in NY : \n Cornell University \n RPI \n Columbia University \n Clarkson University ", bg="white", fg = "crimson", font=("EB Garamond", 24))
        microelecinfo.pack()


      def clicksignalpro():
        controlsysinfo.pack_forget()
        next2.pack_forget()
        global signalproinfo
        signalproinfo = Label(root, text = "A signal processing engineer is an information technologies expert \n that analyzes and alters digital signals to make them more accurate and reliable.\n Median Salary: $105,000 \n Top Colleges in NY : \n Cornell University \n RIT \n Syracuse University ", bg="white", fg = "crimson", font=("EB Garamond", 24))
        signalproinfo.pack()
        global next3
        next3 = Button(root, text = "NEXT", height = 5, width = 8, command = clickmicroelec)
        next3.pack()



      def clickcontrolsys():
        telecominfo.pack_forget()
        next1.pack_forget()
        global controlsysinfo
        controlsysinfo = Label(root, text = "A Control Systems Engineer is responsible for designing, developing, \n and implementing solutions that control dynamic systems. \n Median Salary : $88, 616 \n Job Demand expected to increase 2% in the next 10 yearss. \n Top Colleges in NY : \n RPI \n Cornell University \n West Point \n Binghamton ", bg="white", fg = "crimson", font=("EB Garamond", 24))
        controlsysinfo.pack()

        global next2
        next2 = Button(root, text = "NEXT", height = 5, width = 8, command = clicksignalpro)
        next2.pack()




      def clicktelecom():
        electrical_response.pack_forget()
        subfields.pack_forget()
        global telecominfo
        telecominfo = Label(root, text = "Telecommunications engineers or telecom engineers are expert in managing data \n such as voice, video, calls, and text over different modes of communication. \n Median Salary: $76, 524 \n Job Demand expected to increase around 5% in the next 10 years. \n Top Colleges in NY : \n SUNY Stonybrook", bg="white", fg = "crimson", font=("EB Garamond", 24))
        telecominfo.pack()

        global next1
        next1 = Button(root, text = "NEXT", height = 5, width = 8, command = clickcontrolsys)
        next1.pack()



      def electricalwin():
        global electrical_response
        electrical_response = Label(root, text="Electrical Engineering seems to be the best fit for you. \nElectrical Engineering is an engineering discipline concerned \n with the study, design and application of equipment, devices \n and systems which use electricity, electronics, and electromagnetism.\n Some classes/clubs you should try out are: \n - Robotics \n - Engineering 1 \n - Engineering 2 \n - Coding Club \n - RC Club \n - Computer Science \n Some subfields that you can look into are: \n -Telecommunications \n -Control Systems \n -Signal Processing \n - Microelectronics", bg="white", fg = "crimson", font=("EB Garamond", 24) )
        electrical_response.pack()


        global subfields
        subfields = Button(root, text = "Subfields", height = 5, width = 8, command = clicktelecom)
        subfields.pack()

        


      electricalwin()
    else:
      global question13
      question13 = Label(root, text="Are you interested in designing \n  virtual reality systems?", bg = "white", fg = "crimson", font=("EB Garamond", 24) )
      question13.pack(side="top", expand=True)

      global yesbutton13
      yesbutton13 = Button(root, text="", height=2, width=2, bg="red", command=clickyesbutton13)
      yesbutton13.pack(side="top", expand=True)

      global labelyesbutton13
      labelyesbutton13 = Label(root, text = "Yes", bg = "white", fg = "crimson", font=("EB Garamond", 24) )
      labelyesbutton13.pack(side = "top", expand = True)

      global nobutton13
      nobutton13 = Button(root, text="", height=2, width=2, bg="red", command=clicknobutton13)
      nobutton13.pack(side="top", expand=True)

      global labelnobutton13
      labelnobutton13 = Label(root, text = "No", bg = "white", fg = "crimson" , font=("EB Garamond", 24))
      labelnobutton13.pack(side = "top", expand = True)

      global notsurebutton13
      notsurebutton13 = Button(root, text="", height=2, width=2, bg="red", command=clicknotsurebutton13)
      notsurebutton13.pack(side="top", expand=True)

      global labelnotsurebutton13
      labelnotsurebutton13 = Label(root, text = "Not Sure", bg = "white", fg = "crimson", font=("EB Garamond", 24) )
      labelnotsurebutton13.pack(side = "top", expand = True)


  def clicknobutton12():
    global chemical
    chemical += 1
    question12.pack_forget()
    yesbutton12.pack_forget()
    nobutton12.pack_forget()
    notsurebutton12.pack_forget()
    labelyesbutton12.pack_forget()
    labelnobutton12.pack_forget()
    labelnotsurebutton12.pack_forget()

    if chemical == 9:


      def clickchempro():
        ceramicsinfo.pack_forget()
        next3.pack_forget()
        global chemproinfo
        chemproinfo = Label(root, text = "The main role of chemical engineers is to design and troubleshoot processes for the production \n  of chemicals, fuels, foods, pharmaceuticals, and biologicals. \n Median Salary : $108,700 \n Job Demand expected to increase 4% in the next 10 years. \n Top Colleges in NY : \n Columbia University \n Cornell University \n NYU \n University of Rochester" , bg="white", fg = "crimson", font=("EB Garamond", 24))
        chemproinfo.pack()

  

        

      def clickceramics():
        mineralproinfo.pack_forget()
        next2.pack_forget()
        global ceramicsinfo
        ceramicsinfo = Label(root, text = "Ceramic engineering is the science and technology \n of creating objects from inorganic, non-metallic materials. \n Median Salary: $83,000 \n Job Demand expected to grow 6.8% in next 10 years. \n Top Colleges in NY : \n Alfred University ", bg="white", fg = "crimson", font=("EB Garamond", 24))
        ceramicsinfo.pack()

        global next3
        next3 = Button(root, text = "NEXT", height = 5, width = 8, command = clickchempro)
        next3.pack()



      def clickmineralpro():
        biotechinfo.pack_forget()
        next1.pack_forget()
        global mineralproinfo
        mineralproinfo = Label(root, text = "Mineral Processing Engineering deals with the extraction, \n  separation, and concentration of minerals from raw ores. \n Median Salary : $60,000 \n Job Demand expected to grow 4% in the next 10 years. \n Top Colleges : \n Colorado School of Mines", bg="white", fg = "crimson", font=("EB Garamond", 24))
        mineralproinfo.pack()

        global next2
        next2 = Button(root, text = "NEXT", height = 5, width = 8, command = clickceramics)
        next2.pack()
        



      def clickbiotech():
        chemical_response.pack_forget()
        subfields.pack_forget()
        global biotechinfo
        biotechinfo = Label(root, text = "Biotechnology engineering is the research and study \n of micro-organism, bio-organisms, cell functions in living beings. \n Median Salary : $108,696 \n Job Demand expected to grow 5% in the next 10 years. \n Top Colleges in NY : \n Columbia University \n Cornell University \n Syracuse University \n RPI", bg="white", fg = "crimson", font=("EB Garamond", 24))
        biotechinfo.pack()

        global next1
        next1 = Button(root, text = "NEXT", height = 5, width = 8, command = clickmineralpro)
        next1.pack()






      def chemicalwin():

        global chemical_response
        chemical_response = Label(root, text="Chemical Engineering seems to be the best fit for you. \n Chemical engineering is the branch of engineering that deals \n with chemical production and the manufacture of products through chemical processes.\n Some classes/clubs you should consider are: \n - Calculus \n -Chemistry \n - Computer Science \n Some subfields that you can look into are: \n - Biotechnology \n - Mineral Processing \n - Ceramics \n - Chemical Processing", bg = "white", fg = "crimson", font=("EB Garamond", 24) )
        chemical_response.pack()
        

        global subfields
        subfields = Button(root, text = "Subfields", height = 5, width = 8, command = clickbiotech)
        subfields.pack()

      chemicalwin()
    else:
      global question13
      question13 = Label(root, text="Are you interested in designing \n  virtual reality systems?", bg = "white", fg = "crimson" , font=("EB Garamond", 24))
      question13.pack(side="top", expand=True)

      global yesbutton13
      yesbutton13 = Button(root, text="", height=2, width=2, bg="red", command=clickyesbutton13)
      yesbutton13.pack(side="top", expand=True)

      global labelyesbutton13
      labelyesbutton13 = Label(root, text = "Yes", bg = "white", fg = "crimson" , font=("EB Garamond", 24))
      labelyesbutton13.pack(side = "top", expand = True)

      global nobutton13
      nobutton13 = Button(root, text="", height=2, width=2, bg="red", command=clicknobutton13)
      nobutton13.pack(side="top", expand=True)

      global labelnobutton13
      labelnobutton13 = Label(root, text = "No", bg = "white", fg = "crimson", font=("EB Garamond", 24) )
      labelnobutton13.pack(side = "top", expand = True)

      global notsurebutton13
      notsurebutton13 = Button(root, text="", height=2, width=2, bg="red", command=clicknotsurebutton13)
      notsurebutton13.pack(side="top", expand=True)

      global labelnotsurebutton13
      labelnotsurebutton13 = Label(root, text = "Not Sure", bg = "white", fg = "crimson", font=("EB Garamond", 24) )
      labelnotsurebutton13.pack(side = "top", expand = True)


    

  def clicknotsurebutton12():
    global mechanical
    mechanical += 1
    question12.pack_forget()
    yesbutton12.pack_forget()
    nobutton12.pack_forget()
    notsurebutton12.pack_forget()
    labelyesbutton12.pack_forget()
    labelnobutton12.pack_forget()
    labelnotsurebutton12.pack_forget()

    if mechanical == 9:

      def clickrobotics():
        datainfo.pack_forget()
        next4.pack_forget()
        global roboticsinfo
        roboticsinfo = Label(root, text = "Robotics engineering is a field of engineering \n which centers on building machines that replicate human actions. \n Median Salary : $99,040 \n Job Demand expected to grow 9% in the next 10 years. \n Top Colleges in NY : \n Cornell University \n NYU ", bg="white", fg = "crimson", font=("EB Garamond", 24))
        roboticsinfo.pack()
                
 


      def clickdataanalysis():
        cybersecurityinfo.pack_forget()
        next3.pack_forget()
        global datainfo
        datainfo = Label(root, text = "Data engineers are responsible for finding trends in data sets \n and developing algorithms to help make raw data more useful to the enterprise. \n Median Salary : $137,776 \n Job Demand expected to increase 21% in the next 10 years. \n Top Colleges in NY : \n Columbia University \n Cornell University \n NYU \n Syracuse \n NYIT ", bg="white", fg = "crimson", font=("EB Garamond", 24))
        datainfo.pack()
        global next4
        next4 = Button(root, text = "NEXT", height = 5, width = 8, command = clickrobotics)
        next4.pack()
     

      
      def clickcybersecurity():
        automationinfo.pack_forget()
        next2.pack_forget()
        global cybersecurityinfo
        cybersecurityinfo = Label(root, text = "Cybersecurity engineers, sometimes called information security engineers,\n identify threats and vulnerabilities in systems and software, \n then apply their skills to developing and implementing high-tech solutions \n to defend against hacking, malware and ransomware, \n insider threats and all types of cybercrime. \n Median Salary: $90,120 \n Job Demand expected to grow 31% in the next 10 years. \n Top Colleges in NY : \n NYU \n Syracuse University \n RIT \n Pace University", bg="white", fg = "crimson", font=("EB Garamond", 24))
        cybersecurityinfo.pack()
        global next3
        next3 = Button(root, text = "NEXT", height = 5, width = 8, command = clickdataanalysis)
        next3.pack()
     


      def clickautomation():
        aeroinfo.pack_forget()
        next1.pack_forget()

        global automationinfo
        automationinfo = Label(root, text = "An Automation Engineer utilizes technology \n to improve, streamline and automate a manufacturing process. \n Median Salary : $88,100 \n Job Demand expected to grow around 4% in the next 10 years \n Top Colleges in NY : \n SUNY Farmingdale \n SUNY College of Tech at Alfred", bg="white", fg = "crimson", font=("EB Garamond", 24))
        automationinfo.pack()
        global next2
        next2 = Button(root, text = "NEXT", height = 5, width = 8, command = clickcybersecurity)
        next2.pack()
     


      def clickaerospace():
        subfields.pack_forget()
        mechanical_response.pack_forget()
        global aeroinfo
        aeroinfo = Label(root, text = "Aerospace engineering is the primary field of engineering \n concerned with the development of aircraft and spacecraft.\n Median Salary : $116,500 \n Job Demand expected to grow around 3% in the next 10 years \n Top Colleges in NY : \n Cornell University \n RPI \n Syracuse University \n SUNY Buffalo", bg="white", fg = "crimson", font=("EB Garamond", 24))
        aeroinfo.pack()
        global next1
        next1 = Button(root, text = "NEXT", height = 5, width = 8, command = clickautomation)
        next1.pack()

        


      def mechanicalwin():
        
        global mechanical_response
        mechanical_response = Label(root, text="Mechanical Engineering seems to be the best fit for you.\n Mechanical Engineering is the branch of engineering dealing \n with the design, construction, and use of machines. \n Some classes/clubs you should consider are: \n - Robotics \n - RC Club \n -DDP \n -CAD \n -Engineering 1 \n -Engineering 2 \n - Physics \n -Calculus \n Some subfields you might want to look into are: \n - Aerospace \n - Automation \n - Cybersecurity \n -Robotics \n -Data Analysis", bg="white", fg = "crimson", font=("EB Garamond", 24))
        mechanical_response.pack()


        global subfields
        subfields = Button(root, text = "Subfields", height = 5, width = 8, command = clickaerospace)
        subfields.pack()

      
      mechanicalwin()
    else:
      global question13
      question13 = Label(root, text="Are you interested in designing \n  virtual reality systems?", bg = "white", fg = "crimson" , font=("EB Garamond", 24))
      question13.pack(side="top", expand=True)

      global yesbutton13
      yesbutton13 = Button(root, text="", height=2, width=2, bg="red", command=clickyesbutton13)
      yesbutton13.pack(side="top", expand=True)

      global labelyesbutton13
      labelyesbutton13 = Label(root, text = "Yes", bg = "white", fg = "crimson", font=("EB Garamond", 24) )
      labelyesbutton13.pack(side = "top", expand = True)

      global nobutton13
      nobutton13 = Button(root, text="", height=2, width=2, bg="red", command=clicknobutton13)
      nobutton13.pack(side="top", expand=True)

      global labelnobutton13
      labelnobutton13 = Label(root, text = "No", bg = "white", fg = "crimson" , font=("EB Garamond", 24))
      labelnobutton13.pack(side = "top", expand = True)

      global notsurebutton13
      notsurebutton13 = Button(root, text="", height=2, width=2, bg="red", command=clicknotsurebutton13)
      notsurebutton13.pack(side="top", expand=True)

      global labelnotsurebutton13
      labelnotsurebutton13 = Label(root, text = "Not Sure", bg = "white", fg = "crimson", font=("EB Garamond", 24) )
      labelnotsurebutton13.pack(side = "top", expand = True)


   

  def clickyesbutton11():
    global civil
    civil += 1
    question11.pack_forget()
    yesbutton11.pack_forget()
    nobutton11.pack_forget()
    notsurebutton11.pack_forget()
    labelyesbutton11.pack_forget()
    labelnobutton11.pack_forget()
    labelnotsurebutton11.pack_forget()
    if civil == 9:


      def clickstructural():
        environment.pack_forget()
        next3.pack_forget()

        global structural
        structural = Label(root, text = "Structural engineers focus on the physical integrity and \n design of projects such as buildings, bridges, and tunnels.\n Median Salary: $78,460 \n Job Demand expected to increase 6% in the next 10 years. \n Top Colleges in NY: \n NYU \n UBuffalo", bg="white", fg = "crimson", font=("EB Garamond", 24))
        structural.pack()

    


      def clickenvironment():
        geotech.pack_forget()
        next2.pack_forget()

        global environment
        environment = Label(root, text = "Environmental engineers use the principles of engineering, soil science, biology, \n and chemistry to develop solutions to environmental problems. They work to improve \n recycling, waste disposal, public health, and water and air pollution control. \n Median Salary : $84,560 \n Job Demand expected to increase 3% in the next 10 years. \n Top Colleges in NY: \n Columbia University \n Cornell University \n RPI \n RIT", bg="white", fg = "crimson", font=("EB Garamond", 24))
        environment.pack()

        global next3
        next3 = Button(root, text = "NEXT" , height = 5, width = 8, command = clickstructural)
        next3.pack()


      def clickgeotech():
        coastaleng.pack_forget()
        next1.pack_forget()

        global geotech
        geotech = Label(root, text = "Geotechnical engineering, also known as geotechnics, is the branch \n of civil engineering concerned with the engineering behavior of earth materials.\n Median Salary: $65,497 \n Job Demand expected to increase 11% in the next 10 years. \n Top Colleges in NY: \n Columbia University \n Cornell University \n RPI", bg="white", fg = "crimson", font=("EB Garamond", 24))
        geotech.pack()

        global next2
        next2 = Button(root, text = "NEXT" , height = 5, width = 8, command = clickenvironment)
        next2.pack()



      def clickcoastaleng():
        civil_response.pack_forget()
        subfields.pack_forget()

        global coastaleng
        coastaleng = Label(root, text = "Coastal engineering is a division of civil engineering responsible for \n the organization, conception, development and preservation of works in the coastal area. \n Median Salary: $98,000 \n Job Demand expected to increase 1% in the next 10 years. \n Top Colleges in NY : \n Columbia University \n Cornell University \n RPI", bg="white", fg = "crimson", font=("EB Garamond", 24))
        coastaleng.pack()

        global next1
        next1 = Button(root, text = "NEXT" , height = 5, width = 8, command = clickgeotech)
        next1.pack()




      def civilwin():
        global civil_response
        civil_response = Label(root, text="Civil Engineering seems to be the best fit for you. \nCivil engineering is a professional engineering discipline that deals \n with the design, construction, and maintenance of the physical and naturally built environment.\n Some classes/clubs that you should consider are: \n -CAD \n - Engineering 1 \n - Engineering 2 \n -Robotics \n -Calculus \n -Physics \n - Communication Technology \n - Transportation Technology \n Some subfields that you can look into are: \n - Coastal Engineering \n - Geotechnical Engineering \n - Environmental Engineering \n - Structural Engineering ", bg = "white", fg = "crimson", font=("EB Garamond", 24))
        civil_response.pack()
       

        global subfields
        subfields = Button(root, text = "NEXT", height = 5, width = 8, command = clickcoastaleng)
        subfields.pack()
      civilwin()
    else:
      global question12
      question12 = Label(root, text="How would others describe you?", bg="white", fg = "crimson" , font=("EB Garamond", 24))
      question12.pack(side="top", expand=True)


      global yesbutton12
      yesbutton12 = Button(root, text="", height=2, width=2, bg="red", command=clickyesbutton12)
      yesbutton12.pack(side="top", expand=True)

      global labelyesbutton12
      labelyesbutton12 = Label(root, text="Logical,\n Meticulous", bg = "white", fg = "crimson", font=("EB Garamond", 24) )
      labelyesbutton12.pack(side = "top", expand = True)


      global nobutton12
      nobutton12 = Button(root, text="", height=2, width=2, bg="red", command=clicknobutton12)
      nobutton12.pack(side="top", expand=True)

      global labelnobutton12
      labelnobutton12 = Label(root, text="Adventurous,\n Bold", bg = "white", fg = "crimson" , font=("EB Garamond", 24))
      labelnobutton12.pack(side = "top", expand = True)

      global notsurebutton12
      notsurebutton12 = Button(root, text="",height=2, width=2, bg="red", command=clicknotsurebutton12)
      notsurebutton12.pack(side="top", expand=True)

      global labelnotsurebutton12
      labelnotsurebutton12 = Label(root, text="Tinkerer,\n Crafty", bg = "white", fg = "crimson" , font=("EB Garamond", 24))
      labelnotsurebutton12.pack(side = "top", expand = True)


  def clicknobutton11():
    global civil
    civil -= 1
    question11.pack_forget()
    yesbutton11.pack_forget()
    nobutton11.pack_forget()
    notsurebutton11.pack_forget()
    labelyesbutton11.pack_forget()
    labelnobutton11.pack_forget()
    labelnotsurebutton11.pack_forget()

    global question12
    question12 = Label(root, text="How would others describe you?", bg = "white", fg = "crimson", font=("EB Garamond", 24) )
    question12.pack(side="top", expand=True)


    global yesbutton12
    yesbutton12 = Button(root, text="", height=2, width=2, bg="red", command=clickyesbutton12)
    yesbutton12.pack(side="top", expand=True)

    global labelyesbutton12
    labelyesbutton12 = Label(root, text="Logical,\n Meticulous", bg = "white", fg = "crimson" , font=("EB Garamond", 24))
    labelyesbutton12.pack(side = "top", expand = True)


    global nobutton12
    nobutton12 = Button(root, text="", height=2, width=2, bg="red", command=clicknobutton12)
    nobutton12.pack(side="top", expand=True)

    global labelnobutton12
    labelnobutton12 = Label(root, text="Adventurous,\n Bold", bg = "white", fg = "crimson" , font=("EB Garamond", 24))
    labelnobutton12.pack(side = "top", expand = True)

    global notsurebutton12
    notsurebutton12 = Button(root, text="",height=2, width=2, bg="red", command=clicknotsurebutton12)
    notsurebutton12.pack(side="top", expand=True)

    global labelnotsurebutton12
    labelnotsurebutton12 = Label(root, text="Tinkerer,\n Crafty", bg = "white", fg = "crimson" , font=("EB Garamond", 24))
    labelnotsurebutton12.pack(side = "top", expand = True)


  def clicknotsurebutton11():
    question11.pack_forget()
    yesbutton11.pack_forget()
    nobutton11.pack_forget()
    notsurebutton11.pack_forget()
    labelyesbutton11.pack_forget()
    labelnobutton11.pack_forget()
    labelnotsurebutton11.pack_forget()
    
    global question12
    question12 = Label(root, text="How would others describe you?", bg = "white", fg = "crimson", font=("EB Garamond", 24) )
    question12.pack(side="top", expand=True)


    global yesbutton12
    yesbutton12 = Button(root, text="", height=2, width=2, bg="red", command=clickyesbutton12)
    yesbutton12.pack(side="top", expand=True)

    global labelyesbutton12
    labelyesbutton12 = Label(root, text="Logical,\n Meticulous", bg = "white", fg = "crimson" , font=("EB Garamond", 24))
    labelyesbutton12.pack(side = "top", expand = True)


    global nobutton12
    nobutton12 = Button(root, text="", height=2, width=2, bg="red", command=clicknobutton12)
    nobutton12.pack(side="top", expand=True)

    global labelnobutton12
    labelnobutton12 = Label(root, text="Adventurous,\n Bold", bg = "white", fg = "crimson", font=("EB Garamond", 24) )
    labelnobutton12.pack(side = "top", expand = True)

    global notsurebutton12
    notsurebutton12 = Button(root, text="",height=2, width=2, bg="red", command=clicknotsurebutton12)
    notsurebutton12.pack(side="top", expand=True)

    global labelnotsurebutton12
    labelnotsurebutton12 = Label(root, text="Tinkerer,\n Crafty", bg = "white", fg = "crimson" , font=("EB Garamond", 24))
    labelnotsurebutton12.pack(side = "top", expand = True)



  def clickyesbutton10():
    global chemical
    chemical += 1
    question10.pack_forget()
    yesbutton10.pack_forget()
    nobutton10.pack_forget()
    notsurebutton10.pack_forget()
    labelyesbutton10.pack_forget()
    labelnobutton10.pack_forget()
    labelnotsurebutton10.pack_forget()

    global question11
    question11 = Label(root, text="Are you interested about \n what goes on at \n construction sites?" , bg = "white", fg = "crimson" , font=("EB Garamond", 24))
    question11.pack(side="top", expand=True)

    global yesbutton11
    yesbutton11 = Button(root, text="", height=2, width=2, bg="red", command=clickyesbutton11)
    yesbutton11.pack(side="top", expand=True)

    global labelyesbutton11
    labelyesbutton11 = Label(root, text = "Yes", bg = "white" , fg = "crimson", font=("EB Garamond", 24) )
    labelyesbutton11.pack(side = "top", expand = True)

    global nobutton11
    nobutton11 = Button(root, text="", height=2, width=2, bg="red", command=clicknobutton11)
    nobutton11.pack(side="top", expand=True)

    global labelnobutton11
    labelnobutton11 = Label(root, text = "No", bg = "white" , fg = "crimson" , font=("EB Garamond", 24))
    labelnobutton11.pack(side = "top", expand = True)


    global notsurebutton11
    notsurebutton11 = Button(root, text="", height=2, width=2, bg="red", command=clicknotsurebutton11)
    notsurebutton11.pack(side="top", expand=True)

    global labelnotsurebutton11
    labelnotsurebutton11 = Label(root, text = "Not Sure", bg = "white" , fg = "crimson", font=("EB Garamond", 24) )
    labelnotsurebutton11.pack(side = "top", expand = True)


  def clicknobutton10():
    global chemical
    chemical -= 1
    question10.pack_forget()
    yesbutton10.pack_forget()
    nobutton10.pack_forget()
    notsurebutton10.pack_forget()
    labelyesbutton10.pack_forget()
    labelnobutton10.pack_forget()
    labelnotsurebutton10.pack_forget()

    global question11
    question11 = Label(root, text="Are you interested about \n what goes on at \n construction sites?" , bg = "white", fg = "crimson" , font=("EB Garamond", 24))
    question11.pack(side="top", expand=True)

    global yesbutton11
    yesbutton11 = Button(root, text="", height=2, width=2, bg="red", command=clickyesbutton11)
    yesbutton11.pack(side="top", expand=True)

    global labelyesbutton11
    labelyesbutton11 = Label(root, text = "Yes", bg = "white" , fg = "crimson", font=("EB Garamond", 24) )
    labelyesbutton11.pack(side = "top", expand = True)

    global nobutton11
    nobutton11 = Button(root, text="", height=2, width=2, bg="red", command=clicknobutton11)
    nobutton11.pack(side="top", expand=True)

    global labelnobutton11
    labelnobutton11 = Label(root, text = "No", bg = "white" , fg = "crimson", font=("EB Garamond", 24) )
    labelnobutton11.pack(side = "top", expand = True)


    global notsurebutton11
    notsurebutton11 = Button(root, text="", height=2, width=2, bg="red", command=clicknotsurebutton11)
    notsurebutton11.pack(side="top", expand=True)

    global labelnotsurebutton11
    labelnotsurebutton11 = Label(root, text = "Not Sure", bg = "white" , fg = "crimson" , font=("EB Garamond", 24))
    labelnotsurebutton11.pack(side = "top", expand = True)


  def clicknotsurebutton10():
    question10.pack_forget()
    yesbutton10.pack_forget()
    nobutton10.pack_forget()
    notsurebutton10.pack_forget()
    labelyesbutton10.pack_forget()
    labelnobutton10.pack_forget()
    labelnotsurebutton10.pack_forget()

    global question11
    question11 = Label(root, text="Are you interested about \n what goes on at \n construction sites?" , bg = "white" , fg = "crimson", font=("EB Garamond", 24) )
    question11.pack(side="top", expand=True)

    global yesbutton11
    yesbutton11 = Button(root, text="", height=2, width=2, bg="red", command=clickyesbutton11)
    yesbutton11.pack(side="top", expand=True)

    global labelyesbutton11
    labelyesbutton11 = Label(root, text = "Yes", bg = "white" , fg = "crimson" , font=("EB Garamond", 24))
    labelyesbutton11.pack(side = "top", expand = True)

    global nobutton11
    nobutton11 = Button(root, text="", height=2, width=2, bg="red", command=clicknobutton11)
    nobutton11.pack(side="top", expand=True)

    global labelnobutton11
    labelnobutton11 = Label(root, text = "No", bg = "white" , fg = "crimson", font=("EB Garamond", 24) )
    labelnobutton11.pack(side = "top", expand = True)


    global notsurebutton11
    notsurebutton11 = Button(root, text="", height=2, width=2, bg="red", command=clicknotsurebutton11)
    notsurebutton11.pack(side="top", expand=True)

    global labelnotsurebutton11
    labelnotsurebutton11 = Label(root, text = "Not Sure", bg = "white" , fg = "crimson" , font=("EB Garamond", 24))
    labelnotsurebutton11.pack(side = "top", expand = True)






  def clickyesbutton9(): 
    global chemical
    chemical += 1
    question9.pack_forget()
    yesbutton9.pack_forget()
    nobutton9.pack_forget()
    notsurebutton9.pack_forget()
    labelyesbutton9.pack_forget()
    labelnobutton9.pack_forget()
    labelnotsurebutton9.pack_forget()

    global question10
    question10 = Label(root, text="Would you like to do work in the \n food or pharmaceutical industry?",bg = "white", fg = "crimson" , font=("EB Garamond", 24))
    question10.pack(side="top", expand=True)

    global yesbutton10
    yesbutton10 = Button(root, text="", height=2, width=2, bg="red", command=clickyesbutton10)
    yesbutton10.pack(side="top", expand=True)

    global labelyesbutton10
    labelyesbutton10 = Label(root, text = "Yes", bg = "white" , fg = "crimson", font=("EB Garamond", 24) )
    labelyesbutton10.pack(side = "top", expand = True)

    global nobutton10
    nobutton10 = Button(root, text="", height=2, width=2, bg="red", command=clicknobutton10)
    nobutton10.pack(side="top", expand=True)

    global labelnobutton10
    labelnobutton10 = Label(root, text = "No", bg = "white", fg = "crimson" , font=("EB Garamond", 24) )
    labelnobutton10.pack(side = "top", expand = True)

    global notsurebutton10
    notsurebutton10 = Button(root, text="", height=2, width=2, bg="red", command=clicknotsurebutton10)
    notsurebutton10.pack(side="top", expand=True)

    global labelnotsurebutton10
    labelnotsurebutton10 = Label(root, text = "Not Sure", bg = "white" , fg = "crimson" , font=("EB Garamond", 24))
    labelnotsurebutton10.pack(side = "top", expand = True)

  def clicknobutton9():
    global chemical
    chemical -= 1
    question9.pack_forget()
    yesbutton9.pack_forget()
    nobutton9.pack_forget()
    notsurebutton9.pack_forget()
    labelyesbutton9.pack_forget()
    labelnobutton9.pack_forget()
    labelnotsurebutton9.pack_forget()

    global question10
    question10 = Label(root, text="Would you like to do work in the \n food or pharmaceutical industry?",bg = "white", fg = "crimson", font=("EB Garamond", 24) )
    question10.pack(side="top", expand=True)

    global yesbutton10
    yesbutton10 = Button(root, text="", height=2, width=2, bg="red", command=clickyesbutton10)
    yesbutton10.pack(side="top", expand=True)

    global labelyesbutton10
    labelyesbutton10 = Label(root, text = "Yes", bg = "white" , fg = "crimson" , font=("EB Garamond", 24))
    labelyesbutton10.pack(side = "top", expand = True)

    global nobutton10
    nobutton10 = Button(root, text="", height=2, width=2, bg="red", command=clicknobutton10)
    nobutton10.pack(side="top", expand=True)

    global labelnobutton10
    labelnobutton10 = Label(root, text = "No", bg = "white" , fg = "crimson", font=("EB Garamond", 24) )
    labelnobutton10.pack(side = "top", expand = True)

    global notsurebutton10
    notsurebutton10 = Button(root, text="", height=2, width=2, bg="red", command=clicknotsurebutton10)
    notsurebutton10.pack(side="top", expand=True)

    global labelnotsurebutton10
    labelnotsurebutton10 = Label(root, text = "Not Sure", bg = "white" , fg = "crimson" , font=("EB Garamond", 24))
    labelnotsurebutton10.pack(side = "top", expand = True)

  def clicknotsurebutton9():
    question9.pack_forget()
    yesbutton9.pack_forget()
    nobutton9.pack_forget()
    notsurebutton9.pack_forget()
    labelyesbutton9.pack_forget()
    labelnobutton9.pack_forget()
    labelnotsurebutton9.pack_forget()

    global question10
    question10 = Label(root, text="Would you like to do work in the \n food or pharmaceutical industry?",bg = "white", fg = "crimson" , font=("EB Garamond", 24))
    question10.pack(side="top", expand=True)

    global yesbutton10
    yesbutton10 = Button(root, text="", height=2, width=2, bg="red", command=clickyesbutton10)
    yesbutton10.pack(side="top", expand=True)

    global labelyesbutton10
    labelyesbutton10 = Label(root, text = "Yes", bg = "white" , fg = "crimson" , font=("EB Garamond", 24))
    labelyesbutton10.pack(side = "top", expand = True)

    global nobutton10
    nobutton10 = Button(root, text="", height=2, width=2, bg="red", command=clicknobutton10)
    nobutton10.pack(side="top", expand=True)

    global labelnobutton10
    labelnobutton10 = Label(root, text = "No", bg = "white" , fg = "crimson" , font=("EB Garamond", 24))
    labelnobutton10.pack(side = "top", expand = True)

    global notsurebutton10
    notsurebutton10 = Button(root, text="", height=2, width=2, bg="red", command=clicknotsurebutton10)
    notsurebutton10.pack(side="top", expand=True)

    global labelnotsurebutton10
    labelnotsurebutton10 = Label(root, text = "Not Sure", bg = "white" , fg = "crimson" , font=("EB Garamond", 24))
    labelnotsurebutton10.pack(side = "top", expand = True)









  def clickyesbutton8():
    global mechanical
    mechanical += 1
    question8.pack_forget()
    yesbutton8.pack_forget()
    nobutton8.pack_forget()
    notsurebutton8.pack_forget()
    labelyesbutton8.pack_forget()
    labelnobutton8.pack_forget()
    labelnotsurebutton8.pack_forget()

    global question9
    question9 = Label(root, text="Would you like your workday \n to be spent in a laboratory?", bg = "white", fg = "crimson" , font=("EB Garamond", 24))
    question9.pack(side="top", expand=True)

    global yesbutton9
    yesbutton9 = Button(root, text="", height=2, width=2, bg="red", command=clickyesbutton9)
    yesbutton9.pack(side="top", expand=True)

    global labelyesbutton9
    labelyesbutton9 = Label(root, text = "Yes", bg = "white" , fg = "crimson" , font=("EB Garamond", 24))
    labelyesbutton9.pack(side = "top", expand = True)

    global nobutton9
    nobutton9 = Button(root, text="", height=2, width=2, bg="red", command=clicknobutton9)
    nobutton9.pack(side="top", expand=True)

    global labelnobutton9
    labelnobutton9 = Label(root, text = "No", bg = "white" , fg = "crimson", font=("EB Garamond", 24) )
    labelnobutton9.pack(side = "top", expand = True)

    global notsurebutton9
    notsurebutton9 = Button(root, text="", height=2, width=2, bg="red", command=clicknotsurebutton9)
    notsurebutton9.pack(side="top", expand=True)

    global labelnotsurebutton9
    labelnotsurebutton9 = Label(root, text = "Not Sure", bg = "white" , fg = "crimson", font=("EB Garamond", 24) )
    labelnotsurebutton9.pack(side = "top", expand = True)


  def clicknobutton8():
    global mechanical
    mechanical -= 1
    question8.pack_forget()
    yesbutton8.pack_forget()
    nobutton8.pack_forget()
    notsurebutton8.pack_forget()
    labelyesbutton8.pack_forget()
    labelnobutton8.pack_forget()
    labelnotsurebutton8.pack_forget()

    global question9
    question9 = Label(root, text="Would you like your workday \n to be spent in a laboratory?", bg = "white", fg = "crimson" , font=("EB Garamond", 24))
    question9.pack(side="top", expand=True)

    global yesbutton9
    yesbutton9 = Button(root, text="", height=2, width=2, bg="red", command=clickyesbutton9)
    yesbutton9.pack(side="top", expand=True)

    global labelyesbutton9
    labelyesbutton9 = Label(root, text = "Yes", bg = "white" , fg = "crimson", font=("EB Garamond", 24) )
    labelyesbutton9.pack(side = "top", expand = True)

    global nobutton9
    nobutton9 = Button(root, text="", height=2, width=2, bg="red", command=clicknobutton9)
    nobutton9.pack(side="top", expand=True)

    global labelnobutton9
    labelnobutton9 = Label(root, text = "No", bg = "white" , fg = "crimson", font=("EB Garamond", 24) )
    labelnobutton9.pack(side = "top", expand = True)

    global notsurebutton9
    notsurebutton9 = Button(root, text="", height=2, width=2, bg="red", command=clicknotsurebutton9)
    notsurebutton9.pack(side="top", expand=True)

    global labelnotsurebutton9
    labelnotsurebutton9 = Label(root, text = "Not Sure", bg = "white" , fg = "crimson" , font=("EB Garamond", 24))
    labelnotsurebutton9.pack(side = "top", expand = True)

  def clicknotsurebutton8():
    question8.pack_forget()
    yesbutton8.pack_forget()
    nobutton8.pack_forget()
    notsurebutton8.pack_forget()
    labelyesbutton8.pack_forget()
    labelnobutton8.pack_forget()
    labelnotsurebutton8.pack_forget()

    global question9
    question9 = Label(root, text="Would you like your workday \n to be spent in a laboratory?", bg = "white", fg = "crimson" , font=("EB Garamond", 24))
    question9.pack(side="top", expand=True)

    global yesbutton9
    yesbutton9 = Button(root, text="", height=2, width=2, bg="red", command=clickyesbutton9)
    yesbutton9.pack(side="top", expand=True)

    global labelyesbutton9
    labelyesbutton9 = Label(root, text = "Yes", bg = "white" , fg = "crimson" , font=("EB Garamond", 24))
    labelyesbutton9.pack(side = "top", expand = True)

    global nobutton9
    nobutton9 = Button(root, text="", height=2, width=2, bg="red", command=clicknobutton9)
    nobutton9.pack(side="top", expand=True)

    global labelnobutton9
    labelnobutton9 = Label(root, text = "No", bg = "white" , fg = "crimson" , font=("EB Garamond", 24))
    labelnobutton9.pack(side = "top", expand = True)

    global notsurebutton9
    notsurebutton9 = Button(root, text="", height=2, width=2, bg="red", command=clicknotsurebutton9)
    notsurebutton9.pack(side="top", expand=True)

    global labelnotsurebutton9
    labelnotsurebutton9 = Label(root, text = "Not Sure", bg = "white" , fg = "crimson" , font=("EB Garamond", 24))
    labelnotsurebutton9.pack(side = "top", expand = True)




  def clickyesbutton7():
    global civil
    civil += 1
    question7.pack_forget()
    yesbutton7.pack_forget()
    nobutton7.pack_forget()
    notsurebutton7.pack_forget()
    labelyesbutton7.pack_forget()
    labelnobutton7.pack_forget()
    labelnotsurebutton7.pack_forget()
    if civil == 9:
      def clickstructural():
        environment.pack_forget()
        next3.pack_forget()

        global structural
        structural = Label(root, text = "Structural engineers focus on the physical integrity and \n design of projects such as buildings, bridges, and tunnels.\n Median Salary: $78,460 \n Job Demand expected to increase 6% in the next 10 years. \n Top Colleges in NY: \n NYU \n UBuffalo", bg="white", fg = "crimson", font=("EB Garamond", 24))
        structural.pack()

    


      def clickenvironment():
        geotech.pack_forget()
        next2.pack_forget()

        global environment
        environment = Label(root, text = "Environmental engineers use the principles of engineering, soil science, biology, \n and chemistry to develop solutions to environmental problems. They work to improve \n recycling, waste disposal, public health, and water and air pollution control. \n Median Salary : $84,560 \n Job Demand expected to increase 3% in the next 10 years. \n Top Colleges in NY: \n Columbia University \n Cornell University \n RPI \n RIT", bg="white", fg = "crimson", font=("EB Garamond", 24))
        environment.pack()

        global next3
        next3 = Button(root, text = "NEXT" , height = 5, width = 8, command = clickstructural)
        next3.pack()


      def clickgeotech():
        coastaleng.pack_forget()
        next1.pack_forget()

        global geotech
        geotech = Label(root, text = "Geotechnical engineering, also known as geotechnics, is the branch \n of civil engineering concerned with the engineering behavior of earth materials.\n Median Salary: $65,497 \n Job Demand expected to increase 11% in the next 10 years. \n Top Colleges in NY: \n Columbia University \n Cornell University \n RPI", bg="white", fg = "crimson", font=("EB Garamond", 24))
        geotech.pack()

        global next2
        next2 = Button(root, text = "NEXT" , height = 5, width = 8, command = clickenvironment)
        next2.pack()



      def clickcoastaleng():
        civil_response.pack_forget()
        subfields.pack_forget()

        global coastaleng
        coastaleng = Label(root, text = "Coastal engineering is a division of civil engineering responsible for \n the organization, conception, development and preservation of works in the coastal area. \n Median Salary: $98,000 \n Job Demand expected to increase 1% in the next 10 years. \n Top Colleges in NY : \n Columbia University \n Cornell University \n RPI", bg="white", fg = "crimson", font=("EB Garamond", 24))
        coastaleng.pack()

        global next1
        next1 = Button(root, text = "NEXT" , height = 5, width = 8, command = clickgeotech)
        next1.pack()




      def civilwin():
        global civil_response
        civil_response = Label(root, text="Civil Engineering seems to be the best fit for you. \nCivil engineering is a professional engineering discipline that deals \n with the design, construction, and maintenance of the physical and naturally built environment.\n Some classes/clubs that you should consider are: \n -CAD \n - Engineering 1 \n - Engineering 2 \n -Robotics \n -Calculus \n -Physics \n - Communication Technology \n - Transportation Technology \n Some subfields that you can look into are: \n - Coastal Engineering \n - Geotechnical Engineering \n - Environmental Engineering \n - Structural Engineering ", bg = "white", fg = "crimson", font=("EB Garamond", 24))
        civil_response.pack()
       

        global subfields
        subfields = Button(root, text = "NEXT", height = 5, width = 8, command = clickcoastaleng)
        subfields.pack()
      civilwin()
    else:
      global question8
      question8 = Label(root, text="Do/did you enjoy playing around with LEGOS?", bg = 'white', fg = "crimson" , font=("EB Garamond", 24))
      question8.pack(side="top", expand=True)

      global yesbutton8
      yesbutton8 = Button(root, text="", height=2, width=2, bg="red", command=clickyesbutton8)
      yesbutton8.pack(side="top", expand=True)

      global labelyesbutton8
      labelyesbutton8 = Label(root, text = "Yes", bg = "white" , fg = "crimson", font=("EB Garamond", 24) )
      labelyesbutton8.pack(side = "top", expand = True)

      global nobutton8
      nobutton8 = Button(root, text="", height=2, width=2, bg="red", command=clicknobutton8)
      nobutton8.pack(side="top", expand=True)

      global labelnobutton8
      labelnobutton8 = Label(root, text = "No", bg = "white" , fg = "crimson", font=("EB Garamond", 24) )
      labelnobutton8.pack(side = "top", expand = True)

      global notsurebutton8
      notsurebutton8 = Button(root, text="", height=2, width=2, bg="red", command=clicknotsurebutton8)
      notsurebutton8.pack(side="top", expand=True)

      global labelnotsurebutton8
      labelnotsurebutton8 = Label(root, text = "Not Sure", bg = "white" , fg = "crimson" , font=("EB Garamond", 24))
      labelnotsurebutton8.pack(side = "top", expand = True)


  def clicknobutton7():
    global civil
    civil -= 1
    question7.pack_forget()
    yesbutton7.pack_forget()
    nobutton7.pack_forget()
    notsurebutton7.pack_forget()
    labelyesbutton7.pack_forget()
    labelnobutton7.pack_forget()
    labelnotsurebutton7.pack_forget()
    global question8
    question8 = Label(root, text="Do/did you enjoy playing around with LEGOS?", bg = 'white', fg = "crimson" , font=("EB Garamond", 24))
    question8.pack(side="top", expand=True)

    global yesbutton8
    yesbutton8 = Button(root, text="", height=2, width=2, bg="red", command=clickyesbutton8)
    yesbutton8.pack(side="top", expand=True)

    global labelyesbutton8
    labelyesbutton8 = Label(root, text = "Yes", bg = "white" , fg = "crimson", font=("EB Garamond", 24) )
    labelyesbutton8.pack(side = "top", expand = True)

    global nobutton8
    nobutton8 = Button(root, text="", height=2, width=2, bg="red", command=clicknobutton8)
    nobutton8.pack(side="top", expand=True)

    global labelnobutton8
    labelnobutton8 = Label(root, text = "No", bg = "white" , fg = "crimson" , font=("EB Garamond", 24))
    labelnobutton8.pack(side = "top", expand = True)

    global notsurebutton8
    notsurebutton8 = Button(root, text="", height=2, width=2, bg="red", command=clicknotsurebutton8)
    notsurebutton8.pack(side="top", expand=True)

    global labelnotsurebutton8
    labelnotsurebutton8 = Label(root, text = "Not Sure", bg = "white" , fg = "crimson" , font=("EB Garamond", 24))
    labelnotsurebutton8.pack(side = "top", expand = True)


  def clicknotsurebutton7():
    question7.pack_forget()
    yesbutton7.pack_forget()
    nobutton7.pack_forget()
    notsurebutton7.pack_forget()
    labelyesbutton7.pack_forget()
    labelnobutton7.pack_forget()
    labelnotsurebutton7.pack_forget()
    global question8
    question8 = Label(root, text="Do/did you enjoy playing around with LEGOS?", bg = 'white', fg = "crimson", font=("EB Garamond", 24) )
    question8.pack(side="top", expand=True)

    global yesbutton8
    yesbutton8 = Button(root, text="", height=2, width=2, bg="red", command=clickyesbutton8)
    yesbutton8.pack(side="top", expand=True)

    global labelyesbutton8
    labelyesbutton8 = Label(root, text = "Yes", bg = "white" , fg = "crimson" , font=("EB Garamond", 24))
    labelyesbutton8.pack(side = "top", expand = True)

    global nobutton8
    nobutton8 = Button(root, text="", height=2, width=2, bg="red", command=clicknobutton8)
    nobutton8.pack(side="top", expand=True)

    global labelnobutton8
    labelnobutton8 = Label(root, text = "No", bg = "white" , fg = "crimson" , font=("EB Garamond", 24))
    labelnobutton8.pack(side = "top", expand = True)

    global notsurebutton8
    notsurebutton8 = Button(root, text="", height=2, width=2, bg="red", command=clicknotsurebutton8)
    notsurebutton8.pack(side="top", expand=True)

    global labelnotsurebutton8
    labelnotsurebutton8 = Label(root, text = "Not Sure", bg = "white" , fg = "crimson", font=("EB Garamond", 24) )
    labelnotsurebutton8.pack(side = "top", expand = True)










  def clickyesbutton6():
    global electrical
    electrical += 1
    question6.pack_forget()
    yesbutton6.pack_forget()
    nobutton6.pack_forget()
    notsurebutton6.pack_forget()
    labelyesbutton6.pack_forget()
    labelnobutton6.pack_forget()
    labelnotsurebutton6.pack_forget()

    global question7
    question7 = Label(root, text="Are you interested in using \n computer aided design (CAD) in the future?",bg = 'white', fg = "crimson", font=("EB Garamond", 24) )
    question7.pack(side="top", expand=True)

    global yesbutton7
    yesbutton7 = Button(root, text="", height=2, width=2, bg="red", command=clickyesbutton7)
    yesbutton7.pack(side="top", expand=True)

    global labelyesbutton7
    labelyesbutton7 = Label(root, text = "Yes", bg = "white" , fg = "crimson" , font=("EB Garamond", 24))
    labelyesbutton7.pack(side = "top", expand = True)

    global nobutton7
    nobutton7 = Button(root, text="", height=2, width=2, bg="red", command=clicknobutton7)
    nobutton7.pack(side="top", expand=True)

    global labelnobutton7
    labelnobutton7 = Label(root, text = "No", bg = "white" , fg = "crimson", font=("EB Garamond", 24) )
    labelnobutton7.pack(side = "top", expand = True)

    global notsurebutton7
    notsurebutton7 = Button(root, text="", height=2, width=2, bg="red", command=clicknotsurebutton7)
    notsurebutton7.pack(side="top", expand=True)

    global labelnotsurebutton7
    labelnotsurebutton7 = Label(root, text = "Not Sure", bg = "white" , fg = "crimson" , font=("EB Garamond", 24))
    labelnotsurebutton7.pack(side = "top", expand = True)

  def clicknobutton6():
    global electrical
    electrical -= 1
    question6.pack_forget()
    yesbutton6.pack_forget()
    nobutton6.pack_forget()
    notsurebutton6.pack_forget()
    labelyesbutton6.pack_forget()
    labelnobutton6.pack_forget()
    labelnotsurebutton6.pack_forget()

    global question7
    question7 = Label(root, text="Are you interested in using \n computer aided design (CAD) in the future?",bg = 'white', fg = "crimson", font=("EB Garamond", 24) )
    question7.pack(side="top", expand=True)

    global yesbutton7
    yesbutton7 = Button(root, text="", height=2, width=2, bg="red", command=clickyesbutton7)
    yesbutton7.pack(side="top", expand=True)

    global labelyesbutton7
    labelyesbutton7 = Label(root, text = "Yes", bg = "white" , fg = "crimson" , font=("EB Garamond", 24))
    labelyesbutton7.pack(side = "top", expand = True)

    global nobutton7
    nobutton7 = Button(root, text="", height=2, width=2, bg="red", command=clicknobutton7)
    nobutton7.pack(side="top", expand=True)

    global labelnobutton7
    labelnobutton7 = Label(root, text = "No", bg = "white" , fg = "crimson" , font=("EB Garamond", 24))
    labelnobutton7.pack(side = "top", expand = True)

    global notsurebutton7
    notsurebutton7 = Button(root, text="", height=2, width=2, bg="red", command=clicknotsurebutton7)
    notsurebutton7.pack(side="top", expand=True)

    global labelnotsurebutton7
    labelnotsurebutton7 = Label(root, text = "Not Sure", bg = "white" , fg = "crimson", font=("EB Garamond", 24) )
    labelnotsurebutton7.pack(side = "top", expand = True)


  def clicknotsurebutton6():
    question6.pack_forget()
    yesbutton6.pack_forget()
    nobutton6.pack_forget()
    notsurebutton6.pack_forget()
    labelyesbutton6.pack_forget()
    labelnobutton6.pack_forget()
    labelnotsurebutton6.pack_forget()

    global question7
    question7 = Label(root, text="Are you interested in using \n computer aided design (CAD) in the future?",bg = 'white', fg = "crimson", font=("EB Garamond", 24) )
    question7.pack(side="top", expand=True)

    global yesbutton7
    yesbutton7 = Button(root, text="", height=2, width=2, bg="red", command=clickyesbutton7)
    yesbutton7.pack(side="top", expand=True)

    global labelyesbutton7
    labelyesbutton7 = Label(root, text = "Yes", bg = "white" , fg = "crimson", font=("EB Garamond", 24) )
    labelyesbutton7.pack(side = "top", expand = True)

    global nobutton7
    nobutton7 = Button(root, text="", height=2, width=2, bg="red", command=clicknobutton7)
    nobutton7.pack(side="top", expand=True)

    global labelnobutton7
    labelnobutton7 = Label(root, text = "No", bg = "white" , fg = "crimson", font=("EB Garamond", 24) )
    labelnobutton7.pack(side = "top", expand = True)

    global notsurebutton7
    notsurebutton7 = Button(root, text="", height=2, width=2, bg="red", command=clicknotsurebutton7)
    notsurebutton7.pack(side="top", expand=True)

    global labelnotsurebutton7
    labelnotsurebutton7 = Label(root, text = "Not Sure", bg = "white" , fg = "crimson" , font=("EB Garamond", 24))
    labelnotsurebutton7.pack(side = "top", expand = True)




  


  def clickyesbutton5():
    global chemical
    chemical += 1
    question5.pack_forget()
    yesbutton5.pack_forget()
    nobutton5.pack_forget()
    notsurebutton5.pack_forget()
    labelyesbutton5.pack_forget()
    labelnobutton5.pack_forget()
    labelnotsurebutton5.pack_forget()

    global question6
    question6 = Label(root, text="Are you interested in learning more about \n quantum physics and its applications?", bg = "white", fg = "crimson", font=("EB Garamond", 24) )
    question6.pack(side="top", expand=True)

    global yesbutton6
    yesbutton6 = Button(root, text="", height=2, width=2, bg="red", command=clickyesbutton6)
    yesbutton6.pack(side="top", expand=True)

    global labelyesbutton6
    labelyesbutton6 = Label(root, text = "Yes", bg = "white" , fg = "crimson" , font=("EB Garamond", 24))
    labelyesbutton6.pack(side = "top", expand = True)

    global nobutton6
    nobutton6 = Button(root, text="", height=2, width=2, bg="red", command=clicknobutton6)
    nobutton6.pack(side="top", expand=True)

    global labelnobutton6
    labelnobutton6 = Label(root, text = "No", bg = "white" , fg = "crimson" , font=("EB Garamond", 24))
    labelnobutton6.pack(side = "top", expand = True)

    global notsurebutton6
    notsurebutton6 = Button(root, text="", height=2, width=2, bg="red", command=clicknotsurebutton6)
    notsurebutton6.pack(side="top", expand=True)

    global labelnotsurebutton6
    labelnotsurebutton6 = Label(root, text = "Not Sure", bg = "white" , fg = "crimson", font=("EB Garamond", 24) )
    labelnotsurebutton6.pack(side = "top", expand = True)

  def clicknobutton5():
    global chemical
    chemical -= 1
    question5.pack_forget()
    yesbutton5.pack_forget()
    nobutton5.pack_forget()
    notsurebutton5.pack_forget()
    labelyesbutton5.pack_forget()
    labelnobutton5.pack_forget()
    labelnotsurebutton5.pack_forget()

    global question6
    question6 = Label(root, text="Are you interested in learning more about \n quantum physics and its applications?", bg="white", fg = "crimson", font=("EB Garamond", 24) )
    question6.pack(side="top", expand=True)

    global yesbutton6
    yesbutton6 = Button(root, text="", height=2, width=2, bg="red", command=clickyesbutton6)
    yesbutton6.pack(side="top", expand=True)

    global labelyesbutton6
    labelyesbutton6 = Label(root, text = "Yes", bg = "white", fg = "crimson" , font=("EB Garamond", 24) )
    labelyesbutton6.pack(side = "top", expand = True)

    global nobutton6
    nobutton6 = Button(root, text="", height=2, width=2, bg="red", command=clicknobutton6)
    nobutton6.pack(side="top", expand=True)

    global labelnobutton6
    labelnobutton6 = Label(root, text = "No", bg = "white" , fg = "crimson", font=("EB Garamond", 24) )
    labelnobutton6.pack(side = "top", expand = True)

    global notsurebutton6
    notsurebutton6 = Button(root, text="", height=2, width=2, bg="red", command=clicknotsurebutton6)
    notsurebutton6.pack(side="top", expand=True)

    global labelnotsurebutton6
    labelnotsurebutton6 = Label(root, text = "Not Sure", bg = "white" , fg = "crimson", font=("EB Garamond", 24) )
    labelnotsurebutton6.pack(side = "top", expand = True)


  def clicknotsurebutton5():
    question5.pack_forget()
    yesbutton5.pack_forget()
    nobutton5.pack_forget()
    notsurebutton5.pack_forget()
    labelyesbutton5.pack_forget()
    labelnobutton5.pack_forget()
    labelnotsurebutton5.pack_forget()

    global question6
    question6 = Label(root, text="Are you interested in learning more about \n quantum physics and its applications?", bg="white", fg = "crimson", font=("EB Garamond", 24) )
    question6.pack(side="top", expand=True)

    global yesbutton6
    yesbutton6 = Button(root, text="", height=2, width=2, bg="red", command=clickyesbutton6)
    yesbutton6.pack(side="top", expand=True)

    global labelyesbutton6
    labelyesbutton6 = Label(root, text = "Yes", bg = "white" , fg = "crimson" , font=("EB Garamond", 24))
    labelyesbutton6.pack(side = "top", expand = True)

    global nobutton6
    nobutton6 = Button(root, text="", height=2, width=2, bg="red", command=clicknobutton6)
    nobutton6.pack(side="top", expand=True)

    global labelnobutton6
    labelnobutton6 = Label(root, text = "No", bg = "white" , fg = "crimson" , font=("EB Garamond", 24))
    labelnobutton6.pack(side = "top", expand = True)

    global notsurebutton6
    notsurebutton6 = Button(root, text="", height=2, width=2, bg="red", command=clicknotsurebutton6)
    notsurebutton6.pack(side="top", expand=True)

    global labelnotsurebutton6
    labelnotsurebutton6 = Label(root, text = "Not Sure", bg = "white" , fg = "crimson", font=("EB Garamond", 24) )
    labelnotsurebutton6.pack(side = "top", expand = True)







  def clickyesbutton4():
    global civil
    civil += 1
    question4.pack_forget()
    yesbutton4.pack_forget()
    nobutton4.pack_forget()
    notsurebutton4.pack_forget()
    labelyesbutton4.pack_forget()
    labelnobutton4.pack_forget()
    labelnotsurebutton4.pack_forget()

    global question5
    question5 = Label(root, text="Do you like biology and chemistry?", bg = "white", fg = "crimson" , font=("EB Garamond", 24))
    question5.pack(side="top", expand=True)

    global yesbutton5
    yesbutton5 = Button(root, text="", height=2, width=2, bg="red", command=clickyesbutton5)
    yesbutton5.pack(side="top", expand=True)

    global labelyesbutton5
    labelyesbutton5 = Label(root, text = "Yes", bg = "white" , fg = "crimson" , font=("EB Garamond", 24))
    labelyesbutton5.pack(side = "top", expand = True)

    global nobutton5
    nobutton5 = Button(root, text="", height=2, width=2, bg="red", command=clicknobutton5)
    nobutton5.pack(side="top", expand=True)

    global labelnobutton5
    labelnobutton5 = Label(root, text = "No", bg = "white" , fg = "crimson" , font=("EB Garamond", 24))
    labelnobutton5.pack(side = "top", expand = True)

    global notsurebutton5
    notsurebutton5 = Button(root, text="", height=2, width=2, bg="red", command=clicknotsurebutton5)
    notsurebutton5.pack(side="top", expand=True)

    global labelnotsurebutton5
    labelnotsurebutton5 = Label(root, text = "Not Sure", bg = "white" , fg = "crimson" , font=("EB Garamond", 24))
    labelnotsurebutton5.pack(side = "top", expand = True)

  def clicknobutton4():
    global civil
    civil -= 1
    question4.pack_forget()
    yesbutton4.pack_forget()
    nobutton4.pack_forget()
    notsurebutton4.pack_forget()
    labelyesbutton4.pack_forget()
    labelnobutton4.pack_forget()
    labelnotsurebutton4.pack_forget()

    global question5
    question5 = Label(root, text="Do you like biology and chemistry?", bg="white", fg = "crimson", font=("EB Garamond", 24))
    question5.pack(side="top", expand=True)

    global yesbutton5
    yesbutton5 = Button(root, text="", height=2, width=2, bg="red", command=clickyesbutton5)
    yesbutton5.pack(side="top", expand=True)

    global labelyesbutton5
    labelyesbutton5 = Label(root, text = "Yes", bg = "white" , fg = "crimson", font=("EB Garamond", 24) )
    labelyesbutton5.pack(side = "top", expand = True)

    global nobutton5
    nobutton5 = Button(root, text="", height=2, width=2, bg="red", command=clicknobutton5)
    nobutton5.pack(side="top", expand=True)

    global labelnobutton5
    labelnobutton5 = Label(root, text = "No", bg = "white" , fg = "crimson" , font=("EB Garamond", 24))
    labelnobutton5.pack(side = "top", expand = True)

    global notsurebutton5
    notsurebutton5 = Button(root, text="", height=2, width=2, bg="red", command=clicknotsurebutton5)
    notsurebutton5.pack(side="top", expand=True)

    global labelnotsurebutton5
    labelnotsurebutton5 = Label(root, text = "Not Sure", bg = "white" , fg = "crimson", font=("EB Garamond", 24) )
    labelnotsurebutton5.pack(side = "top", expand = True)

  def clicknotsurebutton4():
    question4.pack_forget()
    yesbutton4.pack_forget()
    nobutton4.pack_forget()
    notsurebutton4.pack_forget()
    labelyesbutton4.pack_forget()
    labelnobutton4.pack_forget()
    labelnotsurebutton4.pack_forget()

    global question5
    question5 = Label(root, text="Do you like biology and chemistry?", bg="white", fg = "crimson", font=("EB Garamond", 24))
    question5.pack(side="top", expand=True)

    global yesbutton5
    yesbutton5 = Button(root, text="", height=2, width=2, bg="red", command=clickyesbutton5)
    yesbutton5.pack(side="top", expand=True)

    global labelyesbutton5
    labelyesbutton5 = Label(root, text = "Yes", bg = "white" , fg = "crimson", font=("EB Garamond", 24) )
    labelyesbutton5.pack(side = "top", expand = True)

    global nobutton5
    nobutton5 = Button(root, text="", height=2, width=2, bg="red", command=clicknobutton5)
    nobutton5.pack(side="top", expand=True)

    global labelnobutton5
    labelnobutton5 = Label(root, text = "No", bg = "white" , fg = "crimson" , font=("EB Garamond", 24))
    labelnobutton5.pack(side = "top", expand = True)

    global notsurebutton5
    notsurebutton5 = Button(root, text="", height=2, width=2, bg="red", command=clicknotsurebutton5)
    notsurebutton5.pack(side="top", expand=True)

    global labelnotsurebutton5
    labelnotsurebutton5 = Label(root, text = "Not Sure", bg = "white" , fg = "crimson" , font=("EB Garamond", 24))
    labelnotsurebutton5.pack(side = "top", expand = True)








  def clickq3aanswer1():
    global electrical
    electrical += 1
    question3a.pack_forget()
    q3aanswer1.pack_forget()
    q3aanswer2.pack_forget()
    q3aanswer3.pack_forget()
    labelq3aanswer1.pack_forget()
    labelq3aanswer2.pack_forget()
    labelq3aanswer3.pack_forget()

    global question4
    question4 = Label(root, text="Are you interested in working \n to maintain infrastructure like bridges, \n roads, water systems and sea ports?", bg="white", fg = "crimson", font=("EB Garamond", 24))
    question4.pack(side="top", expand=True)

    global yesbutton4
    yesbutton4 = Button(root, text="", height=2, width=2, bg="red", command=clickyesbutton4)
    yesbutton4.pack(side="top", expand=True)

    global labelyesbutton4
    labelyesbutton4 = Label(root, text = "Yes", bg = "white" , fg = "crimson" , font=("EB Garamond", 24))
    labelyesbutton4.pack(side = "top", expand = True)

    global nobutton4
    nobutton4 = Button(root, text="", height=2, width=2, bg="red", command=clicknobutton4)
    nobutton4.pack(side="top", expand=True)

    global labelnobutton4
    labelnobutton4 = Label(root, text = "No", bg = "white" , fg = "crimson" , font=("EB Garamond", 24))
    labelnobutton4.pack(side = "top", expand = True)

    global notsurebutton4
    notsurebutton4 = Button(root, text="", height=2, width=2, bg="red", command=clicknotsurebutton4)
    notsurebutton4.pack(side="top", expand=True)

    global labelnotsurebutton4
    labelnotsurebutton4 = Label(root, text = "Not Sure", bg = "white" , fg = "crimson" , font=("EB Garamond", 24))
    labelnotsurebutton4.pack(side = "top", expand = True)

  def clickq3aanswer2():
    global civil
    civil += 1
    question3a.pack_forget()
    q3aanswer1.pack_forget()
    q3aanswer2.pack_forget()
    q3aanswer3.pack_forget()
    labelq3aanswer1.pack_forget()
    labelq3aanswer2.pack_forget()
    labelq3aanswer3.pack_forget()

    global question4
    question4 = Label(root, text="Are you interested in working \n to maintain infrastructure like bridges, \n roads, water systems and sea ports?", bg = "white" , fg = "crimson", font=("EB Garamond", 24) )
    question4.pack(side="top", expand=True)

    global yesbutton4
    yesbutton4 = Button(root, text="", height=2, width=2, bg="red", command=clickyesbutton4)
    yesbutton4.pack(side="top", expand=True)

    global labelyesbutton4
    labelyesbutton4 = Label(root, text = "Yes", bg = "white" , fg = "crimson" , font=("EB Garamond", 24))
    labelyesbutton4.pack(side = "top", expand = True)

    global nobutton4
    nobutton4 = Button(root, text="", height=2, width=2, bg="red", command=clicknobutton4)
    nobutton4.pack(side="top", expand=True)

    global labelnobutton4
    labelnobutton4 = Label(root, text = "No", bg = "white" , fg = "crimson", font=("EB Garamond", 24) )
    labelnobutton4.pack(side = "top", expand = True)

    global notsurebutton4
    notsurebutton4 = Button(root, text="", height=2, width=2, bg="red", command=clicknotsurebutton4)
    notsurebutton4.pack(side="top", expand=True)

    global labelnotsurebutton4
    labelnotsurebutton4 = Label(root, text = "Not Sure", bg = "white" , fg = "crimson" , font=("EB Garamond", 24))
    labelnotsurebutton4.pack(side = "top", expand = True)


  def clickq3aanswer3():
    global mechanical
    mechanical += 1
    question3a.pack_forget()
    q3aanswer1.pack_forget()
    q3aanswer2.pack_forget()
    q3aanswer3.pack_forget()
    labelq3aanswer1.pack_forget()
    labelq3aanswer2.pack_forget()
    labelq3aanswer3.pack_forget()

    global question4
    question4 = Label(root, text="Are you interested in working \n to maintain infrastructure like bridges, \n roads, water systems and sea ports?", bg="white", fg  = "crimson", font=("EB Garamond", 24))
    question4.pack(side="top", expand=True)

    global yesbutton4
    yesbutton4 = Button(root, text="", height=2, width=2, bg="red", command=clickyesbutton4)
    yesbutton4.pack(side="top", expand=True)

    global labelyesbutton4
    labelyesbutton4 = Label(root, text = "Yes", bg = "white" , fg= "crimson" , font=("EB Garamond", 24))
    labelyesbutton4.pack(side = "top", expand = True)

    global nobutton4
    nobutton4 = Button(root, text="", height=2, width=2, bg="red", command=clicknobutton4)
    nobutton4.pack(side="top", expand=True)

    global labelnobutton4
    labelnobutton4 = Label(root, text = "No", bg = "white" , fg= "crimson", font=("EB Garamond", 24) )
    labelnobutton4.pack(side = "top", expand = True)

    global notsurebutton4
    notsurebutton4 = Button(root, text="", height=2, width=2, bg="red", command=clicknotsurebutton4)
    notsurebutton4.pack(side="top", expand=True)

    global labelnotsurebutton4
    labelnotsurebutton4 = Label(root, text = "Not Sure", bg = "white", fg= "crimson" , font=("EB Garamond", 24) )
    labelnotsurebutton4.pack(side = "top", expand = True)
    






  def clickyesbutton3():
    global civil
    civil += 1
    question3.pack_forget()
    yesbutton3.pack_forget()
    nobutton3.pack_forget()
    notsurebutton3.pack_forget()
    labelyesbutton3.pack_forget()
    labelnobutton3.pack_forget()
    labelnotsurebutton3.pack_forget()

    global question3a
    question3a = Label(root, text="You are put in a room \n and asked to fix a robot.\n What do you do first?", bg="white", fg = "crimson", font=("EB Garamond", 24))
    question3a.pack(side="top", expand=True)

    global q3aanswer1
    q3aanswer1 = Button(root, text="", height=2, width=2, bg="red",command=clickq3aanswer1)
    q3aanswer1.pack(side="top", expand=True)

    global labelq3aanswer1
    labelq3aanswer1 = Label(root, text = "Toy with the wires and \n start coding", bg = "white", fg = "crimson", font=("EB Garamond", 24))
    labelq3aanswer1.pack(side = "top", expand = True)

    global q3aanswer2
    q3aanswer2 = Button(root, text="", height=2, width=2, bg="red",command=clickq3aanswer2)
    q3aanswer2.pack(side="top", expand=True)

    global labelq3aanswer2
    labelq3aanswer2 = Label(root, text = "Get tools and sketch \n a blueprint of the bot", bg = "white", fg = "crimson", font=("EB Garamond", 24))
    labelq3aanswer2.pack(side = "top", expand = True)

    global q3aanswer3
    q3aanswer3 = Button(root, text="", height=2, width=2, bg="red",command=clickq3aanswer3)
    q3aanswer3.pack(side="top", expand=True)

    global labelq3aanswer3
    labelq3aanswer3 = Label(root, text = "Figure out how the \n robot parts move", bg = "white", fg = "crimson", font=("EB Garamond", 24))
    labelq3aanswer3.pack(side = "top", expand = True)

  def clicknobutton3():
    global civil
    civil -= 1
    question3.pack_forget()
    yesbutton3.pack_forget()
    nobutton3.pack_forget()
    notsurebutton3.pack_forget()
    labelyesbutton3.pack_forget()
    labelnobutton3.pack_forget()
    labelnotsurebutton3.pack_forget()

    global question3a
    question3a = Label(root, text="You are put in a room \n and asked to fix a robot.\n What do you do first?", bg="white", fg = "crimson", font=("EB Garamond", 24))
    question3a.pack(side="top", expand=True)

    global q3aanswer1
    q3aanswer1 = Button(root, text="", height=2, width=2, bg="red",command=clickq3aanswer1)
    q3aanswer1.pack(side="top", expand=True)

    global labelq3aanswer1
    labelq3aanswer1 = Label(root, text = "Toy with the wires and \n start coding", bg = "white", fg = "crimson", font=("EB Garamond", 24))
    labelq3aanswer1.pack(side = "top", expand = True)

    global q3aanswer2
    q3aanswer2 = Button(root, text="", height=2, width=2, bg="red",command=clickq3aanswer2)
    q3aanswer2.pack(side="top", expand=True)

    global labelq3aanswer2
    labelq3aanswer2 = Label(root, text = "Get tools and sketch \n a blueprint of the bot", bg = "white", fg = "crimson", font=("EB Garamond", 24))
    labelq3aanswer2.pack(side = "top", expand = True)

    global q3aanswer3
    q3aanswer3 = Button(root, text="", height=2, width=2, bg="red",command=clickq3aanswer3)
    q3aanswer3.pack(side="top", expand=True)

    global labelq3aanswer3
    labelq3aanswer3 = Label(root, text = "Figure out how the \n robot parts move", bg = "white", fg = "crimson", font=("EB Garamond", 24))
    labelq3aanswer3.pack(side = "top", expand = True)

  def clicknotsurebutton3():
    question3.pack_forget()
    yesbutton3.pack_forget()
    nobutton3.pack_forget()
    notsurebutton3.pack_forget()
    labelyesbutton3.pack_forget()
    labelnobutton3.pack_forget()
    labelnotsurebutton3.pack_forget()

    global question3a
    question3a = Label(root, text="You are put in a room \n and asked to fix a robot.\n What do you do first?", bg="white", fg = "crimson", font=("EB Garamond", 24))
    question3a.pack(side="top", expand=True)

    global q3aanswer1
    q3aanswer1 = Button(root, text="", height=2, width=2, bg="red",command=clickq3aanswer1)
    q3aanswer1.pack(side="top", expand=True)

    global labelq3aanswer1
    labelq3aanswer1 = Label(root, text = "Toy with the wires and \n start coding", bg = "white", fg = "crimson", font=("EB Garamond", 24))
    labelq3aanswer1.pack(side = "top", expand = True)

    global q3aanswer2
    q3aanswer2 = Button(root, text="", height=2, width=2, bg="red",command=clickq3aanswer2)
    q3aanswer2.pack(side="top", expand=True)

    global labelq3aanswer2
    labelq3aanswer2 = Label(root, text = "Get tools and sketch \n a blueprint of the bot", bg = "white", fg = "crimson", font=("EB Garamond", 24))
    labelq3aanswer2.pack(side = "top", expand = True)

    global q3aanswer3
    q3aanswer3 = Button(root, text="", height=2, width=2, bg="red",command=clickq3aanswer3)
    q3aanswer3.pack(side="top", expand=True)

    global labelq3aanswer3
    labelq3aanswer3 = Label(root, text = "Figure out how the \n robot parts move", bg = "white", fg = "crimson", font=("EB Garamond", 24))
    labelq3aanswer3.pack(side = "top", expand = True)






  def clickyesbutton2():
    global electrical
    electrical += 1
    question2.pack_forget()
    yesbutton2.pack_forget()
    nobutton2.pack_forget()
    notsurebutton2.pack_forget()
    labelyesbutton2.pack_forget()
    labelnobutton2.pack_forget()
    labelnotsurebutton2.pack_forget()

    global question3
    question3 = Label(root, text=" Are you interested in designing \n buildings and other infrastructure?",bg="white", fg = "crimson", font=("EB Garamond", 24))
    question3.pack(side="top", expand=True)

    global yesbutton3
    yesbutton3 = Button(root, text="", height=2, width=2, bg="red", command=clickyesbutton3)
    yesbutton3.pack(side="top", expand=True)

    global labelyesbutton3
    labelyesbutton3 = Label(root, text = "Yes", bg = "white", fg = "crimson" , font=("EB Garamond", 24))
    labelyesbutton3.pack(side = "top", expand = True)

    global nobutton3
    nobutton3 = Button(root, text="", height=2, width=2, bg="red", command=clicknobutton3)
    nobutton3.pack(side="top", expand=True)

    global labelnobutton3
    labelnobutton3 = Label(root, text = "No", bg = "white", fg = "crimson" , font=("EB Garamond", 24))
    labelnobutton3.pack(side = "top", expand = True)

    global notsurebutton3
    notsurebutton3 = Button(root, text="", height=2, width=2, bg="red", command=clicknotsurebutton3)
    notsurebutton3.pack(side="top", expand=True)

    global labelnotsurebutton3
    labelnotsurebutton3 = Label(root, text = "Not Sure", bg = "white", fg = "crimson", font=("EB Garamond", 24) )
    labelnotsurebutton3.pack(side = "top", expand = True)


  def clicknobutton2():
    global electrical
    electrical -=1
    question2.pack_forget()
    yesbutton2.pack_forget()
    nobutton2.pack_forget()
    notsurebutton2.pack_forget()
    labelyesbutton2.pack_forget()
    labelnobutton2.pack_forget()
    labelnotsurebutton2.pack_forget()

    global question3
    question3 = Label(root, text=" Are you interested in designing \n buildings and other infrastructure?",bg="white", fg = "crimson", font=("EB Garamond", 24))
    question3.pack(side="top", expand=True)

    global yesbutton3
    yesbutton3 = Button(root, text="", height=2, width=2, bg="red", command=clickyesbutton3)
    yesbutton3.pack(side="top", expand=True)

    global labelyesbutton3
    labelyesbutton3 = Label(root, text = "Yes", bg = "white", fg = "crimson" , font=("EB Garamond", 24))
    labelyesbutton3.pack(side = "top", expand = True)

    global nobutton3
    nobutton3 = Button(root, text="", height=2, width=2, bg="red", command=clicknobutton3)
    nobutton3.pack(side="top", expand=True)

    global labelnobutton3
    labelnobutton3 = Label(root, text = "No", bg = "white", fg = "crimson", font=("EB Garamond", 24) )
    labelnobutton3.pack(side = "top", expand = True)

    global notsurebutton3
    notsurebutton3 = Button(root, text="", height=2, width=2, bg="red", command=clicknotsurebutton3)
    notsurebutton3.pack(side="top", expand=True)

    global labelnotsurebutton3
    labelnotsurebutton3 = Label(root, text = "Not Sure", bg = "white" , fg = "crimson", font=("EB Garamond", 24))
    labelnotsurebutton3.pack(side = "top", expand = True)


  def clicknotsurebutton2():
    question2.pack_forget()
    yesbutton2.pack_forget()
    nobutton2.pack_forget()
    notsurebutton2.pack_forget()
    labelyesbutton2.pack_forget()
    labelnobutton2.pack_forget()
    labelnotsurebutton2.pack_forget()

    global question3
    question3 = Label(root, text=" Are you interested in designing \n buildings and other infrastructure?",bg="white", fg = "crimson", font=("EB Garamond", 24))
    question3.pack(side="top", expand=True)

    global yesbutton3
    yesbutton3 = Button(root, text="", height=2, width=2, bg="red", command=clickyesbutton3)
    yesbutton3.pack(side="top", expand=True)

    global labelyesbutton3
    labelyesbutton3 = Label(root, text = "Yes", bg = "white", fg = "crimson", font=("EB Garamond", 24) )
    labelyesbutton3.pack(side = "top", expand = True)

    global nobutton3
    nobutton3 = Button(root, text="", height=2, width=2, bg="red", command=clicknobutton3)
    nobutton3.pack(side="top", expand=True)

    global labelnobutton3
    labelnobutton3 = Label(root, text = "No", bg = "white", fg = "crimson", font=("EB Garamond", 24) )
    labelnobutton3.pack(side = "top", expand = True)

    global notsurebutton3
    notsurebutton3 = Button(root, text="", height=2, width=2, bg="red", command=clicknotsurebutton3)
    notsurebutton3.pack(side="top", expand=True)

    global labelnotsurebutton3
    labelnotsurebutton3 = Label(root, text = "Not Sure", bg = "white", fg = "crimson", font=("EB Garamond", 24) )
    labelnotsurebutton3.pack(side = "top", expand = True)







  

  def clickyesbutton1():
    global mechanical
    mechanical += 1
    question1.pack_forget()
    yesbutton1.pack_forget()
    nobutton1.pack_forget()
    notsurebutton1.pack_forget()
    labelyesbutton1.pack_forget()
    labelnobutton1.pack_forget()
    labelnotsurebutton1.pack_forget()

    global question2
    question2 = Label(root, text="Would you like working with \n electrical devices and systems?", bg="white", fg = "crimson", font=("EB Garamond", 24))
    question2.pack(side="top")

    global yesbutton2
    yesbutton2 = Button(root, text="", height=2, width=2, bg="red", command=clickyesbutton2)
    yesbutton2.pack(side="top", expand=True)

    global labelyesbutton2
    labelyesbutton2 = Label(root, text = "Yes", bg = "white", fg = "crimson" , font=("EB Garamond", 24))
    labelyesbutton2.pack(side = "top", expand = True)

    global nobutton2
    nobutton2 = Button(root, text="", height=2, width=2, bg="red", command=clicknobutton2)
    nobutton2.pack(side="top", expand=True)

    global labelnobutton2
    labelnobutton2 = Label(root, text = "No", bg = "white", fg = "crimson", font=("EB Garamond", 24) )
    labelnobutton2.pack(side = "top", expand = True)

    global notsurebutton2
    notsurebutton2 = Button(root, text="", height=2, width=2, bg="red", command=clicknotsurebutton2)
    notsurebutton2.pack(side="top", expand=True)

    global labelnotsurebutton2
    labelnotsurebutton2 = Label(root, text = "Not Sure", bg = "white", fg = "crimson", font=("EB Garamond", 24) )
    labelnotsurebutton2.pack(side = "top", expand = True)


  def clicknobutton1():
    global mechanical
    mechanical -= 1
    question1.pack_forget()
    yesbutton1.pack_forget()
    nobutton1.pack_forget()
    notsurebutton1.pack_forget()
    labelyesbutton1.pack_forget()
    labelnobutton1.pack_forget()
    labelnotsurebutton1.pack_forget()

    global question2
    question2 = Label(root, text="Would you like working with \n electrical devices and systems?", bg="white", fg = "crimson",font=("EB Garamond", 24))
    question2.pack(side="top")

    global yesbutton2
    yesbutton2 = Button(root, text="", height=2, width=2, bg="red", command=clickyesbutton2)
    yesbutton2.pack(side="top", expand=True)

    global labelyesbutton2
    labelyesbutton2 = Label(root, text = "Yes", bg = "white", fg = "crimson",font=("EB Garamond", 24) )
    labelyesbutton2.pack(side = "top", expand = True)

    global nobutton2
    nobutton2 = Button(root, text="", height=2, width=2, bg="red", command=clicknobutton2)
    nobutton2.pack(side="top", expand=True)

    global labelnobutton2
    labelnobutton2 = Label(root, text = "No", bg = "white", fg = "crimson",font=("EB Garamond", 24) )
    labelnobutton2.pack(side = "top", expand = True)

    global notsurebutton2
    notsurebutton2 = Button(root, text="", height=2, width=2, bg="red", command=clicknotsurebutton2)
    notsurebutton2.pack(side="top", expand=True)

    global labelnotsurebutton2
    labelnotsurebutton2 = Label(root, text = "Not Sure", bg = "white", fg = "crimson",font=("EB Garamond", 24))
    labelnotsurebutton2.pack(side = "top", expand = True)


  def clicknotsurebutton1():
    question1.pack_forget()
    yesbutton1.pack_forget()
    nobutton1.pack_forget()
    notsurebutton1.pack_forget()
    labelyesbutton1.pack_forget()
    labelnobutton1.pack_forget()
    labelnotsurebutton1.pack_forget()

    global question2
    question2 = Label(root, text="Would you like working with \n electrical devices and systems?", bg="white", fg = "crimson", font=("EB Garamond", 24))
    question2.pack(side="top")

    global yesbutton2
    yesbutton2 = Button(root, text="", height=2, width=2, bg="red", command=clickyesbutton2)
    yesbutton2.pack(side="top", expand=True)

    global labelyesbutton2
    labelyesbutton2 = Label(root, text = "Yes", bg = "white", fg = "crimson" , font=("EB Garamond", 24))
    labelyesbutton2.pack(side = "top", expand = True)

    global nobutton2
    nobutton2 = Button(root, text="", height=2, width=2, bg="red", command=clicknobutton2)
    nobutton2.pack(side="top", expand=True)

    global labelnobutton2
    labelnobutton2 = Label(root, text = "No", bg = "white", fg = "crimson", font=("EB Garamond", 24))
    labelnobutton2.pack(side = "top", expand = True)

    global notsurebutton2
    notsurebutton2 = Button(root, text="", height=2, width=2, bg="red", command=clicknotsurebutton2)
    notsurebutton2.pack(side="top", expand=True)

    global labelnotsurebutton2
    labelnotsurebutton2 = Label(root, text = "Not Sure", bg = "white", fg = "crimson", font=("EB Garamond", 24) )
    labelnotsurebutton2.pack(side = "top", expand = True)











  def clickmyButton():
    global question1
    question1 = Label(root, text="Would you like to apply physics and math in order to \n design/manufacture a mechanical system?" ,bg='white', fg = "crimson", font=("EB Garamond", 24))
    question1.pack(side="top")

    global yesbutton1
    yesbutton1 = Button(root, text="", height=2, width=2, bg="red", command=clickyesbutton1)
    yesbutton1.pack(side="top", expand=True)

    global labelyesbutton1
    labelyesbutton1 = Label(root, text = "Yes", bg = "white", fg = "crimson", font=("EB Garamond", 24) )
    labelyesbutton1.pack(side = "top", expand = True)

    global nobutton1
    nobutton1 = Button(root, text="", height=2, width=2, bg="red", command=clicknobutton1)
    nobutton1.pack(side="top", expand=True)

    global labelnobutton1
    labelnobutton1 = Label(root, text = "No", bg = "white", fg = "crimson", font=("EB Garamond", 24) )
    labelnobutton1.pack(side = "top", expand = True)

    global notsurebutton1
    notsurebutton1 = Button(root, text="", height=2, width=2, bg="red", command=clicknotsurebutton1)
    notsurebutton1.pack(side="top", expand=True)

    global labelnotsurebutton1
    labelnotsurebutton1 = Label(root, text = "Not Sure", bg = "white", fg = "crimson", font=("EB Garamond", 24) )
    labelnotsurebutton1.pack(side = "top", expand = True)

    myLabel.pack_forget()
    myButton.pack_forget()





  myLabel = Label(root, text="Welcome to Engineering Cruising", font=("EB Garamond", 36), fg= "crimson" , bg = "white" )

  myLabel.pack()

  myButton = Button(root, text="Start Quiz", height=2, width=7, fg = 'crimson',  font=("EB Garamond", 18 ),command=clickmyButton)
  myButton.pack()
  

  root.mainloop()







rungame()
