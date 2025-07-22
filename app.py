from flask import Flask, render_template, request, redirect, flash
import threading
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta'

def send_email(subject, body, sender_email, receiver_email, password):
    try:
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender_email, password)
            server.send_message(msg)
        print("Correo enviado correctamente.")
    except Exception as e:
        print("Error al enviar correo:", e)

def send_email_html(subject, html_content, sender_email, receiver_email, password):
    try:
        msg = MIMEMultipart('alternative')
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject
        msg.attach(MIMEText(html_content, 'html'))

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender_email, password)
            server.send_message(msg)
        print("Correo HTML enviado correctamente.")
    except Exception as e:
        print("Error al enviar correo HTML:", e)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/nosotros')
def nosotros():
    return render_template('nosotros.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/ventas')
def ventas():
    return render_template('blog.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']

        sender_email = "ingenieriatecnica23@gmail.com"
        password = "uqzftxgmbnxhz esf".replace(" ", "")  # Contraseña sin espacios
        receiver_email = sender_email

        # Mensaje para el admin
        subject_admin = "Nuevo mensaje de contacto"
        body_admin = f"""Has recibido un nuevo mensaje desde el formulario de contacto:

Nombre: {name}
Correo: {email}
Teléfono: {phone}
Mensaje: {message}
"""

        # Mensaje de confirmación para el usuario (HTML con Tailwind)
        subject_user = "Hemos recibido tu mensaje - INGETSoport"
        body_user_html = render_template("email_confirmation.html", name=name)

        # Enviar en segundo plano
        threading.Thread(target=send_email, args=(subject_admin, body_admin, sender_email, receiver_email, password)).start()
        threading.Thread(target=send_email_html, args=(subject_user, body_user_html, sender_email, email, password)).start()

        flash("Tu mensaje fue enviado correctamente. Nos pondremos en contacto contigo pronto.", "success")
        return redirect('/contact')

    return render_template('contact.html')

# Rutas de servicios específicos
@app.route('/services/software_development')
def software_development():
    return render_template('software_development.html')

@app.route('/services/technical_support')
def technical_support():
    return render_template('technical_support.html')

@app.route('/services/consulting')
def consulting():
    return render_template('consulting.html')

@app.route('/services/cybersecurity')
def cybersecurity():
    return render_template('cybersecurity.html')

@app.route('/services/network_telecom')
def network_telecom():
    return render_template('network_telecom.html')

@app.route('/googleb4b82bf52f2d9d77.html')
def google_verification():
    return send_from_directory('static', 'googleb4b82bf52f2d9d77.html')

if __name__ == '__main__':
    app.run(debug=True)
