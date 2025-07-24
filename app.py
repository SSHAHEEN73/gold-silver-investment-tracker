from flask import Flask, render_template
from extensions import db, csrf
from routes import main_bp
import os

def create_app():
    app = Flask(__name__)

    # إعدادات
    app.config['SECRET_KEY'] = 'your-secret-key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # تهيئة الإضافات
    db.init_app(app)
    csrf.init_app(app)

    # استدعاء الموديلات
    from models import Investment, MetalPrice, ProfitScenario

    # تسجيل Blueprint
    app.register_blueprint(main_bp)

    # إنشاء الجداول
    with app.app_context():
        db.create_all()

    @app.route('/')
    def home():
        return render_template('index.html')

    return app
