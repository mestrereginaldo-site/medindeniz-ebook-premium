from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle, PageBreak
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER, TA_LEFT, TA_RIGHT
from reportlab.lib.units import cm, mm
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from io import BytesIO
import base64
import streamlit as st

# Register fonts - Using default fonts as fallback if custom fonts not available
try:
    pdfmetrics.registerFont(TTFont('DejaVuSans', 'DejaVuSans.ttf'))
    pdfmetrics.registerFont(TTFont('DejaVuSans-Bold', 'DejaVuSans-Bold.ttf'))
except:
    # If custom fonts not found, use standard fonts
    pass

class PDFGenerator:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.buffer = BytesIO()
        self.doc = SimpleDocTemplate(
            self.buffer,
            pagesize=A4,
            rightMargin=72,
            leftMargin=72,
            topMargin=72,
            bottomMargin=72,
            title=title,
            author=author
        )
        
        self.styles = getSampleStyleSheet()
        self._add_custom_styles()
        self.elements = []
        
    def _add_custom_styles(self):
        """Add custom paragraph styles for the document"""
        # Usando fontes padrão do ReportLab de forma adequada para documentos jurídicos
        default_font = 'Helvetica'
        default_bold_font = 'Helvetica-Bold'
        
        # Limpar qualquer estilo existente
        styles = getSampleStyleSheet()
        
        # Cor principal para títulos e elementos de destaque
        main_color = colors.HexColor('#1E64C8')  # Azul jurídico
        
        # Definir estilos personalizados com nomes únicos e formato jurídico adequado
        
        # Estilo para a capa - título principal
        self.styles.add(ParagraphStyle(
            name='EbookCoverTitle',
            parent=styles['Heading1'],
            fontSize=24,  # Fonte maior para o título
            leading=32,   # Espaçamento entre linhas de 1.33
            alignment=TA_CENTER,
            textColor=colors.white,
            backColor=main_color,  # Fundo azul
            borderPadding=12,      # Padding
            spaceAfter=24,
            fontName=default_bold_font
        ))
        
        # Estilo para títulos de capítulos com destaque visual
        self.styles.add(ParagraphStyle(
            name='EbookChapterTitle',
            parent=styles['Heading2'],
            fontSize=18,
            leading=27,  # Espaçamento entre linhas de 1.5
            alignment=TA_LEFT,
            textColor=main_color,
            borderColor=main_color,
            borderWidth=0,
            borderPadding=5,
            borderRadius=5,
            spaceAfter=20,
            spaceBefore=20,
            fontName=default_bold_font
        ))
        
        # Estilo para subtítulos com destaque visual
        self.styles.add(ParagraphStyle(
            name='EbookSubHeading',
            parent=styles['Heading3'],
            fontSize=16,
            leading=24,  # Espaçamento entre linhas de 1.5
            alignment=TA_LEFT,
            textColor=main_color,
            spaceAfter=12,
            spaceBefore=15,
            fontName=default_bold_font
        ))
        
        # Estilo para texto normal com espaçamento jurídico
        self.styles.add(ParagraphStyle(
            name='EbookBodyText',
            parent=styles['Normal'],
            fontSize=12,       # Tamanho maior e mais legível
            leading=18,       # Espaçamento entre linhas de 1.5 (padrão jurídico)
            alignment=TA_JUSTIFY,
            firstLineIndent=20,  # Indentação de primeira linha
            spaceBefore=3,     # Reduzido para diminuir espaço em branco
            spaceAfter=3,      # Reduzido para diminuir espaço em branco
            fontName=default_font
        ))
        
        # Estilo para citações e destaques
        self.styles.add(ParagraphStyle(
            name='EbookQuote',
            parent=styles['Normal'],
            fontSize=11,
            leading=16.5,     # Espaçamento entre linhas de 1.5
            alignment=TA_JUSTIFY,
            leftIndent=30,
            rightIndent=30,
            spaceBefore=12,
            spaceAfter=12,
            borderWidth=1,
            borderColor=colors.lightgrey,
            borderPadding=8,
            borderRadius=5,
            fontName=default_font,
            textColor=colors.darkgrey
        ))
        
        # Estilo para marcadores (bullets)
        self.styles.add(ParagraphStyle(
            name='EbookBulletPoint',
            parent=styles['Normal'],
            fontSize=12,
            leading=18,       # Espaçamento entre linhas de 1.5
            leftIndent=40,
            firstLineIndent=-20,  # Espaço para o marcador
            spaceBefore=3,
            spaceAfter=3,
            bulletIndent=20,
            fontName=default_font
        ))
        
        # Estilo para células de tabela
        self.styles.add(ParagraphStyle(
            name='EbookTableCell',
            parent=styles['Normal'],
            fontSize=11,
            leading=15,
            alignment=TA_LEFT,
            fontName=default_font
        ))
        
        # Estilo para cabeçalho de tabela
        self.styles.add(ParagraphStyle(
            name='EbookTableHeader',
            parent=styles['Normal'],
            fontSize=12,
            leading=16,
            alignment=TA_CENTER,
            textColor=colors.white,
            fontName=default_bold_font
        ))
        
        # Estilo para avisos e informações importantes
        self.styles.add(ParagraphStyle(
            name='EbookWarning',
            parent=styles['Normal'],
            fontSize=12,
            leading=18,
            alignment=TA_LEFT,
            backColor=colors.HexColor('#FFF8E6'),  # Fundo amarelo claro
            borderColor=colors.HexColor('#FFB200'),  # Borda amarela
            borderWidth=1,
            borderPadding=10,
            spaceBefore=12,
            spaceAfter=12,
            fontName=default_font
        ))
        
        # Estilo para dicas e blocos de destaque
        self.styles.add(ParagraphStyle(
            name='EbookTip',
            parent=styles['Normal'],
            fontSize=12,
            leading=18,
            alignment=TA_LEFT,
            backColor=colors.HexColor('#E8F0FE'),  # Fundo azul claro
            borderColor=main_color,  # Borda azul
            borderWidth=1,
            borderPadding=10,
            spaceBefore=12,
            spaceAfter=12,
            fontName=default_font
        ))
        
        # Estilo para rodapé
        self.styles.add(ParagraphStyle(
            name='EbookFooter',
            parent=styles['Normal'],
            fontSize=9,
            leading=12,
            textColor=colors.gray,
            alignment=TA_CENTER,
            fontName=default_font
        ))
    
    def add_cover_page(self, title, subtitle, author_name, author_title):
        """Add a cover page to the document"""
        # Cores corporativas para a capa
        main_color = colors.HexColor('#1E64C8')  # Azul principal
        accent_color = colors.HexColor('#E0E9F5')  # Azul claro para detalhes
        
        # Cabeçalho com o nome da marca em vez da barra azul sem texto
        header_style = ParagraphStyle(
            name='HeaderStyle',
            parent=self.styles['EbookCoverTitle'],
            fontSize=22,
            leading=28,
            alignment=TA_CENTER,
            textColor=colors.white,
            backColor=main_color,
            borderPadding=15,
        )
        header_data = [[Paragraph("MedIndeniz", header_style)]]
        header = Table(header_data, colWidths=[self.doc.width], rowHeights=[1.5*cm])
        header.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, -1), main_color),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ]))
        self.elements.append(header)
        
        # Espaço antes do título
        self.elements.append(Spacer(1, 2*cm))
        
        # Título principal em destaque com borda e fundo
        title_style = ParagraphStyle(
            name='CoverTitle',
            parent=self.styles['EbookCoverTitle'],
            fontSize=26,
            leading=32,
            alignment=TA_CENTER,
            textColor=colors.white,
            backColor=main_color,
            borderPadding=15,
            spaceAfter=30,
        )
        self.elements.append(Paragraph(title, title_style))
        
        # Subtítulo 
        subtitle_style = ParagraphStyle(
            name='CoverSubtitle',
            parent=self.styles['EbookSubHeading'],
            fontSize=16,
            leading=24,
            alignment=TA_CENTER,
            textColor=colors.darkblue,
            spaceAfter=20,
        )
        self.elements.append(Spacer(1, 0.8*cm))
        self.elements.append(Paragraph(subtitle, subtitle_style))
        
        # Informação do ano e edição
        year_style = ParagraphStyle(
            name='CoverYear',
            parent=self.styles['EbookBodyText'],
            fontSize=14,
            alignment=TA_CENTER,
            textColor=colors.darkgrey,
        )
        self.elements.append(Spacer(1, 1*cm))
        self.elements.append(Paragraph("Edição 2025 - Atualizada com jurisprudência recente", year_style))
        
        # Espaço antes da informação do autor
        self.elements.append(Spacer(1, 4*cm))
        
        # Informações do autor em um box destacado
        author_box_data = [[
            Paragraph(author_name, ParagraphStyle(
                name='AuthorName',
                parent=self.styles['EbookChapterTitle'],
                fontSize=18,
                alignment=TA_CENTER,
                textColor=main_color,
            )),
        ], [
            Paragraph(author_title, ParagraphStyle(
                name='AuthorTitle',
                parent=self.styles['EbookBodyText'],
                fontSize=14,
                alignment=TA_CENTER,
                textColor=colors.darkgrey,
            )),
        ]]
        
        # Criar tabela para o box do autor
        author_box = Table(author_box_data, colWidths=[400])
        author_box.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, -1), accent_color),
            ('TEXTCOLOR', (0, 0), (0, 0), main_color),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 10),
            ('TOPPADDING', (0, 0), (-1, -1), 10),
            ('BOX', (0, 0), (-1, -1), 1, colors.lightgrey),
            ('ROUNDEDCORNERS', [10, 10, 10, 10]),
        ]))
        
        # Centralizar a tabela do autor na página
        author_table = Table([[author_box]], colWidths=[self.doc.width])
        author_table.setStyle(TableStyle([
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ]))
        
        self.elements.append(author_table)
        
        # Rodapé da capa
        self.elements.append(Spacer(1, 3*cm))
        footer_style = ParagraphStyle(
            name='CoverFooter',
            parent=self.styles['EbookFooter'],
            fontSize=10,
            alignment=TA_CENTER,
            textColor=colors.darkgrey,
        )
        self.elements.append(Paragraph("Todos os direitos reservados © 2025", footer_style))
        
        # Quebra de página após a capa
        self.elements.append(PageBreak())
    
    def add_chapter(self, title, content_elements, is_first_chapter=False):
        """Add a chapter to the document"""
        # Apenas adiciona quebra de página se não for o primeiro capítulo
        if not is_first_chapter:
            self.elements.append(PageBreak())
        
        # Adiciona um pequeno espaço antes do título
        self.elements.append(Spacer(1, 0.5*cm))
                
        # Título do capítulo com formatação aprimorada
        self.elements.append(Paragraph(title, self.styles['EbookChapterTitle']))
        
        # Linha horizontal sutil abaixo do título (substitui a barra azul por uma linha mais elegante)
        subtitle_line = Table([['']], colWidths=[self.doc.width * 0.8])
        subtitle_line.setStyle(TableStyle([
            ('LINEBELOW', (0, 0), (-1, -1), 0.5, colors.HexColor('#1E64C8')),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
            ('TOPPADDING', (0, 0), (-1, -1), 5),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ]))
        self.elements.append(subtitle_line)
        
        # Pequeno espaço após a linha
        self.elements.append(Spacer(1, 0.3*cm))
        
        # Processa os elementos do conteúdo com melhor formatação
        for element in content_elements:
            if isinstance(element, dict):
                if element['type'] == 'paragraph':
                    self.elements.append(Paragraph(element['text'], self.styles['EbookBodyText']))
                    # Sem espaçamento adicional para manter o espaçamento 1.5 consistente
                
                elif element['type'] == 'subheading':
                    # Adiciona espaço antes dos subtítulos
                    self.elements.append(Spacer(1, 0.4*cm))
                    self.elements.append(Paragraph(element['text'], self.styles['EbookSubHeading']))
                    self.elements.append(Spacer(1, 0.2*cm))
                
                elif element['type'] == 'bullet':
                    # Formata marcadores com símbolos mais modernos
                    self.elements.append(Paragraph(f"• {element['text']}", self.styles['EbookBulletPoint']))
                
                elif element['type'] == 'quote':
                    # Citações em estilo de bloco com formatação especial
                    self.elements.append(Spacer(1, 0.3*cm))
                    self.elements.append(Paragraph(f"\"{element['text']}\"", self.styles['EbookQuote']))
                    if 'source' in element:
                        source_text = f"— {element['source']}"
                        self.elements.append(Paragraph(source_text, self.styles['EbookQuote']))
                    self.elements.append(Spacer(1, 0.3*cm))
                
                elif element['type'] == 'warning':
                    # Avisos importantes em um bloco destacado
                    self.elements.append(Spacer(1, 0.3*cm))
                    self.elements.append(Paragraph(f"⚠️ {element['text']}", self.styles['EbookWarning']))
                    self.elements.append(Spacer(1, 0.3*cm))
                
                elif element['type'] == 'tip':
                    # Dicas e informações úteis em um bloco destacado
                    self.elements.append(Spacer(1, 0.3*cm))
                    self.elements.append(Paragraph(f"💡 {element['text']}", self.styles['EbookTip']))
                    self.elements.append(Spacer(1, 0.3*cm))
                
                elif element['type'] == 'spacer':
                    # Espaçador personalizável
                    self.elements.append(Spacer(1, element.get('size', 0.5)*cm))
                
                elif element['type'] == 'table' and 'data' in element:
                    # Adiciona título da tabela se existir
                    if 'title' in element:
                        self.elements.append(Paragraph(element['title'], self.styles['EbookSubHeading']))
                        self.elements.append(Spacer(1, 0.3*cm))
                    
                    # Tabelas com estilos aprimorados
                    self._add_table(element['data'], element.get('col_widths', None))
                    
                elif element['type'] == 'jurisprudence':
                    # Formatação especial para citações de jurisprudência
                    self.elements.append(Spacer(1, 0.4*cm))
                    
                    # Caixa para jurisprudência com fundo colorido
                    jur_style = ParagraphStyle(
                        name='EbookJurisprudence',
                        parent=self.styles['EbookBodyText'],
                        fontSize=11,
                        leading=16.5,
                        alignment=TA_JUSTIFY,
                        leftIndent=20,
                        rightIndent=20,
                        spaceBefore=10,
                        spaceAfter=10,
                        borderWidth=1,
                        borderColor=colors.HexColor('#E0E9F5'),
                        borderPadding=8,
                        backColor=colors.HexColor('#F8FAFD')
                    )
                    
                    # Adiciona a jurisprudência em destaque
                    self.elements.append(Paragraph(element['text'], jur_style))
                    
                    # Adiciona fonte da jurisprudência em itálico
                    if 'source' in element:
                        source_style = ParagraphStyle(
                            name='EbookJurisprudenceSource',
                            parent=self.styles['EbookBodyText'],
                            fontSize=10,
                            textColor=colors.darkblue,
                            alignment=TA_RIGHT,
                        )
                        self.elements.append(Paragraph(element['source'], source_style))
                    
                    self.elements.append(Spacer(1, 0.4*cm))
                
            else:
                # Se o elemento for apenas texto, adicionar como parágrafo normal
                self.elements.append(Paragraph(element, self.styles['EbookBodyText']))
        
        # Linha horizontal sutil para marcar o final do capítulo (opcional)
        end_line = Table([['']], colWidths=[self.doc.width * 0.5])
        end_line.setStyle(TableStyle([
            ('LINEBELOW', (0, 0), (-1, -1), 0.3, colors.lightgrey),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
            ('TOPPADDING', (0, 0), (-1, -1), 5),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ]))
        self.elements.append(Spacer(1, 0.3*cm))
        self.elements.append(end_line)
    
    def _add_table(self, data, col_widths=None):
        """Helper method to add a table to the document"""
        # Process table data to ensure all cells are Paragraph objects
        processed_data = []
        for row in data:
            processed_row = []
            for cell in row:
                if isinstance(cell, str):
                    processed_row.append(Paragraph(cell, self.styles['EbookTableCell']))
                else:
                    processed_row.append(cell)
            processed_data.append(processed_row)
        
        # Create the table
        if col_widths:
            table = Table(processed_data, colWidths=col_widths)
        else:
            table = Table(processed_data)
        
        # Usar fonte padrão para evitar problemas
        table_header_font = 'Helvetica-Bold'
            
        # Style the table
        style = TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#E0E9F5')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.HexColor('#1E64C8')),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (-1, 0), table_header_font),
            ('FONTSIZE', (0, 0), (-1, 0), 10),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.white),
            ('GRID', (0, 0), (-1, -1), 1, colors.lightgrey),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('PADDING', (0, 0), (-1, -1), 6),
        ])
        table.setStyle(style)
        
        self.elements.append(table)
        self.elements.append(Spacer(1, 0.5*cm))
    
    def add_footer(self, text):
        """Add footer text to the document"""
        # Remover o texto do rodapé para evitar duplicação com o rodapé automático
        # Esse método é mantido vazio para compatibilidade com o código existente
    
    def build(self):
        """Build the PDF document and return it as base64 encoded string"""
        # Adicionar rodapé, marca d'água e proteção contra cópia em todas as páginas
        def add_page_number(canvas, doc):
            # Dimensões da página
            page_width = doc.pagesize[0]
            page_height = doc.pagesize[1]
            
            # PROTEÇÃO CONTRA CÓPIA - Adiciona uma camada invisível que dificulta a seleção de texto
            # Isso não é 100% seguro, mas funciona para a maioria dos leitores PDF
            canvas.saveState()
            # Cor totalmente transparente para não ser visível
            canvas.setFillColor(colors.Color(0, 0, 0, alpha=0))
            # Caracteres aleatórios por toda a página para confundir software de OCR
            for i in range(0, int(page_height), 10):
                for j in range(0, int(page_width), 5):
                    if (i + j) % 7 == 0:  # Padrão esparso
                        canvas.drawString(j, i, "×")
            canvas.restoreState()
            
            # MARCA D'ÁGUA 
            canvas.saveState()
            # Definir fonte e tamanho para a marca d'água
            canvas.setFont("Helvetica-Bold", 48)
            # Cor semi-transparente
            canvas.setFillColor(colors.Color(0, 0, 0, alpha=0.07))  # Cinza muito claro, quase invisível
            # Rotacionar o canvas
            canvas.translate(page_width/2, page_height/2)
            canvas.rotate(45)
            # Texto da marca d'água
            watermark_text = "MedIndeniz"
            # Calcular largura do texto para centralizar
            watermark_width = canvas.stringWidth(watermark_text, "Helvetica-Bold", 48)
            # Desenhar a marca d'água
            canvas.drawString(-watermark_width/2, 0, watermark_text)
            canvas.restoreState()
            
            # RODAPÉ
            # Definir fonte e tamanho para o rodapé
            canvas.setFont("Helvetica", 8)
            canvas.setFillColor(colors.grey)
            
            # Posicionamento do texto
            x = 30
            
            # Adicionar texto do rodapé em duas linhas
            canvas.drawString(x, 30, "© 2025 MedIndeniz - Todos os direitos reservados")
            canvas.drawString(x, 20, "Este material tem caráter informativo e não substitui a consulta a um advogado especializado.")
            
            # Adicionar número de página
            canvas.drawRightString(page_width - 30, 30, f"Página {doc.page}")
            
        # Construir o documento com o rodapé e marca d'água em cada página
        self.doc.build(self.elements, onFirstPage=add_page_number, onLaterPages=add_page_number)
        
        pdf_data = self.buffer.getvalue()
        self.buffer.close()
        return base64.b64encode(pdf_data).decode('utf-8')

