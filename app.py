from flask import Flask, render_template, request, session, redirect, url_for
import os

app = Flask(__name__)
app.secret_key = 'medindeniz_secret_key_2025'

# Conteúdo do e-book
chapters = [
    {
        'title': 'Introdução ao Erro Médico',
        'content': 'Bem-vindo ao guia completo sobre indenização por erro médico...'
    },
    {
        'title': 'Capítulo 1: Identificação',
        'content': 'Como identificar um erro médico...'
    },
    {
        'title': 'Capítulo 2: Cálculos',
        'content': 'Parâmetros para cálculo de indenizações...'
    }
]

@app.route('/', methods=['GET', 'POST'])
def login():
    if session.get('authenticated'):
        return redirect('/home')
    
    if request.method == 'POST':
        password = request.form.get('password')
        if password == "medindeniz2025":
            session['authenticated'] = True
            return redirect('/home')
        else:
            return render_template('login.html', error="Senha incorreta")
    
    return render_template('login.html')

@app.route('/home')
def home():
    if not session.get('authenticated'):
        return redirect('/')
    return render_template('home.html', chapters=chapters)

@app.route('/chapter/<int:chapter_id>')
def chapter(chapter_id):
    if not session.get('authenticated'):
        return redirect('/')
    
    if chapter_id < 0 or chapter_id >= len(chapters):
        return redirect('/home')
    
    chapter_data = chapters[chapter_id]
    return render_template('chapter.html', 
                         chapter=chapter_data, 
                         chapter_id=chapter_id,
                         total_chapters=len(chapters))

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
