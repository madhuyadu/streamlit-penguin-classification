# streamlit-penguin-classification
# Project details
Building a classification model (Random Forest classifier) for Penguin classification on Streamlit web app </br>
The application has following features:</br>
1. User can provide input to the classification model for prediction in 2 ways:</br>
a. By way of adjusting the sliding/selector bars present in the sidebar, which are basically features to the model</br>
b. By way of uploading files to the app via button "Browse files" under section - <ins>Drag & Drop file here</ins> </br>
2. Results of the classification model are displayed in the main page. </br>
a. Prediction class, which tells the class to which Penguin belongs is displayed along with prediction probability for each class.
3. The input features fed to the model (via either way) is also displayed in the tabular form in the main page
4. The app is deployed on Heroku platform successfully & tested via Heroku CLI & also on Heroku GUI

# Screenshots of the App
**Main page**</br>

![image](https://user-images.githubusercontent.com/56335301/190420096-e5d839b1-f773-496b-90cc-cea03c12e5b9.png)
![image](https://user-images.githubusercontent.com/56335301/190420173-45814462-7225-4542-b83e-4e118b5bfab3.png)


**Sidebar**</br>

![image](https://user-images.githubusercontent.com/56335301/190420267-27c3b371-54ba-426f-98ec-4262ac3a9e56.png)
![image](https://user-images.githubusercontent.com/56335301/190420384-f5921a4a-419b-42e3-8446-87d1713d55fc.png)
![image](https://user-images.githubusercontent.com/56335301/190420458-3933014b-611c-4510-99be-5f420bfb0d9c.png)


**Whole page view**</br>

![image](https://user-images.githubusercontent.com/56335301/190420599-9b8293f9-5590-476d-ac6c-c34ed145f0cd.png)
![image](https://user-images.githubusercontent.com/56335301/190420685-6842acec-5530-42fe-bb68-f934a292f825.png)



# Screenshots showing app deployment on Heroku - via Heroku CLI
Before proceeding with below steps, ensure following
* Heroku CLI is installed on local
* Heroku account is created already
* Git is installed on local

1. Clone the git repo on local & change to dir inside cloned repo for further steps
![image](https://user-images.githubusercontent.com/56335301/190913997-a541e8c2-6be5-4236-b4c6-201446b0dd76.png)

2. Log into Heroku account
![image](https://user-images.githubusercontent.com/56335301/190914112-6a1b56d5-f8c2-4ee6-86a7-0eaf186f81ae.png)

3. Create Heroku app
![image](https://user-images.githubusercontent.com/56335301/190914132-785c44ee-16fe-4582-825c-e9f7c51ddb16.png)

4. Execute below git commands
$ git init </br>
$ git add . </br>
$ git commit -m "commit message" </br>
$ git branch -M main </br>
$ git push heroku main </br>

![image](https://user-images.githubusercontent.com/56335301/190914155-2a917fd3-d80e-4803-9311-cd073ed74390.png)
![image](https://user-images.githubusercontent.com/56335301/190914210-f9907645-7e38-4fc1-8fff-6c5787c7076e.png)

5. Check for the message: deployed to Heroku inside the logs printed
![image](https://user-images.githubusercontent.com/56335301/190914254-967e332f-65c9-4d55-a653-4b7cded80e14.png)

6. Check for the message:  Procfile declares types -> web, to avoid the error "Application error" when app is successfully deployed
![image](https://user-images.githubusercontent.com/56335301/190914270-0dfaff0d-34e2-4b21-bafd-747df9c614de.png)

7. App successfully deployed on Heroku
![image](https://user-images.githubusercontent.com/56335301/190914730-0fcaee82-bf29-4404-a4ec-56067d9e09aa.png)


# Screenshots showing app deployment on Heroku - via Heroku GUI
1. Go to the option "Create the App", give a name for the app. Click the button "Create app"
![image](https://user-images.githubusercontent.com/56335301/190914808-675d9cae-e8b4-4d22-8b86-37c22cd08bd2.png)

2. Select Github as Deployment method
![image](https://user-images.githubusercontent.com/56335301/190914875-466e1e17-459e-4917-be85-a4b59d87480b.png)

3. Search for github repo name & click Connect
![image](https://user-images.githubusercontent.com/56335301/190914910-acf0461c-86b1-478c-8874-4b1887ae3725.png)

4. You can also enable Automatic deployment as below
![image](https://user-images.githubusercontent.com/56335301/190914931-109ebbc1-71c4-424c-8c7a-ddd2558f99fd.png)

5. Manually deploy the app as below & ensure all steps are completed successfully
![image](https://user-images.githubusercontent.com/56335301/190914981-324a2014-6bea-476f-8820-3a180181fdf5.png)
![image](https://user-images.githubusercontent.com/56335301/190915002-b7451f5a-b28d-4cfe-a7df-3f334168e38d.png)

6. Check for below message to ensure successful deployment of app
![image](https://user-images.githubusercontent.com/56335301/190915043-61ffff8d-36d5-4e8f-9835-1f514cfd4944.png)

7. You can also check status of app like below
![image](https://user-images.githubusercontent.com/56335301/190915077-dd5a2859-1c71-487c-a59d-8bb868932118.png)

8. App can also be accessed under Settings option
![image](https://user-images.githubusercontent.com/56335301/190915117-564801c0-5bbb-414f-b963-8c5b3d401607.png)

9. Successfully deployed app
![image](https://user-images.githubusercontent.com/56335301/190915141-7fd225af-c947-4aa1-82c9-fc675cdab16c.png)



# NOTE: 
1. The web app was developed on Anaconda navigator as replit faced issues related to streamlit, pandas, python, numpy library versions
2. The example CSV input file (the hyperlink, which can be seen on the left side pane) is available @ https://raw.githubusercontent.com/dataprofessor/data/master/penguins_example.csv, and not present in the repository
3. The github repo which is deployed as app on Heroku should contain following important files:
- app.py --> containing the main script to run/ starting point

Using the setup.sh and Procfile files, you can tell Heroku the needed commands for starting the application.</br>
In the setup.sh file, we will create a streamlit folder with a credentials.toml and a config.toml file.( pls refer setup.sh file inside this repo for content) </br>
The Procfile is used to execute the setup.sh and then call streamlit run to run the application. </br>

- Procfile --> shouldnt contain any extension
- setup.sh --> should contain extension .sh
- requirements.txt --> contains all dependencies along with version info.</br> The requirements.txt file contains all the libraries that need to be installed for the project to work. </br> This file can be created manually by going through all files and looking at what libraries are used or </br> automatically using something like pipreqs. </br>
pipreqs ./  --> SYNTAX to be used in cmd

- README.txt 
- any other supporting files such as input file, model.pkl file & so on


# Credits
This web app is created based on tutorial on youtube channel "dataprofessor"
