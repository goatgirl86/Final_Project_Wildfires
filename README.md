# Scorched!
An Analysis of U.S. Wildfires from 1992-2015

### By: k.E.G.d. (Katlin, Enzo, Graham, Danieli)

![image](https://user-images.githubusercontent.com/92705556/164362996-733acdf8-498c-4ec8-83fc-886dc000c433.png)

## Project Visualizations
- **Web App**: coming soon
- **Google Slides Presentation**: *https://docs.google.com/presentation/d/1k6_nFs06r_e-iALVW8RSOxMYcdh0ALGk/edit?usp=sharing&ouid=108250606024172523210&rtpof=true&sd=true*

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
-   Has the number, size, and cause of wildfires changed over time?
-   Has the timing and distribution of wildfires changed over time?
-   Can temperature, wind, humidity, discovery month, and state be used to predict whether a fire will grow to at least 50 acres in size?

### Technologies, Languages, Tools, and Algorithms Used
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
The initial data analysis included creating basic plots using matplotlib and linear regression, creating new dataframes using the 'groupby' function in both Python and SQL, and using R to run simple statistical analyses (Multiple Linear Regression and Chi-Squared Analysis).  

After some of the initial analysis, we also decided to add five news coloumns in the dataset to provide additional information needed for further analysis and machine learning models. *Columns added **df_all_k.csv**: 'state_no', 'discovery_month_no', 'fire_size_bin', 'fire_size_bin_no', 'medium_plus'.
- The 'fire_size_bin' column (and the associated 'fire_size_bin_no' and 'medium_plus' columns) are the main additions to the dataset.  The 'fire_size' columns included over 3000 unique values, so we decided to bin the fire sizes into groups based on acreage (Bin Name / Bin No): 0-5 acres (Teacup / 1), 5-10 acres (Toy / 2), 10-50 acres (Mini / 3), 50-1000 acres (Medium / 4), 1,000-10,000 acres (Large / 5), >10,000 acres (XL / 6).  We also added an additional column for 'medium_plus'.  Fires that were at least medium in size were given a value of '1'. Teacup, Toy, Mini fires were given a value of '0'.  By adding this column, we could perform machine learning models that predicted whether a fire would grow to at least 50 acres in size.  

***Screenshot 3**: Code showing creation of fire_size_bins and fire_size_bin_no*

![image](https://user-images.githubusercontent.com/92705556/168167177-b2b067d0-7d96-4954-ae74-97e3f3d2c3dd.png)


### Machine Learning
Using our knowledge of Supervised and Unsupervised Machine Learning, we ran several different models on our dataset.  
- **Unsupervised Machine Learning**: KMeans, Primary Component Analysis (PCA), and Heirarchical Clustering were all used to identify 'groupings' of datapoints based on temperature, humidity, and wind variables.

***Sreenshot 4**: Unsupervised Machine Learning KMeans Scaled Model Plot showing 3 classes of pre_7 weather data (weather condition 7 days prior to fire start)*

![image](https://user-images.githubusercontent.com/92705556/168200740-36ab1e37-916e-4c2c-8d15-5e443d9967ed.png)

-  **Supervised Machine Learning**: Neural Networking, Random Forest Classifier, Balanced Random Forest Classifier, Easy Ensemble Classifier, Naive Random Oversampling, SMOTE Oversampling, Cluster Centroids Undersampling, SMOTEENN Over and Undersampling, Gradient Boosting Classifier, and Logistic Regression models were all run to determine accuracy of prediction models. Models were run using both 'Label Encoder' and 'One Hot Encoder' for comparison.

***Sreenshot 5**: Supervised Machine Learning Accuracy Results (using OneHot Encoder)*

![image](https://user-images.githubusercontent.com/92705556/168201343-9b222c38-ebaa-4bb5-a2f9-617a14094cc0.png)

***Sreenshot 6**: Supervised Machine Learning Accuracy Results (using Label Encoder)*

![image](https://user-images.githubusercontent.com/92705556/168187077-49326184-59f4-4a25-a4ed-b9abe56baf0e.png)

**Using Neural Networking with OneHot Encoder results in the highest accuracy percentage which will give our model the best chance of quickly predicting a fire size. This will not only be helpful but also not require large amounts of time and technology to run, thus providing an entertaining and informative tool for wildfire education.**

## Database
To create our Database, we chose to use PgAdmin and SQL Alchemy.  Within our database, we have four main tables that are all connected through a common field: 'fire_id'. The original four tables were: fire_category, fire_info, fire_location, and weather_data. Using SQLAlchemy and Python, we then queried and joined information from the four original tables to create new tables.

***Sreenshot 7**: Entity Relationship Diagram (ERD) for our database*

![image](https://user-images.githubusercontent.com/92705556/167992926-9e43c1b5-547e-432f-90e7-badf56cf6f97.png)

***Sreenshot 8**: Code showing SQL Alchemy connection with database and query / join of data from original tables into new dataframe*

![image](https://user-images.githubusercontent.com/92705556/168187328-59b19e08-9a2e-4397-bdbd-a15376612bc4.png)

## Dashboard
To make the dashboard, we used our knowledge of HTML and Javascript to create a stylish web app that includes background information, wildfire photos, interactive visualizations of our Tableau and Google Slides, and a "Predict Your Fire" page.  The prediction page allows a user to run user inputs through our Machine Learning model to predict whether a medium-sized fire or larger will result in the next 7 days.  

## Conclusions
Just as predicting the weather is notoriously challenging even for the professionals, predicting wildfires is also difficult due to varying weather conditions and unpredictable human behavior.  Once a fire sparks, the ability of it to be contained quickly depends not only on weather but also on response times, resource allocation and capacity, and much more.  

With this fire prediction tool we hope to provide new information that can help assist fire prevention teams with distribution of assets and even help them to request more resources from local and federal programs. Tableau map visualizations may also help highlight highly affected areas that need attention on a growing basis. 

Additionally, by predicting whether or not a fire will grow beyond a “Medium” size, first responders may address
- Asset relocation
- Early containment
- Set possible evacuation areas.
- **Ideally, together, we can help prevent future loss of life and reduce property damage.** 

### As the climate change crisis now creates conditions that are deteriorating and causing worse destruction, having the capability to determine fire size is essential.

**Climate change affects us all and needs to be a topic of discussion at all levels of government and public forum.** Tools like this one that are easy to understand and bring pertinent issues to the forefront are needed to bring us all in the fight for a more stable future.

