import random
import string
import datetime
import numpy as np
import pandas as pd

subareas = {
    "Logística": ["Gestión de inventario", "Transporte y distribución", "Optimización de rutas", "Gestión de almacenes", "Logística inversa"],
    "Producción": ["Control de calidad", "Cadena de suministro", "Mejora de procesos", "Planificación", "Mantenimiento"],
    "Planificación": ["Planificación estratégica", "Capacidad", "Planificación de proyectos"],
    "Calidad": ["Control de calidad", "Gestión de riesgos", "Mejora continua", "Auditoría interna"],
    "Financias": ["Contabilidad y registros financieros", "Gestión de tesorería"],
    "Mantenimiento": ["Mantenimiento correctivo", "Gestión de activos"]
}

registroCWID = []

def generate_unique_word(text):
    word = ''.join(np.random.choice(list(string.ascii_uppercase), size=6))
    while word in registroCWID:
        word = ''.join(np.random.choice(list(string.ascii_uppercase), size=6))
    registroCWID.append(word)
    return word

def plant_employee(empresa):
    if empresa in ["Unge", "Hays"]:
        return "Local"
    else:
        return "Externo"

def assign_subarea(sector):
    return random.choice(subareas[sector])

def generate_random_weekday_date():
    while True:
        year = random.randint(2020, 2022)
        month = random.randint(1, 12)
        day = random.randint(1, 28)
        hour = random.randint(8, 16)
        minute = random.randint(0, 59)
        second = random.randint(0, 59)
        date = datetime.datetime(year, month, day, hour, minute, second)
        if date.weekday() < 5:
            return date

def select_random_item(lst):
    selected_item = random.choice(lst)
    while True:
        new_item = random.choice(lst)
        if new_item >= selected_item:
            return [new_item, selected_item]

# Análisis y confección de agregados de datos de usuarios
usuarios = pd.read_csv("MOCK_DATA.csv")

usuarios["CWID"] = usuarios["Nombre"].apply(generate_unique_word)
usuarios["Externo"] = usuarios["Empresa"].apply(plant_employee)
usuarios["SubArea"] = usuarios["Área"].apply(assign_subarea)

# Nueva tabla de empresas
empresas = usuarios.drop_duplicates(subset="Empresa")[["Empresa", "Externo"]]
empresas["EID"] = empresas["Empresa"].apply(generate_unique_word)

# Nueva tabla de SubAreas
subareas_table = usuarios.drop_duplicates(subset="SubArea")[["Área", "SubArea"]]
subareas_table["SAID"] = subareas_table["SubArea"].apply(generate_unique_word)
subareas_table = subareas_table[["Área", "SubArea", "SAID"]].drop_duplicates()

# Combinación de IDs
usuarios = usuarios.merge(empresas, how='left', on='Empresa')
usuarios = usuarios.merge(subareas_table, how='left', on='SubArea')
usuarios = usuarios[["Nombre", "Apellido", "Genero", "CWID", "EID", "SAID"]]

# Creación de tabla de registros
practicas = ["Mejor enfocada", "Gestión visual", "Trabajo en equipo", "5S", "Mindset digital"]
motivos = ["Flexibilidad", "Liderazgo", "Integridad", "Eficiencia"]

registros = [{
    "id": n+1,
    "nominador": selected_item[0],
    "nominado": selected_item[1],
    "práctica": random.choice(practicas),
    "motivo": random.choice(motivos),
    "fecha": generate_random_weekday_date()
} for n, selected_item in enumerate(select_random_item(list(usuarios["CWID"])) for _ in range(3000))]

data = pd.DataFrame(registros)

# Exportación de datasets
data.to_csv("Registros.csv", index=False)
usuarios.to_csv("Usuarios.csv", index=False)
empresas.to_csv("Empresas.csv", index=False)
subareas_table.to_csv("SubAreas.csv", index=False)
