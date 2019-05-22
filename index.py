#coding:utf-8
import cgi 

print("Content-type: text/html; charset=utf-8\n")

html = """<!DOCTYPE html>
<head>
    <meta charset='utf-8'>
    <style>
    h1,div{
        margin: auto;
        margin-bottom: 100px;
        width: 60%;
        border: 3px solid #73AD21;
        padding: 10px;
        text-align: center;
    }
</style>
</head>
<body>
    <h1 style="color:blue;">Renseigner formulaire contact</h1>
    <div>
    <form action="/forms_list.py" method="post">
        <p><label for="">Prénom</label>
        <input type="text" name="prenom"></p>
        <p><label for="">Nom</label>
        <input type="text" name="nom"></p>
        <p><label for="">Numéro</label>
        <input type="text" name="numero"></p>
        <button type="submit">Ajouter</button>
    </form>
    
    </div>
</body>
</html>
"""

print(html)
 