def generate_pdf(title, author, content):
    """
    Generate a PDF document with the given content
    
    Args:
        title (str): The document title
        author (str): The document author
        content (dict): Dictionary containing content elements
    
    Returns:
        str: Base64 encoded PDF document
    """
    try:
        generator = PDFGenerator(title, author)
        
        # Add cover page
        generator.add_cover_page(
            content['title'],
            content['subtitle'],
            content['author_name'],
            content['author_title']
        )
        
        # Add chapters - primeiro capítulo sem quebra de página
        first_chapter = True
        for chapter in content['chapters']:
            generator.add_chapter(
                chapter['title'], 
                chapter['content'],
                is_first_chapter=first_chapter
            )
            first_chapter = False  # apenas o primeiro capítulo tem flag True
        
        # Add footer
        generator.add_footer(content['footer'])
        
        # Build and return the PDF
        return generator.build()
    except Exception as e:
        st.error(f"Erro ao gerar PDF: {str(e)}")
        return None

def get_pdf_download_link(pdf_data, filename, text):
    """
    Generate a download link for the PDF document
    
    Args:
        pdf_data (str): Base64 encoded PDF data
        filename (str): Name of the file for download
        text (str): Text to display on the download button
    
    Returns:
        str: HTML link for downloading the PDF
    """
    # Adicionando atributos para restringir funcionalidades no PDF baixado
    # O atributo data-no-copy ajuda a indicar que não deve ser copiado (apenas indicativo)
    current_date = "24/04/2025"  # Data fixa para fins de demonstração
    # Botão estilizado com classe para CSS personalizado
    href = f'''
    <div style="text-align:center; margin:20px 0;">
        <a href="data:application/pdf;base64,{pdf_data}" 
           download="{filename}" 
           style="background-color:#1E64C8; color:white; padding:10px 15px; 
                  text-decoration:none; border-radius:5px; font-weight:bold;"
           data-content-protection="true"
           data-no-copy="true"
           data-document-date="{current_date}">
           {text}
        </a>
        <p style="color:#666; font-size:12px; margin-top:8px;">
            PDF com marca d'água e proteção contra cópia
        </p>
    </div>
    '''
    return href
