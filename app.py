from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from routes import main_bp
import os

# إنشاء التطبيق
app = Flask(__name__)

# إعدادات
app.config['SECRET_KEY'] = 'your-secret-key'  # غيّرها بمفتاحك الخاص
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# التهيئة
db = SQLAlchemy(app)
csrf = CSRFProtect(app)

# استدعاء الموديلات
from models import Investment, MetalPrice, ProfitScenario

# تسجيل Blueprint
app.register_blueprint(main_bp)

# إنشاء الجداول إذا لم تكن موجودة
with app.app_context():
    db.create_all()

# صفحة رئيسية بسيطة
@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
