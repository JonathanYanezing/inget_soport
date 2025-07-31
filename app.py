from flask import Flask, render_template, request, redirect, flash, send_from_directory, jsonify
import threading
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sqlite3
from datetime import datetime, timedelta
import json
import os

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta'

# Configuración de la base de datos
DATABASE = 'visits.db'

def init_db():
    """Inicializar la base de datos"""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    # Tabla de visitas
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS visits (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            page TEXT NOT NULL,
            ip_address TEXT,
            user_agent TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            referrer TEXT,
            session_id TEXT
        )
    ''')
    
    # Tabla de estadísticas diarias
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS daily_stats (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date DATE UNIQUE,
            total_visits INTEGER DEFAULT 0,
            unique_visitors INTEGER DEFAULT 0,
            pages_viewed TEXT
        )
    ''')
    
    conn.commit()
    conn.close()

def get_client_ip():
    """Obtener la IP real del cliente"""
    if request.headers.get('X-Forwarded-For'):
        return request.headers.get('X-Forwarded-For').split(',')[0]
    return request.remote_addr

def record_visit(page):
    """Registrar una visita"""
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        
        ip = get_client_ip()
        user_agent = request.headers.get('User-Agent', '')
        referrer = request.headers.get('Referer', '')
        session_id = request.cookies.get('session_id', '')
        
        cursor.execute('''
            INSERT INTO visits (page, ip_address, user_agent, referrer, session_id)
            VALUES (?, ?, ?, ?, ?)
        ''', (page, ip, user_agent, referrer, session_id))
        
        conn.commit()
        conn.close()
    except Exception as e:
        print(f"Error registrando visita: {e}")

def get_visit_stats():
    """Obtener estadísticas de visitas"""
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        
        # Total de visitas
        cursor.execute('SELECT COUNT(*) FROM visits')
        total_visits = cursor.fetchone()[0]
        
        # Visitas únicas (por IP)
        cursor.execute('SELECT COUNT(DISTINCT ip_address) FROM visits')
        unique_visitors = cursor.fetchone()[0]
        
        # Páginas más visitadas
        cursor.execute('''
            SELECT page, COUNT(*) as count 
            FROM visits 
            GROUP BY page 
            ORDER BY count DESC 
            LIMIT 10
        ''')
        top_pages = cursor.fetchall()
        
        # Visitas de hoy
        today = datetime.now().date()
        cursor.execute('''
            SELECT COUNT(*) FROM visits 
            WHERE DATE(timestamp) = ?
        ''', (today,))
        today_visits = cursor.fetchone()[0]
        
        # Visitas de esta semana
        week_ago = datetime.now() - timedelta(days=7)
        cursor.execute('''
            SELECT COUNT(*) FROM visits 
            WHERE timestamp >= ?
        ''', (week_ago,))
        week_visits = cursor.fetchone()[0]
        
        # Visitas de este mes
        month_ago = datetime.now() - timedelta(days=30)
        cursor.execute('''
            SELECT COUNT(*) FROM visits 
            WHERE timestamp >= ?
        ''', (month_ago,))
        month_visits = cursor.fetchone()[0]
        
        conn.close()
        
        return {
            'total_visits': total_visits,
            'unique_visitors': unique_visitors,
            'top_pages': top_pages,
            'today_visits': today_visits,
            'week_visits': week_visits,
            'month_visits': month_visits
        }
    except Exception as e:
        print(f"Error obteniendo estadísticas: {e}")
        return {
            'total_visits': 0,
            'unique_visitors': 0,
            'top_pages': [],
            'today_visits': 0,
            'week_visits': 0,
            'month_visits': 0
        }

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
    record_visit('index')
    return render_template('index.html')

@app.route('/nosotros')
def nosotros():
    record_visit('nosotros')
    return render_template('nosotros.html')

@app.route('/services')
def services():
    record_visit('services')
    return render_template('services.html')

@app.route('/ventas')
def ventas():
    record_visit('ventas')
    return render_template('blog.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    record_visit('contact')
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
    record_visit('software_development')
    return render_template('software_development.html')

@app.route('/services/technical_support')
def technical_support():
    record_visit('technical_support')
    return render_template('technical_support.html')

@app.route('/services/consulting')
def consulting():
    record_visit('consulting')
    return render_template('consulting.html')

@app.route('/services/cybersecurity')
def cybersecurity():
    record_visit('cybersecurity')
    return render_template('cybersecurity.html')

@app.route('/services/network_telecom')
def network_telecom():
    record_visit('network_telecom')
    return render_template('network_telecom.html')

# Ruta para estadísticas (solo para administradores)
@app.route('/admin/stats')
def admin_stats():
    stats = get_visit_stats()
    return render_template('admin_stats.html', stats=stats)

# API para obtener estadísticas en tiempo real
@app.route('/api/stats')
def api_stats():
    stats = get_visit_stats()
    return jsonify(stats)

# Ruta para Google Search Console verification
@app.route('/googleb4b82bf52f2d9d77.html')
def google_verification():
    return send_from_directory('static', 'googleb4b82bf52f2d9d77.html')

if __name__ == '__main__':
    init_db()  # Inicializar base de datos al arrancar
    app.run(debug=True)
