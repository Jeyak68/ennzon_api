import datetime
import time

from rest_framework.decorators import api_view
from rest_framework.response import Response
import firebase_admin
from firebase_admin import credentials, firestore, storage

json_key = {
    "type": "service_account",
    "project_id": "evnzon-2dac3",
    "private_key_id": "55c2e3417c0da15ae9b33c51f1979d25d3cca91f",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC1mu+GZRf4hmpF\nrXE/P4bPt+inrQeA5RzMlWlTSpTQQwfxYlS0/d6+DWm1l4GwW91VDrkME4iRA9BA\nOMS24lSBRweexFKsu87sotWpehlM87/F6Q71EhBe/IuPd+j02Mz/lsF37KgB4PF9\nAhW1hQlT3rgTXOUIoB94lSbFNSREj6wlgH9mm4hexkloRcIsjyPRALusLEtOd5OV\nr53fpLT/L6Xd0Yxqt4ekAhVN1RvTqj52iobuYuVRCUpnLh85nPUQZU2Frtyucp9A\nr/O2GixuYr1B7BWamg1NPjqw5g6ORsRx9sMIEHfkkvXN8it36zl3pYZvZaDWHgUS\nVZc7JhwtAgMBAAECggEAA/uA+4GrBrxX3JhNmUqjglmbmgBi35I7+/EzgpaU8IOP\nyzInU7gU0uEeFikw4wpYrl1TdIQsegBLPaVLtwumjmvdgGn4utNRhIHw9+BMFBJs\n/FeR3ZDxrUuSJJQcwTB3P7bxc4JL5Y1RGQyF0lm3rHsABA4E8xf5KLPzSjQnS/OQ\nbDDY5otvyuZiS5iEJdMkTzxuzpcesqKQmQDw6sR847BQt5VgyxtGtu/+J9FyrFv5\n1BBDBfI66YaaIh3MrbrMMqCxu/ivgoVeMlm+AfhwMWhDbRqb0Iv1keNoHRje2x7s\nCXT7yL5e3L9tLxzfvOEwMcPgDWlKH5F5bOC4pRj4FwKBgQDzfCkKlBJfLsjeEWkD\nz1GwC4qkqH+lxg4y9BwqyaABxkXISv8jJn7N51w5+h91oWKCCkBiRL2TUFMjVEIX\nbb4cw5I+r2AWK4bb/BO7+8QRd8rYm+4TyLWhmLnnlWEUuMOKneHFIzz59u2poqbZ\n9px1W/ZlnK+430/9ifRY6pYgmwKBgQC+8It7sxhvR8SuK7MjEJBJotTgS4/qqRxa\n3AZbPTGerSpGkYdDU/Gf9ZURAcgleUR3c152zVhVsqi8KHUyL4mYAlOhu9cbNEyQ\n/zXg6W5kBfrBGxNeCHCWPt4Ko2eIopPpg5+uWUtiD1Hi42i8dKTgvFfoVcgg3yfd\n2O1WVbzO1wKBgQCjf/RvTg8oK1pnBHnoPQc1mAp5l0xgHSbbwGBJuyrfBi1F2laJ\nXAg6a+naZMNLUhu8BvZFBrPmgEHTr3jSErdeyVUjEtELEh91CUiXKvD2aeKkodC1\nKEoPQWdUw1J1f7yPEIXSw17m25GsH7S7GIbnp+FFSnoVQp+MOV8DdkNpkQKBgDos\nUWLTsuscg4jJGZ/iSQOWT6MyglttQI1SIcGkiDye55VuezaBGcmxacQvtcntA3Yd\nOTea4oHhl9UTwnkS0Kn2c4KAF05bhcRbbQ/kLtTcmYRB+omYqqyr5Lx7Am03kzb+\n+iSFYhkzL7CftmZMZ3ttBp9rmzigpKXLlKvMHWUrAoGAdNk4fSykdnyWHKUC2zRS\nV26J+w97qvvbuepyhS0tH1dmiKzeVtYf5niT4NBLysubfYoHTY8GDi4bYFFbp3lY\nNizy9L2qrxJS4Hsa3oiy67UfVWF0LohQhlwu/9WCLxmqpJ4mPUKq3bzZEx2KWXad\nKUSfUPuaOfBrewBSHeFxurk=\n-----END PRIVATE KEY-----\n",
    "client_email": "firebase-adminsdk-2howu@evnzon-2dac3.iam.gserviceaccount.com",
    "client_id": "115532745794068979032",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-2howu%40evnzon-2dac3.iam.gserviceaccount.com",
    "universe_domain": "googleapis.com"
}

