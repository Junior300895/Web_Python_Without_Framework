import pyodbc

class Database:
    conn = pyodbc.connect('Driver={SQL Server};''Server=DESKTOP-SMDFK6B\MYSQLSERVER;''DATABASE=annuaire;''Trusted_Connection=yes;')

    def save(self, prenom,nom,num):
        try:
            cursor = self.conn.cursor()
            cursor.execute("""insert into annuaire.dbo.contact values(?,?,?,?,?)""",(prenom,nom,num,"",""))
            cursor.commit()
        except Exception:
            print("Erreur de sauvergarde")

    def lister(self):
        liste = list()
        try:
            cursor = self.conn.cursor()
            cursor.execute("select * from annuaire.dbo.contact")
            for row in cursor:
                liste.append(row)
            return liste
        except Exception:
            print("Erreur de listing")

