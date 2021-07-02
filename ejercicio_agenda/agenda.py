class Direccion:
    def __init__(self):
        self.calle = ""
        self.piso = ""
        self.ciudad = ""
        self.cp = ""
    
    def setCalle(self, calle):
        self.calle = calle
    def getCalle(self):
        return self.calle
    def setPiso(self,piso):
        self.piso = piso
    def getPiso(self):
        return self.piso
    def setCiudad(self,ciudad):
        self.ciudad = ciudad
    def getCiudad(self):
        return self.ciudad
    def setCP(self,cp):
        self.cp = cp
    def getCP(self):
        return self.cp
    def mostrarDireccion(self):
        print("Datos Dirección:")
        print("\tCalle: ",self.calle)
        print("\tPiso: ",self.piso)
        print("\tCiudad: ",self.ciudad)
        print("\tCP: ",self.cp)
class Persona:
    def __init__(self):
        self.nombre = ""
        self.apellidos =""
        self.fechaNacimiento = ""
    
    def setNombre(self,nombre):
        self.nombre = nombre
    def getNombre(self):
        return self.nombre
    def setApellidos(self,apellidos):
        self.apellidos = apellidos
    def getApellidos(self):
        return self.apellidos
    def setFechaNacimiento(self,fechaNacimiento):
        self.fechaNacimiento = fechaNacimiento
    def getFechaNacimiento(self):
        return self.fechaNacimiento
    def mostrarPersona(self):
        print("Información de la Persona:")
        print("\tNombre: ",self.nombre)
        print("\tApellidos: ",self.apellidos)
        print("\tFecha de Nacimiento: ",self.fechaNacimiento)
class Telefono:
    def __init__(self):
        self.tfijo = ""
        self.tmovil = ""
        self.ttrabajo = ""
    def setTfijo(self,tfijo):
        self.tfijo = tfijo
    def getTfijo(self):
        return self.tfijo
    def setTmovil(self,tmovil):
        self.tmovil = tmovil
    def getTmovil(self):
        return self.tmovil
    def setTtrabajo(self,ttrabajo):
        self.ttrabajo = ttrabajo
    def getTtrabajo(self):
        return self.ttrabajo
    def mostrarTelefono(self):
        print("Datos telefono:")
        print("\tTelefono Fijo: ",self.tfijo)
        print("\tTelefono movil: ",self.tmovil)
        print("\tTelefono trabajo: ",self.ttrabajo)
class Contacto(Direccion,Persona,Telefono):
    def __init__(self):
        self.email = ""
    def setEmail(self,email):
        self.email = email
    def getEmail(self):
        return self.email
    def mostrarContacto(self):
        print("#################")
        print("Contacto:")
        print(self.mostrarDireccion())
        print(self.mostrarPersona())
        print(self.mostrarTelefono())
        print("\tEmail: ",self.email)
class Agenda:

    def __init__(self):
        self.path = "./agenda.txt"
        self.listaContactos = ""
        
        
    

    def cargarContactos(self):
        with open(self.path, 'r') as f:
            self.listaContactos = f.read()
        print(self.listaContactos)
    def guardarContacto(self):
        self.listaContactos = "Rodriguez"
        with open(self.path, 'w') as f:
            f.write(self.listaContactos)
            

        
a = Agenda()
a.guardarContacto()
a.cargarContactos()