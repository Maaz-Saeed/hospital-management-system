from flask import Blueprint, render_template, session, redirect, url_for, flash
from models import ContactMessage, ChatbotLog, User
from functools import wraps

admin = Blueprint('admin', __name__, url_prefix='/admin')

def admin_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if 'user_id' not in session:
            flash('Please login first.', 'warning')
            return redirect(url_for('auth.login'))
        if session.get('user_role') != 'admin':
            flash('Access denied. Admin privileges required.', 'danger')
            return redirect(url_for('auth.dashboard'))
        return f(*args, **kwargs)
    return decorated

@admin.route('/')
@admin_required
def admin_dashboard():
    messages = ContactMessage.query.order_by(ContactMessage.timestamp.desc()).all()
    logs = ChatbotLog.query.order_by(ChatbotLog.timestamp.desc()).limit(50).all()
    users = User.query.all()
    return render_template('admin_dashboard.html',
                           messages=messages, logs=logs, users=users)
