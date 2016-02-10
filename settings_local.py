DATABASE_ENGINE = 'mysql'         
DATABASE_NAME = 'logoclon'            
DATABASE_USER = 'root'            
DATABASE_PASSWORD = 'ser ver 2'   

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('rdoroshko', 'rdoroshko@gmail.com'),
)

MANAGERS = ADMINS

DEFAULT_VARS = {
    'phone': '(495) 649-83-65',
    'buyColCount': 3,
    'emailFaq': 'info@2orange.com',
    'emailContact': 'info@2orange.com',
}