class Config:
    DEBUG                = True
    SECRET_KEY           = 'your secret'

    MAIL_SERVER          = ''
    MAIL_PORT            =  587
    MAIL_USERNAME        = ''
    MAIL_PASSWORD        = ''
    MAIL_USE_TLS         = True
    MAIL_USE_SSL         = False
    MAIL_MAX_EMAILS      = 1  
    # ^^ because this app provides sending mail for individuals so they don't send bulk mail

    RECAPTCHA_PUBLIC_KEY = ''
    RECAPTCHA_PRIVATE_KEY= ''

class Production(Config):
    DEBUG  = False