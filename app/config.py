class Config:
    DEBUG = False  # Valor por defecto desactivado

class DevelopmentConfig(Config):
    DEBUG = True # Activa el modo depuración
    
config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}
