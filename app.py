from flask import Flask,request,render_template,redirect,url_for
import os
import csv
import tensorflow as tf



#firebase:
'''
import firebase_admin
from firebase_admin import credentials, firestore
'''


app=Flask(__name__)

#ML model:
#model=tf.keras.models.load_model('efficientnetb3-Eye Disease-96.19.h5')
# Register the custom object in case it's necessary

#try2
'''
custom_objects = {
    'TFOpLambda': tf.keras.layers.Lambda  # This is a generic example; adjust as needed
}

# Load the model with the custom object scope
with custom_object_scope(custom_objects):
    model = tf.keras.models.load_model("C:\\Users\\akash\\OneDrive\\Documents\\imai trial\\efficientnetb3-Eye Disease-96.19.h5")
'''


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/1session',methods=['POST','GET'])
def session1():
    return render_template('session1.html')

@app.route('/2session',methods=['POST','GET'])
def session2():
    if request.method=='POST':
        R_remarks=request.form.get('line')
        
    
    L_remarks=request.args.get('L_remarks')
    #L_remarks= request.args.get('L_remarks')
    # L_remarks = session.get('L_remarks') 

    

    return render_template('session2.html',R_remarks=R_remarks,L_remarks=L_remarks)


@app.route('/submit',methods=['POST','GET'])
def submit():
    if request.method=='POST':

        
        first_name=str(request.form['First Name'])
        last_name=str(request.form['Last Name'])

        age=int(request.form['age'])
        occupation=str(request.form.get('occupation'))
        gender=str(request.form['gender'])
        prev_eye_surgery=str(request.form.get('prev_eye_surgery'))
        existing_ailments=str(request.form.get('existing_ailments'))
        high_bp=str(request.form.get('high_bp'))
        Diabetes=request.form.get('Diabetes')
        chief_complaints=request.form.getlist('Chief complaints')

        contact=int(request.form['contact'])
        email=str(request.form.get('email'))
        relative_contact=str(request.form.get('relative_contact'))
        existing_doctor=str(request.form.get('existing_doctor'))
        family_history=str(request.form.get('family_history'))
        Glaucoma=str(request.form.get('Glaucoma'))
        Macular_Degeneration=str(request.form.get('Macular Degeneration'))


        # if str(request.form.get('line1')) not in'Ee' or str(request.form.get('line2')) not in 'FPfp':


        L_remarks=request.args.get('L_remarks')
        R_remarks=request.args.get('R_remarks')




        hosp_name=str(request.form['hosp'])
        fundus=request.files['fundus']

        # prediction=model.predict(fundus)

        data=[first_name,last_name,age,occupation,gender,prev_eye_surgery,existing_ailments,high_bp,Diabetes,chief_complaints,contact,email,relative_contact,existing_doctor,family_history,Glaucoma,Macular_Degeneration,L_remarks,R_remarks,hosp_name]
        
       
            
        #main folderL
        # Base folder:
        base_folder='C:/Imai_data'
        os.makedirs(base_folder,exist_ok=True)


        #hosp folder:
        hosp_folder=os.path.join(base_folder,hosp_name)
        os.makedirs(hosp_folder,exist_ok=True)

        #image folder path:
        img_folder=os.path.join(hosp_folder,'fundus_images')
        os.makedirs(img_folder,exist_ok=True)
        #adding image
        file_path=os.path.join(img_folder,fundus.filename)
        fundus.save(file_path)


        #csv file path:
        csv_file=os.path.join(hosp_folder,'data.csv')

        #writing data into csv file
        file_exists=os.path.isfile(csv_file)
        with open(csv_file,mode='a',newline='') as file:
            writer=csv.writer(file)
            if not file_exists:
                writer.writerow(['First Name','Last Name','Age','Occupation','Gender','Previous eye surgeries','Existing Ailments','High B.P','Diabetes','Chief Complaints','Contact',"email",'relative_contact','existing_doctor','family_history','Glaucoma','Macular_Degeneration','Left eye remarks','Right eye remarks','hosp_name'])
            writer.writerow(data)
        return render_template('submit_page.html')
    else:
        return 'some issue'
    


@app.route('/diagnosis',methods=['POST','GET'])
def diagnosis():
    if request.method=='POST':
        if request.form.get('docid')=='doc123':
            return'DOCTOR VERFIED' 
        else:
            return 'WRONG DOCTOR ID'
    else:
        return 'couldnt find data'

      
@app.route('/L_eyetest',methods=['POST','GET'])
def eyetest():
    return render_template('left_eyetest.html')



@app.route('/R_eyetest',methods=['POST','GET'])
def R_eyetest():   
    if request.method=='POST':
        L_remarks = request.form['line']
  
    return render_template('right_eyetest.html',L_remarks=L_remarks) 


'''

    
    
    


# @app.route('/<name>',methods=['POST','GET'])

'''




if __name__ == '__main__':
    app.run(debug=True)
