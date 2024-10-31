from PIL import ImageEnhance, Image

def convert_to_grayscale(input_path, output_path):
    """
    Converte a imagem para escala de cinza.
    
    :param input_path: Caminho da imagem original.
    :param output_path: Caminho para salvar a imagem em escala de cinza.
    """
    with Image.open(input_path) as img:
        grayscale_img = img.convert("L")
        grayscale_img.save(output_path)

def adjust_brightness(input_path, output_path, factor):
    """
    Ajusta o brilho da imagem.
    
    :param input_path: Caminho da imagem original.
    :param output_path: Caminho para salvar a imagem ajustada.
    :param factor: Fator de ajuste de brilho (1.0 = original, <1.0 = mais escuro, >1.0 = mais claro).
    """
    with Image.open(input_path) as img:
        enhancer = ImageEnhance.Brightness(img)
        bright_img = enhancer.enhance(factor)
        bright_img.save(output_path)