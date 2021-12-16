###Para generar el ejecutable el comando es 
#     pyinstaller moodle2owl.py
#  debes de crear el directorio que falta lasdos ultimas carpetas vacias dist/moodle2owl/owlready2/pellet
# debes copiar elarchivo config.yml a la carpeta  dist/moodle2owl/
# ya luego basta con ejecutar el fichero  ./dist/moodle2owl/moodle2owl
#import json
#import request
import mysql.connector
from mysql.connector import Error
from owlready2 import *
import yaml
import os
import re
import sys

#barra de progreso
from tqdm import tqdm

#csv
import csv

#import urllib 
#from datetime import datetime
#import owlready2

#Script Generador de Ontologias para la plataforma Moodle 
# Probado enla version 3.6 y version 3.9
cfg = {}

dbusername = ""
dbpass = ""
dbhostname = ""
dbname = ""
moodlebaseurl = ""
cprofile = ""
uprofile = ""
repositorio = ""
ontologia = ""

if len(sys.argv) > 1 :
     dbtype        = sys.argv[1]  
     dbhostname    = sys.argv[2] 
     dbname        = sys.argv[3]  
     dbusername    = sys.argv[4] 
     dbpass        = sys.argv[5]  
     moodlebaseurl = sys.argv[6]   
     repositorio =  "%s/static" % os.path.abspath("../../")
     print("repositorio")
     print(repositorio)
     #Ubicacion http de la ontologia
     ontologia = "%s/static/moodle.owl" % moodlebaseurl
     print('ontologia')
     print(ontologia)

else:
     print("sin argumentos buscando entonces config.yml")
     if os.path.exists('config.yml'):
          with open("%s/config.yml" % os.getcwd(),"r") as ymlfile:
               cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)
               ################################################################################
               #####Configuracion : Modifique los parametros a continuacion acorde a su entorno

               #conexion
               dbusername = cfg['dbusername']
               dbpass = cfg['dbpass']
               dbhostname = cfg['dbhostname']
               dbname = cfg["dbname"]

               moodlebaseurl = cfg["moodlebaseurl"]
               #/course/view.php?id=2
               cprofile = cfg["cprofile"]
               #/user/profile.php?id=14
               uprofile = cfg["uprofile"]

               #Datos de Ontologia
               #Donde se almacenara el archivo moodle.owl
               repositorio = cfg['repositorio']
               #Ubicacion http de la ontologia
               ontologia = cfg["ontologia"]

               ##############################################################
     



# configphp = '../../config.php'


# configo = { "dbtype" : "", "dbhost" : "", "dbname" : "", "dbuser" : "", "dbpass" : "", "wwwroot" : ""}
# cprofile = "course/view.php?id:"
# uprofile = "user/profile.php?id:"


# if os.path.exists(configphp):
#      with open(configphp, "r") as configuracionphp:
#           ctext = str(configuracionphp.read())
#           #print(ctext)
#           #dbusername_regex = re.compile(r'''dbuser*=[\'\"](*)[\'\"]''')
#           #dbusername_regex = re.compile(r'''(dbuser)(\s*)(=)(\s*)(['"])([\w\s\\]*)(['"])''')
#           for dato in configo:
#                db_regex = re.compile(r'''%s\s*=\s*['"](.*)['"]''' % dato)
#                configo[dato] = db_regex.findall(ctext)
#           print(configo)
#           #dbusername_regex = re.compile(r'''dbuser\s*=\s*['"](.*)['"]''')
#           #mo = dbusername_regex.findall(ctext)
#           #print(mo)
#           print('///////////////////////')
          

# print("buscando funcion para pat relativo")
# print(os.getcwd())
# print(os.path.abspath(os.getcwd()))



# print("///////////////////////////////////////////////////////")

