import streamlit as st
from PIL import Image

style_css = """
ul {
    padding-left: 1.5rem;
  }

h1 {
    text-align:center;
}

h5 {
    text-align:center;
}

img {
    margin-left: 17.2rem;
}

#MainMenu {
    visibility: hidden;
}
footer {
    visibility: hidden;
}
header {
    visibility: hidden;
}
"""

st.markdown('<style>{}</style>'.format(style_css), unsafe_allow_html=True)

#####################
# Header 
st.write('''
# Hong Nguyen
''')

image = Image.open('hn_professional_photo.png')
st.image(image, width=150)

#####################
# # Navigation

##16A2CB
st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)
st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #6AB187;">
  <a class="navbar-brand" href="https://www.linkedin.com/in/hongpn/" target="_blank">Hong Nguyen</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="/">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item active">
        <a class="nav-link" href="#about-me">About Me</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#work-experience">Work Experience</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#projects">Projects</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#skills">Skills</a>
      </li>
      <li>
      <li class="nav-item">
        <a class="nav-link" href="#social-media">Social Media</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

#####################
# Custom function for printing text
def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.write(a,unsafe_allow_html=True)
  with col2:
    st.markdown(b)

def txt2(a, source_b, b, source_c, c):
  col1, col2, col3, col4, col5 = st.columns([5,1,1.5,2,2])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.write(f"[{source_b}]({b})")
  with col3:
    st.write(f"[{source_c}]({c})")
    # st.markdown(b)

def txt3(project, project_image_link, project_link):
  st.write(f"[{project}]({project_link})")
  image_2 = Image.open(project_image_link)
  st.image(image_2, use_column_width ='auto')
    
