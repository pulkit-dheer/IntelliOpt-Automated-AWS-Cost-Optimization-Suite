# IntelliOpt: Automated AWS Cost Optimization Suite



![IntelliOpt: Automated-AWS-Cost-Optimization-Suite-diagram](https://github.com/pulkit-dheer/IntelliOpt-Automated-AWS-Cost-Optimization-Suite/blob/main/assets/IntelliOpt%3A%20Automated%20AWS%20Cost%20Optimization%20Suite.gif)





### Overview:
In the ever-evolving cloud landscape, businesses often face rising AWS expenses due to **underutilized EC2 instances, idle EBS snapshots, and unused security groups.** Managing these resources efficiently is crucial for cost control and operational excellence. As organizations scale, tracking and optimizing cloud resources can become complex, leading to hidden costs and reduced efficiency. Proactive, automated solutions are essential to **maintain agility** while ensuring cloud spending aligns with business objectives.

[IntelliOpt](https://github.com/pulkit-dheer/IntelliOpt-Automated-AWS-Cost-Optimization-Suite.git) is a powerful, automated suite developed to streamline AWS resource utilization, reduce superfluous costs, and simplify cloud management with minimal manual intervention.

### Key Advantages of IntelliOpt:

- **Proactive Cost Savings:**  
   Through automation, IntelliOpt identifies and decommissions underused or orphaned resources, enabling organizations to lower AWS costs and avoid unnecessary spending.

- **Enhanced Operational Efficiency:**  
   By handling optimization autonomously, IntelliOpt frees up valuable time for IT teams, allowing them to focus on core business priorities instead of routine monitoring and management.

- **Compliance and Best Practices:**  
   The suite ensures regular cleanup of unused resources, aligning with AWS best practices and promoting adherence to **organizational governance standards for a clean and compliant cloud environment.


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
For more information see [Boto3 Documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html).

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
    `ec2:DeleteSecurityGroup`,
    `logs:CreateLogGroup`,
    `logs:CreateLogStream`,
    `logs:PutLogEvents`


![lambda_permission](https://github.com/pulkit-dheer/IntelliOpt-Automated-AWS-Cost-Optimization-Suite/blob/main/assets/lambda_permission.png)


4. Configuration (Optionally): You may customize the CPU utilization threshold in the AWSCostOptimizerSuite class based on your cost optimization strategy. 





## 🎯 Challenges
**Underutilized EC2 Instances:** Many EC2 instances may be running with low CPU utilization, leading to unnecessary costs. Identifying and stopping these instances can significantly reduce monthly expenses.

**Stalled EBS Snapshot:** Organizations often accumulate numerous EBS snapshots over time, many of which become orphaned and are no longer attached to any volumes. These orphaned snapshots not only consume storage space but also contribute to unnecessary costs.

**Orphaned Security Groups:** As instances are terminated, their associated security groups may remain unused. Identifying and cleaning up these orphaned security groups can help maintain a tidy and manageable cloud environment.


## 💡 The Solution

The [IntelliOpt](https://github.com/pulkit-dheer/IntelliOpt-Automated-AWS-Cost-Optimization-Suite.git) suite provides a comprehensive and automated approach to optimizing AWS resource utilization, significantly lowering costs and enhancing operational efficiency. Here’s how the suite effectively addresses the identified challenges:


### 1. Automated Scanning and Management of Underutilized EC2 Instances

The suite employs AWS CloudWatch to continuously monitor the CPU utilization of EC2 instances over the past 24 hours. By analyzing these metrics, IntelliOpt identifies instances with consistently low CPU usage. When an instance’s average utilization falls below the specified threshold (default of 10%), the suite automatically stops the instance. Importantly, the suite is designed to only delete EC2 instances that are tagged with **"staging" or "dev"** ensuring that production resources remain intact. This proactive management helps organizations:

- **Reduce Costs:** By stopping underutilized instances, organizations can achieve significant savings on compute expenses, potentially cutting costs by up to 90% for instances not fully utilized.

- **Resource Reallocation:** The saved resources can be reallocated to more critical workloads, improving overall performance.

### 2. Stalled EBS Snapshot Cleanup for Cost-Effective Storage Management

Over time, organizations often accumulate numerous **EBS snapshots**, many of which may no longer be relevant. The suite automates the process of identifying and deleting orphaned snapshots that are not attached to any active volumes. Key benefits include:

- **Cost Savings:** Deleting unnecessary snapshots helps in reclaiming storage space and reducing storage costs associated with EBS.

- **Simplified Management:** This automated cleanup ensures that your storage environment remains tidy and manageable, allowing for easier data governance and compliance.

### 3. Automatic Cleanup of Unused Security Groups for a Safer, Simpler Network

As instances are launched and terminated, associated security groups may become orphaned, leading to a cluttered AWS environment. The IntelliOpt suite **automatically identifies** and deletes these unused security groups. This functionality provides:

- **Streamlined Security Management:** Keeping security groups clean and relevant reduces potential security risks and simplifies network management.

- **Compliance with Best Practices:** Regularly removing orphaned security groups aligns with AWS best practices, ensuring that your cloud environment adheres to organizational governance standards.


### 4. Daily Automated Execution via AWS EventBridge for Continuous Optimization
IntelliOpt is configured to run daily, leveraging AWS EventBridge to trigger and schedule the suite’s operations, ensuring that AWS resources are continuously monitored and optimized. This regular execution enables IntelliOpt to swiftly detect underutilized EC2 instances, orphaned EBS snapshots, and unnecessary security groups, automating actions as needed. Key advantages include:

- **Continuous Cost Savings:** With AWS EventBridge orchestrating daily executions, IntelliOpt maximizes cost savings by promptly addressing inefficiencies, minimizing unnecessary expenses on an ongoing basis.

- **Timely Resource Management:** Daily monitoring and cleanup powered by EventBridge ensure that your AWS resources remain dynamically aligned with business requirements, eliminating waste and improving cost efficiency.

![aws_lambda_code](https://github.com/pulkit-dheer/IntelliOpt-Automated-AWS-Cost-Optimization-Suite/blob/main/assets/aws_lambda_code.png)


### 5. Enhanced Focus on Business Innovation through Automated Cost Optimization

By automating the optimization of AWS resources, IntelliOpt frees up valuable time for IT teams. Instead of focusing on manual resource management and monitoring, teams can concentrate on core business initiatives, driving innovation and growth.



## 🏁 Conclusion
With IntelliOpt, organizations can take a proactive approach to cloud cost management, achieving substantial cost savings while enhancing operational efficiency. By automating the identification and remediation of underutilized resources, the suite not only optimizes cloud spending but also aligns resource allocation with business needs, ensuring that every dollar spent on AWS contributes to maximizing ROI.







## ❓ FAQ
1. How does the suite determine if an EC2 instance is underutilized?

    Solution: The suite utilizes **AWS CloudWatch** to gather CPU utilization metrics for each running **EC2 instance** over the **past 24 hours.** It computes the average CPU utilization percentage; if this average is below a specified threshold (default set at 10%), the instance is classified as **underutilized.** By proactively stopping these instances, the suite can significantly **reduce operational costs**, potentially saving up to **90% on compute expenses** for instances that are not being fully utilized. This strategic approach to cost optimization not only enhances resource efficiency but also ensures that cloud spending aligns more closely with actual usage, and **maximizing ROI.**

2. What happens to my stopped instances? Will they automatically restart?

    Solution: When the AWSCostOptimizerSuite stops an underutilized EC2 instance, it **remains in a stopped state** until you manually start it again or implement an automated process to restart it. Stopping instances can **save costs**, but it's important to monitor your workloads to ensure that necessary instances are restarted as needed. The suite is designed to **optimize costs** without compromising the functionality of your environment.

