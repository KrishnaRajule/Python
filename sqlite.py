import sqlite3

cont = sqlite3.connect("mailct.sqlite")
cur = cont.cursor()

cur.execute("DROP TABLE IF EXISTS Counts")
cur.execute("CREATE TABLE Counts (org TEXT, count INTEGER)")

fname = input("Enter the file name: ")
if len(fname)<1: fname = "mbox.txt"
hfile = open(fname)

for line in hfile:
    if not line.startswith("From: "): continue
    wrds = line.split()
    emaild = (wrds[1].split("@"))[1]
    cur.execute("SELECT count FROM Counts WHERE org = ?", (emaild,))
    row = cur.fetchone()

    if row is None:
        cur.execute("INSERT INTO Counts (org, count) VALUES (?, 1)", (emaild,))
    else:
        cur.execute("UPDATE Counts SET count = count + 1 WHERE org = ?", (emaild,))

cont.commit()

sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for ele in cur.execute(sqlstr):
    print(str(ele[0]), ele[1])

cur.close()
