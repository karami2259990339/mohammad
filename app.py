from flask import Flask, render_template, jsonify

app = Flask(__name__)

bones_data = {
    "skull": {
        "title": "Skull",
        "count": "22 bones",
        "description": "The skull is made of 22 bones that protect the brain. It includes the cranial bones and facial bones."
    },
    "spine": {
        "title": "Spine (Vertebral Column)",
        "count": "33 vertebrae",
        "description": "The spine consists of 33 vertebrae and protects the spinal cord. It is divided into cervical, thoracic, lumbar, sacral, and coccygeal regions."
    },
    "arm": {
        "title": "Arm and Hand Bones",
        "count": "30 bones in each arm",
        "description": "Includes the humerus (upper arm), radius and ulna (forearm), carpal bones (wrist), and the bones of the hand and fingers."
    },
    "leg": {
        "title": "Leg and Foot Bones",
        "count": "30 bones in each leg",
        "description": "Includes the femur (thigh bone – the strongest bone in the body), tibia and fibula (lower leg), tarsal bones (ankle), and the bones of the foot and toes."
    },
    "chest": {
        "title": "Rib Cage (Thorax)",
        "count": "25 bones",
        "description": "Consists of the sternum (breastbone) and 12 pairs of ribs. It protects the heart and lungs."
    }
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/bones/<part>")
def get_bone_info(part):
    data = bones_data.get(part)
    if data:
        return jsonify(data)
    return jsonify({"error": "Not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)