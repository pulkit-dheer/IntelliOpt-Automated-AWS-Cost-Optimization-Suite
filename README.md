# IntelliOpt: Automated-AWS-Cost-Optimization-Suite

**Problem Statement:**  In today's cloud computing environment, organizations often face challenges in efficiently managing their AWS resources, particularly Amazon **EC2 instances**, **EBS snapshots, and Security groups.** With the increasing costs associated with unused or underutilized resources, it becomes imperative for businesses to optimize their infrastructure to ensure cost-effectiveness and operational efficiency.


The purpose of [IntelliOpt](https://github.com/pulkit-dheer/IntelliOpt-Automated-AWS-Cost-Optimization-Suite.git) repository is to demonstrate how a suite of tools and scripts designed to enhance resource utilization, reduce unnecessary costs, and simplify cloud resource management.


- **Automating the optimization** process enables organizations to significantly reduce AWS costs by proactively identifying and decommissioning **underutilized** and **orphaned resources.**

- The suite enhances **operational efficiency**, allowing teams to focus on **core business initiatives** instead of manual resource management and continuous monitoring.

- Regular **cleanup of orphaned resources** ensures compliance with **organizational governance standards** and aligns with **cloud best practices.**


## 📦 Requirements

Let's jump into the Python packages you need. Within the Python environment of your choice, run:

Python Environment: The suite is implemented in Python. Make sure you have Python 3.x installed on your machine.


```bash
git clone https://github.com/pulkit-dheer/IntelliOpt-Automated-AWS-Cost-Optimization-Suite.git
cd IntelliOpt-Automated-AWS-Cost-Optimization-Suite/
pip install -r requirements.txt
```

Boto3 Library: Install the Boto3 library, which is the AWS SDK for Python, to interact with AWS services. You can install it using pip:

```bash
pip install boto3
```


### Additional Requirements

1. AWS Account: You must have an active AWS account with sufficient permissions to access and manage EC2 instances, EBS snapshots, and security groups.

2. AWS CLI Installed: Ensure that the AWS Command Line Interface (CLI) is installed and configured on your machine to facilitate interactions with AWS services.

3. IAM Permissions: The AWS Identity and Access Management (IAM) role or user executing this suite should have the following permissions:

    `ec2:DescribeRegions` 
    `ec2:DescribeInstances`
    `ec2:StopInstances`
    `ec2:DescribeSnapshots`
    `ec2:DeleteSnapshot`
    `ec2:DescribeVolumes`
    `ec2:DeleteSecurityGroup`


4. Configuration: Optionally, you may customize the CPU utilization threshold in the AWSCostOptimizerSuite class based on your cost optimization strategy. 





## 🎯 Challenges
**Underutilized EC2 Instances:** Many EC2 instances may be running with low CPU utilization, leading to unnecessary costs. Identifying and stopping these instances can significantly reduce monthly expenses.

**Stalled EBS Snapshot:** Organizations often accumulate numerous EBS snapshots over time, many of which become orphaned and are no longer attached to any volumes. These orphaned snapshots not only consume storage space but also contribute to unnecessary costs.

**Orphaned Security Groups:** As instances are terminated, their associated security groups may remain unused. Identifying and cleaning up these orphaned security groups can help maintain a tidy and manageable cloud environment.






## ❓ FAQ
1. How does the suite determine if an EC2 instance is underutilized?

    The suite utilizes **AWS CloudWatch** to gather CPU utilization metrics for each running **EC2 instance** over the **past 24 hours.** It computes the average CPU utilization percentage; if this average is below a specified threshold (default set at 10%), the instance is classified as **underutilized.** By proactively stopping these instances, the suite can significantly **reduce operational costs**, potentially saving up to **90% on compute expenses** for instances that are not being fully utilized. This strategic approach to cost optimization not only enhances resource efficiency but also ensures that cloud spending aligns more closely with actual usage, and **maximizing ROI.**