# dbtype        = configo["dbtype"][0]  
# dbhostname    = configo["dbhost"][0] 
# dbname        = configo["dbname"][0]  
# dbusername    = configo["dbuser"][0] 
# dbpass        = configo["dbpass"][0]  
# moodlebaseurl = configo["wwwroot"][0]    






#onto.load()
#crea la ontologia por el nombre de usuario y elnombre corto de los cursos

onto_path.append(repositorio)
onto = get_ontology(ontologia)

with onto:
    #Definicion de Objetos
    class Teacher(Thing):
        pass
    class Course(Thing):
        pass
    #Relaciones entre objetos
    class has_for_teacher(ObjectProperty):
         domain  = [onto.Course] 
         range   = [onto.Teacher]
         #inverse_property = is_teacher_in
    class is_teacher_in(ObjectProperty):
         domain  = [onto.Teacher] 
         range   = [onto.Course]
         ##inverse_property = has_for_teacher
    #Propiedades del Objeto Teacher
    class has_for_uid(DataProperty, FunctionalProperty): 
         domain    = [onto.Teacher]
         range     = [int]
    class has_for_username(DataProperty, FunctionalProperty): 
         domain    = [onto.Teacher]
         range     = [str]
    class has_for_firstname(DataProperty, FunctionalProperty): 
         domain    = [onto.Teacher]
         range     = [str]
    class has_for_lastname(DataProperty, FunctionalProperty): 
         domain    = [onto.Teacher]
         range     = [str]
    class has_for_email(DataProperty, FunctionalProperty): 
         domain    = [onto.Teacher]
         range     = [str]
    class has_for_city(DataProperty, FunctionalProperty): 
         domain    = [onto.Teacher]
         range     = [str]
    class has_for_country(DataProperty, FunctionalProperty): 
         domain    = [onto.Teacher]
         range     = [str]
    class has_for_institution(DataProperty, FunctionalProperty): 
         domain    = [onto.Teacher]
         range     = [str]
    class has_for_department(DataProperty, FunctionalProperty): 
         domain    = [onto.Teacher]
         range     = [str]
    class has_for_phone(DataProperty, FunctionalProperty): 
         domain    = [onto.Teacher]
         range     = [str]
    class has_for_orcid(DataProperty, FunctionalProperty): 
         domain    = [onto.Teacher]
         range     = [str]
    class has_for_orcid_uri(DataProperty, FunctionalProperty): 
         domain    = [onto.Teacher]
         range     = [str]
    class has_for_user_uri(DataProperty, FunctionalProperty): 
         domain    = [onto.Teacher]
         range     = [str]

    #Propiedades del objeto Course
    class has_for_cid(DataProperty, FunctionalProperty): 
        domain    = [onto.Course]
        range     = [int]
    class has_for_shortname(DataProperty, FunctionalProperty): 
        domain    = [onto.Course]
        range     = [str]
    class has_for_fullname(DataProperty, FunctionalProperty): 
        domain    = [onto.Course]
        range     = [str]
    class has_for_startdate(DataProperty, FunctionalProperty): 
        domain    = [onto.Course]
        range     = [str]
    class has_for_enddate(DataProperty, FunctionalProperty): 
        domain    = [onto.Course]
        range     = [str]
    class has_for_faculty(DataProperty, FunctionalProperty): 
        domain    = [onto.Course]
        range     = [str]

 
def getFacultad(cid,ccat,cursor):
            #category =$DB->get_record('course_categories', array("id" => $ccat));
            sql = '''select * from mdl_course_categories where id = %d ''' % ccat
            #categoryparent
            cursor.execute(sql)
            category = cursor.fetchone()
            parentcatid = category[12].split("/")[1]
            sql = "SELECT name FROM mdl_course_categories WHERE id = %s" % parentcatid
            cursor.execute(sql)
            facultad = cursor.fetchone()
            return facultad[0]

