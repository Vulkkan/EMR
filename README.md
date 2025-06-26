# EMR
- FastAPI
- SQLite3
- OAuth 2.0
- RazorPay & Email automation.


## Endpints:
#### 1. ADMIN

##### i.)  Adding new admin (POST operation)
            /admin/add
##### ii.) Login (POST operation)
            /admin/token
######   NOTE- This request will return a token for authentication of the user.
##### ii.) Delete admin (DELETE operation)
            /admin/delete-admin


#### 2. DOCTORS
        
#####   i.)  Show all doctors in the hospital (GET operation)
            /doctors/        
#####   iii.) Add new doctor  (POST operation)            
            /doctors/                     
#####   iv.)  Edit a doctor's details(PUT operation)            
            /doctors   
#####   v.)   Delete a doctor from database (DELETE operation)            
            /doctors


#### 3. PATIENTS
        
#####   i.)  Show all the patients in the hospital (GET operation)
            /patients/        
#####   ii.) Show details of a specific patient(GET operation)
            /patients/{patient_id}    
#####   iii.) Add new patient  (POST operation)            
            /patients/                     
#####   iv.)  Edit a patient's details(PUT operation)            
            /patients/
#####   v.)   Delete a patient from the database (DELETE operation)            
            /patients/
#####   vi.) Assign doctor to a patient
            /patients/doc
#####   vii.)Create payment_ticket(POST operation)
            /patients/create_order
#####   vii.)Verify the payment (GET operation)
            /patients/verify_order/{input}

