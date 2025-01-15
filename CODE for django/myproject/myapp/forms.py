from django import forms
from .models import CustomerInfo  # 导入模型



class CustomerInfoForm(forms.ModelForm):
    class Meta:
        model = CustomerInfo
        fields = '__all__'  
        widgets = {
            'customer_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter customer name'}),
            'functional_requirements': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Detailed functional requirements'}),
            'non_functional_requirements': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Non-functional requirements like performance, security, etc.'}),
            'data_requirements': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Describe data requirements (sources, storage, etc.)'}),
            'project_scope': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Define the project goals and scope'}),
            'constraints': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Specify any technical, time, or budget limitations'}),
            'existing_resources': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Provide any existing system resources (docs, APIs, etc.)'}),
            'ui_ux_design': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'UI/UX design requirements (branding, interface needs)'}),
            'user_roles': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Describe target users and access devices'}),
            'mid_stage_feedback': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Specify mid-stage feedback requirements'}),
            'test_cases': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Provide test case references based on customer scenarios'}),
            'acceptance_criteria': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Clear functional and performance benchmarks'}),
            'data_samples': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Provide real or simulated data samples'}),
            'production_requirements': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Specify production environment requirements'}),
            'permission_settings': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Role-based access permissions'}),
            'go_live_support': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Specify go-live support (e.g., training, docs, etc.)'}),
        }


