# 🚀 SpeakX DevOps Project: My Journey

## 🌐 Project Domains & Endpoints

### Primary Domain
- **Domain**: [flightman.lol](https://flightman.lol)

### API Endpoints
| Endpoint | Description | Response |
|----------|-------------|----------|
| `/` | Home Endpoint | Welcome message |
| `/status` | Application Status | JSON status |
| `/pic` | Image Retrieval | Static image |

## 🛠 How I Did It: A Personal Journey

### Initial Conceptualization
When I first approached this DevOps assignment, I knew I wanted to create something robust, scalable, and secure. My goal was to demonstrate not just technical skills, but a comprehensive understanding of cloud infrastructure and deployment strategies.

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

5. **HTTPS Configuration**
   ```bash
   # SSL Certificate Generation
   sudo certbot certonly --standalone -d flightman.lol
   ```

6. **Deployment Strategy**
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

## 🧪 Testing the Application

```bash
# API Endpoint Tests
curl -k https://flightman.lol/
curl -k https://flightman.lol/status
curl -k https://flightman.lol/pic
```

## 📊 Project Diagram
[Architectural Diagram Placeholder]

## 🔒 Security Highlights
- AWS Secrets Manager integration
- Environment-based configuration
- HTTPS-only communication
- Restricted network access

## 🚢 Previous Iteration: Railway.app

### Initial Project
- **Domain**: [shavok.up.railway.app](https://shavok.up.railway.app)
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
- Importance of infrastructure as code
- Benefits of cloud-native architectures
- Value of comprehensive deployment strategies

## 🤝 Acknowledgments
Special thanks to Railway.app for providing an initial platform for rapid development and deployment.

## 🤝 Contributing
Contributions are welcome! Please open an issue or submit a pull request.

## 📜 License
[Your License Details]