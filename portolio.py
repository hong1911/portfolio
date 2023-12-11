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
  # st.write(f"[{project}]({project_link})\n")
  st.write(f"[{project}]({project_link})")
  # st.write("")
  # st.image(project_image_link,use_column_width ='auto')
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
I am a data scientist with a strong background in business and supply chain. 
I hold a Master of Science in Business Analytics from University of California, Irvine.
I am passionate about using data to solve complex business problems and drive value for organizations.
I have recently expanded my skill sets to various topics including natural language processing, cluster analysis, predictive modeling, and data visualization. 
I am excited to keep learning new methods in a challenging and fast-paced environment.
''')

#####################
st.markdown('''
## Work Experience
''')

txt('''**KAISER PERMANENTE, OAKLAND, CA** <br>**Student Data Analyst**''',
  '01/2023 - 06/2023')
st.markdown('''
Analyzed 10M+ rows of data to identify workload trends, and employee performance that informed business
decision-making related to staffing for 900+ employees. Communicate recommendations and insights to data
financial leadership through effective dashboards and presentations.
- Cleaned `10M+` rows of transaction records using Python, performing cluster model to segment performance of 1000+ employees.
- Created KPIs metrics and developed `10+` informative Tableau visualization dashboards to aid finance leadership in evaluating the staffing effectiveness.
''')

txt('''**ALLTIUS, IRVINE, CA** <br>**Data Analyst Intern**''',
  '09/2022 - Present')
st.markdown('''
Analyzed the business processes and developed metrics to evaluate the performance of AI chatbot. Extracted and
analyzed large volume of text data and communicated insights with the software developers through effective
metrics. Ensured AI chatbot performance meets or exceeds the benchmarks set by the company and identified
areas for product improvement.
- Applied natural language techniques (NLP) techniques and ChatGPT API in Python to analyze AI chatbot
response and develop an automated testing model, accelerating `30%` velocity of the testing cycle.
- Utilized NoSQL to extract text data from Weaviate vector database, performing text analysis, and using
Google Sheet API to create a summary report that increased `20%` efficiency to analyze product defects.
- Improved `10%` AI chatbot response accuracy by using NLP techniques in Python to analyze chatbot response
and communicating insights to software developers.
''')

txt('''**LACACO, TUSTIN, CA** <br>**Supply Chain Analyst**''',
  '02/2019 – 04/2022')
st.markdown('''
Responsible for analyzing supply chain data to identify opportunities to match supply and demand, reduce costs,
and improve operational efficiencies. Collaborated with business partners to deliver data insights that directly
impact business decisions and improve the value chain.
- Performed inventory analytics to explore financial performance trends of different brands based on cost,
purchase volume, profit, and service level, which led to a `10%` ROI improvement.
- Analyzed purchasing and sales data to assess the business impact of trends, which supported the sales team
to identify trending products and led to a `30%` revenue increase.
- Developed dashboard reports with Tableau to increase inter-departmental transparency, resulting in a `25%`
decrease in time required for management teams to analyze information and make informed decisions.
- Increased fulfillment rate `50%` by analyzing and communicating critical supply chain metrics to stakeholders,
providing recommendations to leadership, and executing solutions to improve supply chain performance.          
''')

txt('''**CST INDUSTRIES, KANSAS, USA (VIETNAM OFFICE)** <br>**Regional Project Manager – Asia**''',
  '02/2012 – 12/2016')
st.markdown('''
Managed all aspects of 50+ projects for customers in Asia, including project planning, execution, monitoring, and
controlling. Coordinated with customers to understand their needs and collaborated with cross functional teams
to ensure that projects are delivered on time, within budget, and to customer satisfaction.
- Independently engaged with customers and business partners such as engineering, manufacturing, logistics,
and accounting to gather requirements and validate project results. Created tracking Excel sheet to manage
`50+` projects to be on track with project scope, schedules, and customer satisfaction.
- Collected and analyzed a large database from multiple sources including logistics, finance, and manufacturing
to produce actionable plans that led to a `30%` on-time delivery rate increase.
- Successfully delivered `$5M+` projects within budget and timeline constraints by utilizing root cause analysis to
mitigate risks and address issues related to manufacturing, quality, and logistics.
- Utilized Microsoft Excel pivot tables to perform project financial analysis to identify areas for cost saving
related to outsourcing and logistics, which increased project profit up to `5%`.     
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
# image_2 = Image.open('spend_analytics.PNG')
# st.image(image_2, width=150)
txt3('Spend Analytics', 'Tableau photos/spend_analytics.PNG', 'https://public.tableau.com/app/profile/hong.nguyen2260/viz/SpendAnalytics_16731414474670/ExecutiveTotalSpend')

txt5('World Demographics Animation', 'https://public.tableau.com/app/profile/hong.nguyen2260/viz/WorldDemographicsAnimation_16727080793640/WorldDemographics')
txt5('Data Science Salary', 'Tableau photos/data_science_salary.png', 'https://public.tableau.com/app/profile/hong.nguyen2260/viz/DataScienceSalaryAnalysis_16732413979580/Dashboard1')
txt5('Clothing Retail Industry Analysis', 'Tableau photos/retail.png', 'https://public.tableau.com/app/profile/hong.nguyen2260/viz/ClothingRetailIndustryAnalysis_16727010423040/FinalPresentation')
txt5('Customer Analysis', 'Tableau photos/customer_analysis.png', 'https://public.tableau.com/app/profile/hong.nguyen2260/viz/CustomerAnalysis_16727167027430/Dashboard1')
txt5('Startups Analysis', 'Tableau photos/startups_analysis.png', 'https://public.tableau.com/app/profile/hong.nguyen2260/viz/Startupsanalysis_16726215150380/TheStartUpQuadrant')

txt5('LinkedIn', 'https://www.linkedin.com/in/hongpn/')

#####################
st.markdown('''
## Education
''')

txt('**Master of SCience in Business Analytics**, *University of California, Irvine*', 'June 2023')
st.markdown('''
- GPA: `3.98/4.00`
- Graduated with Highest GPA.
''')

txt('**Bachelor of Art Business Administration**, *University of California, Irvine*', 'June 2002')
st.markdown('''
- GPA: `4.00/4.00`
- Honors: Delta Sigma Pi Scholarship Key
''')

txt('**Certified Supply Chain Professional**, *APICS*','November 2021')

#####################
st.markdown('''
## Skills
''')
txt4('Programming', '`Python`, `R`')
txt4('Data processing/wrangling', '`SQL`, `NoSQL`, `Pandas`, `Numpy`')
txt4('Data visualization', '`Tableau`, `Power BI`')
txt4('Machine Learning', '`Scikit-learn`')
txt4('Model deployment', '`Streamlit`, `AWS`')
txt4('ERP', '`SAP`, `NetSuite`')
txt4('Others','`Git`, `Jira`, `Advanced Excel (VBA, PivotTables, Index/Match)`')

#####################
st.markdown('''
## Social Media
''')
txt5('LinkedIn', 'https://www.linkedin.com/in/hongpn/')
txt5('GitHub', 'https://github.com/hong1911')
txt5('Tableau', 'https://public.tableau.com/app/profile/hong.nguyen2260/vizzes?fbclid=IwAR2QS1SJOq9QBbAuFqD-f3Nvnu5H8CIY3VP03DGC7H3eIxhxfYbD-zckdL8')
