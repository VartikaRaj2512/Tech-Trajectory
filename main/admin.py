from django.contrib import admin
from .models import LevelSelection

class LevelSelectionAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'get_database_fundamentals',
        'get_computer_architecture',
        'get_distributed_computing_systems',
        'get_cyber_security',
        'get_networking',
        'get_software_development',
        'get_programming_skills',
        'get_data_analyst',
        'get_computer_forensics_fundamentals',
        'get_technical_communication',
        'get_ai_ml',
        'get_software_engineering',
        'get_business_analysis',
        'get_communication_skills',
        'get_data_science',
        'get_troubleshooting_skills',
        'get_graphics_designing',
        'get_role'
    )

    # Show numeric value for each field
    def get_database_fundamentals(self, obj):
        return obj.database_fundamentals  # Shows the numeric value (0-6)

    def get_computer_architecture(self, obj):
        return obj.computer_architecture  # Shows the numeric value (0-6)

    def get_distributed_computing_systems(self, obj):
        return obj.distributed_computing_systems  # Shows the numeric value (0-6)

    def get_cyber_security(self, obj):
        return obj.cyber_security  # Shows the numeric value (0-6)

    def get_networking(self, obj):
        return obj.networking  # Shows the numeric value (0-6)

    def get_software_development(self, obj):
        return obj.software_development  # Shows the numeric value (0-6)

    def get_programming_skills(self, obj):
        return obj.programming_skills  # Shows the numeric value (0-6)

    def get_data_analyst(self, obj):
        return obj.data_analyst  # Shows the numeric value (0-6)

    def get_computer_forensics_fundamentals(self, obj):
        return obj.computer_forensics_fundamentals  # Shows the numeric value (0-6)

    def get_technical_communication(self, obj):
        return obj.technical_communication  # Shows the numeric value (0-6)

    def get_ai_ml(self, obj):
        return obj.ai_ml  # Shows the numeric value (0-6)

    def get_software_engineering(self, obj):
        return obj.software_engineering  # Shows the numeric value (0-6)

    def get_business_analysis(self, obj):
        return obj.business_analysis  # Shows the numeric value (0-6)

    def get_communication_skills(self, obj):
        return obj.communication_skills  # Shows the numeric value (0-6)

    def get_data_science(self, obj):
        return obj.data_science  # Shows the numeric value (0-6)

    def get_troubleshooting_skills(self, obj):
        return obj.troubleshooting_skills  # Shows the numeric value (0-6)

    def get_graphics_designing(self, obj):
        return obj.graphics_designing  # Shows the numeric value (0-6)

    def get_role(self, obj):
        return obj.Role  # Shows the role value (e.g., Admin, User, Moderator)

# Registering the model with the admin site
admin.site.register(LevelSelection, LevelSelectionAdmin)
