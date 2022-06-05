# Scorched!
A Final Project Analysis of U.S. Wildfires from 1992-2015

### By: k.E.G.d. (Katlin, Enzo, Graham, Danieli)

![image](https://user-images.githubusercontent.com/92705556/164362996-733acdf8-498c-4ec8-83fc-886dc000c433.png)

## Summary of Project
“Scorched!” is Team k.E.G.d.’s (Katlin, Enzo, Graham, and Danieli) final analysis project on U.S. Wildfires from 1992-2015.  Using Python / Pandas, PostgreSQL / PgAdmin, Tableau, and Javascript our team assessed and visually displayed trends in the data over time, including filters for year, state, month, fire size, and fire cause.  Applying our skills in Supervised Machine Learning with the Easy Ensemble Classifier model, we also created a tool that can predict whether a fire would grow to more than 50 acres based on user inputs of state, month, temperature, wind, and humidity.  Overall, fire size has increased since the early ‘90s, and, with climate forecasts projecting a hotter and drier future, the occurrence of massive wildfires is likely to continue.  

## Project Visualizations
- **Web App**: *https://salty-depths-05618.herokuapp.com/*
    - Web App GitHub (includes web application files only): *https://github.com/goatgirl86/wildfire_deploy1.git*
- **Tableau**: *https://public.tableau.com/shared/M9HQJBKBQ?:display_count=n&:origin=viz_share_link*
- **Google Slides Presentation**: *https://docs.google.com/presentation/d/e/2PACX-1vRcpefueeL0hf7W42UyXHPVGJ4oJcOoGwTu4AZiRIH_-beuVVj-dWq7IrlwUGHWFlr_si-9TXeTJbFG/embed?start=false&loop=false&delayms=3000*

## Project Overview
### Purpose
**Why Study Wildfires?**  *Wildfires affect us all!*
- Wildfires have the potential to harm property, livelihoods, and human health. 
- Studies show that climate change has already led to an increase in wildfire season length, wildfire frequency, and burned area.  It is bound to lead to further destruction in the future.
- **Colorado Wildfire Stats**: *from Colorado Division of Fire Prevention and Control: https://dfpc.colorado.gov/wildfire-information-center/historical-wildfire-information*
    - 4 of the 5 largest CO wildfires have occured since 2018
    - The top 20 largest CO wildfires have occured in the last 20 years

### Source Data 
- **U.S. Wildfire data (plus other attributes)**: *https://www.kaggle.com/datasets/capcloudcoder/us-wildfire-data-plus-other-attributes* 

### Questions to Investigate
-   Has the number, size, and cause of wildfires changed over time? *(general analysis and visualization)*
-   Has the timing and distribution of wildfires changed over time? *(general analysis and visualization)*
-   Can temperature, wind, humidity, discovery month, and state be used to predict whether a fire will grow to at least 50 acres in size? *(machine learning)*

### Technologies, Languages, Tools, and Algorithms Used
- **Requirements.txt**: Shows all packages and libraries used throughout project
- **Libraries.txt**: Shows libraries imported by .ipynb file
- **Data Storage**: GitHub
- **Data Preprocessing**: Python, VSCode, PgAdmin
- **Data Analysis**: Python, VSCode, RStudio
- **Database Management**: Python, VSCode, PgAdmin (PostgreSQL), SQL Alchemy, Quick DBD for ERD development
- **Dashboard / Web App**: Javascript, Python, Google Slides, Tableau, VSCode, Flask

### Communication Plan
- **Communication Platforms utilized for group discussions**: GitHub, Google Drive, Instagram, Slack, Zoom

Beginning on March 26, 2022, the group held weekly meetings via Zoom in addition to more frequent communication via the platforms listed above. Each group member actively participated in meetings, contributed to group discussions, sought to help other group members who were stuck or struggling, and played to their personal coding strengths to make the final product the best it could be.

## Data Exploration
The "U.S. Wildfire data (plus other attributes)" dataset was downloaded from *kaggle* and explored using both Google Colab and Pandas. 
- *Entire Dataset: 55,367 rows from 43 columns* 
  
### Data Preprocessing
Based on the original dataset, it was determined that the data needed to be cleaned of columns and rows dominated by large numbers of empty cells, null values, and zeros. 'Putout_time'required reclassification of the data type from string to date, and 'fire_cause' was binned to reduce number of unique values. 
- *Cleaned Data: 13,138 rows from 18 columns* 

***Screenshot 1**: Dataframe showing rows needing to be cleaned/removed (putout_time is a string, '-1.000' values in weather columns, multiple '0' values)*

![image](https://user-images.githubusercontent.com/92705556/166401401-c87669e4-9566-478c-9c48-6acccc5d442f.png)

***Screenshot 2**: Final Cleaned DF (temps_to_7.csv) - Columns kept: 'fire_id', 'fire_size', 'fire_cause', 'latitude', 'longitude', 'state', 'discovery_month', 'Temp_pre_30', 'Temp_pre_15', 'Temp_pre_7', 'Wind_pre_30', 'Wind_pre_15', 'Wind_pre_7', 'Hum_pre_30', 'Hum_pre_15', 'Hum_pre_7', 'year', 'putout_time'.* 

![image](https://user-images.githubusercontent.com/92705556/168163351-0453e240-97c7-4811-8c7a-4332da024fbd.png)

## Data Analysis & Machine Learning
### General Data Analysis and Refinement                                     
The initial data analysis included creating basic plots using matplotlib and linear regression, creating new dataframes using the 'groupby' function in both Python and SQL, and using R to run simple statistical analyses (Multiple Linear Regression and Chi-Square Test). 

***Screenshot 3**: Scatter plot of fire size by year.*

![image](https://user-images.githubusercontent.com/92705556/168409947-b381d6ca-1cde-4133-a814-68fcc6ace20e.png)

***Screenshot 4**: Linear Regression of Temperature (x) vs Humidity (y) (pre_7).*

![image](https://user-images.githubusercontent.com/92705556/168409963-92e00960-a406-4e54-a551-94e53bc2b0de.png)

***Screenshot 5**: Chi Square test of fire cause and year.*

![image](https://user-images.githubusercontent.com/92705556/168409899-420a83f2-9613-4966-8d9a-998091409dfb.png)


After some of the initial analysis, we also decided to add five news coloumns in the dataset to provide additional information needed for further analysis and machine learning models. *Columns added **df_all_k.csv**: 'state_no', 'discovery_month_no', 'fire_size_bin', 'fire_size_bin_no', 'medium_plus'.
- The 'fire_size_bin' column (and the associated 'fire_size_bin_no' and 'medium_plus' columns) are the main additions to the dataset.  The 'fire_size' columns included over 3000 unique values, so we decided to bin the fire sizes into groups based on acreage (Bin Name / Bin No): 0-5 acres (Teacup / 1), 5-10 acres (Toy / 2), 10-50 acres (Mini / 3), 50-1000 acres (Medium / 4), 1,000-10,000 acres (Large / 5), >10,000 acres (XL / 6).  We also added an additional column for 'medium_plus'.  Fires that were at least medium in size were given a value of '1'. Teacup, Toy, Mini fires were given a value of '0'.  By adding this column, we could perform machine learning models that predicted whether a fire would grow to at least 50 acres in size.  

***Screenshot 6**: Code showing creation of fire_size_bins and fire_size_bin_no*

![image](https://user-images.githubusercontent.com/92705556/168167177-b2b067d0-7d96-4954-ae74-97e3f3d2c3dd.png)

***Screenshot 7**: Correlation Matrix*

This correlation matrix was made using Python's Seaborn library for data visualization.  Correlations measure the positive or negative relationship between two variables.

![image](https://user-images.githubusercontent.com/92705556/169682518-403d997e-430f-4144-ae59-786405c9c01f.png)


### Machine Learning
Using our knowledge of Supervised and Unsupervised Machine Learning, we ran several different models on our dataset.  
- **Unsupervised Machine Learning**: KMeans, Primary Component Analysis (PCA), and Heirarchical Clustering were all used to identify 'groupings' of datapoints based on temperature, humidity, and wind variables. *Note: Unsupervised Machine Learning was NOT used for the deployment of our machine learning model but rather used for visualization purposes.*  

***Sreenshot 8**: Unsupervised Machine Learning KMeans Scaled Model Plot showing 3 classes of pre_7 weather data (weather condition 7 days prior to fire start)*

![image](https://user-images.githubusercontent.com/92705556/168200740-36ab1e37-916e-4c2c-8d15-5e443d9967ed.png)

-  **Supervised Machine Learning**: Neural Networking, Random Forest Classifier, Balanced Random Forest Classifier, Easy Ensemble Classifier, Naive Random Oversampling, SMOTE Oversampling, Cluster Centroids Undersampling, SMOTEENN Over and Undersampling, Gradient Boosting Classifier, and Logistic Regression models were all run to determine accuracy of prediction models. Models were run using both 'Label Encoder' and 'One Hot Encoder' for comparison. *Note*: For Supervised Machine Learning Models, we used the following columns for our analyses.
    - Target (y) value: 'medium_plus'
    - X values: 'state', 'discovery_month', 'Temp_pre_7', 'Hum_pre_7', 'Wind_pre_7'

***Sreenshot 9**: Supervised Machine Learning Accuracy Results (using OneHot Encoder)*

![image](https://user-images.githubusercontent.com/92705556/168201343-9b222c38-ebaa-4bb5-a2f9-617a14094cc0.png)

***Sreenshot 10**: Supervised Machine Learning Accuracy Results (using Label Encoder)*

![image](https://user-images.githubusercontent.com/92705556/170169236-00e58144-994f-4a40-b6b3-a2fe06629178.png)


**NOTE: In the end, we decided to go with Easy Ensemble Classifer using Label Encoder for our prediction tool. This model had a high accuracy score and was easier to merge with our web app than some of the other models.**

## Database
To create our Database, we chose to use PgAdmin and SQL Alchemy.  Within our database, we have four main tables that are all connected through a common field: 'fire_id'. The original four tables were: fire_category, fire_info, fire_location, and weather_data. Using SQLAlchemy and Python, we then queried and joined information from the four original tables to create new tables.

***Sreenshot 11**: Entity Relationship Diagram (ERD) for our database*

![image](https://user-images.githubusercontent.com/92705556/168500770-1f526ccc-263b-4ff0-9b58-13ea47908a7b.png)

***Sreenshot 12 (group)**: Code and dataframes showing SQL Alchemy connection with database and query / join of data from original tables*

![image](https://user-images.githubusercontent.com/92705556/168447437-bc456946-d81d-4bce-acb1-2df477b3f777.png)
![image](https://user-images.githubusercontent.com/92705556/168447419-bc98c370-7a6b-4cbb-9338-3af69c29ad72.png)
![image](https://user-images.githubusercontent.com/92705556/168447429-7b3090c5-d16a-4712-901b-7c4596b34b5b.png)


## Dashboard
To make the dashboard, we used our knowledge of HTML and Javascript to create a stylish web app that includes background information, wildfire photos, interactive visualizations of our Tableau and Google Slides, and a "Predict Your Fire" page.  The prediction page allows page visitors to run user inputs through our Machine Learning model to predict whether a fire 50 acres or larger will result in the next 7 days.  
 - https://salty-depths-05618.herokuapp.com/

***Sreenshot 13**: Page 1 of our web app*

![image](https://user-images.githubusercontent.com/92705556/170163543-025acf1b-bbff-4d31-a6f3-be7feaeebb9e.png)
![image](https://user-images.githubusercontent.com/92705556/170163404-1327c862-ec69-4632-9a42-9b057b3c97f2.png)
![image](https://user-images.githubusercontent.com/92705556/171564204-cf7ace24-5c47-40fe-ad6e-88edc7790690.png)


***Sreenshot 14 (group)**: Page 2 of our web app*

![image](https://user-images.githubusercontent.com/92705556/171562151-255e45f0-a0df-4c1b-8d89-53cdbeb4f070.png)
![image](https://user-images.githubusercontent.com/92705556/171564095-8fe8e4ef-ff6f-487a-a82a-0bed04fb2fbc.png)



## Conclusions
Just as predicting the weather is notoriously challenging even for the professionals, predicting wildfires is also difficult due to varying weather conditions and unpredictable human behavior.  Once a fire sparks, the ability of it to be contained quickly depends not only on weather but also on response times, resource allocation and capacity, and much more.  

**Analytical Conclusions**
- The size of fires has steadily increased over the 23 year period.
- The total square acreage of burned area has hit a 23 year high in 2015.  
- Increase in fire size may be a result of increase in temperatures during the study period.  

**Real Life Applications**

With a fire prediction and visualization tool like ours, first responders may address
- Asset relocation
- Early containment
- Possible evacuation areas
- **Prevent future loss of life and minimize property damage** 
- Additionally, we hope our model results can help fire prevention teams request additional resource and funding support from local, state, federal sources. Tableau map visualizations could also highlight highly affected areas that need attention. 

### As the climate change crisis now creates conditions that are deteriorating and causing worse destruction, having the capability to determine potential fire size is essential.

**Climate change affects us all and needs to be a topic of discussion at all levels of government and public forum.** Tools like this one that are easy to understand and bring pertinent issues to the forefront are needed to bring us all in the fight for a more stable future.

## Credits
***This project was created in 2022 as part of a Final Project for the University of Denver's Data Analytics BootCamp (a Trilogy Education Services program). It is NOT intended to provide real life predictions.*** 
- Team k.E.G.d. wishes to thank our instructor, Svitlana, and our T.A.s, James, Sheri, and Simon, for all their assistance on this project.  
- Credit is also due to Team Lizard People, and their Conspiracy Theory project, for inspiration when our coding struggles got real.
- Lastly, without DU’s Data Analytics Bootcamp, this team, our friendship, and our project wouldn’t even exist!!!
