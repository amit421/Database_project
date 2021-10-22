import subprocess as sp
import pymysql
import pymysql.cursors
from tabulate import tabulate
from datetime import date
def printRowsAsTable(rows):
    r = []
    r.append(list(rows[0].keys()))
    for row in rows:
        rr = []
        for k in row.keys():
            rr.append(row[k])
        r.append(rr)
    print(tabulate(r, tablefmt="psql", headers="firstrow"))
    print()

def viewCricketers():
    """
    Function to fire an employee
    """
    try:
        inp=input("Enter team: ")
        query="select * from CRICKETER where Team_Id=('%d')"%(int(inp))
        print(query)
        cur.execute(query)
        rows=cur.fetchall()
        printRowsAsTable(rows)
        con.commit()

        # print("Inserted Into Database")
    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print (">>>>>>>>>>>>>", e)
    # print("Not implemented")

def deleteCricketers():
    """
    Function performs one of three jobs
    1. Increases salary
    2. Makes employee a supervisor
    3. Makes employee a manager
    """
    try:
        inp=input("Enter player Id: ")
        query="delete from CRICKETER where Cricketer_Id=('%d')"%(int(inp))
        print(query)
        cur.execute(query)
        # rows=cur.fetchall()
        # printRowsAsTable(rows)
        con.commit()

        # print("Inserted Into Database")
    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print (">>>>>>>>>>>>>", e)


def addANewMatch():
	try:
		row={}
		row[0]=int(input("Enter Match Id: "))
		row[1]=int(input("Enter first team ID: "))
		row[2]=int(input("Enter second team ID: "))
		row[3]=int(input("Enter won by team ID: "))
		row[4]=input("Margin: ")
		row[5]=int(input("MOM cricketer Id: "))
		query="select Team_Id from CRICKETER where Cricketer_Id=('%d')"%(row[5])
		# print(query)
		cur.execute(query)
		rows=cur.fetchall()
		tmp=0
		for column1 in rows:
			tmp=column1['Team_Id']
		con.commit()
		query="INSERT INTO MAN_OF_THE_MATCH (Cricketer_Id ,Team_Id) SELECT * FROM (SELECT '%d' as a,'%d' as b) AS tmp WHERE NOT EXISTS (SELECT * FROM MAN_OF_THE_MATCH WHERE Cricketer_Id='%d' ) LIMIT 1"%(row[5],int(tmp),row[5])
		print(query)
		cur.execute(query)
		con.commit()
		query = "INSERT INTO `WORLD_CUP_MATCHES` VALUES('%d','%s','%d','%d','%d','%d');" % (
			row[0], row[4], row[5], row[1], row[2], row[3])
		print(query)
		cur.execute(query)
		query = "INSERT INTO `MOM_MATCHES_INFO` VALUES('%d','%d');" % (
			 row[5], row[0])
		print(query)
		cur.execute(query)
		# rows=cur.fetchall()
		# printRowsAsTable(rows)
		con.commit()

	# print("Inserted Into Database")
	except Exception as e:
	    con.rollback()
	    print("Failed to insert into database")
	    print (">>>>>>>>>>>>>", e)
    # print("Not implemented")
def addANewTeam():
	try:
		row={}
		row[0]=int(input("Team Id: "))
		row[1]=input("Team name: ")
		# row[2]=input("Team cricket captain Id: ")
		query="insert into `TEAMS_AND_PERFORMANCE` VALUES('%d','%s',NULL) "%(row[0],row[1])
		print(query)
		cur.execute(query)
		# rows=cur.fetchall()
		# printRowsAsTable(rows)
		con.commit()

		# print("Inserted Into Database")
	except Exception as e:
		con.rollback()
		print("Failed to insert into database")
		print (">>>>>>>>>>>>>", e)
    # print("Not implemented")
def addANewCaptain():
	try:
		row={}
		row[0]=int(input("Cricketer_Id: "))
		row[1]=int(input("Captain_Id: "))
		# row[2]=input("Team cricket captain Id: ")
		query="insert into `CAPTAIN` VALUES('%d','%d') "%(row[0],row[1])
		print(query)
		cur.execute(query)
		# rows=cur.fetchall()
		# printRowsAsTable(rows)
		con.commit()

		# print("Inserted Into Database")
	except Exception as e:
		con.rollback()
		print("Failed to insert into database")
		print (">>>>>>>>>>>>>", e)

def updateTheCaptain():
	try:
		row={}
		row[0]=int(input("Team_Id: "))
		row[1]=int(input("Cricketer_Id: "))
		# row[2]=input("Team cricket captain Id: ")
		query="update `TEAMS_AND_PERFORMANCE` set `Team_Captain_CRICKETER_ID`=%d where `Team_Id`=%d "%(row[1],row[0])
		print(query)
		cur.execute(query)
		# rows=cur.fetchall()
		# printRowsAsTable(rows)
		con.commit()

		# print("Inserted Into Database")
	except Exception as e:
		con.rollback()
		print("Failed to insert into database")
		print (">>>>>>>>>>>>>", e)
