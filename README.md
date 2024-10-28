# IntelliOpt: Automated-AWS-Cost-Optimization-Suite

**Problem Statement:**  In today's cloud computing environment, organizations often face challenges in efficiently managing their AWS resources, particularly Amazon **EC2 instances**, **EBS snapshots, and Security groups.** With the increasing costs associated with unused or underutilized resources, it becomes imperative for businesses to optimize their infrastructure to ensure cost-effectiveness and operational efficiency.


The purpose of [IntelliOpt](https://github.com/pulkit-dheer/IntelliOpt-Automated-AWS-Cost-Optimization-Suite.git) repository is to demonstrate how a suite of tools and scripts designed to enhance resource utilization, reduce unnecessary costs, and simplify cloud resource management.


- **Automating the optimization** process enables organizations to significantly reduce AWS costs by proactively identifying and decommissioning **underutilized** and **orphaned resources.**

- The suite enhances **operational efficiency**, allowing teams to focus on **core business initiatives** instead of manual resource management and continuous monitoring.

- Regular **cleanup of orphaned resources** ensures compliance with **organizational governance standards** and aligns with **cloud best practices.**


## 🐍 Python Requirements

Let's jump into the Python packages you need. Within the Python environment of your choice, run:


``` git clone https://github.com/pulkit-dheer/IntelliOpt-Automated-AWS-Cost-Optimization-Suite.git
cd IntelliOpt-Automated-AWS-Cost-Optimization-Suite/
pip install -r requirements.txt ```













## Challenges
Underutilization of EC2 Instances: Many EC2 instances may be running with low CPU utilization, leading to unnecessary costs. Identifying and stopping these instances can significantly reduce monthly expenses.

EBS Snapshot Management: Organizations often accumulate numerous EBS snapshots over time, many of which become orphaned and are no longer attached to any volumes. These orphaned snapshots not only consume storage space but also contribute to unnecessary costs.

Orphaned Security Groups: As instances are terminated, their associated security groups may remain unused. Identifying and cleaning up these orphaned security groups can help maintain a tidy and manageable cloud environment.