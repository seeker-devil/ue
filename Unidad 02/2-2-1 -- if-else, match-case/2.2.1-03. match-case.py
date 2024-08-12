# switch-case (Python >> match-case)
dia = input('Ingrese el dia de la semana: ')

match dia:
    case 'lunes':
        print('Hoy es lunes')
    case 'martes':
        print('Hoy es martes')
    case 'miercoles':
        print('Hoy es miercoles')
    case 'jueves':
        print('Hoy es jueves')
    case 'viernes':
        print('Hoy es viernes')
    case 'sabado':
        print('Hoy es sabado')
    case 'domingo':
        print('Hoy es domingo')
    case _:
        print('Dia no reconocido o un valor erroneo')