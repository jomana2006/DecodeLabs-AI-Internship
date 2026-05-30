

# Lists:
# Role Lists

dataScientist = ["python", "sql", ["machine learning", "ml"], "statistics", "data analysis", "tensorflow", "numpy", "pandas"]
backendDeveloper = ["java", "python", "sql", "api", "databases", "rest", "node.js", "django"]
frontendDeveloper = ["javascript", "html", "css", "react", ["ui", "ux", "ui/ux"], "typescript", "figma"]
devOpsEngineer = ["docker", "kubernetes", "aws", ["ci", "cd", "ci/cd"], "linux", "git", "automation", "bash"]
cloudArchitect = ["aws", "azure", "cloud", "networking", "security", "terraform", "docker"]
cybersecurityAnalyst = ["networking", "security", "linux", "cryptography", "firewall", "ethical hacking"]
aiMlEngineer = ["python", "tensorflow", ["machine learning", "ml"], ["deep learning", "dl"], "numpy", "pytorch", "algorithms"]
mobileDeveloper = ["swift", "kotlin", "java", "android", "ios", "flutter", "react"]
databaseAdministrator = ["sql", "databases", "oracle", "mongodb", "postgresql", "optimisation"]
fullStackDeveloper = ["javascript", "python", "sql", "react", "node.js", "api", "html", "css", "git"]
dataEngineer = ["python", "sql", "spark", "hadoop", "etl", "airflow", "kafka", "databases", "numpy"]
systemsEngineer = ["linux", "bash", "c", "networking", "hardware", "embedded systems", "assembly"]
gameDeveloper = ["c++", "unity", "opengl", "physics", "java", "algorithms", "python", "unreal engine"]
blockChainDeveloper = ["solidity", "cryptography", "ethereum", "smart contracts", "python", "security", "web3"]
qaEngineer = ["testing", "automation", "selenium", "python", "sql", ["ci", "cd", "ci/cd"], "git", "bug tracking"]
networkEngineer = ["networking", "cisco", "firewall", "linux", "security", "tcp/ip", "routing", "switching"]
embeddedSystemsEngineer = ["c", "c++", "assembly", "hardware", "linux", "rtos", "microcontrollers", "embeddes systems"]
nlpEngineer = ["python", ["natural language processing", "nlp"], "tensorflow", ["deep learning", "dl"], "linguistics", "pytorch", "nltk", "transformers"]
computerVisionEngineer = ["python", "opencv", ["deep learning", "dl"], "tensorflow", "pytorch", "image processing", "cnn"]
roboticsEngineer = ["python", "c++", "ros", "embedded systems", "hardware", "algorithms", "sensors", "control systems"]
siteReliabilityEngineer = ["linux", "docker", "kubernetes", "monitoring", "automation", "python", ["ci", "cd", "ci/cd"], "aws"]
businessIntelligenceAnalyst = ["sql", "tableau", "powerbi", "data analysis", "statistics", "excel", "reporting"]

# User List

userInput = []

# Job Name List

jobNames = ["Data Scientist", "Backend Developer", "Frontend Developer", "DevOps Engineer", "Cloud Architect", "Cybersecurity Analyst", "AI/ML Engineer", "Mobile Developer", "Database Administrator", "Full Stack Developer", "Data Engineer", "Systems Engineer", "Game Developer", "Blockchain Developer", "QA Engineer", "Network Engineer", "Embedded Systems Engineer", "NLP Engineer", "Computer Vision Engineer", "Robotics Engineer", "Site Reliability Engineer", "Business Intelligence Analyst"]

# Using .join(), we will turn these lists into strings for the vectorizer.
#Role list to string
DataScientist = " ".join(dataScientist)
BackendDeveloper = " ".join(backendDeveloper)
FrontendDeveloper = " ".join(frontendDeveloper)
DevOpsEngineer = " ".join(devOpsEngineer)
CloudArchitect = " ".join(cloudArchitect)
CybersecurityAnalyst = " ".join(cybersecurityAnalyst)
AIMLEngineer = " ".join(aiMlEngineer)
MobileDeveloper = " ".join(mobileDeveloper)
DatabaseAdministrator = " ".join(databaseAdministrator)
FullStackDeveloper = " ".join(fullStackDeveloper)
DataEngineer = " ".join(dataEngineer)
SystemsEngineer = " ".join(systemsEngineer)
GameDeveloper = " ".join(gameDeveloper)
BlockChainDeveloper = " ".join(blockChainDeveloper)
QAEngineer = " ".join(qaEngineer)
NetworkEngineer = " ".join(networkEngineer)
EmbeddedSystemsEngineer = " ".join(embeddedSystemsEngineer)
NLPEngineer = " ".join(nlpEngineer)
ComputerVisionEngineer = " ".join(computerVisionEngineer)
RoboticsEngineer = " ".join(roboticsEngineer)
SiteReliabilityEngineer = " ".join(siteReliabilityEngineer)
BusinessIntelligenceAnalyst = " ".join(businessIntelligenceAnalyst)

# Creating a job matrix

jobStrings = [DataScientist, BackendDeveloper, FrontendDeveloper, DevOpsEngineer, CloudArchitect, CybersecurityAnalyst, AIMLEngineer, MobileDeveloper, DatabaseAdministrator, FullStackDeveloper, DataEngineer, SystemsEngineer, GameDeveloper, BlockChainDeveloper, QAEngineer, NetworkEngineer, EmbeddedSystemsEngineer, NLPEngineer, ComputerVisionEngineer, RoboticsEngineer, SiteReliabilityEngineer, BusinessIntelligenceAnalyst]