cred = credentials.Certificate(json_key)
firebase_admin.initialize_app(cred, {'storageBucket': 'evnzon-2dac3.appspot.com'})
bucket = storage.bucket()


@api_view(["POST"])
def add_service(request):
    data = request.data
    if 'description' in data and 'direction' in data and 'fromPrice' in data and 'photos' in data and "location" in data and "mobile" in data and "name" in data and "noofRatings" in data and "queries" in data and "ratings" in data and "totalRating" in data and "type" in data and 'service_name' in data:
        url_list = []
        for i in data['photos']:
            blob = bucket.blob(i.name)
            blob.upload_from_file(i.file)
            blob.make_public()
            url_list.append( blob.public_url)

        db = firestore.client()
        db.collection('services').document(data['service_name']).collection(data['service_name']).document().set({
            "description": data['description'],
            "direction": data['direction'],
            "fromPrice": data['fromPrice'],
            "photos": url_list,
            "location": data['location'],
            "mobile": data['mobile'],
            "name": data['name'],
            "noofRatings": data['noofRatings'],
            "queries": data['queries'],
            "ratings": data['ratings'],
            "totalRating": data['totalRating'],
            "type": data['type']
        })
        return Response({"status": "200", "message": "data added successfully"})
    else:
        return Response({"status": "400", "message": "Please Provide all fields"})


@api_view(["POST"])
def edit_service(request):
    data = request.data
    if 'description' in data and 'direction' in data and 'fromPrice' in data and 'photos' in data and "location" in data and "mobile" in data and "name" in data and "noofRatings" in data and "queries" in data and "ratings" in data and "totalRating" in data and "type" in data and "id" in data and 'service_name' in data:
        url_list = []
        for i in data['photos']:
            if type(i) is str:
                url_list.append(i)
            else:
                blob = bucket.blob(i.name)
                blob.upload_from_file(i.file)
                blob.make_public()
                url_list.append( blob.public_url)

        db = firestore.client()
        db.collection('services').document(data['service_name']).collection(data['service_name']).document(data['id']).set({
            "description": data['description'],
            "direction": data['direction'],
            "fromPrice": data['fromPrice'],
            "photos": url_list,
            "location": data['location'],
            "mobile": data['mobile'],
            "name": data['name'],
            "noofRatings": data['noofRatings'],
            "queries": data['queries'],
            "ratings": data['ratings'],
            "totalRating": data['totalRating'],
            "type": data['type']
        })
        return Response({"status": "200", "message": "data added successfully"})
    else:
        return Response({"status": "400", "message": "Please Provide all fields"})


@api_view(["POST"])
def delete_service(request):
    data = request.data
    if "id" in data and "service_name" in data:
        db = firestore.client()
        db.collection('services').document(data['service_name']).collection(data['service_name']).document(data['id']).delete()
        return Response({"status": "200", "message": "data deleted successfully"})
    else:
        return Response({"status": "400", "message": "Please Provide all fields"})


@api_view(["POST"])
def service_edit_details(request):
    data = request.data
    if "id" in data and "service_name" in data:
        db = firestore.client()
        details = db.collection('services').document(data['service_name']).collection(data['service_name']).document(data['id']).get()
        return Response({"status": "200", "message": "data fetched successfully", "data":details.to_dict()})
    else:
        return Response({"status": "400", "message": "Please Provide all fields"})


@api_view(["POST"])
def service_list(request):
    data = request.data
    if "service_name" in data:
        fs = firestore.client()
        users_doc = fs.collection('services').document( data['service_name']).collection(data['service_name']).get()
        users = []
        for i in users_doc:
            d = i.to_dict()
            d['id'] = i.id
            users.append(d)
        return Response({"status": "200", "message": "Success", "data": users})
    else:
        return Response({"status": "400", "message": "Please Provide all fields"})


