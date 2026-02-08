from flask import Flask, render_template_string

app = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Atul Anand | Portfolio</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #f4f6f8;
            margin: 0;
            padding: 0;
        }
        .container {
            max-width: 900px;
            margin: 40px auto;
            background: #ffffff;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.1);
        }
        h1 {
            color: #2c3e50;
        }
        h2 {
            color: #34495e;
            border-bottom: 2px solid #eee;
            padding-bottom: 5px;
        }
        p {
            color: #555;
            line-height: 1.6;
        }
        ul {
            padding-left: 20px;
        }
        li {
            margin-bottom: 8px;
        }
        .links a {
            margin-right: 15px;
            text-decoration: none;
            color: #1abc9c;
            font-weight: bold;
        }
        .links a:hover {
            text-decoration: underline;
        }
        footer {
            margin-top: 30px;
            text-align: center;
            color: #888;
            font-size: 14px;
        }
    </style>
</head>
<body>

<div class="container">
    <h1>Atul Anand</h1>
    <p><strong>DevOps | Cloud | AWS | Automation</strong></p>

    <h2>About Me</h2>
    <p>
        I am a DevOps and Cloud enthusiast with hands-on experience in AWS networking,
        EC2, VPC architecture, automation, and CI/CD concepts.
        I enjoy building scalable infrastructure and learning by doing.
    </p>

    <h2>Projects</h2>
    <ul>
        <li>AWS VPC with Public & Private Subnets</li>
        <li>EC2 Jump Box (Bastion Host) Architecture</li>
        <li>NAT Gateway for Private Subnet Internet Access</li>
        <li>Flask App Deployment using Gunicorn & Nginx</li>
    </ul>

    <h2>Tech Stack</h2>
    <ul>
        <li>AWS: EC2, VPC, Subnets, IGW, NAT Gateway</li>
        <li>Linux, Bash Scripting</li>
        <li>Python, Flask</li>
        <li>Git, GitHub</li>
    </ul>

    <h2>Connect With Me</h2>
    <div class="links">
        <a href="https://github.com/YOUR_GITHUB_USERNAME" target="_blank">GitHub</a>
        <a href="https://linkedin.com/in/YOUR_LINKEDIN_ID" target="_blank">LinkedIn</a>
    </div>

    <footer>
        © 2026 Atul Anand | Hosted on AWS EC2 🚀
    </footer>
</div>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML_PAGE)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
