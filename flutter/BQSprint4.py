# -*- coding: utf-8 -*-

import firebase_admin
from firebase_admin import credentials, firestore

# Replace 'path/to/your/credentials.json' with the actual path to your Firebase Admin SDK credentials file
cred = credentials.Certificate('google-services.json')
firebase_admin.initialize_app(cred)

# Replace 'your-collection-name' with the name of your Firestore collection
collection_name = 'postReports'

# Initialize Firestore
db = firestore.client()

# Get a reference to the collection
collection_ref = db.collection(collection_name)

# Get documents from the collection
docs = collection_ref.get()

# Count the number of documents
num_documents = len(docs)

# Print the number of documents
print(f'The number of documents in the collection {collection_name} is: {num_documents}')
