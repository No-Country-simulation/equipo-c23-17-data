import pickle
import streamlit as st
import pandas as pd
import base64
from PIL import Image
model_file = 'model_C=1.0.bin'

with open(model_file, 'rb') as f_in:
    dv, model = pickle.load(f_in)


def main():

	image = Image.open('images/icone.png')
	image2 = Image.open('images/image.png')
	st.image(image,use_column_width=False)
	add_selectbox = st.sidebar.selectbox(
	"How would you like to predict?",
	("Online", "Batch"))
	st.sidebar.info('Esta aplicación fue creada por el equipo-c23-17-data para predecir el abandono de clientes de una empresa de Telecomunicaciones')
	st.sidebar.image(image2)
	st.title("Predicción de abandono de clientes")
	if add_selectbox == 'Online':
		gender = st.selectbox('Gender:', ['male', 'female'])
		seniorcitizen= st.selectbox(' Customer is a senior citizen:', [0, 1])
		partner= st.selectbox(' Customer has a partner:', ['yes', 'no'])
		dependents = st.selectbox(' Customer has  dependents:', ['yes', 'no'])
		phoneservice = st.selectbox(' Customer has phoneservice:', ['yes', 'no'])
		multiplelines = st.selectbox(' Customer has multiplelines:', ['yes', 'no', 'no_phone_service'])
		internetservice= st.selectbox(' Customer has internetservice:', ['dsl', 'no', 'fiber_optic'])
		onlinesecurity= st.selectbox(' Customer has onlinesecurity:', ['yes', 'no', 'no_internet_service'])
		onlinebackup = st.selectbox(' Customer has onlinebackup:', ['yes', 'no', 'no_internet_service'])
		deviceprotection = st.selectbox(' Customer has deviceprotection:', ['yes', 'no', 'no_internet_service'])
		techsupport = st.selectbox(' Customer has techsupport:', ['yes', 'no', 'no_internet_service'])
		streamingtv = st.selectbox(' Customer has streamingtv:', ['yes', 'no', 'no_internet_service'])
		streamingmovies = st.selectbox(' Customer has streamingmovies:', ['yes', 'no', 'no_internet_service'])
		contract= st.selectbox(' Customer has a contract:', ['month-to-month', 'one_year', 'two_year'])
		paperlessbilling = st.selectbox(' Customer has a paperlessbilling:', ['yes', 'no'])
		paymentmethod= st.selectbox('Payment Option:', ['bank_transfer_(automatic)', 'credit_card_(automatic)', 'electronic_check' ,'mailed_check'])
		tenure = st.number_input('Number of months the customer has been with the current telco provider :', min_value=0, max_value=240, value=0)
		monthlycharges= st.number_input('Monthly charges :', min_value=0, max_value=240, value=0)
		totalcharges = tenure*monthlycharges
		output= ""
		output_prob = ""
		input_dict={
				"gender":gender ,
				"seniorcitizen": seniorcitizen,
				"partner": partner,
				"dependents": dependents,
				"phoneservice": phoneservice,
				"multiplelines": multiplelines,
				"internetservice": internetservice,
				"onlinesecurity": onlinesecurity,
				"onlinebackup": onlinebackup,
				"deviceprotection": deviceprotection,
				"techsupport": techsupport,
				"streamingtv": streamingtv,
				"streamingmovies": streamingmovies,
				"contract": contract,
				"paperlessbilling": paperlessbilling,
				"paymentmethod": paymentmethod,
				"tenure": tenure,
				"monthlycharges": monthlycharges,
				"totalcharges": totalcharges
			}

		if st.button("Predict"):
			print("Online Input Dict:", input_dict)  # Log the input dictionary
			st.write("Online Input Dict:", input_dict)  # Display input_dict in the app
			X = dv.transform([input_dict])
			y_pred = model.predict_proba(X)[0, 1]
			churn = y_pred >= 0.5
			output_prob = float(y_pred)
			output = bool(churn)
		st.success('Churn: {0}, Risk Score: {1}'.format(output, output_prob))

	if add_selectbox == 'Batch':
		def file_download_link(file_path, file_label='Descargar archivo'):
			with open(file_path, "rb") as f:
				data = f.read()
			b64 = base64.b64encode(data).decode()
			href = f'<a href="data:text/csv;base64,{b64}" download="{file_path}">{file_label}</a>'
			return href

		# Mostrar el enlace en la app
		st.markdown(file_download_link("batch_ejemplo.csv", "Descargar CSV"), unsafe_allow_html=True)

		file_upload = st.file_uploader("Upload csv file for predictions", type=["csv"])
		if file_upload is not None:
			data = pd.read_csv(file_upload)
			
			# Rename columns to match online input dictionary
			data = data.rename(columns={
				"SeniorCitizen": "seniorcitizen",
				"Partner": "partner",
				"Dependents": "dependents",
				"PhoneService": "phoneservice",
				"MultipleLines": "multiplelines",
				"InternetService": "internetservice",
				"OnlineSecurity": "onlinesecurity",
				"OnlineBackup": "onlinebackup",
				"DeviceProtection": "deviceprotection",
				"TechSupport": "techsupport",
				"StreamingTV": "streamingtv",
				"StreamingMovies": "streamingmovies",
				"Contract": "contract",
				"PaperlessBilling": "paperlessbilling",
				"PaymentMethod": "paymentmethod",
				"MonthlyCharges": "monthlycharges",
				"TotalCharges": "totalcharges"
			})
			
			# Standardize categorical values
			data['gender'] = data['gender'].str.lower()
			data['partner'] = data['partner'].str.lower()
			data['dependents'] = data['dependents'].str.lower()
			data['phoneservice'] = data['phoneservice'].str.lower()
			data['multiplelines'] = data['multiplelines'].str.lower().replace("no phone service", "no_phone_service")
			data['internetservice'] = data['internetservice'].str.lower().replace("fiber optic", "fiber_optic")
			data['onlinesecurity'] = data['onlinesecurity'].str.lower().replace("no internet service", "no_internet_service")
			data['onlinebackup'] = data['onlinebackup'].str.lower().replace("no internet service", "no_internet_service")
			data['deviceprotection'] = data['deviceprotection'].str.lower().replace("no internet service", "no_internet_service")
			data['techsupport'] = data['techsupport'].str.lower().replace("no internet service", "no_internet_service")
			data['streamingtv'] = data['streamingtv'].str.lower().replace("no internet service", "no_internet_service")
			data['streamingmovies'] = data['streamingmovies'].str.lower().replace("no internet service", "no_internet_service")
			data['contract'] = data['contract'].str.lower().replace(" ", "-")
			data['paperlessbilling'] = data['paperlessbilling'].str.lower()
			data['paymentmethod'] = (data['paymentmethod'].str.lower() # Convert to lowercase
							.str.replace(" ", "_")  # Replace spaces with underscores
							.str.replace("(", "")  # Remove "("
							.str.replace(")", "")  # Remove ")"
			)
			
			# Convert data types
			data['monthlycharges'] = data['monthlycharges'].astype(int)
			data['totalcharges'] = data['totalcharges'].astype(int)
			
			# Reorder columns to match online input dictionary
			expected_columns = [
				"gender", "seniorcitizen", "partner", "dependents", "phoneservice",
				"multiplelines", "internetservice", "onlinesecurity", "onlinebackup",
				"deviceprotection", "techsupport", "streamingtv", "streamingmovies",
				"contract", "paperlessbilling", "paymentmethod", "tenure",
				"monthlycharges", "totalcharges"
			]
			data = data[expected_columns]
			
			# Drop unnecessary columns
			data = data.drop(columns=["customerID", "Churn"], errors="ignore")
			
			# Log and display batch data
			print("Batch Data:", data)  # Log the batch data
			st.write("Batch Data:", data)  # Display batch data in the app
			records = data.to_dict(orient='records')
			st.write("Batch Records:", records)  # Display records in the app
			
			# Transform data and make predictions
			X = dv.transform(records)
			y_pred = model.predict_proba(X)[:, 1]
			churn = y_pred >= 0.5
			results = pd.DataFrame({'Churn': churn, 'Risk Score': y_pred})
			st.write(results)

if __name__ == '__main__':
	main()