@api_view(["POST"])
def add_ads(request):
    data = request.data
    if 'image' in data and 'visibility' in data:
        print(type(data['image']))
        if type(data['image']) is str:
            url = data['image']
        else:
            blob = bucket.blob(data['image'].name)
            blob.upload_from_file(data['image'].file)
            blob.make_public()
            url = blob.public_url
        db = firestore.client()
        db.collection('ads').document("ads").set({
            "image": url,
            "visibility": data['visibility'],
        })
        return Response({"status": "200", "message": "data added successfully"})
    else:
        return Response({"status": "400", "message": "Please Provide all fields"})


@api_view(["POST"])
def add_image(request):
    data = request.data
    if 'image' in data:
        blob = bucket.blob(data['image'].name+str(time.time_ns())+".png")
        blob.upload_from_file(data['image'].file)
        blob.make_public()
        url = blob.public_url
        return Response({"status": "200", "message": "data added successfully", "url":url})
    else:
        return Response({"status": "400", "message": "Please Provide all fields"})


@api_view(["POST"])
def add_category(request):
    data = request.data
    if 'image' in data and 'name' in data and 'index' in data:
        if type(data['image']) is str:
            url = data['image']
        else:
            blob = bucket.blob(data['image'].name+str(time.time_ns())+".png")
            blob.upload_from_file(data['image'].file)
            blob.make_public()
            url = blob.public_url
        db = firestore.client()
        db.collection('category').document().set({
            "image": url,
            "name": data['name'],
            "index": data['index']
        })
        return Response({"status": "200", "message": "data added successfully"})
    else:
        return Response({"status": "400", "message": "Please Provide all fields"})


@api_view(["POST"])
def category_list(request):
    fs = firestore.client()
    users_doc = fs.collection("category").get()
    users = []
    for i in users_doc:
        d = i.to_dict()
        d['id'] = i.id
        users.append(d)
    return Response({"status": "200", "message": "Success", "data": users})


@api_view(["POST"])
def edit_category(request):
    data = request.data
    if 'image' in data and 'name' in data and 'index' in data and 'id' in data:
        if type(data['image']) is str:
            url = data['image']
        else:
            blob = bucket.blob(data['image'].name+str(time.time_ns())+".png")
            blob.upload_from_file(data['image'].file)
            blob.make_public()
            url = blob.public_url
        db = firestore.client()
        db.collection('category').document(data['id']).update({
            "image": url,
            "name": data['name'],
            "index": data['index']
        })
        return Response({"status": "200", "message": "data added successfully"})
    else:
        return Response({"status": "400", "message": "Please Provide all fields"})


@api_view(["POST"])
def delete_category(request):
    data = request.data
    if 'id' in data:
        db = firestore.client()
        db.collection('category').document(data['id']).delete()
        return Response({"status": "200", "message": "data deleted successfully"})
    else:
        return Response({"status": "400", "message": "Please Provide all fields"})


@api_view(["POST"])
def category_edit_details(request):
    data = request.data
    if 'id' in data:
        db = firestore.client()
        data = db.collection('category').document(data['id']).get()
        return Response({"status": "200", "message": "data fetched successfully", "data":data.to_dict()})
    else:
        return Response({"status": "400", "message": "Please Provide all fields"})


@api_view(["POST"])
def add_banner(request):
    data = request.data
    if 'banner' in data:
        url_list = []
        for i in data['banner']:
            if type(i) is str:
                url_list.append(i)
            else:
                blob = bucket.blob(i.name)
                blob.upload_from_file(i.file)
                blob.make_public()
                url_list.append(blob.public_url)
        db = firestore.client()
        db.collection('banner').document("Coimbatore").set({
            "banner": url_list
        })
        return Response({"status": "200", "message": "data added successfully"})
    else:
        return Response({"status": "400", "message": "Please Provide all fields"})


@api_view(["POST"])
def banner_list(request):
    fs = firestore.client()
    users_doc = fs.collection('banner').document("Coimbatore").get()
    return Response({"status": "200", "message": "Success", "data": users_doc.to_dict()})


@api_view(["POST"])
def get_users(request):
    fs = firestore.client()
    users_doc = fs.collection("user").get()
    users = []
    for i in users_doc:
        users.append(i.to_dict())
    return Response({"status": "200", "message": "Success", "data":users})
