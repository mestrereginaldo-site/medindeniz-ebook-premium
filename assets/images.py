# URLs para imagens utilizadas no e-book sobre Erro Médico

def get_image_urls():
    """
    Retorna URLs para imagens usadas na aplicação
    
    Returns:
        dict: Dicionário contendo URLs de imagens por categoria
    """
    images = {
        "medical_error": [
            "https://images.pexels.com/photos/4173251/pexels-photo-4173251.jpeg?auto=compress&cs=tinysrgb&w=800",  # Médico com máscara
            "https://images.pexels.com/photos/236380/pexels-photo-236380.jpeg?auto=compress&cs=tinysrgb&w=800",  # Hospital
            "https://images.pexels.com/photos/3259629/pexels-photo-3259629.jpeg?auto=compress&cs=tinysrgb&w=800",  # Médico com estetoscópio
            "https://images.pexels.com/photos/263337/pexels-photo-263337.jpeg?auto=compress&cs=tinysrgb&w=800"    # Sala de operação
        ],
        "legal_documents": [
            "https://images.pexels.com/photos/5668473/pexels-photo-5668473.jpeg?auto=compress&cs=tinysrgb&w=800",   # Martelo de juiz
            "https://images.pexels.com/photos/159832/justice-law-case-hearing-159832.jpeg?auto=compress&cs=tinysrgb&w=800",   # Livros jurídicos
            "https://images.pexels.com/photos/5668481/pexels-photo-5668481.jpeg?auto=compress&cs=tinysrgb&w=800",   # Balança da justiça
            "https://images.pexels.com/photos/4439901/pexels-photo-4439901.jpeg?auto=compress&cs=tinysrgb&w=800"    # Documentos legais
        ],
        "doctor_patient": [
            "https://images.pexels.com/photos/5327585/pexels-photo-5327585.jpeg?auto=compress&cs=tinysrgb&w=800",   # Consulta médica
            "https://images.pexels.com/photos/7089401/pexels-photo-7089401.jpeg?auto=compress&cs=tinysrgb&w=800",   # Médico com paciente
            "https://images.pexels.com/photos/4167541/pexels-photo-4167541.jpeg?auto=compress&cs=tinysrgb&w=800",   # Médico explicando diagnóstico
            "https://images.pexels.com/photos/7579831/pexels-photo-7579831.jpeg?auto=compress&cs=tinysrgb&w=800"    # Hospital com médico e paciente
        ],
        "law_office": [
            "https://images.pexels.com/photos/5668858/pexels-photo-5668858.jpeg?auto=compress&cs=tinysrgb&w=800",   # Escritório de advocacia
            "https://images.pexels.com/photos/8867433/pexels-photo-8867433.jpeg?auto=compress&cs=tinysrgb&w=800",   # Advogado trabalhando
            "https://images.pexels.com/photos/8867482/pexels-photo-8867482.jpeg?auto=compress&cs=tinysrgb&w=800",   # Sala de reuniões jurídicas
            "https://images.pexels.com/photos/159832/justice-law-case-hearing-159832.jpeg?auto=compress&cs=tinysrgb&w=800"    # Biblioteca jurídica
        ]
    }
    
    return images

def get_cover_image():
    """
    Retorna URL para a imagem de capa do e-book
    
    Returns:
        str: URL da imagem de capa
    """
    return "https://images.pexels.com/photos/5668481/pexels-photo-5668481.jpeg?auto=compress&cs=tinysrgb&w=800"  # Martelo de juiz com balança

def get_author_image():
    """
    Retorna URL para a imagem do perfil do autor
    
    Returns:
        str: URL da imagem do autor
    """
    return "https://images.pexels.com/photos/5588215/pexels-photo-5588215.jpeg?auto=compress&cs=tinysrgb&w=400"  # Homem de terno (advogado)
