from myproject.donors.models import Donor


class DonorForm(forms.ModelForm):
    class Meta:
        model = Donor
        fields = [
            "name",
            "blood_group",
            "gender",
            "age",
            "phone_number",
            "national_number",
        ]