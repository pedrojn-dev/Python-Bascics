# Operadores and y or

usuario_logueado = True
usuario_admin = True

if usuario_logueado or usuario_admin:
    print('Administrador')
elif usuario_logueado:
    print('Acceso al sistema')
else:
    print('Debes Iniciar sesión')