from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from werkzeug.middleware.proxy_fix import ProxyFix
import os

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)

# إعدادات التطبيق
app.config['SECRET_KEY'] = os.getenv('SESSION_SECRET', 'dev_secret_key')

# إعداد قاعدة البيانات
DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///investments.db')
if DATABASE_URL.startswith('postgres://'):
    DATABASE_URL = DATABASE_URL.replace('postgres://', 'postgresql://')
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
csrf = CSRFProtect(app)

# استيراد الملفات الداخلية
from models import Investment, MetalPrice, ProfitScenario
import routes

# إنشاء الجداول في حالة عدم وجودها
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
