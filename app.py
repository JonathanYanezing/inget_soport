from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta'  # Necesaria para usar flash messages

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

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
        message = request.form['message']
        
        # Aquí puedes agregar la lógica para manejar el mensaje
        flash('Tu mensaje ha sido enviado. ¡Gracias por contactarnos!')
        return redirect(url_for('contact'))
    
    return render_template('contact.html')

# Otras rutas para servicios específicos
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

