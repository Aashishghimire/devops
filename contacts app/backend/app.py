# app.py (Flask API for Contact List CRUD)
from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config["MONGO_URI"] = "mongodb://db:27017/contactsdb"
mongo = PyMongo(app)

contacts = mongo.db.contacts

@app.route("/api/contacts", methods=["GET"])
def get_contacts():
    all_contacts = contacts.find()
    result = []
    for contact in all_contacts:
        result.append({
            "_id": str(contact["_id"]),
            "name": contact["name"],
            "email": contact["email"],
            "phone": contact["phone"]
        })
    return jsonify(result)

@app.route("/api/contacts/<id>", methods=["GET"])
def get_contact(id):
    contact = contacts.find_one({"_id": ObjectId(id)})
    if contact:
        return jsonify({
            "_id": str(contact["_id"]),
            "name": contact["name"],
            "email": contact["email"],
            "phone": contact["phone"]
        })
    return jsonify({"error": "Contact not found"}), 404

@app.route("/api/contacts", methods=["POST"])
def add_contact():
    data = request.get_json()
    inserted = contacts.insert_one({
        "name": data["name"],
        "email": data["email"],
        "phone": data["phone"]
    })
    return jsonify({"_id": str(inserted.inserted_id)}), 201

@app.route("/api/contacts/<id>", methods=["PUT"])
def update_contact(id):
    data = request.get_json()
    updated = contacts.update_one(
        {"_id": ObjectId(id)},
        {"$set": {
            "name": data["name"],
            "email": data["email"],
            "phone": data["phone"]
        }}
    )
    if updated.matched_count == 0:
        return jsonify({"error": "Contact not found"}), 404
    return jsonify({"message": "Contact updated"})

@app.route("/api/contacts/<id>", methods=["DELETE"])
def delete_contact(id):
    deleted = contacts.delete_one({"_id": ObjectId(id)})
    if deleted.deleted_count == 0:
        return jsonify({"error": "Contact not found"}), 404
    return jsonify({"message": "Contact deleted"})

if __name__ == "__main__":
    app.run(debug=True)