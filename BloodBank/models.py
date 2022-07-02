import mysql.connector as mysql

def getConn():
    return mysql.connect(host='localhost',user='root',password='root',database='bloodbank')

def listOtherRequest(id):
    try:        
        cnn = getConn()
        cr = cnn.cursor()
        query = "select personname,phone,bloodgroup,hospital,city from request where user!={}".format(id)
        cr.execute(query)

        rec = cr.fetchall()
        cnn.close()
        return rec
    except Exception as ex:
        print("List Erorr : ",ex)    
        return []
def listUserRequest(id):
    try:        
        cnn = getConn()
        cr = cnn.cursor()
        query = "select personname,phone,bloodgroup,hospital,city from request where user={}".format(id)
        cr.execute(query)

        rec = cr.fetchall()
        cnn.close()
        return rec
    except Exception as ex:
        print("List Erorr : ",ex)    
        return []

def saveRequest(data,id):
    try:
        name = data.get('name')
        phone = data.get('phone')
        group = data.get('group')
        hospital = data.get('hospital')
        city = data.get('city')

        cnn = getConn()
        cr =  cnn.cursor()

        query = "insert into request(personname,phone,bloodgroup,hospital,city,user) value('{}','{}','{}','{}','{}',{})".format(name,phone,group,hospital,city,id)

        cr.execute(query)
        cnn.commit()
        cnn.close()
        return True
    except Exception as ex:
        print("Request Error : ",ex)    
        return False

def listUser(id):
    try:        
        cnn = getConn()
        cr = cnn.cursor()
        query = "select name,phone,email,bloodgroup from user where userid!={}".format(id)
        cr.execute(query)

        rec = cr.fetchall()
        cnn.close()
        return rec
    except Exception as ex:
        print("List Erorr : ",ex)    
        return []


def loginUser(data):
    try:
        email = data.get('email')
        password = data.get('password')
        cnn = getConn()
        cr = cnn.cursor()
        query = "select userid,name,email from user where email='{}' and password='{}'".format(email,password)
        cr.execute(query)

        rec = cr.fetchone()
        cnn.close()
        return rec
    except Exception as ex:
        print("Login Erorr : ",ex)    
        return None

def saveUser(data):
    try:
        name = data.get('name')
        phone = data.get('phone')
        email = data.get('email')
        password = data.get('password')
        group = data.get('group')

        cnn = getConn()
        cr =  cnn.cursor()

        query = "insert into user(name,phone,email,password,bloodgroup) value('{}','{}','{}','{}','{}')".format(name,phone,email,password,group)

        cr.execute(query)
        cnn.commit()
        cnn.close()
        return True
    except Exception as ex:
        print("Reg Error : ",ex)    
        return False
