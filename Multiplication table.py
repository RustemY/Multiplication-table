f = open('test.html', 'w')

f.write("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Multiplication table</title>
        </head>
        <body>""")

f.write("<h1>")
f.write("""<table border="1">
           <caption>Multiplication table</caption>""")
f.write("<tr>")
f.write("<th>&nbsp;</th>")

for i in range(1, 11):
    f.write("<th>" + str(i) + "</th>")
f.write("</tr>")

for i in range(1, 11):
    f.write("<tr>")
    f.write("<td>" + str(i) + "</td>")
    for j in range(1, 11):
        f.write("<td>" + str(i * j) + "</td>")
    f.write("</tr>")
    
f.write("</table>")  
f.write("</h1>")
f.write("""</body>
        </html>""")

f.close()
