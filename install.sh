#!/bin/bash
# Script de instalação para o aplicativo MedIndeniz

# Verifica se o python está instalado
if ! command -v python3 &> /dev/null; then
    echo "Python não encontrado. Por favor, instale o Python 3.8 ou superior."
    exit 1
fi

# Criar ambiente virtual (opcional)
echo "Criando ambiente virtual..."
python3 -m venv venv
source venv/bin/activate

# Instalar dependências
echo "Instalando dependências..."
pip install streamlit==1.35.0 psycopg2-binary==2.9.9 reportlab==4.1.0 sqlalchemy==2.0.28 trafilatura==1.6.4

# Criar diretório .streamlit se não existir
mkdir -p .streamlit

# Verificar se config.toml existe, se não existir, criar
if [ ! -f .streamlit/config.toml ]; then
    echo "Criando arquivo de configuração do Streamlit..."
    cat > .streamlit/config.toml << EOL
[server]
headless = true
address = "0.0.0.0"
port = 5000

[browser]
gatherUsageStats = false

[theme]
primaryColor = "#1E64C8"
backgroundColor = "#FFFFFF"
secondaryBackgroundColor = "#F0F2F6"
textColor = "#333333"
font = "sans serif"
EOL
fi

echo "Instalação concluída com sucesso!"
echo "Para iniciar o aplicativo, execute: streamlit run app.py"