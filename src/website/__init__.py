from flask import Flask

#1 - Je créé l'app, lignes de codes non modifiables-----------------------------------------------------------
def create_app():
    app = Flask(__name__)

#2 - Je m'occupe des Blueprint--------------------------------------------------------------------------------
    #depuis la feuille "views" j'importe la variable views (qui contient le blueprint)
    from .views import views
    #J'enregistre ces Blueprint dans mon app
    app.register_blueprint(views, url_prefix="/")
    
    return app