def getorcid(id, id_orcid, cursor):

    #obtener el orcid del usuario
    print
    sql = '''select data from mdl_user_info_data where userid = %d and fieldid = %d ;''' % (id, id_orcid)
    cursor.execute(sql)
    orcid = cursor.fetchone()
    if orcid : 
        return orcid[0]
    return "0000-0000-0000-0000"
    

with open('profesores_cursosAll.csv', 'w', newline='') as csvfile:
    fieldnames = ['orcid','username','ufirstname','ulastname','uemail','ucity',
    'ucountry','uinstitution','udepartment','phone1','cid','cfullname','cstartdate',
    'cenddate','cshortname','cfacultad','course_uri']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    #writer = csv.writer(csvfile, dialect='excel')
    writer.writeheader()

    #writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
    #writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
    #writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})            

         
    try:
        connection = mysql.connector.connect(host = dbhostname,
                                            database = dbname,
                                            user = dbusername,
                                            password = dbpass)
        if connection.is_connected():
            dbinfo = connection.get_server_info()
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print('Conectado al servidor %s' % dbinfo)                                         
            print('Conectado a la base de datos %s' % record)

            #obtener el id del campo orcid de una vez con distinc por si tienen mas de una cuenta
            #que pongan orcid en la que usan en docencia solamentes
            sql = '''select distinct id from mdl_user_info_field where (name = "orcid" OR name = "Orcid" OR name = "ORCID")'''
            cursor.execute(sql)
            d = cursor.fetchone()
            if d : id_orcid = d[0]

            #TODO omitir los que no tienen orcid o tienen orcid mal escrito
            #obteniendo listado de ids de usuarios
            print("Obteniendo usuarios")

            #para obtener todos
            sql = '''select id from mdl_user;'''  
            
            #para obtener con orcid
            #sql = "SELECT U.id as id FROM mdl_user_info_data as CF , mdl_user as U WHERE CF.data like '____-____-____-____' AND CF.fieldid={} AND CF.userid=U.id;".format(id_orcid)  
            
            cursor.execute(sql)
            ids_usuarios = cursor.fetchall()
            print("Total de usuarios captados: {}".format(len(ids_usuarios))) 

            #Verificando usuarios que son profesores en cursos
            print("Verificando usuarios que son profesores en cursos")
            oprofesores = []
            ocursos = []
            i = 0
            
            for id_usuario in tqdm(ids_usuarios): 
                #reducir la tupla
                id_usuario = id_usuario[0]
                #if i < 100 :
                if i>-1:
                    i+=1
                    sql='''SELECT 
                    u.username, 
                    u.firstname,  
                    u.lastname, 
                    u.email,  
                    u.city,     
                    u.country,    
                    u.institution,
                    u.department, 
                    u.phone1,   

                    c.id, 
                    c.fullname, 
                    c.startdate, 
                    c.enddate, 
                    c.shortname, 
                    
                    r.shortname, 
                    ct.path, 
                    c.category

                    FROM mdl_course AS c
                    JOIN mdl_context AS ct ON c.id = ct.instanceid
                    JOIN mdl_role_assignments AS ra ON ra.contextid = ct.id
                    JOIN mdl_user AS u ON u.id = ra.userid
                    JOIN mdl_role AS r ON r.id = ra.roleid
                    WHERE (r.shortname = 'editingteacher' OR r.shortname = 'manager' OR r.shortname = 'teacher') AND u.id = %d
                    ''' % id_usuario
                    cursor.execute(sql)
                    cursos = cursor.fetchall()


                    #verificamos si es profesor por los cursos que tiene
                    if len(cursos) != 0: 
            
                        #print(orcid)
                        #print("usuario con id = %d es profesor" % id_usuario)
                        #Ahora Trabajamoscon los cursos de este profesor
                        for curso in cursos:

                            #datos del profesor
                            orcid = getorcid(id_usuario, id_orcid, cursor)
                            iusuario = {
                                        "uid" : id_usuario, 
                                        "username" : curso[0] ,
                                        "firstname" : curso[1] ,
                                        "lastname" : curso[2] ,
                                        "email" : curso[3] ,
                                        "city" : curso[4] ,
                                        "country" : curso[5] ,
                                        "institution" : curso[6] ,
                                        "department" : curso[7] ,
                                        "phone1" : curso[8] ,
                                        "orcid" : orcid ,
                                        "orcid_uri" : "http:www.orcid.org/%s" % orcid ,
                                        "user_uri" : "%s%s%s" % (moodlebaseurl, uprofile, id_usuario) 
                                        }

                            #Datos del curso
                            icurso = {"cid" : curso[9], 
                                    "shortname" : curso[13],
                                    "fullname" : curso[10],
                                    "startdate" : curso[11],
                                    "enddate" : curso[12],
                                    "facultad" : getFacultad(curso[9], curso[16], cursor),
                                    "course_uri" : "%s%s%s" % (moodlebaseurl, cprofile, curso[9])                                 
                                    }
                            #profesores
                        #excell
                            writer.writerow({
                                'orcid':orcid,
                                #comentado para evitar confusion
                                #'uid': iusuario["uid"], 
                                'username': iusuario["username"],
                                'ufirstname': iusuario["firstname"], 
                                'ulastname': iusuario["lastname"], 
                                'uemail': iusuario["email"], 
                                'ucity': iusuario["city"], 
                                'ucountry': iusuario["country"], 
                                'uinstitution': iusuario["institution"], 
                                'udepartment': iusuario["department"], 
                                'phone1': iusuario["phone1"], 
                                "cid" : icurso['cid'],
                                "cshortname" : icurso['shortname'],
                                "cfullname" : icurso['fullname'],
                                "cstartdate" : icurso['startdate'],
                                "cenddate" : icurso['enddate'],
                                "cfacultad" : icurso['facultad'],
                                "course_uri" : icurso['course_uri']
                                })

                        #ontologia
                            t = onto.Teacher(iusuario["username"])
                            
                            t.has_for_uid = iusuario["uid"]
                            t.has_for_username = iusuario["username"]
                            t.has_for_firstname = iusuario["firstname"]
                            t.has_for_lastname = iusuario["lastname"]
                            t.has_for_email = iusuario["email"]
                            t.has_for_city = iusuario["city"]
                            t.has_for_country = iusuario["country"]
                            t.has_for_institution = iusuario["institution"]
                            t.has_for_department = iusuario["department"]
                            t.has_for_phone1 = iusuario["phone1"]
                            t.has_for_orcid = iusuario["orcid"]
                            t.has_for_orcid_uri = iusuario["orcid_uri"]
                            t.has_for_user_uri = iusuario["user_uri"]

                            oprofesores.append(t)
                            
                            #cursos
                            shortnameN = icurso["shortname"].replace('#','Nro')
                            c = onto.Course(shortnameN)
                            
                            c.has_for_cid = icurso["cid"]
                            c.has_for_fullname = icurso["fullname"]
                            c.has_for_shortname = shortnameN
                            c.has_for_startdate = icurso["startdate"]
                            c.has_for_enddate = icurso["enddate"]
                            c.has_for_faculty = icurso["facultad"]
                            c.has_for_course_uri = icurso["course_uri"]

                            ocursos.append(c)

                            t.is_teacher_in.append(c)
                            c.has_for_teacher.append(t)
                            
                            #print(shortnameN)
                            #print(iusuario["username"])
                            #print("-----------------------------------------------------")
            
            AllDifferent(oprofesores)
            AllDifferent(ocursos)


        if (connection.is_connected()) :
            cursor.close()
            connection.close()
            onto.save()
            print("Razonando")
            #with onto:
                    #sync_reasoner()

            #onto.save()
            print('Ontologia salvada en %s' % repositorio )
            print('conexion cerrada')                                       
    except Error as e:
        print(e)
