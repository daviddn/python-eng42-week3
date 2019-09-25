## Stupid School Teacher
#Create a program to have a conversation with your teacher. This is how he reacts to your responses
# if you responde to your school teacher:
    # Go back to school!
# if you ask a questions
    # HAHAHA! AHAHAHAHHA!! OMG! WHAT a silly question! Go back TO SCHOOL!
# if your respond with something ending with !
    # YES! YESS! I WANT YOU TO BE MOTIVATED!! YES!
# if your response is 'I'm a doctor'
    # WELLL DONE! YOU can now talk to me
    # Exits

student_answer = ''

while True:
    student_answer = input('What do you want? ').lower()
    if '?' in student_answer:
        print('HAHAHA! AHAHAHAHHA!! OMG! WHAT a silly question! Go back TO SCHOOL!')
    elif '!' in student_answer:
        print('YES! YESS! I WANT YOU TO BE MOTIVATED!! YES!')
    elif "i'm a doctor" in student_answer:
        print('WELL DONE! YOU can now talk to me!')
        break
    else:
        print('Go back to school!')