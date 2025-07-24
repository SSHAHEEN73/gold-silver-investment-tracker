from flask import Flask, render_template
from extensions import db, csrf
from routes import main_bp
import os

def create_app():
    app = Flask(__name__)

    # الإعدادات
    app.config['SECRET_KEY'] = 'your-secret-key'  # غيره لمفتاح قوي
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # تهيئة الإضافات
    db.init_app(app)
    csrf.init_app(app)

    # إنشاء الجداول عند تشغيل التطبيق
    with app.app_context():
        from models import Investment, MetalPrice, ProfitScenario
        db.create_all()

    # تسجيل المسارات
    app.register_blueprint(main_bp)

    # صفحة رئيسية
    @app.route('/')
    def home():
        return render_template('index.html')

    return app

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app = create_app()
    app.run(debug=True, host="0.0.0.0", port=port)
