# 🚀 SpeakX DevOps Project

## 🌐 Project Domains & Endpoints
### Disclaimer !!!
- #### **The webiste uses secure connection **_(SSL)_** but self-signed, you will see a warning if you're viewing this on a browser, click advanced options and proceed to flightman.lol, <br> if you're using cURL add `-k` flag to skip ssl warning.** ####
## Primary Domain
 - ## **Domain**: [flightman.lol](https://flightman.lol)

### API Endpoints
| Endpoint | Description | Response |
|----------|-------------|----------|
| `/` | Home Endpoint | Welcome message |
| `/status` | Application Status | JSON status |
| `/pic` | Image Retrieval | Random Static image |
| `/health` | Health Check | Health status |
| `/joke` | Joke Endpoint | A random joke |
| `/echo` | Echo Endpoint | Echoes the input JSON |
| `/weather` | Weather Information | Weather info from wttr.in |

## 🧪 Testing the Application

```bash
# API Endpoint Tests
curl -kL https://flightman.lol/
curl -kL https://flightman.lol/status
curl -kL https://flightman.lol/pic
curl -kL https://flightman.lol/health
curl -kL https://flightman.lol/joke
curl -kL -X POST https://flightman.lol/echo -d '{"key":"value"}'
curl -kL https://flightman.lol/weather
```

## 🛠 How I Did It: A Personal Journey

### Initial Conceptualization
When I first approached this DevOps assignment, I initially went with railway.app as my PaaS, inorder to develop a MVP as soon as possible and learn the concepts of devops, Once I gained the knowledge of basic DevOps, then I moved to AWS, it was rough in the beginning stages of dev, since I never used AWS before, understanding the components of aws was the biggest hurdle. But in the end I have made this MVP, Only thing left to do is moving from self-signed to CA-signed.

### Step-by-Step Development Process

1. **Cloud Provider Selection**
   - Chose AWS for its comprehensive services
   - Created an AWS account
   - Generated IAM user credentials

2. **Local Development**
   - Developed a simple Flask application
   - Created basic API endpoints
   - Structured the application for containerization

3. **Containerization**
   ```bash
   # Dockerfile creation
   docker build -t speakx-flask-api .
   
   # Local testing
   docker run -p 3000:3000 speakx-flask-api
   ```

4. **Infrastructure as Code**
   - Used Terraform to define infrastructure
   - Created security groups
   - Provisioned EC2 instance
   - Set up Elastic IP
   - Created ECR repository


5. **Deployment Strategy**
   - Used Docker Compose for container orchestration
   - Configured Nginx as a reverse proxy
   - Implemented SSL termination


#### Security Considerations
- Implemented strict security group rules
- Used environment variables for sensitive data
- Ensured no hard-coded credentials



## 🔍 Technical Architecture

### Infrastructure Components
- **Cloud**: AWS
- **Compute**: EC2
- **Containerization**: Docker
- **Orchestration**: Docker Compose
- **IaC**: Terraform



## 📊 Project Diagram
<details open>
<summary>Development Workflow</summary>

![Development Workflow](https://github.com/user-attachments/assets/a22019b6-9c7e-47ec-baa3-118b0740a1e6)


</details>


## 🔒 Security Highlights
- AWS Secrets Manager integration
- Environment-based configuration
- HTTPS-only communication
- Restricted network access

## 🚢 Previous Iteration: Railway.app

### Initial Project
- **Domain**: Given in [flightman.lol](https://flightman.lol)
- **Approach**: Simplified PaaS deployment
- **Limitations**: Less control, basic scalability


## 🛤️ Railway.app Deployment Journey

### Project Genesis
My initial approach to the SpeakX project began with Railway.app, a Platform as a Service (PaaS) that simplifies deployment and scaling.

### Technical Specifications
- **Platform**: Railway.app
- **Deployment Method**: Direct GitHub Repository Integration
- **Technology Stack**: 
  - Python Flask
  - Containerized Application

### Deployment Process
1. **Repository Setup**
   - Configured GitHub repository
   - Prepared application for cloud deployment

2. **Railway Configuration**
   - Connected GitHub repository
   - Automatic build and deployment
   - Simplified environment management

### Limitations of Initial Approach
- Limited infrastructure control
- Basic scaling capabilities
- Reduced customization options

### Transition Motivation
The move from Railway.app to AWS was driven by:
- Need for more granular infrastructure control
- Advanced security requirements
- Scalability and enterprise-level features

## 🔍 Comparative Analysis

| Aspect | Railway.app | AWS Solution |
|--------|-------------|--------------|
| Deployment Complexity | Low | High |
| Infrastructure Control | Limited | Comprehensive |
| Scalability | Basic | Advanced |
| Cost | Free Tier | Flexible, Pay-as-you-go |
| Security Configuration | Basic | Extensive |

## 🚀 Lessons Learned
  - 🔧 Declarative syntax of Terraform for provinsion
  - 🌍 AWS Ecosystem, EC2, ECR, S3 Bucket, Security Groups (SG)
  - 💡 Containerization using Docker and Orchestration using docker-compose

## 🤝 Acknowledgments
Special thanks to Railway.app for providing an initial platform for rapid development and deployment.<br>
Special thanks to [Aryan](https://github.com/theredditbandit) for reviewing this project and giving thoughtful insights.

## 🤝 Contributing
Contributions are welcome! Please open an issue or submit a pull request.

## 📜 License
GLWTS
