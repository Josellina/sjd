# A simple Y/N validation function
# q_text = Question text
# question = 'Are we learning any python yet'


def get_answer (question):
    gotanswer = False
    while gotanswer == False:
        x = str(input(question + '? [Y/N]: ')).upper()
        if x == 'Y':
            return True
            gotanswer = True
           
        if x == 'N':
            return False
            gotanswer = True

        
           
  


# Ask question and define result
if get_answer('Are we learning any python yet'):
    print('Yes')
else:
    print('No')

