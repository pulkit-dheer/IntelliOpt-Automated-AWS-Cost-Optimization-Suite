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


4. Configuration (Optionally): You may customize the CPU utilization threshold in the AWSCostOptimizerSuite class based on your cost optimization strategy. 





## 🎯 Challenges
**Underutilized EC2 Instances:** Many EC2 instances may be running with low CPU utilization, leading to unnecessary costs. Identifying and stopping these instances can significantly reduce monthly expenses.

**Stalled EBS Snapshot:** Organizations often accumulate numerous EBS snapshots over time, many of which become orphaned and are no longer attached to any volumes. These orphaned snapshots not only consume storage space but also contribute to unnecessary costs.

**Orphaned Security Groups:** As instances are terminated, their associated security groups may remain unused. Identifying and cleaning up these orphaned security groups can help maintain a tidy and manageable cloud environment.


## 💡 The Solution

The [IntelliOpt](https://github.com/pulkit-dheer/IntelliOpt-Automated-AWS-Cost-Optimization-Suite.git) suite provides a comprehensive and automated approach to optimizing AWS resource utilization, significantly lowering costs and enhancing operational efficiency. Here’s how the suite effectively addresses the identified challenges:

### 1. Automated Identification and Management of Underutilized EC2 Instances

    The suite employs AWS CloudWatch to continuously monitor the CPU utilization of EC2 instances over the past 24 hours. By analyzing these metrics, IntelliOpt identifies instances with consistently low CPU usage. When an instance’s average utilization falls below the specified threshold (default of 10%), the suite automatically stops the instance. This proactive management helps organizations:

    - Reduce Costs: By stopping underutilized instances, organizations can achieve significant savings on compute expenses, potentially cutting costs by up to 90% for instances not fully utilized.

    - Resource Reallocation: The saved resources can be reallocated to more critical workloads, improving overall performance.

### 2. Efficient Cleanup of Stalled EBS Snapshots

    Over time, organizations often accumulate numerous **EBS snapshots**, many of which may no longer be relevant. The suite automates the process of identifying and deleting orphaned snapshots that are not attached to any active volumes. Key benefits include:

    - Cost Savings: Deleting unnecessary snapshots helps in reclaiming storage space and reducing storage costs associated with EBS.

    - Simplified Management: This automated cleanup ensures that your storage environment remains tidy and manageable, allowing for easier data governance and compliance.

### 3. Elimination of Orphaned Security Groups

    As instances are launched and terminated, associated security groups may become orphaned, leading to a cluttered AWS environment. The IntelliOpt suite **automatically identifies** and deletes these unused security groups. This functionality provides:

    -  Streamlined Security Management: Keeping security groups clean and relevant reduces potential security risks and simplifies network management.

    - Compliance with Best Practices: Regularly removing orphaned security groups aligns with AWS best practices, ensuring that your cloud environment adheres to organizational governance standards.


### 4. Focus on Core Business Initiatives

    By automating the optimization of AWS resources, IntelliOpt frees up valuable time for IT teams. Instead of focusing on manual resource management and monitoring, teams can concentrate on core business initiatives, driving innovation and growth.


## ❓ FAQ
1. How does the suite determine if an EC2 instance is underutilized?

    Solution: The suite utilizes **AWS CloudWatch** to gather CPU utilization metrics for each running **EC2 instance** over the **past 24 hours.** It computes the average CPU utilization percentage; if this average is below a specified threshold (default set at 10%), the instance is classified as **underutilized.** By proactively stopping these instances, the suite can significantly **reduce operational costs**, potentially saving up to **90% on compute expenses** for instances that are not being fully utilized. This strategic approach to cost optimization not only enhances resource efficiency but also ensures that cloud spending aligns more closely with actual usage, and **maximizing ROI.**

2. What happens to my stopped instances? Will they automatically restart?

    Solution: When the AWSCostOptimizerSuite stops an underutilized EC2 instance, it **remains in a stopped state** until you manually start it again or implement an automated process to restart it. Stopping instances can **save costs**, but it's important to monitor your workloads to ensure that necessary instances are restarted as needed. The suite is designed to **optimize costs** without compromising the functionality of your environment.

