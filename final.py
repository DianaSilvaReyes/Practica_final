import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

def generar_reporte(nombre_archivo):
    datos = [
        "Nombre, Correo, Puntuación",
        "Juan Pérez, juan@example.com, 85",
        "María García, maria@example.com, 90",
        "Luis Ramírez, luis@example.com, 78"
    ]

    with open(nombre_archivo, 'w') as archivo:
        for linea in datos:
            archivo.write(linea + "\n")
    print(f"✅ Reporte '{nombre_archivo}' generado correctamente.")


def generar_reporte_detallado(nombre_archivo):
    datos = [
        "ID, Nombre, Correo, Puntuación, Comentarios",
        "1, Juan Pérez, juan@example.com, 85, Buen desempeño",
        "2, María García, maria@example.com, 90, Excelente trabajo",
        "3, Luis Ramírez, luis@example.com, 78, Necesita mejorar en algunos aspectos"
    ]

    with open(nombre_archivo, 'w') as archivo:
        for linea in datos:
            archivo.write(linea + "\n")
    print(f"✅ Reporte detallado '{nombre_archivo}' generado correctamente.")


def enviar_correo(servidor_smtp, puerto_smtp, correo_remitente, clave_remitente, correo_destinatario, asunto, cuerpo, ruta_archivo=None):
    try:
        print("SMTP (Simple Mail Transfer Protocol) es el protocolo usado para enviar correos electrónicos.")
        print("Debes ingresar los datos correctos del servidor SMTP y la autenticación.")
        print("Ejemplos de servidores SMTP:")
        print("- Gmail: smtp.gmail.com, puerto 587")
        print("- Outlook/Hotmail: smtp.office365.com, puerto 587")
        print("- Yahoo: smtp.mail.yahoo.com, puerto 465 o 587")

        mensaje = MIMEMultipart()
        mensaje['From'] = correo_remitente
        mensaje['To'] = correo_destinatario
        mensaje['Subject'] = asunto
        mensaje.attach(MIMEText(cuerpo, 'plain'))

        if ruta_archivo:
            with open(ruta_archivo, 'rb') as archivo:
                adjunto = MIMEApplication(archivo.read(), _subtype="txt")
                adjunto.add_header('Content-Disposition', 'attachment', filename=ruta_archivo.split("/")[-1])
                mensaje.attach(adjunto)

        with smtplib.SMTP(servidor_smtp, puerto_smtp) as servidor:
            servidor.starttls()
            servidor.login(correo_remitente, clave_remitente)
            servidor.sendmail(correo_remitente, correo_destinatario, mensaje.as_string())

        print("✅ Correo enviado exitosamente a", correo_destinatario)

    except Exception as e:
        print("❌ Error al enviar correo:", e)


def menu():
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Generar reporte")
        print("2. Generar reporte detallado")
        print("3. Enviar correo con reporte adjunto")
        print("4. Salir")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == '1':
            nombre_archivo = input("Nombre del archivo de reporte (ejemplo: reporte.txt): ")
            generar_reporte(nombre_archivo)
        elif opcion == '2':
            nombre_archivo = input("Nombre del archivo de reporte detallado (ejemplo: reporte_detallado.txt): ")
            generar_reporte_detallado(nombre_archivo)
        elif opcion == '3':
            print("Asegúrate de usar los datos correctos del servidor SMTP y autenticación.")
            servidor_smtp = input("Servidor SMTP: ")
            puerto_smtp = int(input("Puerto SMTP: "))
            correo_remitente = input("Correo del remitente: ")
            clave_remitente = input("Contraseña: ")
            correo_destinatario = input("Correo del destinatario: ")
            asunto = input("Asunto del correo: ")
            cuerpo = input("Cuerpo del correo: ")
            ruta_archivo = input("Ruta del archivo adjunto (dejar en blanco si no hay): ") or None

            enviar_correo(servidor_smtp, puerto_smtp, correo_remitente, clave_remitente, correo_destinatario, asunto, cuerpo, ruta_archivo)
        elif opcion == '4':
            print("Saliendo del programa...")
            break
        else:
            print("❌ Opción no válida. Inténtalo de nuevo.")

menu()