def txt4(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt5(source_a,a):
  st.write(f"[{source_a}]({a})")

#####################
st.markdown('## About Me')
st.info('''
I am a data analytics professional and AI product manager with several years of experience driving operation and supply chain efficiency through data-driven solutions.
With a strong foundation in AI and machine learning, I specialize in building metrics, optimizing processes, and enhancing decision-making for businesses.
I hold a Master of Science in Business Analytics and am passionate about developing AI-powered solutions that drive innovation and efficiency.
Continuously exploring new methodologies, I thrive in fast-paced environments that challenge me to push the boundaries of AI and analytics.
''')

#####################
st.markdown('''
## Work Experience
''')


txt('''**NIAGARA BOTTLING, DIAMOND BAR, CA** <br>**Senior Supply Chain Solution Analyst, AI**''',
  '07/2024 - Present')
st.markdown('''
Lead AI product management and data analytics, developing AI-driven automation solutions to optimize customer service and logistics operations.
Design KPI metrics, analyze large datasets for actionable insights, and collaborate with cross-functional teams to implement AI solutions.
- Developed AI-powered automation system, leveraging Generative AI, Machine Learning, and Computer Vision to enhance customer service and logistics operations processes, achieving a `60% reduction in ticket resolution time`.
- Designed KPI metrics for the AI products and built interactive Power BI dashboards that increased decision-making efficiency by `30%`.
- Partnered with data science teams to develop an intent classification model in Python, predicting carrier intent with `90% accuracy`, resulting in a `25% boost in automation rate`.
- Conducted analysis on over `800,000 incident records`, presenting business insights to optimize customer service and logistics operations.
- Facilitated cross-departmental change management, collaborating with IT, logistics operations, and customer service teams to successfully implement AI solutions.
''')


txt('''**TEACHER CREATED MATERIALS, HUNGTINTON BEACH, CA** <br>**Supply Chain Analyst**''',
  '05/2023 - 07/2024')
st.markdown('''
Responsible for maintaining demand planning reviews and procurement plans to ensure availability of inventory that meet company fulfillment rate target.
Orchestrated inventory management and forecasting strategies, effectively aligning stock optimization with company goals.
- Developed machine learning models with `85% accuracy` in Python to predict the win probability of opportunities, improving revenue forecasting accuracy and optimizing sales processes.
- Achieved over `95% fulfillment rate` through building demand forecasting models and developing inventory replenishment plans.
- Automated Extract, Transform, and Load (ETL) process with SQL, Python, and VBA, leading to a `50% increase efficiency` for the demand planning process.
- Analyzed `10 years of sales data` to identify correlation patterns and collaborated with the marketing team to develop a targeted marketing strategy, enhancing cross-selling opportunities and driving increased revenue.
- Developed dashboards to monitor inventory key performance indicator (KPI) metrics of over 40,000 products
''')

txt('''**KAISER PERMANENTE, OAKLAND, CA** <br>**Student Data Scientist**''',
  '01/2023 - 06/2023')
st.markdown('''
Analyzed millions of transaction data to identify workload trends and employee performance,
informing business decision-making related to staffing. Communicated insights to data scientist and financial leadership through effective dashboards and presentations.
- Performed data cleaning and exploratory analysis in Python on a dataset of `10+ million` transaction records.
- Developed a cluster machine learning model in Python to segment performance of `1000+ employees`. This allowed finance leadership to efficiently evaluate staffing needs.
- Formulated KPIs for employee performance and presented them through `10+` interactive Tableau dashboards.
''')

txt('''**ALLTIUS, IRVINE, CA** <br>**Data Analyst Intern**''',
  '09/2022 - Present')
st.markdown('''
Designed and implemented automated testing processes to evaluate the performance of an AI chatbot.
Worked closely with software developers to ensure the AI chatbot met or exceeded the performance benchmarks set by the company and identified areas for product improvement.
- Created the testing process and wrote Python script to automate it, `boosting testing cycle velocity by 30%`.
- Collected chatbot data from vector database, performed text analysis, and created an accuracy report. This `increased 20% efficiency` to analyze product defects and
`improved 10% chatbot response accuracy`.
- Developed an interactive web dashboard with Streamlit to monitor input email data quality. This supported the email intent classification model to achieve `95% accuracy`.
''')

txt('''**ORTHO CLINICAL DIAGNOSTICS, RARITAN, NJ** <br>**Supply Chain Business Analyst Planning Intern**''',
  '05/2022 - 09/2022')
st.markdown('''
Supported cross-functional teams to identify areas for improvement in supply chain master data quality and implement solutions to improve data accuracy and consistency.
Responsible for analyzing data to ensure compliance with data governance policies.
- Performed root-cause analysis of data irregularities of multiple data sources, leading to an `increase of 25%` product master data accuracy. 
- Incorporated feedback from Master Data, IT and Warehouse team to implement process enhancements to maintain accuracy of supply chain master data,
which `reduced 15%` time for data management.
- Technology used: Excel, SAP.
''')

txt('''**LACACO, TUSTIN, CA** <br>**Business Analyst**''',
  '02/2019 – 04/2022')
st.markdown('''
Analyzed business data to identify opportunities for aligning supply and demand, reducing costs, and enhancing operational efficiencies.
Collaborated with business partners to deliver data-driven insights that directly influenced business decisions, enhancing the value chain.
- Developed a machine learning model achieving `90%+` accuracy in classifying incoming email intents. Automated task assignment based on identified email intents,
leading to `50%` operation efficiency increase.
- Analyzed purchasing, sales, and inventory data of over `10,000` products. This helped the company to identify top trending products to purchase, resulting in a `30%` revenue increase.
- Created business metrics and developed Tableau visualizations, reducing analysis time by `25%`.
- Analyzed B2B customer behavior and communicated insights to stakeholders. This allowed the sales team to efficiently offer the right products to each customer.
- Analyzed products profit margin and operational cost to optimize pricing for over `100 brands`.       
''')

txt('''**CST INDUSTRIES, KANSAS, USA (VIETNAM OFFICE)** <br>**Regional Project Manager – Asia**''',
  '02/2012 – 12/2016')
st.markdown('''
Managed all aspects of `50+` projects for customers in Asia, including project planning, execution, monitoring, and controlling.
Coordinated with customers to understand their needs and collaborated with cross functional teams to ensure that projects are delivered on time, within budget, and to customer satisfaction.
- Collaborated with customers and business partners such as engineering, manufacturing, logistics, and accounting to validate project results.
Annually managed `50+` projects to be on track.
- Analyzed engineering, logistics and manufacturing data to produce actionable plans that led to a `30%` on-time delivery rate increase.
- Successfully delivered `$5M+` projects within budget and timeline constraints by utilizing root cause analysis to mitigate risks and address issues related to manufacturing, quality, and logistics.
- Developed project metrics including scope, schedule, budget, and quality. Built dashboards to communicate with leadership, leading to `30%` efficiency in monitoring projects.
''')

#####################
st.markdown('''
## Projects
''')
st.markdown('''
#### Data Science Projects
''')
txt2('Predict Customer Churn project',
     'Github','https://github.com/hong1911/Predict-customer-churn-in-Telecom-industry/blob/main/Predict%20customer%20churn.ipynb',
     '','')
txt2('Movies Rating Prediction',
     'Github','https://github.com/hong1911/Rotten-Tomatoes-Movies-Rating-Prediction/blob/main/Rotten%20Tomatoes%20Movies%20Rating%20Prediction.ipynb',
     '','')
txt2('Sentiment Analysis Hackathon',
     'Github','https://github.com/hong1911/NLP_Sentiment-Analysis_hackathon/blob/main/NLP_hackathon_032423.ipynb',
     '','')
txt2('Kaggle Data Survey Analysis',
     'Github','https://github.com/hong1911/Kaggle-Data-Science-Survey-Analysis/blob/main/Kaggle%20Data%20Science%20Survey%20-%20Analysis.ipynb',
     '','')
txt2('Machine Learning with Streamlit',
     'Github','https://github.com/hong1911/Machine-Learning-with-Streamlit?tab=readme-ov-file',
     'Streamlit','https://machine-learning-app.streamlit.app/')

st.markdown('''
#### Tableau Projects
''')
txt3('Spend Analytics', 'Tableau photos/spend_analytics.PNG',
     'https://public.tableau.com/app/profile/hong.nguyen2260/viz/SpendAnalytics_16731414474670/ExecutiveTotalSpend')
txt3('World Demographics Animation', 'Tableau photos/world_demographics.PNG',
     'https://public.tableau.com/app/profile/hong.nguyen2260/viz/WorldDemographicsAnimation_16727080793640/WorldDemographics')
txt3('Data Science Salary', 'Tableau photos/data_science_salary.PNG',
     'https://public.tableau.com/app/profile/hong.nguyen2260/viz/DataScienceSalaryAnalysis_16732413979580/Dashboard1')
txt3('Clothing Retail Industry Analysis', 'Tableau photos/retail.PNG',
     'https://public.tableau.com/app/profile/hong.nguyen2260/viz/ClothingRetailIndustryAnalysis_16727010423040/FinalPresentation')
txt3('Customer Analysis', 'Tableau photos/customer_analysis.PNG',
     'https://public.tableau.com/app/profile/hong.nguyen2260/viz/CustomerAnalysis_16727167027430/Dashboard1')
txt3('Startups Analysis', 'Tableau photos/startups_analysis.PNG',
     'https://public.tableau.com/app/profile/hong.nguyen2260/viz/Startupsanalysis_16726215150380/TheStartUpQuadrant')

#####################
st.markdown('''
## Education
''')

txt('**Master of SCience in Business Analytics**, *University of California, Irvine*', 'June 2023')
st.markdown('''
- GPA: `3.98/4.00`
- Graduated with Highest GPA
''')

txt('**Bachelor of Art Business Administration**, *University of California, Irvine*', 'June 2002')
st.markdown('''
- GPA: `4.00/4.00`
- Delta Sigma Pi Scholarship Key
''')

txt('**Certified Supply Chain Professional**, *APICS*','November 2021')

#####################
st.markdown('''
## Skills
''')
txt4('AI/ML', '`Generative AI`, `Computer Vision`, `Scikit-learn`')
txt4('Programming', '`Python`, `R`')
txt4('Data processing/wrangling', '`SQL`, `NoSQL`, `Pandas`, `Numpy`')
txt4('Data visualization', '`Tableau`, `Power BI`')
txt4('Model deployment', '`Streamlit`, `AWS`, `Azure`')
txt4('ERP', '`Oracle`, `SAP`, `NetSuite`')
txt4('Others','`Git`, `Jira`, `Advanced Excel (VBA, PivotTables, Index/Match)`')

#####################
st.markdown('''
## Social Media
''')
txt5('LinkedIn', 'https://www.linkedin.com/in/hongpn/')
txt5('GitHub', 'https://github.com/hong1911')
txt5('Tableau', 'https://public.tableau.com/app/profile/hong.nguyen2260/vizzes?fbclid=IwAR2QS1SJOq9QBbAuFqD-f3Nvnu5H8CIY3VP03DGC7H3eIxhxfYbD-zckdL8')
