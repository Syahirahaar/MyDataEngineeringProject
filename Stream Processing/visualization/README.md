For visualizaton, I'm using Streamlit app to enable interaction between the database and end user

# Steps to connect to streamlit
1. Open you cmd prompt 
2. Change directory to where the Streamlit file reside
3. Type "streamlit run file name.py
4. Press Enter
5. Wait for the browser to prompt

The file can be found here [streamlit file](https://github.com/Syahirahaar/MyDataEngineeringProject/blob/main/Stream%20Processing/visualization/test_tostreamlit3.py)

Streamlit app

![image](https://user-images.githubusercontent.com/48470854/130242541-7a5368fc-b9f9-48a2-83fc-eba0b38cc2f8.png)

**disclaimer : I'm still improving on how to make the web work by just inputting certain keywords that can display the answers**

# Topic 10 : Visualization Pipeline Redshift Data Warehouse

In this topic, I choose to connect the Redshift to Microsoft PowerBI. 

# Connect Redshift with PowerBI

1. Add rule into inbound rule to allow Redshift be connected to the outside world 

![image](https://user-images.githubusercontent.com/48470854/130232936-81d0eaac-e848-41f0-9e7e-34ef4a1d926f.png)

2. Create a connection at PowerBI side

PowerBI > Get data > Redshift > enter information as below :

![image](https://user-images.githubusercontent.com/48470854/130233423-ceff6f4c-bf14-4c3a-adae-f6900e74de81.png)

Server : Endpoint at Redshift's cluster dahsboard

![image](https://user-images.githubusercontent.com/48470854/130233766-c04713a2-7d04-4e57-b536-5b09339106f5.png)


PowerBI dashboard example

![image](https://user-images.githubusercontent.com/48470854/130241502-81ee2ce5-da2f-44e8-a598-5038e1e1a98a.png)



