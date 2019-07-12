apetece_helado_input = input("¿te apetece un helado? (si / no) ").upper()
if apetece_helado_input == 'SI':
    apetece_helado = True
elif apetece_helado_input == "NO":
    apetece_helado = False
else:
    print("te he dicho que me digas si o no, no se que has dicho pero cuento como que no")
    apetece_helado = False

tienes_dinero_input = input("¿tienes dinero para un helado? (si / no) ").upper()
esta_el_senor_helados_input = input("¿Esta el señor de los halados? (si / no) ").upper()
esta_tu_tia_input = input("¿ESta tu tia? (si / no) ").upper()

apetece_helado = apetece_helado_input == "SI"
tienes_dinero = tienes_dinero_input == "SI"
esta_tu_tia = esta_tu_tia_input == "SI"
puedes_permitirtelo = tienes_dinero or esta_tu_tia
esta_el_senor_helados = esta_el_senor_helados_input == "SI"



if apetece_helado or puedes_permitirtelo or esta_el_senor_helados:
    print("Pues comete el helado")
else:
    print("Pues nada")
