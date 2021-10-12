def validaciones_nombre(name:str):
    #Validacion nombre vacio
    if len(name)==0:
        raise Exception('Debe ingresar un nombre')
    if len(name)>25:
        raise Exception('El nombre no debe tener mas de 25 caracteres')
    if len(name)<3:
        raise Exception('El nombre debe tener mas de 2 caracteres')
    if not name.isalnum():
        raise Exception('El nombre no puede tener caracteres especiales o espacios')


