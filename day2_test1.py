import statistics

x = 1
r = 0
l = 0
s = 0
m = 0
ma = 0
avg = 0.00
student_code = ""
student_name = ""
student_score = 0

student_code_total= ["","","",""]
student_name_total= ["","","",""]
student_score_total= [0,0,0,0]



while x<2:
    print("menu bar ---------------------------------------")
    print("กด A บันทึกข้อมูลนักเรียน")
    print("กด B บันทึกคะแนนนักเรียน")
    print("กด C แสดงคะแนนนักเรียน")
    print("กด Q ปิดโปรแกรม")
    print("------------------------------------------------")
    enter = input("Enter munber for menu : ")

    match enter :


        case "a":
            print("กรอกข้อมูลนักเรียน---------------------------------------")
            student_code = input("กรอกโค้ดนักเรียน : ")
            student_name = input("กรอกชื่อนักเรียน  : ")
            code_confirmA = input("ต้องการ บันทึกหรือไม่ Y/N : ")
            match code_confirmA:
                case "y":
                    if r > 3 :
                        print("ข้อมูลนักเรียนเต็ม !!!")
                        print("  ")
                    else : 
                        print("บันทึกข้อมูลเสร็จสิ้น !!!")
                        print("  ")
                        student_code_total[r] = student_code
                        student_name_total[r] = student_name
                        student_code = ""
                        student_name = ""
                        r += 1
                case "n":
                    print("ยกเลิกเรียบร้อย !!")
                    student_code = ""
                    student_name = ""


        case "b":
            print("กรอกคะเเนนนักเรียน---------------------------------------")
            if s > r-1 :
                print("ข้อมูลคะแนนนักเรียนเต็ม !!!")
                print("  ")
            else :
                student_score = input("กรอกคะแนนนักเรียน : ")
                code_confirmB = input("ต้องการ บันทึกหรือไม่ Y/N : ")
                match code_confirmB:
                    case "y":
                        print("บันทึกข้อมูลเสร็จสิ้น !!!")
                        print("  ")
                        student_score_total[s] = student_score
                        student_score = 0
                        s += 1
                    case "n":
                        print("ยกเลิกเรียบร้อย !!")
                        student_score = 0


        case "c":
            if student_code_total[0] == "" :
                print("ไม่พบชื่อผู้ใช้งาน !!")
                code_confirmC = input("ต้องการออกกด Q : ")
                match code_confirmC:
                    case "q":
                        print("ออกเรียบร้อย !!!")
                        print("  ")
            else :
                print("คะเเนนนักเรียน---------------------------------------")
                while l < 4 :
                    if student_code_total[l] == "":
                        l += 1
                    else :
                        print("รหัส : ",student_code_total[l],"              ชื่อ : ",student_name_total[l],"                คะแนน : ",student_score_total[l])
                        student_score_total = [int(val) for val in student_score_total]
                        m = min(student_score_total)
                        ma = max(student_score_total)
                        avg = statistics.mean(student_score_total)
                        l += 1
                print("--------------------------")
                print("min : ",m)
                print("max : ",ma)
                print("avg : ",avg)

                    
                code_confirmC = input("ต้องการออกกด Q : ")
                match code_confirmC:
                    case "q":
                        print("ออกเรียบร้อย !!!")
                        print("  ")
                        l = 0


        case "q":
            print("ออกโปรแกรมเรียบร้อย !!")
            x = 2

        

                    
