from django.db import models

# Create your models here.
class TodoItem(models.Model):
    title = models. CharField(max_length=200)
    completed = models.BooleanField(default=False)
from django.db import models

class CustomerInfo(models.Model):
    customer_name = models.CharField(max_length=100)  # 客户名称 / Customer Name
    functional_requirements = models.TextField()  # 功能性需求 / Functional Requirements
    non_functional_requirements = models.TextField()  # 非功能性需求 / Non-functional Requirements
    data_requirements = models.TextField()  # 数据需求 / Data Requirements
    project_scope = models.TextField()  # 项目目标和范围 / Project Objectives and Scope
    constraints = models.TextField()  # 约束条件 / Constraints
    existing_resources = models.TextField()  # 当前系统资源 / Existing System Resources
    ui_ux_design = models.TextField(blank=True, null=True)  # UI/UX设计 / UI/UX Design
    user_roles = models.TextField(blank=True, null=True)  # 用户角色 / User Roles
    mid_stage_feedback = models.TextField(blank=True, null=True)  # 必要的中期反馈 / Mid-stage Feedback
    test_cases = models.TextField(blank=True, null=True)  # 测试用例参考 / Test Case References
    acceptance_criteria = models.TextField(blank=True, null=True)  # 验收标准 / Acceptance Criteria
    data_samples = models.TextField(blank=True, null=True)  # 数据样本 / Data Samples
    production_requirements = models.TextField(blank=True, null=True)  # 生产环境要求 / Production Environment Requirements
    permission_settings = models.TextField(blank=True, null=True)  # 权限配置 / Permission Settings
    go_live_support = models.TextField(blank=True, null=True)  # 上线支持 / Go-live Support


    def __str__(self):
        return self.customer_name

class CopilotResponse(models.Model):
    customer_info = models.OneToOneField(CustomerInfo, on_delete=models.CASCADE, related_name='copilot_response')  # 一对一关系
    response_data = models.TextField()  # Copilot返回的完整数据
    created_at = models.DateTimeField(auto_now_add=True)  # 创建时间

    def __str__(self):
        return f"Response for {self.customer_info.customer_name}"
