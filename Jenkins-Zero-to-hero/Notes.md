# Understanding CI/CD
- Continuous Integration (CI): CI is a practice where developers frequently commit code changes into a shared repository. This code is then automatically built and tested to identify and fix bugs early. The goal of CI is to ensure that code changes are integrated smoothly, improve software quality, and expedite the release of new features.

- Continuous Delivery (CD): CD builds on CI by ensuring that the software can be reliably and quickly released to users. It involves running comprehensive tests in a staging environment that mirrors production to catch any issues before deployment. CD automates the release process, making the software deployment more efficient and reducing the risk of errors in production.

# What Is a Build Job in Jenkins?
- Fetching Dependencies: Automatically retrieving necessary libraries or packages.

- Compiling Code: Transforming source code into executable programs.

- Running Tests: Executing tests to ensure code quality and functionality.

- Deploying Applications: Publishing the application to different environments.

# Jenkins offers several types of build jobs, including:

- Freestyle Projects: Simple and flexible, allowing various configurations and integrations.

- Pipelines: Advanced setups using DSL (Domain-Specific Language) scripts for complex workflows.

- Multi-Configuration Projects: Jobs that run with different configurations to test various scenarios.

- Multibranch Pipelines: Automatically manage branches in a repository, making it easier to handle multiple feature branches.

- Organization Folders: Manage projects in a folder structure for better organization and scalability.