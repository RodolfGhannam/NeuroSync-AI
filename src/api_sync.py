import logging
from typing import Dict, Any, Tuple
from flask import Flask, request, jsonify
from werkzeug.exceptions import BadRequest

# Configure production-grade logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("NeuroSync-API")

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health_check() -> Tuple[Dict[str, Any], int]:
    """
    Health check endpoint for Kubernetes/Docker deployment monitoring.
    """
    return jsonify({
        "status": "healthy",
        "version": "1.0.0",
        "artifact": "NeuroSync AI",
        "layer": "Synchronous (C-CARE Protocol)"
    }), 200

@app.route('/api/v1/sync_affective_state', methods=['POST'])
def sync_affective_state() -> Tuple[Dict[str, Any], int]:
    """
    Synchronous Layer (C-CARE Protocol):
    Receives real-time affective data (e.g., from Hume EVI) and dynamically calibrates 
    the conversational agent's anthropomorphism level.
    
    Theoretical Anchor: 
    Prevents the "Trojan Horse" effect (Uysal et al., 2024) by ensuring high-stress 
    users receive functional, low-cognitive-load responses rather than fake empathy.
    """
    try:
        if not request.is_json:
            raise BadRequest("Payload must be a valid JSON")
            
        data = request.get_json()
        session_id = data.get('session_id')
        
        if not session_id:
            raise BadRequest("Missing required field: 'session_id'")
            
        # Extract stress level (0.0 = relaxed, 1.0 = highly stressed/frustrated)
        user_stress_level = float(data.get('stress_level', 0.0))
        
        # Validate input bounds
        if not (0.0 <= user_stress_level <= 1.0):
            raise ValueError("stress_level must be between 0.0 and 1.0")
        
        # C-CARE Logic: Dynamic Anthropomorphism Modulation
        # Inverse relationship: High stress demands lower anthropomorphism (functional focus)
        # Low stress allows higher anthropomorphism (affective warmth)
        anthropomorphism_level = max(0.1, 1.0 - user_stress_level)
        
        logger.info(f"Session {session_id}: Stress={user_stress_level:.2f} -> AnthroLevel={anthropomorphism_level:.2f}")
        
        response_payload = {
            "session_id": session_id,
            "recommended_anthropomorphism_level": round(anthropomorphism_level, 2),
            "action": "calibrate_tone",
            "metadata": {
                "theory_anchor": "Trojan Horse Effect (Uysal et al., 2024)",
                "mechanism": "Affective State Calibration"
            }
        }
        
        return jsonify(response_payload), 200
        
    except BadRequest as e:
        logger.warning(f"Bad Request: {str(e)}")
        return jsonify({"error": "Bad Request", "message": str(e)}), 400
    except ValueError as e:
        logger.warning(f"Validation Error: {str(e)}")
        return jsonify({"error": "Validation Error", "message": str(e)}), 422
    except Exception as e:
        logger.error(f"Internal Server Error processing affective state: {str(e)}")
        return jsonify({"error": "Internal Server Error"}), 500

if __name__ == '__main__':
    # Fallback for local development. In production, use Gunicorn (see Dockerfile).
    app.run(host='0.0.0.0', port=5000, debug=False)
