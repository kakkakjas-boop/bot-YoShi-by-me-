while True:
    message = input("คุณ: ")

    if message == "เป็นเหี้ยไร":
        print("บอท: แล้วมึงเสือกไรล่ะ ควย")

    elif message == "มึงตัวๆกับกูไหมล่ะ":
        print("บอท: มึงก็มาสิวะ กูกลัวที่ไหน")

    elif message == "กูไปล่ะ":
        print("บอท: เรื่องของมึง")
        break
    if "กูเกลียดมึง" in message:
        print("บอท: กูชอบมึงมากมั้ง")

    elif "ชื่อ" in message:
        print("บอท: มึงเสือกไร")

    elif "อายุ" in message:
        print("บอท: กูมีอายุที่ไหน ไอควาย กู Ai")

    elif "ห้าว เด๊่ยวได้โดนตีน" in message:
        print("บอท: โง่ กูกินได่หรอ ไอสัส ควายจริงๆมึงเนี่ย")

    elif "สวัสดี" in message:
        print("บอท: มีควยไร")


    else:
        print("บอท: พิมเหี้ยไรมึงเนี่ย?")