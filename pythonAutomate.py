for i in range(1,8):
    i = str(i)
    with open("audience"+i+".html",'w') as file:
            file.write('<!DOCTYPE html>\n<html lang="en">\n<head>\n\t<meta charset="UTF-8">\n\t<meta '
               'http-equiv="X-UA-Compatible" content="IE=edge">\n\t<meta name="viewport" content="width=device-width, '
               'initial-scale=1.0">\n<title>KBC</title>\n<link rel="stylesheet" href="style.css">\n<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200" />\n<style>\nh1{\nposition: relative;\nleft: 33%;top:18%;}</style></head>\n<body>\n<h1>YOU ARE USING AUDIENCE POLL</h1>\n<h1 class="st-en"><a href="index'+i+'.html">CANCEL</a></h1></body></html>')