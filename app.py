from flask import Flask, render_template, request, session, redirect, url_for, send_file
from utils.pdf_generator import generate_pdf
from content.chapters import ebook_content
from content.templates import get_petition_templates
from assets.images import get_image_urls, get_cover_image
from assets.logo import get_medindeniz_logo_svg, get_medindeniz_about
import base64
from io import BytesIO

app = Flask(__name__)
app.secret_key = 'medindeniz_secret_key_2025'

# Sistema de autenticação
def require_auth(f):
    def decorated(*args, **kwargs):
        if not session.get('autenticado'):
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    decorated.__name__ = f.__name__
    return decorated

@app.route('/')
def login():
    if session.get('autenticado'):
        return redirect(url_for('capa'))
    
    medindeniz_logo_url = get_medindeniz_logo_svg()
    
    if request.method == 'POST':
        senha = request.form.get('senha')
        if senha == "medindeniz2025":
            session['autenticado'] = True
            return redirect(url_for('capa'))
        else:
            return render_template('login.html', 
                                error="Senha incorreta", 
                                logo_url=medindeniz_logo_url)
    
    return render_template('login.html', logo_url=medindeniz_logo_url)

@app.route('/capa')
@require_auth
def capa():
    images = get_image_urls()
    medindeniz_info = get_medindeniz_about()
    return render_template('capa.html', 
                         cover_image=get_cover_image(),
                         ebook_content=ebook_content,
                         medindeniz_info=medindeniz_info,
                         images=images)

@app.route('/visualizar')
@require_auth
def visualizar():
    chapter_index = request.args.get('chapter', 0, type=int)
    if chapter_index >= len(ebook_content["chapters"]):
        chapter_index = 0
    
    chapter = ebook_content["chapters"][chapter_index]
    images = get_image_urls()
    medindeniz_info = get_medindeniz_about()
    
    return render_template('visualizar.html',
                         chapter=chapter,
                         chapter_index=chapter_index,
                         chapters=ebook_content["chapters"],
                         ebook_content=ebook_content,
                         images=images,
                         medindeniz_info=medindeniz_info)

@app.route('/baixar-pdf')
@require_auth
def baixar_pdf():
    try:
        pdf_data = generate_pdf(
            ebook_content["title"],
            ebook_content["author_name"],
            ebook_content
        )
        
        if pdf_data:
            pdf_bytes = base64.b64decode(pdf_data)
            return send_file(
                BytesIO(pdf_bytes),
                download_name="Ebook_Indenizacao_Erro_Medico.pdf",
                as_attachment=True,
                mimetype='application/pdf'
            )
    except Exception as e:
        return f"Erro ao gerar PDF: {str(e)}", 500

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
