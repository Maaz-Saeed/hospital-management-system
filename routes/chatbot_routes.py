from flask import Blueprint, render_template, request, jsonify
from models import db, ChatbotLog
from datetime import datetime

chatbot = Blueprint('chatbot', __name__)

RESPONSES = {
    'departments': {
        'keywords': ['department', 'departments', 'specialty', 'specialties', 'ward'],
        'response': '🏥 Our hospital has the following departments:\n• Cardiology\n• Neurology\n• Orthopedics\n• Pediatrics\n• Oncology\n• Emergency & Trauma\n• General Surgery\n• Radiology\n• Pathology\n• Obstetrics & Gynecology'
    },
    'timings': {
        'keywords': ['timing', 'timings', 'hours', 'open', 'close', 'schedule', 'time'],
        'response': '⏰ Hospital Timings:\n• OPD: Monday–Saturday, 8:00 AM – 8:00 PM\n• Emergency: 24/7 (Always Open)\n• Lab & Radiology: 7:00 AM – 10:00 PM\n• Pharmacy: 24/7'
    },
    'emergency': {
        'keywords': ['emergency', 'urgent', 'ambulance', 'accident', 'critical'],
        'response': '🚨 Emergency Contact:\n• Emergency Hotline: +92-300-1234567\n• Ambulance: 1122\n• Emergency Room: Ground Floor, Building A\n• Available 24/7 — We are always here for you!'
    },
    'doctors': {
        'keywords': ['doctor', 'doctors', 'physician', 'specialist', 'appointment', 'available', 'availability'],
        'response': '👨‍⚕️ Doctor Availability:\n• OPD doctors are available Mon–Sat, 9 AM – 5 PM\n• To book an appointment, call: +92-21-9876543\n• Online booking is also available via our portal\n• Emergency doctors are on-call 24/7'
    },
    'location': {
        'keywords': ['location', 'address', 'where', 'directions', 'map', 'find'],
        'response': '📍 Our Location:\n• Address: 123 Medical Center Drive, Karachi, Pakistan\n• Near City Mall, Main Boulevard\n• Parking available on-site\n• GPS Coordinates: 24.8607° N, 67.0011° E'
    },
    'fees': {
        'keywords': ['fee', 'fees', 'cost', 'price', 'charges', 'payment'],
        'response': '💳 Fee Information:\n• Consultation fee: Rs. 500 – Rs. 2000 (varies by specialist)\n• Emergency fee: Rs. 1000\n• We accept cash, card, and insurance\n• Discounts available for senior citizens and low-income patients'
    },
    'insurance': {
        'keywords': ['insurance', 'insured', 'coverage', 'efu', 'jubilee'],
        'response': '🛡️ Insurance:\n• We are affiliated with major insurance providers\n• EFU Health, Jubilee Life, State Life, and more\n• Please bring your insurance card at the time of visit\n• For queries, contact our billing desk'
    },
    'hello': {
        'keywords': ['hello', 'hi', 'hey', 'greetings', 'good morning', 'good afternoon', 'good evening'],
        'response': '👋 Hello! Welcome to City General Hospital\'s virtual assistant.\n\nI can help you with:\n• Department information\n• Hospital timings\n• Emergency contacts\n• Doctor availability\n• Location & directions\n• Fee information\n\nHow can I assist you today?'
    },
    'thanks': {
        'keywords': ['thanks', 'thank you', 'thank', 'appreciate', 'helpful'],
        'response': '😊 You\'re welcome! Is there anything else I can help you with? Your health is our priority!'
    },
    'bye': {
        'keywords': ['bye', 'goodbye', 'see you', 'exit', 'quit'],
        'response': '👋 Goodbye! Take care and stay healthy. Visit us anytime at City General Hospital!'
    }
}

DEFAULT_RESPONSE = ("🤔 I'm sorry, I didn't quite understand that. You can ask me about:\n"
                    "• Hospital departments\n• Timings & hours\n• Emergency contacts\n"
                    "• Doctor availability\n• Our location\n• Fees & insurance\n\n"
                    "Type 'hello' to see a full list of topics!")


def get_bot_response(query: str) -> str:
    query_lower = query.lower().strip()
    for category, data in RESPONSES.items():
        for keyword in data['keywords']:
            if keyword in query_lower:
                return data['response']
    return DEFAULT_RESPONSE


@chatbot.route('/chatbot')
def chatbot_page():
    return render_template('chatbot.html')


@chatbot.route('/chatbot/message', methods=['POST'])
def chatbot_message():
    data = request.get_json()
    if not data or 'message' not in data:
        return jsonify({'error': 'Invalid request'}), 400

    user_query = data['message'].strip()
    if not user_query:
        return jsonify({'error': 'Empty message'}), 400

    bot_response = get_bot_response(user_query)

    log = ChatbotLog(user_query=user_query, bot_response=bot_response)
    db.session.add(log)
    db.session.commit()

    return jsonify({'response': bot_response, 'timestamp': datetime.utcnow().strftime('%H:%M')})
