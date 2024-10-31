from PIL import Image

def resize_image(input_path, output_path, size):
    """
    Redimensiona a imagem para o tamanho especificado.
    
    :param input_path: Caminho da imagem original.
    :param output_path: Caminho para salvar a imagem redimensionada.
    :param size: Tuple com (largura, altura).
    """
    with Image.open(input_path) as img:
        resized_img = img.resize(size)
        resized_img.save(output_path)