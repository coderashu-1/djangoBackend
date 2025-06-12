
import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    port=3306,
    password="Password",
    database="fx"
)
cursor = con.cursor()



queryLoginTable = '''CREATE TABLE IF NOT EXISTS login_id_cred (
    id INT AUTO_INCREMENT PRIMARY KEY,
    login_id TEXT COLLATE utf8mb4_bin,
    login_password TEXT COLLATE utf8mb4_bin,
    login_type TEXT COLLATE utf8mb4_bin
    )'''

# cursor.execute(queryLoginTable)
# con.commit()

# q1 = '''insert into login_id_cred(login_id, login_password, login_type) values('admin', 'admin123', 'admin')'''
# cursor.execute(q1)
# con.commit()

exportRegister = '''CREATE TABLE IF NOT EXISTS export_register (
    id INT AUTO_INCREMENT PRIMARY KEY,
    month_year TEXT COLLATE utf8mb4_bin,
    exposure_type TEXT COLLATE utf8mb4_bin,
    exposure_input_date TEXT COLLATE utf8mb4_bin,
    po_date TEXT COLLATE utf8mb4_bin,
    bl_date TEXT COLLATE utf8mb4_bin,
    collection_date TEXT COLLATE utf8mb4_bin,
    amount TEXT COLLATE utf8mb4_bin,
    adjustment_amount TEXT COLLATE utf8mb4_bin,
    currency TEXT COLLATE utf8mb4_bin,
    budget_rate TEXT COLLATE utf8mb4_bin,
    hedged_amount TEXT COLLATE utf8mb4_bin,
    invoice_no TEXT COLLATE utf8mb4_bin,
    po_no TEXT COLLATE utf8mb4_bin,
    party_name TEXT COLLATE utf8mb4_bin,
    bank TEXT COLLATE utf8mb4_bin,
    payment_terms TEXT COLLATE utf8mb4_bin,
    forward_contract_no TEXT COLLATE utf8mb4_bin,
    priority TEXT COLLATE utf8mb4_bin,
    booked_forward_rate TEXT COLLATE utf8mb4_bin,
    remark TEXT COLLATE utf8mb4_bin,
    cretated_date_time TEXT COLLATE utf8mb4_bin

)'''
# cursor.execute(exportRegister)
# con.commit()

# deleteq = '''drop table export_register'''
# cursor.execute(deleteq)
# con.commit()


importRegister = '''CREATE TABLE IF NOT EXISTS import_register (
        id INT AUTO_INCREMENT PRIMARY KEY,
        month_year TEXT COLLATE utf8mb4_bin,
        budget_rate TEXT COLLATE utf8mb4_bin,
        exposure_type TEXT COLLATE utf8mb4_bin,
        exposure_input_date TEXT COLLATE utf8mb4_bin,
        po_date TEXT COLLATE utf8mb4_bin,
        bl_date TEXT COLLATE utf8mb4_bin,
        due_date TEXT COLLATE utf8mb4_bin,
        collection_date TEXT COLLATE utf8mb4_bin,
        amount TEXT COLLATE utf8mb4_bin,
        currency TEXT COLLATE utf8mb4_bin,
        hedged_amount TEXT COLLATE utf8mb4_bin,
        po_no TEXT COLLATE utf8mb4_bin,
        party_name TEXT COLLATE utf8mb4_bin,
        payment_terms TEXT COLLATE utf8mb4_bin,
        booked_forward_rate TEXT COLLATE utf8mb4_bin,
        bank TEXT COLLATE utf8mb4_bin,
        forward_contract_no TEXT COLLATE utf8mb4_bin,
        invoice_no TEXT COLLATE utf8mb4_bin,
        priority TEXT COLLATE utf8mb4_bin,
        cretated_date_time TEXT COLLATE utf8mb4_bin
)'''
cursor.execute(importRegister)
con.commit()
