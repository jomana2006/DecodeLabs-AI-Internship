import time
# from sklearn.feature_extraction import TfidfVectorizer
# from sklearn.metrics.pairwise import cosine_similarity

# Below is a dictionary of aliases for things with various namings.

aliasesSkills = {
     "ml" : "machine learning",
     "dl" : "deep learning",
     "natural langauge processing" : "nlp",
     "real time operating system" : "rtos",
     "robot operating system" : "ros",
     "extract transform load" : "etl",
     "extract, transform, load" : "etl",
     "natural language toolkiy" : "nltk"
}
# Lists:
# Role Lists

dataScientist = ["python", "sql", "machine learning", "statistics", "data analysis", "tensorflow", "numpy", "pandas"]
backendDeveloper = ["java", "python", "sql", "api", "databases", "rest", "node.js", "django"]
frontendDeveloper = ["javascript", "html", "css", "react", "ui/ux", "typescript", "figma"]
devOpsEngineer = ["docker", "kubernetes", "aws", "ci/cd", "linux", "git", "automation", "bash"]
cloudArchitect = ["aws", "azure", "cloud", "networking", "security", "terraform", "docker"]
cybersecurityAnalyst = ["networking", "security", "linux", "cryptography", "firewall", "ethical hacking"]
aiMlEngineer = ["python", "tensorflow", "machine learning", "deep learning", "numpy", "pytorch", "algorithms"]
mobileDeveloper = ["swift", "kotlin", "java", "android", "ios", "flutter", "react"]
databaseAdministrator = ["sql", "databases", "oracle", "mongodb", "postgresql", "optimisation"]
fullStackDeveloper = ["javascript", "python", "sql", "react", "node.js", "api", "html", "css", "git"]
dataEngineer = ["python", "sql", "spark", "hadoop", "etl", "airflow", "kafka", "databases", "numpy"]
systemsEngineer = ["linux", "bash", "c", "networking", "hardware", "embedded systems", "assembly"]
gameDeveloper = ["c++", "unity", "opengl", "physics", "java", "algorithms", "python", "unreal engine"]
blockChainDeveloper = ["solidity", "cryptography", "ethereum", "smart contracts", "python", "security", "web3"]
qaEngineer = ["testing", "automation", "selenium", "python", "sql", "ci/cd", "git", "bug tracking"]
networkEngineer = ["networking", "cisco", "firewall", "linux", "security", "tcp/ip", "routing", "switching"]
embeddedSystemsEngineer = ["c", "c++", "assembly", "hardware", "linux", "rtos", "microcontrollers", "embedded systems"]
nlpEngineer = ["python", "nlp", "tensorflow", "deep learning", "linguistics", "pytorch", "nltk", "transformers"]
computerVisionEngineer = ["python", "opencv", "deep learning", "tensorflow", "pytorch", "image processing", "cnn"]
roboticsEngineer = ["python", "c++", "ros", "embedded systems", "hardware", "algorithms", "sensors", "control systems"]
siteReliabilityEngineer = ["linux", "docker", "kubernetes", "monitoring", "automation", "python", "ci/cd", "aws"]
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

greetingMessage = "Hello.\nPlease enter at least 3 skills to get your career recommendations. Enter 'done' to finish entering the skills."

for character in greetingMessage:
     print(character, end=" ", flush= True)
     time.sleep(0.03)
print()

rePromt = "Please enter at least 3 skills."

while True:
     skillInput = input()
     cleanSkillInput = skillInput.lower().strip()
     
     if cleanSkillInput == "done":
          if len(cleanSkillInput) < 3:
               for character in rePromt:
                    print(character, end=" ", flush=True)
                    time.sleep(0.03)
               print()
          else:
               break
     else:
          aliasSkill = aliasesSkills.get(cleanSkillInput, cleanSkillInput) #if it was found in the aliases dictionary it is replaced, otherwise, for fallback it returns the original input of the user
          userInput.append(cleanSkillInput)

