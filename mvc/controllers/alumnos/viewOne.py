import web
render=web.template.render('mvc/views/alumnos/')

class View:
    def GET(self):
        try: 
            data=web.input()
            matricula=data['matricula']
            name=data['name']
            paterno=data['paterno']
            materno=data['materno']
            edad=data['edad']
            fecha=data['fecha']
            genero=data['genero']
            state=data['state']
            return render.viewOne(matricula,name,paterno,materno,edad,fecha,genero,state)
        except Exception as e:
            result=[]    
            result.append('error'+ str(e.args))
            return result