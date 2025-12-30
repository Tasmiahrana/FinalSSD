from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Configure the app
app.config['SECRET_KEY'] = 'your-secret-key-here'

@app.route('/')
def home():
    """Home page route"""
    return render_template('index.html')

@app.route('/api/health')
def health_check():
    """Health check endpoint for monitoring"""
    return jsonify({
        'status': 'healthy',
        'message': 'Flask app is running successfully!'
    }), 200

@app.route('/api/info')
def info():
    """Information endpoint"""
    return jsonify({
        'app_name': 'Flask CI/CD Demo',
        'version': '1.0.0',
        'description': 'A Flask application with Jenkins CI/CD pipeline'
    }), 200

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({'error': 'Not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    # Run the app
    app.run(host='0.0.0.0', port=5000, debug=True)