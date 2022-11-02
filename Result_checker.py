#Subjcect details (Replicate the line to add more subject and don't forget to add subject name in every where in the code)
English=int(input("Enter your marks in English: "))
Hindi=int(input("Enter your marks in Hindi: "))
Social_Science=int(input("Enter your marks in Social Science: "))
Math=int(input("Enter your marks in Math: "))
Science=int(input("Enter your marks in Science: "))

#marks checking

if (English<30):
    failed_subject="English"
#Replicate the line to add more subject 
elif(Hindi<30):
    failed_subject="Hindi"
elif(Social_Science<30):
    failed_subject="Social_Science"
elif(Math<30):
    failed_subject="Math"
elif(Science<30):
    failed_subject="Science"

# Result Declaration

# to add more subjcet name type (or + "Subject name")
if(English or Hindi or Social_Science or Math or Hindi)<30:
    print("You are failed in",failed_subject)
# change "500" value to total ouctomes of marks
    print("You're overall percentage is",(English + Hindi + Math + Science +Social_Science)/500*100,"%")
# to add more subjcet name type (or + "Subject name")
elif(English + Hindi + Social_Science + Math + Science )/5<30:
    print("You are failed") 
else:
# to add more subjcet name type (or + "Subject name")
    print("Congratulations you're passed")
    print("You're overall percentage is",(English + Hindi + Math + Science +Social_Science)/500*100,"%")
    

