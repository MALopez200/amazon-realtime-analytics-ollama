import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv
load_dotenv()

def enviar_alerta(asunto, cuerpo):
    # 1. Leer credenciales
    email_user = os.getenv('EMAIL_USER')
    email_password = os.getenv('EMAIL_PASSWORD')
    alerta_email = os.getenv('ALERT_EMAIL')

    # 2. Validar que existan
    if not all([email_user, email_password, alerta_email]):
        print('❌ No se aceptan campos vacios')
        return

    servidor = None
    try:
        # 3. Conectar con Gmail (con timeout de 10s)
        servidor = smtplib.SMTP('smtp.gmail.com', 587, timeout=10)
        servidor.starttls()                    # Conversación segura
        servidor.login(email_user, email_password)  # Identificarse

        # 4. Crear la carta
        mensaje = MIMEMultipart()
        mensaje['From'] = email_user
        mensaje['To'] = alerta_email
        mensaje['Subject'] = asunto
        mensaje.attach(MIMEText(cuerpo, 'plain'))

        # 5. Enviar
        servidor.sendmail(email_user, alerta_email, mensaje.as_string())
        print(f'✅ Correo enviado a {alerta_email}')

    except smtplib.SMTPException as e:
        print(f'❌ Error al enviar correo: {e}')
    except Exception as e:
        print(f'❌ Error inesperado: {e}')
    finally:
        if servidor:
            try:
                servidor.quit()
            except Exception:
                pass  # Si ya falló la conexión, ignorar error al cerrar

if __name__ == '__main__':
    enviar_alerta('Prueba', 'Este es un correo de prueba')