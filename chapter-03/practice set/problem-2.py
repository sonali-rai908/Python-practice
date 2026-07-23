# write a program to fill in altter template given below with name and date 
# letter='''
            #  Dear <name>,
            #  you are selected!
            #  <date>
            # '''

letter= '''Dear <name>,
You are selected!
<date>'''

print(letter.replace("<name>","Sonali").replace("<date>","24 September 2024"))