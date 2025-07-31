# 🚀 INGETSOPORT - Soluciones Tecnológicas

## 📋 **Descripción**

Sitio web profesional para **INGETSOPORT** - Innovación y Gestión de Soporte Tecnológico. Plataforma completa con servicios de desarrollo de software, soporte técnico, ciberseguridad, consultoría y redes/telecomunicaciones.

## ✨ **Características Principales**

### 🎨 **Diseño Moderno y Responsivo**
- **Diseño responsive** para todos los dispositivos
- **Interfaz moderna** con gradientes y animaciones
- **Navegación intuitiva** con menú móvil
- **Optimizado para SEO**

### 🤖 **Chatbot Automático**
- **Asistente inteligente** con respuestas automáticas
- **Botón animado** con efecto "titilar"
- **Interfaz de chat** moderna y funcional
- **Base de conocimientos** predefinida

### 📊 **Sistema de Estadísticas**
- **Seguimiento automático** de visitas
- **Panel de administración** con dashboard
- **Estadísticas en tiempo real**
- **API JSON** para integraciones
- **Widget en footer** con contadores

### 📧 **Sistema de Contacto**
- **Formulario de contacto** funcional
- **Envío automático de emails**
- **Confirmación por email** al usuario
- **Notificación al administrador**

### 🔗 **Integración WhatsApp**
- **Botón flotante** de WhatsApp
- **Enlace directo** al chat
- **Diseño responsive** y animado

## 🛠️ **Tecnologías Utilizadas**

- **Backend:** Python Flask
- **Frontend:** HTML5, CSS3, JavaScript
- **Framework CSS:** Tailwind CSS
- **Base de Datos:** SQLite
- **Email:** SMTP (Gmail)
- **Iconos:** Font Awesome, Lucide Icons

## 📁 **Estructura del Proyecto**

```
inget_soport/
├── app.py                 # Aplicación principal Flask
├── requirements.txt       # Dependencias Python
├── README.md             # Documentación principal
├── README_ESTADISTICAS.md # Documentación del sistema de estadísticas
├── .gitignore            # Archivos a ignorar en Git
├── static/               # Archivos estáticos
│   ├── img/             # Imágenes
│   └── *.css            # Archivos CSS
└── templates/            # Plantillas HTML
    ├── base.html         # Plantilla base
    ├── index.html        # Página de inicio
    ├── nosotros.html     # Página Nosotros
    ├── services.html     # Página Servicios
    ├── contact.html      # Página Contacto
    ├── admin_stats.html  # Panel de estadísticas
    └── *.html           # Otras páginas
```

## 🚀 **Instalación y Uso**

### **1. Clonar el repositorio**
```bash
git clone https://github.com/tu-usuario/inget_soport.git
cd inget_soport
```

### **2. Instalar dependencias**
```bash
pip install -r requirements.txt
```

### **3. Ejecutar la aplicación**
```bash
python app.py
```

### **4. Acceder al sitio**
```
http://localhost:5000
```

## 📊 **Sistema de Estadísticas**

### **Panel de Administración**
```
http://localhost:5000/admin/stats
```

### **API de Estadísticas**
```
http://localhost:5000/api/stats
```

### **Características:**
- ✅ Seguimiento automático de visitas
- ✅ Contador de visitantes únicos
- ✅ Páginas más visitadas
- ✅ Estadísticas por período
- ✅ Actualización en tiempo real

## 🎯 **Páginas del Sitio**

### **Páginas Principales:**
- **Inicio** (`/`) - Página principal con hero section
- **Nosotros** (`/nosotros`) - Información de la empresa
- **Servicios** (`/services`) - Catálogo de servicios
- **Contacto** (`/contact`) - Formulario de contacto

### **Páginas de Servicios:**
- **Desarrollo de Software** (`/services/software_development`)
- **Soporte Técnico** (`/services/technical_support`)
- **Consultoría** (`/services/consulting`)
- **Ciberseguridad** (`/services/cybersecurity`)
- **Redes y Telecomunicaciones** (`/services/network_telecom`)

### **Páginas Especiales:**
- **Blog/Ventas** (`/ventas`) - Contenido de ventas
- **Panel de Estadísticas** (`/admin/stats`) - Dashboard de visitas

## 🔧 **Configuración**

### **Variables de Entorno**
El sistema está configurado para usar Gmail SMTP. Asegúrate de tener configuradas las credenciales en `app.py`:

```python
sender_email = "tu-email@gmail.com"
password = "tu-contraseña-de-aplicación"
```

### **Base de Datos**
La base de datos SQLite se crea automáticamente al ejecutar la aplicación.

## 📱 **Responsive Design**

El sitio está completamente optimizado para:
- 📱 **Móviles** (320px+)
- 📱 **Tablets** (768px+)
- 🖥️ **Desktop** (1024px+)
- 🖥️ **Pantallas grandes** (1280px+)

## 🎨 **Características de Diseño**

- **Gradientes modernos** y efectos visuales
- **Animaciones CSS** suaves y profesionales
- **Iconos SVG** y Font Awesome
- **Tipografía optimizada** para legibilidad
- **Paleta de colores** profesional y coherente

## 🔒 **Seguridad**

- **Validación de formularios** en frontend y backend
- **Protección CSRF** en formularios
- **Sanitización de datos** de entrada
- **Base de datos segura** con SQLite

## 📈 **SEO Optimizado**

- **Meta tags** completos en todas las páginas
- **URLs amigables** y semánticas
- **Estructura HTML** semántica
- **Google Search Console** integrado
- **Sitemap** automático

## 🤝 **Contribuir**

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📞 **Contacto**

- **Email:** info@ingetsoport.com
- **WhatsApp:** +593 99 296 1062
- **Sitio Web:** [ingetsoport.com](https://ingetsoport.com)

## 📄 **Licencia**

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 🙏 **Agradecimientos**

- **Tailwind CSS** por el framework de diseño
- **Font Awesome** por los iconos
- **Flask** por el framework web
- **Comunidad Python** por el soporte

---

**¡Gracias por visitar INGETSOPORT! 🚀**

*Innovación y Gestión de Soporte Tecnológico* 