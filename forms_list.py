#coding:utf-8
import cgi
import cgitb
from Web_Python_Without_Framework.dao.dao import Database

dao = Database()
cgitb.enable()
form = cgi.FieldStorage()
print("Content-type: text/html \n")
html = """<!DOCTYPE html>
<html>
<head>
    <meta charset='utf-8'>
     <style>
        h1,div{
            margin: auto;
            margin-bottom: 100px;
            width: 60%;
            border: 3px solid #73AD21;
            padding: 10px;
            text-align: center;}
            td{color:green;}
    </style>
</head>
<body>
    <h1>Liste des contacts</h1>
    <div> 
    <table>
        <thead>
            <tr><th>Prenom</th><th>Nom</th><th>Contact</th></tr>
        </thead>
        <tbody>
"""
print(html)
try:
    if form.getvalue("prenom") and form.getvalue("nom") and form.getvalue("numero"):
        prenom = form.getvalue("prenom")
        nom = form.getvalue("nom")
        numero = form.getvalue("numero")
        dao.save(prenom,nom,numero)
        liste = dao.lister()
        for row in liste:
            html = """<tr><td>{}</td><td>{}</td><td>{}</td>
                    <td><a href="#">Modifier</a></td>
                    <td><a href="#">Supprimer</a></td></tr>
                    """.format(row.prenom, row.nom, row.numero)
            print(html)
    else:
        raise Exception("")
except:
    print("Il existe des champs qui sont potentiellement vides")

html = """
        </tbody>
    </table>
    </div>
</body>
</html>
"""
print(html)
