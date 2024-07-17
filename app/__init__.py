from flask import Flask, render_template, send_file

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)  # Aplica la configuración
    
    @app.route('/')
    def index():
        return render_template("index.html")
    
    @app.route('/download')
    def download_file():
        path = 'static/pdf/resume.pdf'
        return send_file(path, as_attachment=True)

    @app.route('/view')
    def view_file():
        path = 'static/pdf/resume.pdf'
        return send_file(path)
    
    return app


