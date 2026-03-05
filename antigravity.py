from browser import document, html

class Canvas:
    """
    Biblioteca de mock Antigravity para simular e simplificar o desenho em Canvas usando Python/Brython.
    """
    def __init__(self, width, height, parent=None):
        self.canvas = html.CANVAS(width=width, height=height)
        self.ctx = self.canvas.getContext('2d')
        
        # Anexa o elemento canvas ao DOM
        if parent is None:
            document <= self.canvas
        else:
            parent <= self.canvas
            
        self.width = width
        self.height = height

    def clear(self):
        """Limpa todo o quadro para desenhar o próximo frame."""
        self.ctx.clearRect(0, 0, self.width, self.height)

    def rectangle(self, x, y, width, height, fill="green"):
        """Desenha um retângulo."""
        self.ctx.fillStyle = fill
        self.ctx.fillRect(x, y, width, height)
        # Retorna os atributos
        return {"x": x, "y": y, "w": width, "h": height}
    
    def text(self, x, y, text_str, fill="black", font="20px Arial", align="left"):
        """Desenha texto na tela (usado para Game Over, etc)."""
        self.ctx.fillStyle = fill
        self.ctx.font = font
        self.ctx.textAlign = align
        # Para centralização vertical
        self.ctx.textBaseline = "middle"
        self.ctx.fillText(text_str, x, y)