def showPoints():
	try:
		query="select Team_Id,PLAYED,WON,(PLAYED-WON) as LOST,(2*WON) as POINTS from (select der5.Team_Id,der5.Total_Matches_Played as PLAYED,IFNULL(der6.Matches_Won,0) as WON from (select der4.Team_Id,((der4.att1+der4.att2)/2) as 'Total_Matches_Played' from (select der3.Team_Id,count(der3.First_Team_Id) as att2,count(der3.Second_Team_Id) as att1 from (select der1.Team_Id,der2.First_Team_Id,der2.Second_Team_Id from TEAMS_AND_PERFORMANCE as der1 LEFT JOIN WORLD_CUP_MATCHES as der2 on Team_Id=First_Team_Id or Team_Id=Second_Team_Id) as der3 group by der3.Team_Id) as der4) as der5 LEFT JOIN (select WON_BY_TEAM_ID,count(WON_BY_TEAM_ID) as 'Matches_Won' from WORLD_CUP_MATCHES group by WON_BY_TEAM_ID) as der6 on der5.Team_Id=der6.WON_BY_TEAM_ID) as der7"
		print(query)
		cur.execute(query)
		rows=cur.fetchall()
		printRowsAsTable(rows)
		con.commit()

		# print("Inserted Into Database")
	except Exception as e:
		con.rollback()
		print("Failed to insert into database")
		print (">>>>>>>>>>>>>", e)

def addACricketer():
    try:
        # Takes emplyee details as input
        row = {}
        print("Enter new cricketer's details: ")
        name = (input("Name (Fname Lname): ")).split(' ')
        row["FName"] = name[0]
        row["LName"] = name[1]
        row["Cricketer_Id"] = input("cricketer id: ")
        row["Wickets_Taken"] = int(input("Wickets taken:"))
        row["Matches_Played"] = int(input("Matches Played: "))
        row["Runs_Scored"] = int(input("Runs scored: "))
        row["Batsman_Rank"] = int(input("Batsman Rank: "))
        row["Team_Id"] = input("Team Id: ")
        row["Batsman_Points"] = int(input("Batsman Points: "))
        """
        In addition to taking input, you are required to handle domain errors as well

        For example: the SSN should be only 9 characters long
        Sex should be only M or F

        If you choose to take Super_SSN, you need to make sure the foreign key constraint is satisfied

        HINT: Instead of handling all these errors yourself, you can make use of except clause to print the error returned to you by MySQL
        """

        query = "INSERT INTO CRICKETER(FName, LName, Cricketer_Id, Wickets_Taken, Matches_Played, Runs_Scored, Batsman_Rank, Team_Id, Batsman_Points) VALUES('%s', '%s', '%s', '%d', '%d', '%d', '%d', %s, %d)" % (
        	row["FName"], row["LName"], row["Cricketer_Id"], row["Wickets_Taken"], row["Matches_Played"], row["Runs_Scored"], row["Batsman_Rank"], row["Team_Id"],row["Batsman_Points"])

        print(query)
        cur.execute(query)
        con.commit()

        print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print (">>>>>>>>>>>>>", e)
        
    return

def dispatch(ch):
    """
    Function that maps helper functions to option entered
    """

    if(ch==1): 
        addACricketer()
    elif(ch==2):
        viewCricketers()
    elif(ch==3):
        deleteCricketers()
    elif(ch==4):
        addANewMatch()
    elif(ch==5):
        addANewTeam()
    elif(ch==6):
        addANewCaptain()
    elif(ch==7):
        updateTheCaptain()
    elif(ch==8):
        showPoints()    
    else:
        print("Error: Invalid Option")

# Global
while(1):
    tmp = sp.call('clear',shell=True)
    # username = input("Username: ")
    # password = input("Password: ")

    try:
        con = pymysql.connect(host='localhost',
                # user=username,
                # password=password,
                user="teddy",
                password="!Tedd8313!",
                db='WORLDCUP',
                cursorclass=pymysql.cursors.DictCursor)
        tmp = sp.call('clear',shell=True)

        if(con.open):
            print("Connected")
        else:
            print("Failed to connect")
        tmp = input("Enter any key to CONTINUE>")

        with con:
            cur = con.cursor()
            while(1):
                tmp = sp.call('clear',shell=True)
                print("1. Add a new cricketer")
                print("2. View cricketers of a particular team")
                print("3. Delete a particular cricketer(if he retires)")
                print("4. Add a new match")
                print("5. Add a new team")
                print("6. Add a new captain")
                print("7. Update the captain of a team")
                print("8. Show the points of a team")
                print("9. Logout")
                ch = int(input("Enter choice> "))
                tmp = sp.call('clear',shell=True)
                if ch==9:
                    exit()
                else:
                    dispatch(ch)
                    tmp = input("Enter any key to CONTINUE>")


    except:
        tmp = sp.call('clear',shell=True)
        print("Connection Refused: Either username or password is incorrect or user doesn't have access to database")
        tmp = input("Enter any key to CONTINUE>")
    
   


